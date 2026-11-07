#!/usr/bin/env python3
"""把逐章 .norm.md 合并成整本 Markdown。

- docx 版：封面元数据 + Word 目录域 + 分页符（目录需在 Word 里按 F9 更新）
- pdf  版：封面元数据 + LaTeX 分页符（目录由 pandoc --toc 经 template_zh.tex 生成）

用法:
    merge_md.py <工作目录> <输出.md> --format docx|pdf --title "..." \
        [--subtitle "..."] [--date "..."] [--chapters 1-7]
"""
import argparse
import glob
import os
import re

DOCX_PAGE_BREAK = '```{=openxml}\n<w:p><w:r><w:br w:type="page"/></w:r></w:p>\n```\n'
PDF_PAGE_BREAK = '```{=latex}\n\\newpage\n```\n'

TOC_BLOCK = '''```{=openxml}
<w:p><w:r><w:br w:type="page"/></w:r></w:p>
<w:p><w:pPr><w:pStyle w:val="TOCHeading"/></w:pPr><w:r><w:t>目　录</w:t></w:r></w:p>
<w:p><w:r><w:fldChar w:fldCharType="begin"/></w:r><w:r><w:instrText xml:space="preserve"> TOC \\o "1-2" \\h \\z \\u </w:instrText></w:r><w:r><w:fldChar w:fldCharType="separate"/></w:r><w:r><w:t>目录将在打开文档时自动更新</w:t></w:r><w:r><w:fldChar w:fldCharType="end"/></w:r></w:p>
<w:p><w:r><w:br w:type="page"/></w:r></w:p>
```
'''


def yaml_quote(value):
    return '"' + value.replace('\\', '\\\\').replace('"', '\\"') + '"'


def parse_chapters(spec, workdir):
    """'1-7' / '1,2,5' / None（自动发现）→ 章号列表。"""
    if spec:
        nums = []
        for part in spec.split(','):
            part = part.strip()
            if '-' in part:
                a, b = part.split('-', 1)
                nums.extend(range(int(a), int(b) + 1))
            elif part:
                nums.append(int(part))
        return nums
    found = []
    for path in glob.glob(os.path.join(workdir, 'ch*.norm.md')):
        m = re.search(r'ch(\d+)\.norm\.md$', path)
        if m:
            found.append(int(m.group(1)))
    return sorted(found)


def build(workdir, out_path, kind, title, subtitle, date, nums):
    parts = ['---', f'title: {yaml_quote(title)}']
    if subtitle:
        parts.append(f'subtitle: {yaml_quote(subtitle)}')
    if date:
        parts.append(f'date: {yaml_quote(date)}')
    parts.extend(['---', ''])

    if kind == 'docx':
        parts.append(TOC_BLOCK)

    for i, num in enumerate(nums):
        path = os.path.join(workdir, f'ch{num}.norm.md')
        if not os.path.exists(path):
            raise SystemExit(f'缺少 {path}；先跑 convert_chapter.sh')
        body = open(path, encoding='utf-8').read().strip()
        if i > 0:
            parts.append(DOCX_PAGE_BREAK if kind == 'docx' else PDF_PAGE_BREAK)
        parts.append(body + '\n')

    with open(out_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(parts))
    print(f'wrote {out_path} ({len(nums)} 章)')


def main():
    parser = argparse.ArgumentParser(description='合并逐章 Markdown')
    parser.add_argument('workdir')
    parser.add_argument('out')
    parser.add_argument('--format', choices=['docx', 'pdf'], required=True)
    parser.add_argument('--title', required=True)
    parser.add_argument('--subtitle', default='')
    parser.add_argument('--date', default='')
    parser.add_argument('--chapters', default='', help='如 1-7 或 1,2,5')
    args = parser.parse_args()

    nums = parse_chapters(args.chapters, args.workdir)
    if not nums:
        raise SystemExit('工作目录里没有 ch*.norm.md')
    build(args.workdir, args.out, args.format, args.title,
          args.subtitle, args.date, nums)


if __name__ == '__main__':
    main()
