#!/usr/bin/env bash
# 阅读站点：准备静态文件、构建或本地预览。
#
# usage:
#   bash site.sh serve     # 本地预览 http://localhost:8000（默认）
#   bash site.sh build     # 生成静态站点到 site/
#   bash site.sh prepare   # 只把 PDF / Word 复制到 docs/弹性力学/pdf/
set -euo pipefail

ROOT=$(cd "$(dirname "$0")" && pwd)
PY=${PYTHON:-python3}
VENV=${VENV:-$ROOT/.venv}
MKDOCS="$VENV/bin/mkdocs"
PIP_INDEX=${PIP_INDEX:-https://pypi.tuna.tsinghua.edu.cn/simple}

ensure_mkdocs() {
  if [ ! -x "$MKDOCS" ]; then
    echo "首次运行：创建 .venv 并安装 mkdocs-material（用清华镜像）"
    "$PY" -m venv "$VENV"
    "$VENV/bin/pip" install -q -i "$PIP_INDEX" --upgrade pip
    "$VENV/bin/pip" install -q -i "$PIP_INDEX" mkdocs-material
  fi
}

prepare() {
  local dst="$ROOT/docs/弹性力学/pdf"
  mkdir -p "$dst"
  cp "$ROOT/弹性力学"/*.pdf "$dst"/
  cp "$ROOT/弹性力学"/*.docx "$dst"/
  cp "$ROOT/弹性力学"/分章节/*.pdf "$dst"/
  echo "已复制 PDF / Word 到 docs/弹性力学/pdf/"
}

case "${1:-serve}" in
  prepare)
    prepare
    ;;
  build)
    ensure_mkdocs
    prepare
    cd "$ROOT"
    "$MKDOCS" build --clean
    echo "站点已生成：$ROOT/site/index.html"
    ;;
  serve)
    ensure_mkdocs
    prepare
    cd "$ROOT"
    echo "打开 http://localhost:8010 （手机同一 Wi-Fi 用本机 IP:8010）"
    "$MKDOCS" serve -a 0.0.0.0:8010
    ;;
  *)
    echo "用法: bash site.sh [serve|build|prepare]"
    exit 1
    ;;
esac
