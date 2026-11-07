"""Build a Chinese-styled pandoc reference.docx.

Body: 宋体 / Times New Roman, 10.5pt, 1.5 line spacing.
Headings: 黑体, sizes 18/14/12pt, keep-with-next.
Page: A4, 2.54cm top/bottom, 3.0cm left/right.
"""
import os

from docx import Document
from docx.shared import Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_LINE_SPACING
from docx.oxml.ns import qn

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, 'ref_base.docx')
DST = os.path.join(ROOT, 'ref_zh.docx')

LATIN = 'Times New Roman'
HEI = '黑体'
SONG = '宋体'


def set_fonts(style, latin=LATIN, eastasia=SONG):
    style.font.name = latin
    rpr = style.element.get_or_add_rPr()
    rfonts = rpr.get_or_add_rFonts()
    rfonts.set(qn('w:ascii'), latin)
    rfonts.set(qn('w:hAnsi'), latin)
    rfonts.set(qn('w:cs'), latin)
    rfonts.set(qn('w:eastAsia'), eastasia)
    rfonts.set(qn('w:hint'), 'eastAsia')
    # theme attributes override explicit fonts in Word — strip them
    for attr in ('asciiTheme', 'hAnsiTheme', 'eastAsiaTheme', 'cstheme'):
        if qn('w:' + attr) in rfonts.attrib:
            del rfonts.attrib[qn('w:' + attr)]


def set_spacing(style, before=0, after=6, line=1.5, keep_next=False):
    pf = style.paragraph_format
    pf.space_before = Pt(before)
    pf.space_after = Pt(after)
    pf.line_spacing = line
    pf.keep_with_next = keep_next


d = Document(SRC)

# --- page setup: A4, Chinese-style margins -------------------------------
for s in d.sections:
    s.page_width = Cm(21.0)
    s.page_height = Cm(29.7)
    s.top_margin = Cm(2.54)
    s.bottom_margin = Cm(2.54)
    s.left_margin = Cm(3.0)
    s.right_margin = Cm(3.0)

st = d.styles
_by_name = {s.name: s for s in st}


def get(name):
    return _by_name[name]


# --- body ---------------------------------------------------------------
normal = get('Normal')
set_fonts(normal, LATIN, SONG)
normal.font.size = Pt(10.5)
set_spacing(normal, 0, 6, 1.5)

for name in ('Body Text', 'First Paragraph', 'Compact'):
    if name in _by_name:
        s = get(name)
        set_fonts(s, LATIN, SONG)
        s.font.size = Pt(10.5)
        set_spacing(s, 0, 6 if name != 'Compact' else 2, 1.5)

# --- headings -----------------------------------------------------------
h_specs = {
    'Heading 1': (18, True, 18, 12, True),
    'Heading 2': (14, True, 14, 8, True),
    'Heading 3': (12, True, 10, 6, True),
    'Heading 4': (10.5, True, 8, 4, True),
}
for name, (size, bold, before, after, keep) in h_specs.items():
    s = get(name)
    set_fonts(s, LATIN, HEI)
    s.font.size = Pt(size)
    s.font.bold = bold
    s.font.color.rgb = RGBColor(0, 0, 0)
    set_spacing(s, before, after, 1.25, keep)

# deep heading levels / TOC heading: same Chinese heading font
for s in st:
    if s.type != 1:
        continue
    if s.name.startswith('Heading') and s.name not in h_specs:
        set_fonts(s, LATIN, HEI)
        s.font.color.rgb = RGBColor(0, 0, 0)
    elif s.name == 'TOC Heading':
        set_fonts(s, LATIN, HEI)
        s.font.size = Pt(16)
        s.font.bold = True
        s.font.color.rgb = RGBColor(0, 0, 0)

# chapter title centred (Word ignores pageBreakBefore for first paragraph)
get('Heading 1').paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
get('Heading 1').paragraph_format.page_break_before = False

# --- title --------------------------------------------------------------
if 'Title' in _by_name:
    s = get('Title')
    set_fonts(s, LATIN, HEI)
    s.font.size = Pt(26)
    s.font.bold = True
    s.font.color.rgb = RGBColor(0, 0, 0)
    s.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
    s.paragraph_format.space_before = Pt(120)
    s.paragraph_format.space_after = Pt(24)

if 'Subtitle' in _by_name:
    s = get('Subtitle')
    set_fonts(s, LATIN, HEI)
    s.font.size = Pt(14)
    s.font.bold = False
    s.font.color.rgb = RGBColor(0x40, 0x40, 0x40)
    s.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
    s.paragraph_format.space_after = Pt(12)

if 'Date' in _by_name:
    s = get('Date')
    set_fonts(s, LATIN, SONG)
    s.font.size = Pt(12)
    s.font.color.rgb = RGBColor(0x40, 0x40, 0x40)
    s.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER

# --- table-of-contents entry styles ------------------------------------
from docx.enum.style import WD_STYLE_TYPE

for level, (size, bold, indent_cm, before, after) in {
        1: (10.5, True, 0.0, 4, 1),
        2: (10.5, False, 0.6, 0, 0),
}.items():
    name = f'toc {level}'
    if name in _by_name:
        s = get(name)
    else:
        s = st.add_style(name, WD_STYLE_TYPE.PARAGRAPH)
        s.base_style = get('Normal')
    set_fonts(s, LATIN, SONG)
    s.font.size = Pt(size)
    s.font.bold = bold
    s.font.color.rgb = RGBColor(0, 0, 0)
    pf = s.paragraph_format
    pf.left_indent = Cm(indent_cm)
    pf.space_before = Pt(before)
    pf.space_after = Pt(after)
    pf.line_spacing = 1.0

# --- footer: centred page number ---------------------------------------
from docx.oxml import OxmlElement


def add_page_number(paragraph):
    run = paragraph.add_run()
    for kind, text in (('begin', None), (None, ' PAGE '), ('end', None)):
        if kind:
            el = OxmlElement('w:fldChar')
            el.set(qn('w:fldCharType'), kind)
        else:
            el = OxmlElement('w:instrText')
            el.set(qn('xml:space'), 'preserve')
            el.text = text
        run._r.append(el)
    run.font.size = Pt(9)
    run.font.name = LATIN
    run._r.get_or_add_rPr().get_or_add_rFonts().set(qn('w:eastAsia'), SONG)


for s in d.sections:
    p = s.footer.paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    add_page_number(p)

d.save(DST)
print('saved', DST)
