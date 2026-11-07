#!/usr/bin/env python3
"""逐章生成知识点总结（配置驱动，可复用到其他科目）。

用法:
    python3 summarize.py configs/elasticity.json              # 生成配置里的全部章节
    python3 summarize.py configs/elasticity.json ch2 ch3      # 只生成指定章节
    python3 summarize.py configs/elasticity.json --dry-run    # 只检查提示词长度，不调用模型

配置里 llm.cmd 是一个命令列表，其中必须有一个元素包含 {prompt}，运行时会替换成
完整提示词。默认按 deeptutor 的 JSON 事件流解析；换成别的 CLI 时把
llm.response_mode 设为 "stdout"，直接取标准输出。

配置说明见同目录 ../configs/elasticity.json 顶部字段。
"""
import argparse
import json
import os
import subprocess
import sys


def resolve(base, path):
    """相对路径以配置文件所在目录为基准。"""
    return path if os.path.isabs(path) else os.path.normpath(os.path.join(base, path))


def load_config(path):
    with open(path, encoding='utf-8') as f:
        return json.load(f)


def build_prompt(cfg, template, lines, ch):
    """把模板占位符替换成实际内容，再拼上本章原文。"""
    outline = '\n'.join(ch['outline'])
    rules = '\n'.join(f'- {r}' for r in cfg.get('subject_rules', []))
    body = (template
            .replace('{book}', cfg['book'])
            .replace('{edition}', cfg['edition'])
            .replace('{outline}', outline)
            .replace('{subject_rules}', rules))

    start, end = ch['start_line'], ch['end_line']
    if not (1 <= start <= end <= len(lines)):
        raise ValueError(
            f"{ch['key']}: 行号越界 start={start} end={end} 总行数={len(lines)}")
    source = ''.join(lines[start - 1:end])

    return (f"{body}\n\n【章节原文】\n"
            f"《{cfg['book']}》（{cfg['edition']}）{ch['title']}\n\n"
            f"{source}\n\n【输出】只输出总结正文，不要输出思考过程、不要复述指令。")


def call_llm(llm, prompt):
    cmd = [part.replace('{prompt}', prompt) for part in llm['cmd']]
    if not any('{prompt}' in part for part in llm['cmd']):
        raise ValueError('llm.cmd 里没有 {prompt} 占位符')

    proc = subprocess.run(
        cmd, cwd=llm.get('cwd') or None, capture_output=True, text=True,
        timeout=llm.get('timeout', 2400))
    mode = llm.get('response_mode', 'deeptutor_json')

    if mode == 'stdout':
        resp = proc.stdout.strip()
    else:
        resp = None
        for line in proc.stdout.splitlines():
            line = line.strip()
            if not line.startswith('{'):
                continue
            try:
                event = json.loads(line)
            except json.JSONDecodeError:
                continue
            if event.get('type') == 'result':
                resp = (event.get('metadata') or {}).get('response') or event.get('content')

    if not resp:
        print('没有拿到模型回答。stderr 末尾：', file=sys.stderr)
        print(proc.stderr[-1000:], file=sys.stderr)
        print('stdout 末尾：', file=sys.stderr)
        print(proc.stdout[-1000:], file=sys.stderr)
        sys.exit(1)
    return resp


def main():
    parser = argparse.ArgumentParser(description='逐章生成知识点总结')
    parser.add_argument('config', help='配置文件路径，如 configs/elasticity.json')
    parser.add_argument('chapters', nargs='*', help='只生成这些章，如 ch2 ch3；省略则全部')
    parser.add_argument('--dry-run', action='store_true', help='只拼提示词，不调用模型')
    args = parser.parse_args()

    cfg_path = os.path.abspath(args.config)
    cfg_dir = os.path.dirname(cfg_path)
    cfg = load_config(cfg_path)

    template_path = resolve(cfg_dir, cfg['template'])
    with open(template_path, encoding='utf-8') as f:
        template = f.read()

    with open(resolve(cfg_dir, cfg['source_txt']), encoding='utf-8') as f:
        lines = f.read().splitlines(keepends=True)

    outdir = resolve(cfg_dir, cfg['output_dir'])
    os.makedirs(outdir, exist_ok=True)

    wanted = set(args.chapters)
    for ch in cfg['chapters']:
        if wanted and ch['key'] not in wanted:
            continue
        prompt = build_prompt(cfg, template, lines, ch)
        out = os.path.join(outdir, f"{ch['key']}.md")
        print(f"[{ch['key']}] {ch['title']}  原文 {len(prompt)} 字符 → {out}", flush=True)

        if args.dry_run:
            continue

        resp = call_llm(cfg['llm'], prompt)
        with open(out, 'w', encoding='utf-8') as f:
            f.write(resp)
        print(f"[{ch['key']}] 已写入 {len(resp)} 字符", flush=True)

    if args.dry_run:
        print('dry-run 完成，未调用模型。')


if __name__ == '__main__':
    main()
