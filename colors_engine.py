"""
Color Palettes for Scientific Plotting

Core functions:
- get_palette: select and generate palettes
- show_palettes: visualize palette database

Designed for use with Matplotlib.
"""
import random
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from colors_source import palettes

# -----------------------------
# 1) COLOR–COLOR contrast: ΔE in CIELAB (CIE76)
# -----------------------------

def _srgb_channel_to_linear(u: float) -> float:
    """u in [0,1] sRGB -> linear RGB"""
    return u / 12.92 if u <= 0.04045 else ((u + 0.055) / 1.055) ** 2.4

def _lab_to_rgb255(lab):
    """
    Approx inverse of rgb255_to_lab (Lab D65 -> sRGB 0–255).
    Good enough for gradients; not for color-management perfection.
    """
    L, a, b = lab

    # Lab -> XYZ
    def f_inv(t):
        t3 = t**3
        return t3 if t3 > 0.008856 else (t - 16/116) / 7.787

    fy = (L + 16) / 116
    fx = fy + a / 500
    fz = fy - b / 200

    Xn, Yn, Zn = 0.95047, 1.00000, 1.08883
    X = Xn * f_inv(fx)
    Y = Yn * f_inv(fy)
    Z = Zn * f_inv(fz)

    # XYZ -> linear RGB (sRGB D65)
    r_lin =  3.2404542*X - 1.5371385*Y - 0.4985314*Z
    g_lin = -0.9692660*X + 1.8760108*Y + 0.0415560*Z
    b_lin =  0.0556434*X - 0.2040259*Y + 1.0572252*Z

    def linear_to_srgb(u):
        if u <= 0.0031308:
            return 12.92 * u
        return 1.055 * (u ** (1/2.4)) - 0.055

    r = linear_to_srgb(max(0.0, min(1.0, r_lin)))
    g = linear_to_srgb(max(0.0, min(1.0, g_lin)))
    b = linear_to_srgb(max(0.0, min(1.0, b_lin)))

    return (int(round(r*255)), int(round(g*255)), int(round(b*255)))

def rgb255_to_lab(rgb):
    """
    Convert RGB 0–255 (sRGB) to CIELAB (D65 reference white).
    Returns (L*, a*, b*).
    """
    r, g, b = rgb
    r, g, b = r / 255.0, g / 255.0, b / 255.0

    # sRGB -> linear
    r_lin = _srgb_channel_to_linear(r)
    g_lin = _srgb_channel_to_linear(g)
    b_lin = _srgb_channel_to_linear(b)

    # linear RGB -> XYZ (sRGB D65)
    X = 0.4124564 * r_lin + 0.3575761 * g_lin + 0.1804375 * b_lin
    Y = 0.2126729 * r_lin + 0.7151522 * g_lin + 0.0721750 * b_lin
    Z = 0.0193339 * r_lin + 0.1191920 * g_lin + 0.9503041 * b_lin

    # Normalize by D65 reference white
    Xn, Yn, Zn = 0.95047, 1.00000, 1.08883
    x, y, z = X / Xn, Y / Yn, Z / Zn

    # XYZ -> Lab
    def f(t):
        return t ** (1/3) if t > 0.008856 else (7.787 * t + 16/116)

    fx, fy, fz = f(x), f(y), f(z)
    L = 116 * fy - 16
    a = 500 * (fx - fy)
    b = 200 * (fy - fz)

    return (L, a, b)

def delta_e_cie76(lab1, lab2) -> float:
    """Euclidean distance in Lab (CIE76)."""
    dL = lab1[0] - lab2[0]
    da = lab1[1] - lab2[1]
    db = lab1[2] - lab2[2]
    return float(np.sqrt(dL*dL + da*da + db*db))

def min_pairwise_delta_e(rgb_list_255) -> float:
    """
    rgb_list_255: list of (R,G,B) ints in 0–255.
    Returns the minimum ΔE among all pairs (higher = more distinguishable).
    """
    labs = [rgb255_to_lab(rgb) for rgb in rgb_list_255]
    n = len(labs)
    if n < 2:
        return float("inf")
    min_de = float("inf")
    for i in range(n):
        for j in range(i + 1, n):
            de = delta_e_cie76(labs[i], labs[j])
            if de < min_de:
                min_de = de
    return min_de

