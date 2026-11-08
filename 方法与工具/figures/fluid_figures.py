#!/usr/bin/env python3
"""Generate paper-and-ink style figures for the fluid mechanics notes.

Usage: python fluid_figures.py [ch1 ch2 ...]
Output: docs/流体力学/images/*.png
"""
import os
import sys

import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import (
    FancyArrowPatch, Rectangle, Polygon, Circle, Arc, Ellipse, Wedge,
)

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
OUT = os.path.join(ROOT, "docs", "流体力学", "images")
os.makedirs(OUT, exist_ok=True)

PAPER = "#f8f7f3"
INK = "#1b1e1c"
INK2 = "#4d534e"
MUTED = "#7a817a"
RULE = "#deddd5"
ACCENT = "#2f5d50"
ACCENT_L = "#e7efe9"
ACCENT_M = "#9cc3b2"

plt.rcParams.update({
    "font.family": "sans-serif",
    "font.sans-serif": [
        "Noto Sans CJK SC", "Source Han Sans SC", "Microsoft YaHei", "DejaVu Sans",
    ],
    "axes.unicode_minus": False,
    "font.size": 9.5,
    "mathtext.fontset": "dejavusans",
    "figure.facecolor": PAPER,
    "savefig.facecolor": PAPER,
    "savefig.dpi": 220,
})


def save(fig, name):
    path = os.path.join(OUT, name)
    fig.savefig(path, dpi=220, bbox_inches="tight", pad_inches=0.12,
                facecolor=PAPER)
    plt.close(fig)
    print("wrote", path)


def arrow(ax, p1, p2, color=INK2, lw=1.1, ms=9, ls="-", z=4, shrink=0):
    ax.add_patch(FancyArrowPatch(
        p1, p2, arrowstyle="-|>", mutation_scale=ms, lw=lw, color=color,
        linestyle=ls, shrinkA=shrink, shrinkB=shrink, zorder=z,
    ))


def label(ax, x, y, s, size=9, color=INK2, ha="center", va="center", **kw):
    ax.text(x, y, s, fontsize=size, color=color, ha=ha, va=va, zorder=8, **kw)


def panel(ax, s):
    ax.text(0.02, 0.98, s, transform=ax.transAxes, fontsize=9,
            color=MUTED, ha="left", va="top", zorder=9,
            bbox=dict(facecolor=PAPER, edgecolor="none", pad=1.2))


def caption(ax, s, y=-0.10):
    ax.text(0.5, y, s, transform=ax.transAxes, fontsize=8.3,
            color=MUTED, ha="center", va="top", zorder=9)


def blank(ax, xlim, ylim, equal=True):
    ax.set_xlim(*xlim)
    ax.set_ylim(*ylim)
    if equal:
        ax.set_aspect("equal", adjustable="box")
    ax.axis("off")


def open_axes(ax):
    for side in ("top", "right"):
        ax.spines[side].set_visible(False)
    for side in ("left", "bottom"):
        ax.spines[side].set_color(INK2)
        ax.spines[side].set_linewidth(0.9)
    ax.tick_params(labelsize=8, colors=MUTED, width=0.8, length=3)


def wall_hatch(ax, x0, x1, y, direction=-1, n=14):
    ax.plot([x0, x1], [y, y], color=INK, lw=1.8, zorder=3)
    for x in np.linspace(x0, x1, n):
        ax.plot([x, x - 0.1], [y, y + direction * 0.13],
                color=MUTED, lw=0.7, zorder=2)


# ============================================================
# Chapter 1
# ============================================================

