window.MathJax = {
  tex: {
    inlineMath: [["\\(", "\\)"], ["$", "$"]],
    displayMath: [["$$", "$$"], ["\\[", "\\]"]],
    processEscapes: true,
    tags: "none",
    tagSide: "right",
    tagIndent: "0.8em"
  },
  options: {
    ignoreHtmlClass: "no-mathjax",
    processHtmlClass: "arithmatex|md-nav__link|md-nav__title"
  }
};

// 等 MathJax 真正加载完成再排版；Material 的即时导航会再次触发 document$
function whenMathJax(fn) {
  if (window.MathJax && MathJax.startup && MathJax.startup.promise) {
    MathJax.startup.promise.then(fn);
  } else {
    setTimeout(() => whenMathJax(fn), 100);
  }
}

// 章节标题里的 LaTeX 会原样出现在目录里，单独再排一次
function typesetNav() {
  const navMath = Array.from(
    document.querySelectorAll(".md-nav__link, .md-nav__title")
  ).filter((el) => el.textContent.includes("\\("));
  if (navMath.length) {
    MathJax.typesetPromise(navMath);
  }
}

document$.subscribe(() => {
  whenMathJax(() => {
    MathJax.startup.output.clearCache();
    MathJax.typesetClear();
    MathJax.texReset();
    MathJax.typesetPromise().then(typesetNav);
  });
});
