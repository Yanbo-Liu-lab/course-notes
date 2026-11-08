#!/usr/bin/env bash
# 单章规范化 Markdown → PDF（xelatex，公式与 \tag 编号完整保留）。
# 注意：PDF 必须走 xelatex，不能靠 LibreOffice 转 docx——LibreOffice 渲染
# 公式里的方括号会变成竖线。
#
# usage: build_pdf.sh <norm.md> <输出.pdf>
set -euo pipefail

NORM=${1:?用法: build_pdf.sh <norm.md> <输出.pdf>}
OUT=${2:?缺输出 PDF}
ROOT=$(cd "$(dirname "$0")"/.. && pwd)
RES=${RESOURCE_PATH:-$PWD}

pandoc "$NORM" -o "$OUT" \
  --from markdown+tex_math_dollars+pipe_tables+tex_math_single_backslash-implicit_figures \
  --pdf-engine=xelatex \
  --include-in-header="$ROOT/latex/header_zh.tex" \
  --resource-path "$RES" \
  -V documentclass=article -V fontsize=11pt -V linestretch=1.3 -V indent=true \
  -V papersize=a4 \
  -V CJKmainfont="Noto Serif CJK SC" -V mainfont="TeX Gyre Termes" \
  -V geometry:"top=2.54cm,bottom=2.54cm,left=3cm,right=3cm"

echo "OK $OUT"