def fig_ch1_viscosity():
    fig, axes = plt.subplots(1, 2, figsize=(8.6, 3.4),
                             gridspec_kw={"width_ratios": [1.08, 1]})

    ax = axes[0]
    blank(ax, (0, 4.35), (0, 3.4))
    ax.add_patch(Rectangle((0.5, 0.45), 3.2, 2.1, facecolor=ACCENT_L,
                           edgecolor="none", zorder=0))
    wall_hatch(ax, 0.5, 3.7, 0.45, direction=-1)
    ax.plot([0.5, 3.7], [2.55, 2.55], color=INK, lw=1.8, zorder=3)

    for y in np.linspace(0.55, 2.45, 6):
        x0 = 0.75
        x1 = x0 + 0.55 * (y - 0.45) / 2.1
        arrow(ax, (x0, y), (x1, y), color=INK2, lw=0.9, ms=7)

    ys = np.linspace(0.45, 2.55, 60)
    xs = 0.75 + 0.55 * (ys - 0.45) / 2.1
    ax.plot(xs, ys, color=ACCENT, lw=1.1, ls=(0, (4, 3)), zorder=5)

    arrow(ax, (2.0, 2.8), (3.05, 2.8), color=ACCENT, lw=1.4, ms=10)
    label(ax, 3.16, 2.8, r"$U$", color=ACCENT, ha="left")
    label(ax, 1.55, 2.88, "运动上板", size=8.5, color=MUTED)
    label(ax, 1.55, 0.14, "静止下板（无滑移）", size=8.5, color=MUTED)
    label(ax, 0.52, 3.12, r"$\tau=\mu\,\mathrm{d}u/\mathrm{d}y$",
          size=11.5, color=INK, ha="left")

    arrow(ax, (3.95, 0.45), (3.95, 2.55), color=MUTED, lw=0.8, ms=7)
    label(ax, 4.08, 1.5, r"$y$", color=MUTED, ha="left")
    label(ax, 3.78, 0.45, "0", color=MUTED, ha="left", va="top")
    label(ax, 1.35, 1.6, "速度剖面", size=8.5, color=ACCENT)
    panel(ax, "(a)")

    ax = axes[1]
    ax.set_xlim(0, 2.9)
    ax.set_ylim(0, 2.35)
    open_axes(ax)
    x = np.linspace(0, 2.8, 120)
    ax.plot(x, 0.70 * x, color=ACCENT, lw=1.7, label="牛顿流体")
    ax.plot(x, 1.42 * (1 - np.exp(-x / 1.05)), color=INK2, lw=1.4,
            ls=(0, (5, 2.5)), label="剪切变稀")
    ax.plot(x, 0.11 * x ** 1.7, color=MUTED, lw=1.4,
            ls=(0, (1.6, 2.2)), label="剪切增稠")
    ax.set_xlabel(r"切变率 $\mathrm{d}u/\mathrm{d}y$", color=INK2, fontsize=9)
    ax.set_ylabel(r"切应力 $\tau$", color=INK2, fontsize=9)
    ax.legend(frameon=False, fontsize=8, loc="upper left",
              handlelength=2.2, labelcolor=INK2)
    ax.text(0.98, 0.98, "(b)", transform=ax.transAxes, fontsize=9,
            color=MUTED, ha="right", va="top", zorder=9)
    save(fig, "ch1_viscosity.png")


def fig_ch1_lines():
    fig, axes = plt.subplots(1, 3, figsize=(9.8, 2.9))
    fig.subplots_adjust(wspace=0.08)

    ax = axes[0]
    blank(ax, (0, 3.0), (0, 2.4))
    t = np.linspace(0, 1, 160)
    x = 0.3 + 2.1 * t
    y = 0.45 + 1.25 * t + 0.22 * np.sin(2.6 * np.pi * t)
    ax.plot(x, y, color=INK2, lw=1.4)
    for tt, name in ((0.12, r"$t_1$"), (0.5, r"$t_2$"), (0.86, r"$t_3$")):
        i = int(tt * (len(t) - 1))
        ax.plot(x[i], y[i], "o", ms=4.5, color=ACCENT, zorder=6)
        label(ax, x[i] + 0.05, y[i] + 0.14, name, size=9, color=ACCENT,
              ha="left")
    arrow(ax, (x[-8], y[-8]), (x[-1], y[-1]), color=ACCENT, lw=1.2, ms=9)
    caption(ax, "迹线：同一质点的历史")
    panel(ax, "(a)")

    ax = axes[1]
    X, Y = np.meshgrid(np.linspace(0, 3, 90), np.linspace(0, 2.3, 70))
    U = np.ones_like(X)
    V = 0.55 * np.sin(np.pi * X / 3) * np.cos(np.pi * Y / 2.3)
    ax.streamplot(X, Y, U, V, density=0.9, linewidth=0.65, color=INK2,
                  arrowsize=0.7)
    ax.set_xlim(0, 3)
    ax.set_ylim(0, 2.3)
    ax.set_aspect("equal")
    ax.axis("off")
    caption(ax, "流线：同一时刻的速度方向")
    ax.text(0.98, 0.98, "(b)", transform=ax.transAxes, fontsize=9,
            color=MUTED, ha="right", va="top", zorder=9,
            bbox=dict(facecolor=PAPER, edgecolor="none", pad=1.2))

    ax = axes[2]
    blank(ax, (0, 3.0), (0, 2.4))
    sx, sy = 0.35, 1.18
    ax.plot(sx, sy, "o", ms=5, color=ACCENT, zorder=6)
    label(ax, sx, sy + 0.18, "源点", size=8.5, color=ACCENT)
    t = np.linspace(0, 1, 160)
    x = sx + 2.25 * t
    y = sy + 0.55 * t + 0.25 * np.sin(2.2 * np.pi * t)
    ax.plot(x, y, color=INK2, lw=1.4)
    for tt in (0.25, 0.55, 0.82):
        i = int(tt * (len(t) - 1))
        ax.plot(x[i], y[i], "o", ms=4, color=ACCENT, zorder=6)
    arrow(ax, (x[-8], y[-8]), (x[-1], y[-1]), color=ACCENT, lw=1.2, ms=9)
    caption(ax, "脉线：同一源点的连续染色")
    panel(ax, "(c)")
    save(fig, "ch1_lines.png")


# ============================================================
# Chapter 2
# ============================================================

