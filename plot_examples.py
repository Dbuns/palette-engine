import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
from colors_source import palettes
from colors_engine import get_palette, show_palettes

# ---------------------------------------------------------
# SHOWCASE PLOTS
# ---------------------------------------------------------
def _pick_colors(colors, n):
    if len(colors) < n:
        raise ValueError(f"You requested {n} colors, but only {len(colors)} are available in `colors`.")
    return colors[:n]

# ---------------------------------------------------------
# 1) DISCRETE LINE PLOT
# ---------------------------------------------------------
def plot_discrete_lines(colors):
    cols = _pick_colors(colors, 4)

    x = np.linspace(0, 10, 300)
    ys = [
        np.sin(x),
        np.cos(x),
        np.sin(x + 0.7),
        0.7 * np.cos(x + 0.5)
    ]

    plt.figure(figsize=(7, 4))
    for i, y in enumerate(ys):
        plt.plot(x, y, color=cols[i], linewidth=2.2, label=f"Series {i+1}")

    plt.xlabel("Time (a.u.)")
    plt.ylabel("Signal (a.u.)")
    plt.title("Discrete palette – line plot")
    plt.legend(frameon=False)
    plt.tight_layout()
    plt.show()


# ---------------------------------------------------------
# 2) CONTINUOUS LINE PLOT
# ---------------------------------------------------------
def plot_continuous_lines(colors):
    x = np.linspace(0, 10, 300)

    plt.figure(figsize=(7, 4))
    for i, c in enumerate(colors):
        y = np.sin(x + 0.18 * i) + 0.03 * i
        plt.plot(x, y, color=c, linewidth=2)

    plt.xlabel("Time (a.u.)")
    plt.ylabel("Signal (a.u.)")
    plt.title("Continuous palette – many related series")
    plt.tight_layout()
    plt.show()


# ---------------------------------------------------------
# 3) SCATTER + LINE FIT + CONFIDENCE-LIKE BAND
# ---------------------------------------------------------
def plot_scatter_fit(colors):
    cols = _pick_colors(colors, 3)

    rng = np.random.default_rng(42)
    x = np.linspace(0, 10, 35)
    y = 1.8 * x + 4 + rng.normal(scale=2.0, size=len(x))

    coeffs = np.polyfit(x, y, 1)
    fit = np.poly1d(coeffs)

    x_fit = np.linspace(x.min(), x.max(), 200)
    y_fit = fit(x_fit)

    # mock confidence band
    band = 2.2

    plt.figure(figsize=(7, 4))
    plt.fill_between(x_fit, y_fit - band, y_fit + band, color=cols[2], alpha=0.25)
    plt.plot(x_fit, y_fit, color=cols[1], linewidth=2.5, label="Linear fit")
    plt.scatter(x, y, color=cols[0], s=45, edgecolor="black", linewidth=0.5, label="Data")

    plt.xlabel("Concentration (a.u.)")
    plt.ylabel("Response (a.u.)")
    plt.title("Scatter + fit + band")
    plt.legend(frameon=False)
    plt.tight_layout()
    plt.show()


# ---------------------------------------------------------
# 4) GROUPED BAR CHART
# ---------------------------------------------------------
def plot_grouped_bars(colors):
    cols = _pick_colors(colors, 4)

    groups = ["Sample A", "Sample B", "Sample C"]
    vals1 = [1.8, 2.4, 2.0]
    vals2 = [2.3, 2.8, 2.5]
    vals3 = [2.6, 3.0, 2.9]
    vals4 = [3.0, 3.3, 3.1]

    x = np.arange(len(groups))
    w = 0.18

    plt.figure(figsize=(7, 4))
    plt.bar(x - 1.5*w, vals1, width=w, color=cols[0], label="Condition 1")
    plt.bar(x - 0.5*w, vals2, width=w, color=cols[1], label="Condition 2")
    plt.bar(x + 0.5*w, vals3, width=w, color=cols[2], label="Condition 3")
    plt.bar(x + 1.5*w, vals4, width=w, color=cols[3], label="Condition 4")

    plt.ylim(0, 4.5)

    plt.xticks(x, groups)
    plt.ylabel("Measured value")
    plt.title("Grouped bar chart")
    plt.legend(frameon=False, ncol=2)
    plt.tight_layout()
    plt.show()


# ---------------------------------------------------------
# 5) HEATMAP / MATRIX
# ---------------------------------------------------------
def plot_heatmap(colors):
    # use all colors to build a custom colormap
    cmap = LinearSegmentedColormap.from_list("custom_palette", colors, N=256)

    rng = np.random.default_rng(7)
    A = rng.normal(size=(10, 10))
    M = np.corrcoef(A)

    plt.figure(figsize=(5.8, 5))
    im = plt.imshow(M, cmap=cmap, vmin=-1, vmax=1)
    plt.colorbar(im, fraction=0.046, pad=0.04, label="Correlation")
    plt.xticks(range(10), [f"V{i+1}" for i in range(10)], rotation=45)
    plt.yticks(range(10), [f"V{i+1}" for i in range(10)])
    plt.title("Heatmap with continuous palette")
    plt.tight_layout()
    plt.show()


