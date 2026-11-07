"""Normalise chapter markdown for pandoc.

The generated .md files sometimes put a list directly after a paragraph or a
display-math line with no blank line in between. Pandoc then swallows the list
into the paragraph and prints the "-" bullets as literal text (this is what
made the last attempt look "squeezed").  This script only inserts blank lines
around top-level list blocks; it never rewrites content.

usage: normalize_md.py <src.md> <dst.md>
"""
import re
import sys

LIST_RE = re.compile(r'^([ \t]*)([-*+]|\d+[.)])\s+')


def indent(line):
    return len(line) - len(line.lstrip(' \t'))


def is_list(line):
    return LIST_RE.match(line) is not None


def is_blank(line):
    return line.strip() == ''


def normalize(text):
    lines = text.split('\n')
    out = []
    in_code = False
    in_math = False
    inserted = 0

    for line in lines:
        stripped = line.strip()

        # --- fenced code: pass through untouched -------------------------
        if stripped.startswith('```'):
            in_code = not in_code
            out.append(line)
            continue
        if in_code:
            out.append(line)
            continue

        # --- display math: pass through untouched ------------------------
        if in_math:
            out.append(line)
            if '$$' in line:
                in_math = False
            continue
        if stripped.startswith('$$'):
            # single-line $$...$$ stays a normal line
            if not (stripped.count('$$') >= 2 and len(stripped) > 2):
                in_math = True
            out.append(line)
            continue

        # --- list start right after a paragraph / math / heading ---------
        if is_list(line) and out and not is_blank(out[-1]) \
                and not is_list(out[-1]) and not out[-1].lstrip().startswith('|'):
            out.append('')
            inserted += 1

        # --- paragraph (or another block) right after a list item --------
        prev = out[-1] if out else ''
        if (not is_blank(line) and not is_list(line)
                and prev and is_list(prev)
                and indent(line) == 0 and not prev.lstrip().startswith('|')):
            out.append('')
            inserted += 1

        out.append(line)

    return '\n'.join(out), inserted


if __name__ == '__main__':
    src, dst = sys.argv[1], sys.argv[2]
    text = open(src, encoding='utf-8').read()
    fixed, n = normalize(text)
    open(dst, 'w', encoding='utf-8').write(fixed)
    print(f'{src}: inserted {n} blank lines')