def fig_ch2_pressure():
    fig, axes = plt.subplots(1, 2, figsize=(8.8, 3.7),
                             gridspec_kw={"width_ratios": [1.05, 1]})

    ax = axes[0]
    blank(ax, (0, 4.7), (0, 3.9))
    ax.plot([0.6, 0.6], [0.5, 2.9], color=INK, lw=1.6)
    ax.plot([3.6, 3.6], [0.5, 2.9], color=INK, lw=1.6)
    ax.plot([0.6, 3.6], [0.5, 0.5], color=INK, lw=1.6)
    ax.add_patch(Polygon([(0.6, 0.5), (3.6, 0.5), (3.6, 2.7), (0.6, 2.7)],
                         closed=True, facecolor=ACCENT_L, edgecolor="none",
                         zorder=0))
    ax.plot([0.6, 3.6], [2.7, 2.7], color=ACCENT, lw=1.2, zorder=3)
    label(ax, 1.15, 2.82, "自由液面", size=8.5, color=ACCENT)
    arrow(ax, (2.9, 3.3), (2.9, 2.76), color=MUTED, lw=0.9, ms=8)
    label(ax, 2.9, 3.43, r"$p_0$", size=10, color=MUTED)
    label(ax, 0.62, 3.62, r"$p=p_0+\rho g h$", size=11, color=INK, ha="left")

    for y in np.linspace(0.72, 2.5, 6):
        length = 0.25 + 0.55 * (2.7 - y) / 2.2
        arrow(ax, (3.58 - length, y), (3.56, y), color=ACCENT, lw=1.0, ms=7)

    arrow(ax, (3.95, 0.5), (3.95, 2.7), color=MUTED, lw=0.8, ms=7)
    label(ax, 4.1, 1.6, r"$h$", size=10, color=MUTED, ha="left")
    caption(ax, "壁面压强随深度线性增大")
    panel(ax, "(a)")

    ax = axes[1]
    blank(ax, (0, 4.2), (0, 3.55))
    # vessel + tap
    ax.plot([0.3, 0.3, 0.85, 0.85], [2.55, 2.95, 2.95, 2.75],
            color=INK2, lw=1.1)
    label(ax, 0.55, 3.14, r"$p$", size=11, color=INK)
    label(ax, 0.72, 2.45, "接压力", size=8.3, color=MUTED, ha="right")
    # U-shaped fluid band (left level 2.15, right level 2.55)
    band = [(0.85, 2.15), (0.85, 0.7), (3.15, 0.7), (3.15, 2.55),
            (2.7, 2.55), (2.7, 1.2), (1.3, 1.2), (1.3, 2.15)]
    ax.add_patch(Polygon(band, closed=True, facecolor=ACCENT_L,
                         edgecolor=INK2, lw=1.0, zorder=1))
    ax.plot([0.85, 1.3], [2.15, 2.15], color=ACCENT, lw=1.3, zorder=2)
    ax.plot([2.7, 3.15], [2.55, 2.55], color=ACCENT, lw=1.3, zorder=2)
    ax.plot([0.85, 0.85], [2.15, 2.75], color=INK2, lw=1.0)
    arrow(ax, (3.35, 3.2), (3.35, 2.62), color=MUTED, lw=0.9, ms=8)
    label(ax, 3.35, 3.32, r"$p_a$", size=10, color=MUTED)
    label(ax, 2.0, 0.95, r"$\rho$", size=10, color=INK2)
    ax.plot([1.55, 2.0], [2.15, 2.15], color=MUTED, lw=0.7, ls=(0, (2, 2)))
    ax.plot([1.55, 2.0], [2.55, 2.55], color=MUTED, lw=0.7, ls=(0, (2, 2)))
    arrow(ax, (1.78, 2.15), (1.78, 2.55), color=MUTED, lw=0.8, ms=6)
    label(ax, 1.9, 2.35, r"$h$", size=10, color=MUTED, ha="left")
    label(ax, 1.4, 0.3, r"$p-p_a=\rho g h$", size=11, color=INK)
    caption(ax, "U 形管测压：液面差对应压强差")
    panel(ax, "(b)")
    save(fig, "ch2_pressure.png")


