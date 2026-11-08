#!/usr/bin/env bash
# 单章 Markdown → Word（公式为 Word 原生 OMML），同时保留规范化 Markdown 供 PDF 使用。
#
# usage: convert_chapter.sh <源.md> <章号> "<章标题>" <输出目录>
# 环境变量:
#   PYTHON    带 python-docx 的解释器（默认 python3），如 /root/deeptutor/.venv/bin/python
#   REF_DOCX  参考模板（默认 方法与工具/ref_zh.docx，由 make_ref.py 生成）
#   WORK_DIR  规范化 Markdown 的输出目录（默认 <输出目录>/.work）
set -euo pipefail

SRC=${1:?用法: convert_chapter.sh <源.md> <章号> "<章标题>" <输出目录>}
NUM=${2:?缺章号}
TITLE=${3:?缺章标题}
OUT=${4:?缺输出目录}

ROOT=$(cd "$(dirname "$0")"/.. && pwd)
PY=${PYTHON:-python3}
REF=${REF_DOCX:-$ROOT/ref_zh.docx}
NAME=$(basename "$SRC" .md)
WORK=${WORK_DIR:-$OUT/.work}
SRC_ABS=$(cd "$(dirname "$SRC")" && pwd)
mkdir -p "$OUT" "$WORK"

MAP=( [1]=一 [2]=二 [3]=三 [4]=四 [5]=五 [6]=六 [7]=七
      [8]=八 [9]=九 [10]=十 [11]=十一 [12]=十二 )
CN=${MAP[$NUM]:-$NUM}

WORKMD="$WORK/${NAME}.md"
NORM="$WORK/${NAME}.norm.md"

{ printf '# 第%s章 %s\n\n' "$CN" "$TITLE"; cat "$SRC"; } > "$WORKMD"
"$PY" "$ROOT/scripts/normalize_md.py" "$WORKMD" "$NORM"

pandoc "$NORM" -o "$OUT/${NAME}.docx" \
  --from markdown+tex_math_dollars+pipe_tables+tex_math_single_backslash-implicit_figures \
  --reference-doc "$REF" \
  --resource-path "$OUT:$SRC_ABS"

"$PY" "$ROOT/scripts/fix_tables.py" "$OUT/${NAME}.docx" >/dev/null

echo "OK $OUT/${NAME}.docx"
echo "NORM $NORM"
