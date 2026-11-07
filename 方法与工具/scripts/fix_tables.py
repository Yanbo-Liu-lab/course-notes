"""Give pandoc-generated docx tables content-aware column widths.

Pandoc splits a pipe table into equal columns (fixed layout), which squeezes
long text columns and clips short ones. This rewrites each table so column
widths follow the amount of content, fits the text area, rows do not split
across pages, and the header row repeats.

usage: fix_tables.py <file.docx>
"""
import sys

from docx import Document
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

CONTENT_WIDTH = 8504  # A4 21cm minus 3cm margins each side, in twips


def cell_weight(cell):
    text = cell.text or ''
    math = len(cell._tc.findall('.//' + qn('m:oMath')))
    return len(text) + 8 * math + 2


def set_attr(parent, tag, **attrs):
    el = parent.find(qn(tag))
    if el is None:
        el = OxmlElement(tag)
        parent.append(el)
    for k, v in attrs.items():
        el.set(qn('w:' + k), v)
    return el


def fix_table(table):
    ncols = len(table.columns)
    if ncols == 0 or not table.rows:
        return

    weights = []
    for j in range(ncols):
        w = max((cell_weight(row.cells[j]) for row in table.rows), default=4)
        weights.append(max(w, 4))

    total = sum(weights)
    widths = [max(700, int(CONTENT_WIDTH * w / total)) for w in weights]
    # renormalise after clamping so the table still fits the text area
    scale = CONTENT_WIDTH / sum(widths)
    widths = [int(w * scale) for w in widths]

    tbl = table._tbl
    tblPr = tbl.tblPr
    set_attr(tblPr, 'w:tblW', type='dxa', w=str(CONTENT_WIDTH))
    set_attr(tblPr, 'w:tblLayout', type='fixed')

    grid = tbl.find(qn('w:tblGrid'))
    if grid is not None:
        tbl.remove(grid)
    grid = OxmlElement('w:tblGrid')
    for w in widths:
        gc = OxmlElement('w:gridCol')
        gc.set(qn('w:w'), str(w))
        grid.append(gc)
    tbl.insert(list(tbl).index(tblPr) + 1, grid)

    for row in table.rows:
        trPr = row._tr.get_or_add_trPr()
        if trPr.find(qn('w:cantSplit')) is None:
            trPr.append(OxmlElement('w:cantSplit'))
        for j, cell in enumerate(row.cells):
            tcPr = cell._tc.get_or_add_tcPr()
            set_attr(tcPr, 'w:tcW', type='dxa', w=str(widths[j]))


def main(path):
    doc = Document(path)
    for table in doc.tables:
        fix_table(table)
    doc.save(path)
    print(f'{path}: fixed {len(doc.tables)} table(s)')


if __name__ == '__main__':
    main(sys.argv[1])