def fig_ch2_gate():
    fig, axes = plt.subplots(1, 2, figsize=(8.8, 3.5))

    ax = axes[0]
    blank(ax, (0, 4.3), (0, 3.5))
    # water region and curved gate
    ax.add_patch(Polygon([(0.5, 0.6), (3.2, 0.6), (3.2, 2.8), (0.5, 2.8)],
                         closed=True, facecolor=ACCENT_L, edgecolor="none",
                         zorder=0))
    ax.plot([0.5, 0.5], [0.6, 2.8], color=INK, lw=1.4)
    ax.plot([0.5, 3.2], [2.8, 2.8], color=ACCENT, lw=1.1)
    theta = np.linspace(0, np.pi / 2, 80)
    cx, cy, r = 3.2, 0.6, 2.2
    gx = cx - r * np.cos(theta)
    gy = cy + r * np.sin(theta)
    ax.plot(gx, gy, color=INK, lw=2.4, zorder=5)
    label(ax, 1.0, 2.9, "水", size=9, color=ACCENT)
    # force components
    arrow(ax, (2.55, 1.15), (3.6, 1.15), color=ACCENT, lw=1.2, ms=9)
    label(ax, 3.65, 1.15, r"$F_x$", size=10, color=ACCENT, ha="left",
          bbox=dict(facecolor=PAPER, edgecolor="none", pad=1))
    arrow(ax, (2.55, 1.15), (2.55, 2.15), color=ACCENT, lw=1.2, ms=9)
    label(ax, 2.7, 2.3, r"$F_y$", size=10, color=ACCENT,
          bbox=dict(facecolor=PAPER, edgecolor="none", pad=1))
    arrow(ax, (2.55, 1.15), (3.35, 1.75), color=INK2, lw=1.3, ms=9,
          ls=(0, (3, 2)))
    label(ax, 3.45, 1.8, r"$F$", size=10, color=INK2, ha="left",
          bbox=dict(facecolor=PAPER, edgecolor="none", pad=1))
    caption(ax, "曲面总压力：分力求合力")
    panel(ax, "(a)")

    ax = axes[1]
    blank(ax, (0, 4.2), (0, 3.3))
    ax.add_patch(Rectangle((0.4, 0.4), 3.4, 1.8, facecolor=ACCENT_L,
                           edgecolor="none", zorder=0))
    ax.plot([0.4, 3.8], [2.2, 2.2], color=ACCENT, lw=1.1)
    ax.add_patch(Rectangle((1.3, 1.55), 1.5, 0.95, facecolor=PAPER,
                           edgecolor=INK, lw=1.2, zorder=3))
    label(ax, 2.05, 2.02, "浮体", size=9, color=INK2)
    ax.plot([1.3, 2.8], [1.55, 1.55], color=MUTED, lw=0.8, ls=(0, (2, 2)))
    arrow(ax, (2.05, 1.25), (2.05, 0.55), color=INK2, lw=1.1, ms=8)
    label(ax, 2.18, 0.82, r"$G$", size=10, color=INK2, ha="left")
    arrow(ax, (2.05, 1.1), (2.05, 1.8), color=ACCENT, lw=1.2, ms=9)
    label(ax, 2.18, 1.75, r"$F_b$", size=10, color=ACCENT, ha="left")
    label(ax, 0.55, 2.75, r"$F_b=\rho g V_{\mathrm{disp}}$", size=11,
          color=INK, ha="left")
    caption(ax, "阿基米德原理：浮力等于排开液体的重量")
    panel(ax, "(b)")
    save(fig, "ch2_gate.png")


# ============================================================
# Chapter 3
# ============================================================

def fig_ch3_control_volume():
    fig, axes = plt.subplots(1, 2, figsize=(8.8, 3.5))

    ax = axes[0]
    blank(ax, (0, 4.4), (0, 3.4))
    ax.add_patch(Rectangle((1.0, 0.8), 2.2, 1.6, fill=False,
                           edgecolor=MUTED, lw=1.2, ls=(0, (4, 3))))
    label(ax, 2.1, 2.55, "控制体（固定）", size=8.5, color=MUTED)
    ax.add_patch(Polygon([(0.5, 1.0), (2.4, 1.0), (2.4, 2.0), (0.5, 2.0)],
                         closed=True, fill=False, edgecolor=ACCENT, lw=1.4))
    label(ax, 1.2, 2.13, "系统 $t$", size=9, color=ACCENT)
    ax.add_patch(Polygon([(1.2, 0.9), (3.1, 0.9), (3.1, 1.9), (1.2, 1.9)],
                         closed=True, fill=False, edgecolor=INK2, lw=1.2,
                         ls=(0, (2, 2))))
    label(ax, 2.55, 1.78, r"系统 $t+\Delta t$", size=9, color=INK2)
    arrow(ax, (0.15, 1.5), (0.85, 1.5), color=INK2, lw=1.1, ms=8)
    arrow(ax, (3.2, 1.4), (4.05, 1.4), color=INK2, lw=1.1, ms=8)
    label(ax, 0.5, 1.65, "流入", size=8, color=MUTED)
    label(ax, 3.65, 1.55, "流出", size=8, color=MUTED)
    panel(ax, "(a)")

    ax = axes[1]
    blank(ax, (0, 4.4), (0, 3.4))
    ax.add_patch(Rectangle((1.2, 0.9), 2.0, 1.5, fill=False,
                           edgecolor=ACCENT, lw=1.6, ls=(0, (5, 3))))
    label(ax, 2.2, 2.55, "控制体", size=9, color=ACCENT)
    arrow(ax, (0.25, 1.6), (1.15, 1.6), color=INK2, lw=1.2, ms=9)
    arrow(ax, (3.25, 1.6), (4.15, 1.6), color=INK2, lw=1.2, ms=9)
    label(ax, 0.7, 1.78, r"$\mathbf{V}_1$", size=10, color=INK2)
    label(ax, 3.7, 1.78, r"$\mathbf{V}_2$", size=10, color=INK2)
    # normals
    arrow(ax, (1.2, 1.6), (0.95, 1.6), color=MUTED, lw=0.8, ms=7)
    arrow(ax, (3.2, 1.6), (3.45, 1.6), color=MUTED, lw=0.8, ms=7)
    label(ax, 1.08, 1.35, r"$\mathbf{n}$", size=9, color=MUTED)
    label(ax, 3.34, 1.35, r"$\mathbf{n}$", size=9, color=MUTED)
    arrow(ax, (2.2, 1.55), (2.2, 2.2), color=MUTED, lw=0.9, ms=8)
    label(ax, 2.2, 2.32, r"$\mathbf{f}$", size=10, color=MUTED)
    label(ax, 0.55, 0.5, r"$\frac{\mathrm{d}}{\mathrm{d}t}\int_{CV}\rho B\,\mathrm{d}V"
          r"+\oint_{CS}\rho B(\mathbf{V}\cdot\mathbf{n})\,\mathrm{d}A"
          r"=\int_{CV}\rho\,\frac{\mathrm{D}B}{\mathrm{D}t}\,\mathrm{d}V$",
          size=9.5, color=INK, ha="left")
    panel(ax, "(b)")
    save(fig, "ch3_control_volume.png")