# -----------------------------
# 2) COLOR–BACKGROUND contrast: WCAG contrast ratio
# -----------------------------

DEFAULT_MIN_BG_CONTRAST = 1.7

def _parse_background(background):
    """
    background can be:
      - "white" or "black"
      - (R,G,B) in 0–255 ints
    Returns background_rgb_255 as (R,G,B) ints 0–255
    """
    if background is None or background == "white":
        return (255, 255, 255)
    if background == "black":
        return (0, 0, 0)

    if isinstance(background, (tuple, list)) and len(background) == 3:
        r, g, b = background
        return (int(r), int(g), int(b))

    raise ValueError("background must be 'white', 'black', None, or an RGB tuple (0–255 ints)")

def relative_luminance(rgb):
    """
    rgb can be (R,G,B) in 0–255 or floats in 0–1.
    Returns relative luminance Y in [0,1] (linearized).
    """
    r, g, b = rgb
    if max(r, g, b) > 1.0:  # assume 0–255
        r, g, b = r / 255.0, g / 255.0, b / 255.0

    r_lin = _srgb_channel_to_linear(r)
    g_lin = _srgb_channel_to_linear(g)
    b_lin = _srgb_channel_to_linear(b)

    return 0.2126 * r_lin + 0.7152 * g_lin + 0.0722 * b_lin

def wcag_contrast_ratio(rgb1, rgb2) -> float:
    """
    rgb1, rgb2: (R,G,B) in 0–255 or 0–1.
    Returns WCAG contrast ratio in [1, 21]. Higher = better.
    """
    L1 = relative_luminance(rgb1)
    L2 = relative_luminance(rgb2)
    L_light = max(L1, L2)
    L_dark  = min(L1, L2)
    return float((L_light + 0.05) / (L_dark + 0.05))

def min_contrast_vs_background(rgb_list, background_rgb=(255, 255, 255)) -> float:
    """
    Returns the minimum WCAG contrast ratio of any color in rgb_list vs background.
    """
    ratios = [wcag_contrast_ratio(rgb, background_rgb) for rgb in rgb_list]
    return float(min(ratios)) if ratios else float("inf")


# -----------------------------
# 3) UTILS
# -----------------------------

def list_palettes(
    palettes: dict,
    size: int = 2,
    mode: str = "s",
    background="white",
):
    """
    Returns a list of palette IDs that can satisfy:
      - requested size
      - requested mode ('s' or 'p')
      - background readability for screen mode (DEFAULT_MIN_BG_CONTRAST)
    """
    mode = mode.lower().strip()
    if mode not in ("s", "p"):
        raise ValueError("mode must be 's' or 'p'")

    bg255 = _parse_background(background)

    def role_order(p: dict):
        colors = p["colors"]
        keys_input = list(colors.keys())
        roles = p.get("roles", {}) or {}

        ordered = []
        if "dominant" in roles and roles["dominant"] in colors:
            ordered.append(roles["dominant"])
        ordered += [k for k in roles.get("secondary", []) if k in colors]
        ordered += [k for k in roles.get("accent", []) if k in colors]
        for k in keys_input:
            if k not in ordered:
                ordered.append(k)
        return ordered

    def first_n_keys(p: dict):
        ordered = role_order(p)
        return ordered[:size]

    def satisfies(p: dict) -> bool:
        colors = p.get("colors", {})
        if len(colors) < size:
            return False

        keys = first_n_keys(p)

        if mode == "p":
            # all returned colors must have CMYK
            for k in keys:
                if colors[k].get("cmyk", None) is None:
                    return False
            return True

        # mode == "s": enforce background contrast
        rgb255 = [colors[k]["rgb"] for k in keys]
        return min_contrast_vs_background(rgb255, background_rgb=bg255) >= DEFAULT_MIN_BG_CONTRAST

    return [pid for pid, p in palettes.items() if satisfies(p)]


