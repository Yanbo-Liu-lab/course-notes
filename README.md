# 知枢

大三专业课笔记。把每门课的复习资料整理成**可检索、可离线阅读的笔记**，同时保留生成它们的完整方法（提示词、脚本、排版流水线），方便换科目时直接复用。

## 已收录

| 科目 | 教材 / 范围 | 版本 | 篇幅 |
|---|---|---|---|
| [弹性力学](docs/弹性力学/) | 吴家龙《弹性力学》（第 3 版）第 1–7 章 | 自适应结构版 | A4，85 页 |

## 阅读站点

站点用 MkDocs Material 构建，内容来自 `docs/` 里的 Markdown，和 PDF 是同一份内容。

```bash
bash site.sh serve    # 首次运行自动建 .venv 装依赖，然后打开 http://localhost:8010
bash site.sh build    # 只生成静态站点到 site/
```

- 手机和电脑连同一 Wi-Fi 时，用 `本机 IP:8010` 访问；
- 不想跑服务时，也可以直接打开 `弹性力学/` 里的 PDF；
- Word 版目录是域代码，首次打开若页码为空，按 `Ctrl+A` → `F9` 更新。

部署成公开站点有三种方式，按省事程度排列：

1. **GitHub Pages**（和参考站一样的路子）：见下方「部署到 GitHub Pages」。
2. **自己的服务器**：`bash site.sh build` 后把 `site/` 丢给 nginx，配好域名和 HTTPS 即可。大陆服务器绑定域名需要备案。
3. **只自己看**：本地 `bash site.sh serve`，不需要任何托管。

> Gitee 适合放源码和 PDF，但不适合直接托管静态站（Pages 政策不稳定），所以站点部署走 GitHub Pages 或自有服务器。

### 部署到 GitHub Pages

前提：有 GitHub 账号，仓库设为公开（免费 Pages 只支持公开仓库）。

```bash
# 1. 登录 GitHub（按提示在浏览器里授权；国内网络可能需要代理）
gh auth login

# 2. 创建仓库并推送；把 <用户名> 换成你的 GitHub 用户名
gh repo create course-notes --public --source=. --remote=github --push

# 如果仓库已经在网页上建好了，则用：
# git remote add github https://github.com/<用户名>/course-notes.git
# git push -u github master
```

推送后：

1. 打开仓库 **Settings → Pages**；
2. 把 **Build and deployment → Source** 设为 **GitHub Actions**；
3. 到 **Actions** 页面等 `构建并部署站点` 跑完；
4. 访问 `https://<用户名>.github.io/course-notes/`。

`configure-pages` 会尝试自动启用 Pages；如果 Settings 里还是 disabled，手动切到 GitHub Actions 即可。之后每次 `git push` 到 `master` 或 `main` 都会自动重新部署。

国内访问 GitHub Pages 不稳定时，可以像参考站一样用浙大 WebVPN 打开。

## 目录结构

```
course-notes/
├── mkdocs.yml                阅读站点配置（MkDocs Material）
├── site.sh                   预览 / 构建站点
├── overrides/home.html       首页模板（Hero 与公式版式）
├── docs/                     站点内容，同时也是笔记源文件
│   ├── index.md              首页（站点介绍 + 课程目录）
│   ├── 弹性力学/
│   │   ├── index.md          科目页（章节目录 + 下载）
│   │   ├── ch1.md … ch7.md   各章正文
│   │   └── pdf/              构建时复制的 PDF/Word（不进 git）
│   ├── assets/favicon.svg    站点图标
│   ├── javascripts/          MathJax 配置
│   └── stylesheets/          纸墨配色与排版
├── 弹性力学/                 成品：整本 PDF、DOCX、分章节 PDF
├── 方法与工具/               生成与排版流水线
│   ├── 制作流程.md
│   ├── prompts/              提示词模板 + 大纲写法
│   ├── configs/              每门课一份配置（章节行号、各章大纲）
│   ├── scripts/              生成与排版脚本
│   └── latex/                中文 LaTeX 模板
└── .github/workflows/        GitHub Pages 自动部署
```

## 给下一门课复用

1. 把教材 OCR 成纯文本，按章记录行号；
2. 仿照 `方法与工具/configs/elasticity.json` 新建配置，**为每章单独写大纲**（不要套固定模板）；
3. 跑 `scripts/summarize.py` 逐章生成到 `docs/<科目>/`，再人工审校公式与适用条件；
4. 跑 `scripts/render_all.sh` 生成 docx / PDF；
5. 在 `mkdocs.yml` 的 `nav` 里加科目和章节，`bash site.sh serve` 预览。

细节、命令与常见问题见 [方法与工具/制作流程.md](方法与工具/制作流程.md)。

## 说明

- 教材原文（OCR 文本、扫描件）**不在仓库内**：一是受版权保护，二是体积大。仓库只放自己整理的总结、提示词和脚本。
- 总结是个人复习梳理，不能替代教材；公式、结论与符号以教材为准。
- `方法与工具/scripts/update_toc.py` 依赖 LibreOffice + python3-uno，可选；不装也能在 Word 里手动更新目录。
- 站点依赖的 `docs/*/pdf/` 是生成目录，已被 git 忽略；`bash site.sh serve|build` 会自动准备。