def fig_ch3_stress():
    fig, axes = plt.subplots(1, 2, figsize=(8.4, 3.5))

    ax = axes[0]
    blank(ax, (0, 4.2), (0, 3.4))
    ax.add_patch(Rectangle((1.3, 1.0), 1.6, 1.4, facecolor=ACCENT_L,
                           edgecolor=INK, lw=1.2, zorder=2))
    arrow(ax, (2.9, 1.7), (3.55, 1.7), color=ACCENT, lw=1.1, ms=8)
    arrow(ax, (1.3, 1.7), (0.65, 1.7), color=ACCENT, lw=1.1, ms=8)
    label(ax, 3.62, 1.7, r"$\sigma_{xx}$", size=9.5, color=ACCENT, ha="left")
    label(ax, 0.55, 1.7, r"$\sigma_{xx}$", size=9.5, color=ACCENT, ha="right")
    arrow(ax, (2.1, 2.4), (2.1, 3.0), color=ACCENT, lw=1.1, ms=8)
    arrow(ax, (2.1, 1.0), (2.1, 0.4), color=ACCENT, lw=1.1, ms=8)
    label(ax, 2.1, 3.12, r"$\sigma_{yy}$", size=9.5, color=ACCENT)
    label(ax, 2.1, 0.28, r"$\sigma_{yy}$", size=9.5, color=ACCENT)
    arrow(ax, (2.9, 1.35), (2.9, 1.95), color=INK2, lw=1.0, ms=7)
    arrow(ax, (1.3, 1.35), (1.3, 0.75), color=INK2, lw=1.0, ms=7)
    label(ax, 3.05, 1.35, r"$\tau_{xy}$", size=9.5, color=INK2, ha="left")
    label(ax, 1.05, 0.8, r"$\tau_{xy}$", size=9.5, color=INK2, ha="right")
    caption(ax, "一般应力状态（含粘性）：正应力与切应力同时存在")
    panel(ax, "(a)")

    ax = axes[1]
    blank(ax, (0, 4.2), (0, 3.4))
    ax.add_patch(Rectangle((1.3, 1.0), 1.6, 1.4, facecolor=ACCENT_L,
                           edgecolor=INK, lw=1.2, zorder=2))
    for p0, p1 in [((3.45, 1.7), (2.9, 1.7)), ((0.75, 1.7), (1.3, 1.7)),
                   ((2.1, 2.95), (2.1, 2.4)), ((2.1, 0.45), (2.1, 1.0))]:
        arrow(ax, p0, p1, color=ACCENT, lw=1.2, ms=8)
    label(ax, 3.55, 1.7, r"$-p\mathbf{n}$", size=9.5, color=ACCENT,
          ha="left")
    label(ax, 0.65, 1.7, r"$-p\mathbf{n}$", size=9.5, color=ACCENT,
          ha="right")
    label(ax, 2.1, 3.08, r"$-p\mathbf{n}$", size=9.5, color=ACCENT)
    label(ax, 2.1, 0.32, r"$-p\mathbf{n}$", size=9.5, color=ACCENT)
    label(ax, 2.1, 1.7, r"$\mathbf{P}=-p\mathbf{I}$", size=10, color=INK)
    caption(ax, "静止流体 / 运动无粘流体：只有各向等值压力")
    panel(ax, "(b)")
    save(fig, "ch3_stress.png")


# ============================================================
# Chapter 4
# ============================================================

