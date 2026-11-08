#!/usr/bin/env bash
# 一键渲染整门课：单章 docx + PDF，合并版 docx + PDF（封面 + 目录）。
#
# 源目录约定:
#   ch1.md ... chN.md     每章总结正文（## 开头，不含章标题）
#   titles.txt            可选，每行 "ch1=绪论"，缺省用“第N章”
#
# usage:
#   TITLE="弹性力学 前七章知识点总结" \
#   SUBTITLE="依据 吴家龙《弹性力学》（第3版）" \
#   DATE="2026 年 11 月" \
#   bash render_all.sh <源目录> <输出目录> [章数]
#
# 合并版 Word 的目录是域代码，打开后 Ctrl+A、F9 更新；也可以用 update_toc.py
# （需要 LibreOffice + python3-uno）自动更新。
set -euo pipefail

SRC_DIR=${1:?用法: render_all.sh <源目录> <输出目录> [章数]}
OUT=${2:?缺输出目录}
N=${3:-7}

TITLE=${TITLE:-知识点总结}
SUBTITLE=${SUBTITLE:-}
DATE=${DATE:-}
OUTNAME=${OUTNAME:-$TITLE}

ROOT=$(cd "$(dirname "$0")"/.. && pwd)
PY=${PYTHON:-python3}
WORK=${WORK_DIR:-$OUT/.work}
SRC_ABS=$(cd "$SRC_DIR" && pwd)
mkdir -p "$OUT" "$WORK"

if [ ! -f "$ROOT/ref_zh.docx" ]; then
  echo "生成中文 Word 参考模板 ref_zh.docx"
  "$PY" "$ROOT/scripts/make_ref.py"
fi

chapter_title() {
  local key="ch$1" t=""
  if [ -f "$SRC_DIR/titles.txt" ]; then
    t=$(grep -m1 "^${key}=" "$SRC_DIR/titles.txt" | cut -d= -f2- || true)
  fi
  if [ -n "$t" ]; then echo "$t"; else echo "第$1章"; fi
}

for i in $(seq 1 "$N"); do
  t=$(chapter_title "$i")
  echo "== 第 $i 章：$t =="
  WORK_DIR="$WORK" PYTHON="$PY" \
    "$ROOT/scripts/convert_chapter.sh" "$SRC_DIR/ch$i.md" "$i" "$t" "$OUT"
  RESOURCE_PATH="$SRC_ABS" "$ROOT/scripts/build_pdf.sh" "$WORK/ch$i.norm.md" "$OUT/ch$i.pdf"
done

echo "== 合并 Word =="
"$PY" "$ROOT/scripts/merge_md.py" "$WORK" "$WORK/merged_docx.md" \
  --format docx --title "$TITLE" --subtitle "$SUBTITLE" --date "$DATE" --chapters "1-$N"
pandoc "$WORK/merged_docx.md" -o "$OUT/${OUTNAME}.docx" \
  --from markdown+tex_math_dollars+pipe_tables+tex_math_single_backslash-implicit_figures \
  --reference-doc "$ROOT/ref_zh.docx" \
  --resource-path "$SRC_ABS:$OUT"
"$PY" "$ROOT/scripts/fix_tables.py" "$OUT/${OUTNAME}.docx" >/dev/null
echo "OK $OUT/${OUTNAME}.docx"

echo "== 合并 PDF =="
"$PY" "$ROOT/scripts/merge_md.py" "$WORK" "$WORK/merged_pdf.md" \
  --format pdf --title "$TITLE" --subtitle "$SUBTITLE" --date "$DATE" --chapters "1-$N"
pandoc "$WORK/merged_pdf.md" -o "$OUT/${OUTNAME}.pdf" \
  --from markdown+tex_math_dollars+pipe_tables+tex_math_single_backslash-implicit_figures \
  --pdf-engine=xelatex \
  --resource-path "$SRC_ABS" \
  --template="$ROOT/latex/template_zh.tex" \
  --include-in-header="$ROOT/latex/header_zh.tex" \
  --toc --toc-depth=2 -V toc-title="目　录" \
  -V documentclass=article -V fontsize=11pt -V linestretch=1.3 -V indent=true \
  -V papersize=a4 \
  -V CJKmainfont="Noto Serif CJK SC" -V mainfont="TeX Gyre Termes" \
  -V geometry:"top=2.54cm,bottom=2.54cm,left=3cm,right=3cm"
echo "OK $OUT/${OUTNAME}.pdf"
