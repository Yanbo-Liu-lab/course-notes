/* 轻量动效：滚动显现、卡片指针倾斜、章节阅读进度。
   所有效果都尊重 prefers-reduced-motion；即时导航时先清理再重新绑定。 */

(() => {
  "use strict";

  const reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)");
  const canHover = window.matchMedia("(hover: hover) and (pointer: fine)");

  let revealObserver = null;
  let progressEl = null;
  let onScroll = null;
  let onResize = null;
  let scrollFrame = 0;
  let tiltCleanups = [];

  function cleanup() {
    if (revealObserver) {
      revealObserver.disconnect();
      revealObserver = null;
    }
    if (onScroll) {
      window.removeEventListener("scroll", onScroll);
      onScroll = null;
    }
    if (onResize) {
      window.removeEventListener("resize", onResize);
      onResize = null;
    }
    if (progressEl) {
      progressEl.remove();
      progressEl = null;
    }
    if (scrollFrame) {
      cancelAnimationFrame(scrollFrame);
      scrollFrame = 0;
    }
    tiltCleanups.forEach((fn) => fn());
    tiltCleanups = [];
  }

  /* 下方元素进入视口时淡入上移；首屏元素保持静止，避免闪烁 */
  function initReveal() {
    if (reduceMotion.matches || !("IntersectionObserver" in window)) return;

    const items = Array.from(
      document.querySelectorAll(
        ".chapter-item, .download-item, .subject-meta"
      )
    ).filter((el) => el.getBoundingClientRect().top > window.innerHeight * 0.88);

    if (!items.length) return;

    document.documentElement.classList.add("motion-ready");
    items.forEach((el, index) => {
      el.classList.add("reveal");
      el.style.setProperty("--reveal-delay", `${Math.min(index * 35, 210)}ms`);
    });

    revealObserver = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (!entry.isIntersecting) return;
          entry.target.classList.add("is-visible");
          revealObserver.unobserve(entry.target);
        });
      },
      { threshold: 0.12, rootMargin: "0px 0px -4% 0px" }
    );

    items.forEach((el) => revealObserver.observe(el));
  }

  /* 课程卡片跟随指针做很小的 3D 倾斜 */
  function initTilt() {
    if (reduceMotion.matches || !canHover.matches) return;

    document.querySelectorAll(".course-card").forEach((card) => {
      const inner = card.querySelector(".course-card__inner");
      if (!inner) return;

      let rect = null;
      let frame = 0;

      const enter = () => {
        rect = card.getBoundingClientRect();
        inner.classList.add("is-tilting");
      };

      const move = (event) => {
        if (!rect) return;
        const x = (event.clientX - rect.left) / rect.width - 0.5;
        const y = (event.clientY - rect.top) / rect.height - 0.5;
        cancelAnimationFrame(frame);
        frame = requestAnimationFrame(() => {
          const ry = (x * 2).toFixed(2);
          const rx = (-y * 2).toFixed(2);
          inner.style.transform = `perspective(900px) rotateX(${rx}deg) rotateY(${ry}deg)`;
        });
      };

      const leave = () => {
        rect = null;
        cancelAnimationFrame(frame);
        inner.classList.remove("is-tilting");
        inner.style.transform = "";
      };

      card.addEventListener("pointerenter", enter);
      card.addEventListener("pointermove", move);
      card.addEventListener("pointerleave", leave);
      tiltCleanups.push(() => {
        card.removeEventListener("pointerenter", enter);
        card.removeEventListener("pointermove", move);
        card.removeEventListener("pointerleave", leave);
      });
    });
  }

  /* 非首页显示顶部阅读进度 */
  function initProgress() {
    if (document.querySelector(".home-body")) return;

    progressEl = document.createElement("div");
    progressEl.className = "reading-progress";
    progressEl.setAttribute("aria-hidden", "true");
    document.body.appendChild(progressEl);

    const update = () => {
      scrollFrame = 0;
      const max = document.documentElement.scrollHeight - window.innerHeight;
      const ratio = max > 0 ? Math.min(1, Math.max(0, window.scrollY / max)) : 0;
      progressEl.style.transform = `scaleX(${ratio})`;
    };

    onScroll = () => {
      if (!scrollFrame) scrollFrame = requestAnimationFrame(update);
    };
    onResize = onScroll;

    window.addEventListener("scroll", onScroll, { passive: true });
    window.addEventListener("resize", onResize);
    update();
  }

  function start() {
    cleanup();
    if (reduceMotion.matches) {
      document.documentElement.classList.remove("motion-ready");
    }
    initReveal();
    initTilt();
    initProgress();
  }

  if (window.document$ && typeof window.document$.subscribe === "function") {
    window.document$.subscribe(start);
  } else {
    document.addEventListener("DOMContentLoaded", start);
  }
})();