def fig_ch4_bernoulli():
    fig, axes = plt.subplots(1, 2, figsize=(9.0, 3.5),
                             gridspec_kw={"width_ratios": [1.15, 1]})

    ax = axes[0]
    blank(ax, (0, 4.8), (0, 2.9))
    top = [(0.3, 2.1), (1.6, 2.1), (1.9, 1.95), (2.5, 1.95),
           (2.8, 2.1), (4.3, 2.1)]
    bottom = [(4.3, 1.5), (2.8, 1.5), (2.5, 1.65), (1.9, 1.65),
              (1.6, 1.5), (0.3, 1.5)]
    ax.add_patch(Polygon(top + bottom, closed=True, facecolor=ACCENT_L,
                         edgecolor=INK, lw=1.2, zorder=1))
    for x, p in [(1.0, r"$p_1$"), (2.2, r"$p_2$"), (3.6, r"$p_3$")]:
        ax.plot([x, x], [1.4, 2.2], color=MUTED, lw=0.7, ls=(0, (2, 2)))
        label(ax, x, 2.26, p, size=9.5, color=INK2)
    arrow(ax, (0.5, 1.8), (1.35, 1.8), color=INK2, lw=1.1, ms=8)
    arrow(ax, (1.95, 1.8), (2.55, 1.8), color=ACCENT, lw=1.2, ms=8)
    arrow(ax, (3.0, 1.8), (3.9, 1.8), color=INK2, lw=1.1, ms=8)
    label(ax, 0.72, 1.65, r"$V_1$", size=9, color=INK2)
    label(ax, 2.34, 1.65, r"$V_2$", size=9, color=ACCENT)
    label(ax, 3.42, 1.65, r"$V_3$", size=9, color=INK2)
    label(ax, 2.2, 2.48, r"喉部：$A\downarrow,V\uparrow,p\downarrow$",
          size=8.3, color=ACCENT)
    label(ax, 0.45, 0.55, r"$p_1+\frac{1}{2}\rho V_1^2"
          r"=p_2+\frac{1}{2}\rho V_2^2$", size=10, color=INK, ha="left")
    caption(ax, "文丘里管：沿同一条流线，A 减小则 V 增大、p 减小")
    panel(ax, "(a)")

    ax = axes[1]
    blank(ax, (0, 4.2), (0, 3.4))
    for y in (1.0, 1.4, 2.1, 2.5):
        ax.plot([0.2, 3.8], [y, y], color=MUTED, lw=0.6, ls=(0, (2, 2)))
    # Pitot probe: open left end facing the flow, stem down
    ax.plot([1.35, 2.65, 2.65, 2.5, 2.5, 2.15, 2.15, 1.35],
            [1.7, 1.7, 1.45, 1.45, 1.05, 1.05, 1.45, 1.45],
            color=INK, lw=1.4)
    label(ax, 1.25, 1.58, r"$p_0$", size=10, color=ACCENT, ha="right")
    label(ax, 2.85, 1.75, "静压孔", size=8.3, color=MUTED, ha="left")
    label(ax, 2.85, 1.58, r"$p$", size=10, color=INK2, ha="left")
    arrow(ax, (0.5, 2.3), (1.2, 2.3), color=INK2, lw=1.0, ms=8)
    label(ax, 0.85, 2.45, r"$V$", size=9, color=INK2)
    label(ax, 0.45, 0.35, r"$V=\sqrt{2(p_0-p)/\rho}$", size=11,
          color=INK, ha="left")
    caption(ax, "皮托管：驻点压强与静压之差给出速度")
    panel(ax, "(b)")
    save(fig, "ch4_bernoulli.png")