def show_palettes(
    palettes: dict,
    size: int = 2,
    mode: str = "s",
    background="white",
    max_rows: int = 30,
    figsize=None,
):
    """
    Visual gallery of palettes that satisfy list_palettes(...) constraints.
    - Rows of rectangles
    - Dominant emphasized (thicker border + slightly larger width)
    """
    ids = list_palettes(palettes, size=size, mode=mode, background=background)
    ids = ids[:max_rows]

    if not ids:
        raise ValueError("No palettes matched the current constraints.")

    bg255 = _parse_background(background)
    bg01 = (bg255[0]/255.0, bg255[1]/255.0, bg255[2]/255.0)
    
    # decide label text color based on background
    bg_lum = relative_luminance(bg255)
    label_color = "white" if bg_lum < 0.5 else "black"

    # Helpers (same ordering logic)
    def role_order(p: dict):
        colors = p["colors"]
        keys_input = list(colors.keys())
        roles = p.get("roles", {}) or {}

        ordered = []
        if "dominant" in roles and roles["dominant"] in colors:
            ordered.append(roles["dominant"])
        ordered += [k for k in roles.get("secondary", []) if k in colors]
        ordered += [k for k in roles.get("accent", []) if k in colors]
        for k in keys_input:
            if k not in ordered:
                ordered.append(k)
        return ordered

    # figure sizing
    n = len(ids)
    if figsize is None:
        figsize = (10, max(2.5, 0.35 * n))

    fig, ax = plt.subplots(figsize=figsize)
    fig.patch.set_facecolor(bg01)
    ax.set_facecolor(bg01)

    ax.set_xlim(0, 1)
    ax.set_ylim(0, n)
    ax.axis("off")

    # layout constants
    left_label_w = 0.16
    x0 = left_label_w
    x1 = 0.98
    row_h = 0.8
    y_pad = (1 - row_h) / 2

    for row, pid in enumerate(ids):
        p = palettes[pid]
        colors = p["colors"]
        roles = p.get("roles", {}) or {}
        dom = roles.get("dominant", None)

        keys = role_order(p)[:size]

        # weight dominant a bit more
        weights = []
        for k in keys:
            weights.append(1.35 if (dom is not None and k == dom) else 1.0)

        total_w = sum(weights)
        cur_x = x0
        y = n - 1 - row + y_pad  # top to bottom

        # palette label
        ax.text(0.01, y + row_h/2, pid,
                va="center", ha="left",
                fontsize=10,
                color=label_color)

        # draw rectangles
        for k, w in zip(keys, weights):
            frac = w / total_w
            width = (x1 - x0) * frac

            if mode == "s":
                r, g, b = colors[k]["rgb"]
                face = (r/255.0, g/255.0, b/255.0)
            else:
                r, g, b = colors[k]["rgb"]
                face = (r/255.0, g/255.0, b/255.0)

            # dominant: thicker border
            lw = 0.8 if (dom is not None and k == dom) else 0.7

            rect = Rectangle(
                (cur_x, y),
                width,
                row_h,
                facecolor=face,
                edgecolor=(0,0,0),
                linewidth=lw,
            )
            ax.add_patch(rect)
            cur_x += width

    plt.tight_layout()
    plt.show()
    
def _interp_lab(anchors_rgb255, n_out):
    """
    anchors_rgb255: list of (R,G,B) ints in 0–255
    n_out: number of output colors
    Returns list of RGB tuples 0–255, interpolated in Lab space.
    """
    if not isinstance(n_out, int) or n_out <= 0:
        raise ValueError(f"n_out must be a positive int, got {n_out}")

    n_anchors = len(anchors_rgb255)
    if n_anchors == 0:
        return []
    if n_anchors == 1:
        return [anchors_rgb255[0]] * n_out

    if n_out <= n_anchors:
        return anchors_rgb255[:n_out]

    labs = [np.array(rgb255_to_lab(rgb), dtype=float) for rgb in anchors_rgb255]
    segs = n_anchors - 1

    # sample positions across the full chain [0, segs]
    ts = np.linspace(0.0, float(segs), n_out)

    out = []
    for t in ts:
        i = int(np.floor(t))
        if i >= segs:
            # last sample: clamp to last anchor
            lab = labs[-1]
        else:
            u = t - i  # local segment parameter in [0,1]
            lab = (1.0 - u) * labs[i] + u * labs[i + 1]

        out.append(_lab_to_rgb255(tuple(lab)))

    return out

# -----------------------------
# 4) GET_PALETTE
# -----------------------------