# ---------------------------------------------------------
# 6) MULTI-PANEL FIGURE
# ---------------------------------------------------------
def plot_multi_panel(colors):
    cols = _pick_colors(colors, 4)
    rng = np.random.default_rng(123)

    fig, axs = plt.subplots(2, 2, figsize=(9, 6))

    # top-left: line
    x = np.linspace(0, 10, 200)
    axs[0, 0].plot(x, np.sin(x), color=cols[0], linewidth=2.2)
    axs[0, 0].plot(x, np.cos(x), color=cols[1], linewidth=2.2)
    axs[0, 0].set_title("Line plot")

    # top-right: scatter
    xs = np.linspace(0, 8, 25)
    ys = 0.9 * xs + 2 + rng.normal(scale=1.0, size=len(xs))
    axs[0, 1].scatter(xs, ys, color=cols[2], s=40, edgecolor="black", linewidth=0.4)
    axs[0, 1].set_title("Scatter")

    # bottom-left: bars
    vals = [2.2, 3.1, 2.7, 3.4]
    axs[1, 0].bar(np.arange(4), vals, color=cols)
    axs[1, 0].set_xticks(np.arange(4), ["A", "B", "C", "D"])
    axs[1, 0].set_title("Bars")

    # bottom-right: filled curve
    y = np.exp(-0.3 * x) * np.sin(2 * x)
    axs[1, 1].fill_between(x, y, 0, color=cols[3], alpha=0.35)
    axs[1, 1].plot(x, y, color=cols[3], linewidth=2.2)
    axs[1, 1].set_title("Area plot")

    for ax in axs.ravel():
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)

    fig.suptitle("Same palette reused across multiple plot types", y=1.02)
    plt.tight_layout()
    plt.show()


# ---------------------------------------------------------
# 7) BLACK BACKGROUND LINE PLOT
# ---------------------------------------------------------
def plot_black_background(colors):
    cols = _pick_colors(colors, 3)
    x = np.linspace(0, 10, 300)

    fig, ax = plt.subplots(figsize=(7, 4))
    fig.patch.set_facecolor("black")
    ax.set_facecolor("black")

    ax.plot(x, np.sin(x), color=cols[0], linewidth=2.5, label="Series 1")
    ax.plot(x, np.cos(x), color=cols[1], linewidth=2.5, label="Series 2")
    ax.plot(x, np.sin(x + 1.0), color=cols[2], linewidth=2.5, label="Series 3")

    ax.set_title("Palette on black background", color="white")
    ax.set_xlabel("Time", color="white")
    ax.set_ylabel("Signal", color="white")
    ax.tick_params(colors="white")

    for spine in ax.spines.values():
        spine.set_color("white")

    leg = ax.legend(frameon=False)
    for text in leg.get_texts():
        text.set_color("white")

    plt.tight_layout()
    plt.show()

# ---------------------------------------------------------
# PLOT SHOWCASE
# ---------------------------------------------------------

# =========================================================
# 1 — DISCRETE PALETTE EXAMPLES
# =========================================================

colors, palette_id = get_palette(
    palettes,
    size=4,
    palette_id="DCC307",
    mode="s",
    background="white"
)

print("Discrete palette:", palette_id)

plot_discrete_lines(colors)
plot_grouped_bars(colors)
plot_heatmap(colors)
plot_multi_panel(colors)

# =========================================================
# 2 — DARK BACKGROUND EXAMPLE
# =========================================================

colors, palette_id = get_palette(
    palettes,
    size=3,
    palette_id="r",     # random palette
    mode="s",
    background="black"
)

print("Black background palette:", palette_id)

plot_black_background(colors)

# Example good palette for dark backgrounds
# DCC142

# =========================================================
# 3 — SCATTER + REGRESSION EXAMPLE
# =========================================================

colors, palette_id = get_palette(
    palettes,
    size=3,
    palette_id="r",
    mode="s",
    background="white"
)

print("Scatter palette:", palette_id)

plot_scatter_fit(colors)

# Example good palette
# DCC149

# =========================================================
# 4 — CONTINUOUS PALETTE EXAMPLE
# =========================================================

colors, palette_id = get_palette(
    palettes,
    size=4,
    n_out=15,
    palette_id="DCC267",
    mode="s"
)

print("Continuous palette:", palette_id)

plot_continuous_lines(colors)

# Other good continuous palettes
# DCC328
# DCC174

# =========================================================
# 5 — PALETTE GALLERY
# =========================================================

show_palettes(
    palettes,
    size=2,
    mode="s",
    background="white"
)