def fig_ch4_momentum():
    fig, axes = plt.subplots(1, 2, figsize=(8.8, 3.5))

    ax = axes[0]
    blank(ax, (0, 4.2), (0, 3.4))
    # 90-degree bend
    ax.plot([0.3, 1.9, 1.9], [1.2, 1.2, 2.8], color=INK, lw=5.0,
            solid_capstyle="butt", alpha=0.18, zorder=1)
    ax.plot([0.3, 1.9, 1.9], [1.2, 1.2, 2.8], color=ACCENT, lw=1.2,
            zorder=2)
    arrow(ax, (0.4, 1.2), (1.2, 1.2), color=ACCENT, lw=1.3, ms=9)
    arrow(ax, (1.9, 2.7), (1.9, 2.0), color=ACCENT, lw=1.3, ms=9)
    label(ax, 0.8, 1.35, r"$V_1,p_1,A_1$", size=8.5, color=INK2)
    label(ax, 2.05, 2.35, r"$V_2,p_2,A_2$", size=8.5, color=INK2, ha="left")
    ax.add_patch(Rectangle((0.7, 0.95), 1.7, 2.25, fill=False,
                           edgecolor=MUTED, lw=1.0, ls=(0, (4, 3))))
    label(ax, 2.5, 3.0, "控制体", size=8.5, color=MUTED)
    arrow(ax, (1.9, 1.2), (2.55, 1.2), color=INK2, lw=1.0, ms=8)
    label(ax, 2.65, 1.2, r"$R_x$", size=9, color=INK2, ha="left")
    arrow(ax, (1.9, 2.1), (1.9, 2.75), color=INK2, lw=1.0, ms=8)
    label(ax, 1.75, 2.4, r"$R_y$", size=9, color=INK2, ha="right")
    label(ax, 0.25, 0.35, "弯管控制体：动量通量 + 压力 + 合力",
          size=8.5, color=MUTED, ha="left")
    panel(ax, "(a)")

    ax = axes[1]
    blank(ax, (0, 4.2), (0, 3.4))
    # jet and curved vane
    ax.plot([0.2, 2.15], [1.5, 1.5], color=ACCENT, lw=2.4, alpha=0.55)
    arrow(ax, (0.3, 1.5), (2.1, 1.5), color=ACCENT, lw=1.6, ms=10)
    label(ax, 1.1, 1.7, r"$V_1$", size=9, color=ACCENT)
    t = np.linspace(-0.9, 0.9, 80)
    vx = 2.45 + 0.55 * np.cos(t)
    vy = 1.5 + 0.9 * np.sin(t)
    ax.plot(vx, vy, color=INK, lw=2.4)
    label(ax, 2.55, 2.55, "叶片", size=8.5, color=INK2)
    arrow(ax, (2.35, 2.15), (2.9, 2.75), color=ACCENT, lw=1.4, ms=9)
    label(ax, 3.0, 2.85, r"$V_2$", size=9, color=ACCENT, ha="left")
    arrow(ax, (2.6, 1.5), (3.25, 1.5), color=INK2, lw=1.2, ms=9)
    label(ax, 3.3, 1.5, r"$R$", size=10, color=INK2, ha="left")
    label(ax, 0.25, 0.35, r"$F=\rho Q(V_1-V_2\cos\theta)$", size=10,
          color=INK, ha="left")
    panel(ax, "(b)")
    save(fig, "ch4_momentum.png")


# ============================================================
# Chapter 5
# ============================================================

def _cross(ax, x, y, angle=0.0, size=0.16, color=INK, lw=1.2):
    ax.add_patch(Circle((x, y), size * 0.9, fill=False, edgecolor=color,
                        lw=1.0, zorder=7))
    dx, dy = size * 1.35 * np.cos(angle), size * 1.35 * np.sin(angle)
    ax.plot([x, x + dx], [y, y + dy], color=ACCENT, lw=1.8, zorder=8)
    ax.add_patch(Circle((x, y), 0.03, color=ACCENT, zorder=8))


def fig_ch5_vorticity():
    fig, axes = plt.subplots(1, 2, figsize=(8.4, 3.0))

    for k, (ax, rotating, title) in enumerate([
        (axes[0], False, r"$\Omega=0$：微团不转"),
        (axes[1], True, r"$\Omega\ne0$：微团自转"),
    ]):
        blank(ax, (0, 4.2), (0, 3.0))
        t = np.linspace(0, 1, 120)
        x = 0.35 + 3.0 * t
        y = 1.5 + 0.55 * np.sin(2 * np.pi * t)
        ax.plot(x, y, color=INK2, lw=1.4)
        for i, tt in enumerate((0.2, 0.5, 0.8)):
            idx = int(tt * (len(t) - 1))
            angle = (0.7 * i if rotating else 0.0)
            _cross(ax, x[idx], y[idx], angle=angle, color=ACCENT)
        arrow(ax, (x[-8], y[-8]), (x[-1], y[-1]), color=ACCENT, lw=1.1, ms=8)
        label(ax, 2.1, 2.7, title, size=10, color=INK)
        label(ax, 2.1, 0.35, "判断看微团自身是否转动，不看轨迹弯不弯",
              size=8.3, color=MUTED)
        panel(ax, "(a)" if k == 0 else "(b)")
    save(fig, "ch5_vorticity.png")


