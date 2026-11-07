# 方法与工具

这套东西用来把教材文本变成可打印的知识点总结，换科目时只改配置，不改脚本。

```
方法与工具/
├── 制作流程.md          完整步骤 + 常见坑
├── prompts/
│   ├── 总结提示词模板.md  主提示词（{book} {edition} {outline} {subject_rules} 四个占位符）
│   └── 大纲怎么写.md      每章大纲的写法与示例
├── configs/
│   └── elasticity.json   弹性力学的配置（章节行号 + 各章大纲 + 模型命令）
├── hooks/
│   └── clean_search.py   构建后清理搜索索引里的 LaTeX 源码
├── scripts/
│   ├── summarize.py      按配置逐章生成 Markdown
│   ├── make_ref.py       生成中文 Word 参考模板 ref_zh.docx
│   ├── normalize_md.py   给列表前后补空行
│   ├── convert_chapter.sh 单章 Markdown → docx（Word 原生公式）
│   ├── fix_tables.py     按内容重算表格列宽
│   ├── build_pdf.sh      单章 Markdown → PDF（xelatex）
│   ├── merge_md.py       合并整本（docx 目录域 / pdf 分页）
│   ├── render_all.sh     一键：单章 docx+pdf + 合并版 docx+pdf
│   └── update_toc.py     可选：用 LibreOffice 自动更新 Word 目录
├── latex/
│   ├── header_zh.tex     中文标题与列表间距
│   └── template_zh.tex   整本 PDF 的封面/目录/页码模板
└── ref_base.docx         Word 模板基底（make_ref.py 的输入）
```

先读 [制作流程.md](制作流程.md)。新科目从复制 [`configs/elasticity.json`](configs/elasticity.json) 开始改。

阅读站点不在这里：配置在仓库根目录的 `mkdocs.yml`，内容在 `docs/`，根目录 `site.sh` 负责预览和构建。
