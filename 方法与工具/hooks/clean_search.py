"""清理搜索索引里的 LaTeX 源码。

MkDocs 的搜索插件按页面 HTML 抽取文本，MathJax 的公式在索引里仍是
`\\(...\\)` / `\\[...\\]` 源码，搜索结果摘要会直接显示出来。
这里在构建完成后重写 search_index.json，把公式源码去掉。

执行时机：hooks 在插件之后注册，所以 on_post_build 时搜索插件已经写好索引；
`mkdocs serve` 使用的临时站点目录同样会经过这一步。
"""
import json
import os
import re

# 注意：JSON 解析后是单个反斜杠，所以正则里写成 \\\\( ... \\\\) 对应文本 \( ... \)
INLINE_MATH = re.compile(r'\\\(.*?\\\)', re.S)
DISPLAY_BRACKET = re.compile(r'\\\[.*?\\\]', re.S)
DISPLAY_DOLLAR = re.compile(r'\$\$.*?\$\$', re.S)


def clean(text: str) -> str:
    for pattern in (DISPLAY_DOLLAR, DISPLAY_BRACKET, INLINE_MATH):
        text = pattern.sub(' … ', text)
    text = re.sub(r'(?:\s*…\s*)+', ' … ', text)  # 连续公式只留一个省略号
    return re.sub(r'\s+', ' ', text).strip()


def on_post_build(config, **kwargs):
    path = os.path.join(config.site_dir, 'search', 'search_index.json')
    if not os.path.exists(path):
        return

    with open(path, encoding='utf-8') as f:
        data = json.load(f)

    changed = 0
    for doc in data.get('docs', []):
        for field in ('title', 'text'):
            value = doc.get(field)
            if not value:
                continue
            cleaned = clean(value)
            if cleaned != value:
                doc[field] = cleaned
                changed += 1

    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, separators=(',', ':'))

    print(f'[clean_search] 清理了 {changed} 处公式源码')