def get_palette(
    palettes: dict,
    size: int = 2,
    n_out: int = None,
    palette_id: str = 'r',
    mode: str = "s",
    background="white",
):
    """
    palette_id:
        'r' -> random palette that can satisfy `size` in the requested `mode`
        otherwise -> use the given palette_id key (e.g., "PP003")

    size:
        number of colors requested (e.g. 3 curves -> 3 colors)

    mode:
        's' -> list of RGB colors normalized to [0,1] (matplotlib-ready)
        'p' -> list of CMYK tuples (as stored; typically 0–100 ints)

    background:
        "white", "black", None, or RGB tuple (0–255 ints).
        Enforced only for mode='s' using DEFAULT_MIN_BG_CONTRAST.

    Returns:
        list_of_colors
    """
    if n_out is None:
        n_out = size
    if not isinstance(n_out, int) or n_out <= 0:
        raise ValueError(f"n_out must be a positive int, got {n_out}")
    if mode == "p" and n_out != size:
        raise ValueError("For mode='p' (print), n_out must equal size (continuous print not implemented).")
    
    if not isinstance(size, int) or size <= 0:
        raise ValueError(f"size must be a positive int, got {size}")

    mode = mode.lower().strip()
    if mode not in ("s", "p"):
        raise ValueError("mode must be 's' (screen) or 'p' (print)")

    bg255 = _parse_background(background)

    def role_order(p: dict):
        colors = p["colors"]
        keys_input = list(colors.keys())
        roles = p.get("roles", {}) or {}

        ordered = []
        if "dominant" in roles and roles["dominant"] in colors:
            ordered.append(roles["dominant"])
        ordered += [k for k in roles.get("secondary", []) if k in colors]
        ordered += [k for k in roles.get("accent", []) if k in colors]
        for k in keys_input:
            if k not in ordered:
                ordered.append(k)
        return ordered

    def first_n_rgb255(p: dict):
        colors = p["colors"]
        ordered = role_order(p)
        out = []
        for k in ordered:
            out.append(colors[k]["rgb"])  # stored as 0–255
            if len(out) == size:
                break
        return out

    def palette_satisfies(p: dict):
        colors = p.get("colors", {})
        if len(colors) < size:
            return False

        if mode == "p":
            ordered = role_order(p)
            cmyk_ok = [colors[k].get("cmyk", None) is not None for k in ordered]
            return sum(cmyk_ok) >= size

        # mode == "s": enforce background contrast
        rgb255 = first_n_rgb255(p)
        if len(rgb255) < size:
            return False
        return min_contrast_vs_background(rgb255, background_rgb=bg255) >= DEFAULT_MIN_BG_CONTRAST

    # pick palette
    if palette_id == 'r':
        candidates = [pid for pid, p in palettes.items() if palette_satisfies(p)]
        if not candidates:
            raise ValueError(
                f"No palettes found with at least {size} colors for mode='{mode}' "
                f"passing background contrast >= {DEFAULT_MIN_BG_CONTRAST} on background={background}"
            )
        palette_id = random.choice(candidates)

    if palette_id not in palettes:
        raise KeyError(f"palette_id '{palette_id}' not found")

    p = palettes[palette_id]
    if not palette_satisfies(p):
        raise ValueError(
            f"Palette '{palette_id}' cannot satisfy size={size} for mode='{mode}' "
            f"with background contrast >= {DEFAULT_MIN_BG_CONTRAST} on background={background}"
        )

    colors = p["colors"]
    ordered_keys = role_order(p)

    if mode == "s":
        # 1) pick anchors (RGB 0–255)
        anchors_rgb255 = []
        for k in ordered_keys:
            anchors_rgb255.append(colors[k]["rgb"])
            if len(anchors_rgb255) == size:
                break

        # 2) discrete vs continuous
        if n_out <= size:
            rgb255_list = anchors_rgb255[:n_out]
        else:
            rgb255_list = _interp_lab(anchors_rgb255, n_out)

        # 3) matplotlib-ready normalized RGB
        rgb = [(r/255.0, g/255.0, b/255.0) for (r, g, b) in rgb255_list]
        return rgb, palette_id


    # mode == "p"
    out = []
    for k in ordered_keys:
        cmyk = colors[k].get("cmyk", None)
        if cmyk is not None:
            out.append(tuple(cmyk))
            if len(out) == size:
                break
    
    return out, palette_id
# -----------------------------
# END OF CODE
# -----------------------------