def fig_ch5_basic():
    fig, axes = plt.subplots(1, 3, figsize=(9.6, 3.0))
    fig.subplots_adjust(wspace=0.08)

    ax = axes[0]
    blank(ax, (0, 3.0), (0, 2.6))
    for y in (0.7, 1.1, 1.5, 1.9):
        arrow(ax, (0.3, y), (2.65, y), color=INK2, lw=1.0, ms=7)
    for x in (0.8, 1.5, 2.2):
        ax.plot([x, x], [0.6, 2.0], color=MUTED, lw=0.7, ls=(0, (2, 2)))
    label(ax, 1.5, 2.3, "均匀流", size=9, color=INK)
    label(ax, 2.55, 0.45, r"$\varphi=Ux,\ \psi=Uy$", size=9, color=INK2,
          ha="right")
    panel(ax, "(a)")

    ax = axes[1]
    blank(ax, (0, 3.0), (0, 2.6))
    cx, cy = 1.5, 1.3
    for ang in np.linspace(0, 2 * np.pi, 12, endpoint=False):
        dx, dy = np.cos(ang), np.sin(ang)
        arrow(ax, (cx + 0.18 * dx, cy + 0.18 * dy),
              (cx + 0.95 * dx, cy + 0.95 * dy), color=ACCENT, lw=0.9, ms=6)
    ax.plot(cx, cy, "o", ms=5, color=ACCENT)
    label(ax, cx, cy + 1.2, "源（$m>0$）", size=9, color=INK)
    label(ax, 1.5, 0.25, "流线为径向线，等势线为圆", size=8.3, color=MUTED)
    panel(ax, "(b)")

    ax = axes[2]
    blank(ax, (0, 3.0), (0, 2.6))
    cx, cy = 1.5, 1.3
    for r in (0.35, 0.7, 1.05):
        ax.add_patch(Circle((cx, cy), r, fill=False, edgecolor=INK2, lw=0.9))
        arrow(ax, (cx + r, cy), (cx + r * np.cos(0.35), cy + r * np.sin(0.35)),
              color=ACCENT, lw=0.9, ms=6)
    ax.plot(cx, cy, "o", ms=5, color=ACCENT)
    label(ax, cx, cy + 1.25, "点涡（$\\Gamma$）", size=9, color=INK)
    label(ax, 1.5, 0.25, "流线为同心圆，环量决定方向", size=8.3, color=MUTED)
    panel(ax, "(c)")
    save(fig, "ch5_basic_flows.png")


def fig_ch5_cylinder():
    fig, axes = plt.subplots(1, 2, figsize=(9.0, 3.6))
    n = 240
    x = np.linspace(-2.5, 2.5, n)
    y = np.linspace(-1.75, 1.75, n)
    X, Y = np.meshgrid(x, y)
    a, U = 1.0, 1.0
    r = np.maximum(np.hypot(X, Y), 1e-9)
    th = np.arctan2(Y, X)

    for ax, Gamma, title in [
        (axes[0], 0.0, "无环量：前后驻点，无升力"),
        (axes[1], np.pi, "有环量：驻点偏移，产生升力"),
    ]:
        ur = U * (1 - a ** 2 / r ** 2) * np.cos(th)
        ut = -U * (1 + a ** 2 / r ** 2) * np.sin(th) - Gamma / (2 * np.pi * r)
        u = ur * np.cos(th) - ut * np.sin(th)
        v = ur * np.sin(th) + ut * np.cos(th)
        mask = r < a
        u = np.where(mask, np.nan, u)
        v = np.where(mask, np.nan, v)
        ax.streamplot(X, Y, u, v, density=0.8, linewidth=0.55,
                      color=INK2, arrowsize=0.55)
        ax.add_patch(Circle((0, 0), a, facecolor=PAPER, edgecolor=INK,
                            lw=1.3, zorder=5))
        ax.plot([-2.4, 2.4], [0, 0], color=MUTED, lw=0.6, ls=(0, (3, 3)),
                zorder=1)
        arrow(ax, (-2.3, 1.34), (-1.6, 1.34), color=ACCENT, lw=1.0, ms=8)
        label(ax, -1.5, 1.34, r"$U_\infty$", size=9, color=ACCENT,
              ha="left", bbox=dict(facecolor=PAPER, edgecolor="none", pad=1))
        label(ax, 0, a + 0.22, r"$a$", size=9, color=INK2,
              bbox=dict(facecolor=PAPER, edgecolor="none", pad=1))
        if Gamma == 0:
            for sx in (-a, a):
                ax.plot(sx, 0, "o", ms=5, color=ACCENT, zorder=7)
            pass
        else:
            ths = np.arcsin(-Gamma / (4 * np.pi * U * a))
            for ang in (ths, np.pi - ths):
                ax.plot(a * np.cos(ang), a * np.sin(ang), "o", ms=5,
                        color=ACCENT, zorder=7)
            arrow(ax, (0.15, 1.2), (0.15, 1.75), color=ACCENT, lw=1.4, ms=10)
            label(ax, 0.38, 1.55, r"$F_L=\rho U\Gamma$", size=9,
                  color=ACCENT, ha="left",
                  bbox=dict(facecolor=PAPER, edgecolor="none", pad=1))
        ax.set_xlim(-2.5, 2.5)
        ax.set_ylim(-1.75, 1.75)
        ax.set_aspect("equal")
        ax.axis("off")
        caption(ax, title)
        panel(ax, "(a)" if Gamma == 0 else "(b)")
    save(fig, "ch5_cylinder.png")


FIGURES = {
    "ch1": [fig_ch1_viscosity, fig_ch1_lines],
    "ch2": [fig_ch2_pressure, fig_ch2_gate],
    "ch3": [fig_ch3_control_volume, fig_ch3_stress],
    "ch4": [fig_ch4_bernoulli, fig_ch4_momentum],
    "ch5": [fig_ch5_vorticity, fig_ch5_basic, fig_ch5_cylinder],
}


def main():
    wanted = sys.argv[1:] or list(FIGURES)
    for key in wanted:
        for fn in FIGURES.get(key, []):
            fn()


if __name__ == "__main__":
    main()
