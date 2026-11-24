"""Group 06 · shared visual system for the final (C3) views.

One place for the rules agreed from the two W3 works (docs/decision_record.md, part 3):
- blue  = model, grey = grid rule (always hollow markers or hatched bars, so the difference survives without color),
- orange = highlight of the one value or subset the task points to, never a category,
- neutral ink for descriptive charts that are not a model comparison,
- counts drawn as bars start at 0; F1 is drawn with dots on a zoomed common scale (stated in the axis label),
- direct labels instead of legends; F1 with 3 decimals, counts as whole rows, shares with their denominator.
"""
from pathlib import Path
import matplotlib.pyplot as plt

MODEL, RULE, ACCENT = "#2a78d6", "#8a8984", "#eb6834"      # model, grid rule, highlight
INK, INK2, NEUTRAL = "#16181c", "#52514e", "#6f6e69"       # text, secondary text, descriptive bars
GRID, BAND, LIGHT = "#e6e6e3", "#f2f1ee", "#d6d5d0"        # gridlines, group band, light fills
HATCH = "////"                                             # grid rule bars: white fill + grey hatch
FONT = 10                                                  # base font size (pt) at the saved size
DPI = 220


def style():
    """Matplotlib settings shared by every final view."""
    plt.rcdefaults()
    plt.rcParams.update({
        "figure.facecolor": "white", "axes.facecolor": "white", "savefig.facecolor": "white",
        "font.family": "DejaVu Sans", "font.size": FONT, "axes.edgecolor": "#bdbcb7",
        "axes.spines.top": False, "axes.spines.right": False, "axes.grid": True, "grid.color": GRID,
        "grid.linewidth": 0.8, "axes.axisbelow": True, "axes.labelcolor": INK2, "axes.labelsize": FONT,
        "xtick.color": INK2, "ytick.color": INK2, "xtick.labelsize": FONT - 0.5, "ytick.labelsize": FONT - 0.5,
        "legend.frameon": False, "hatch.color": RULE, "hatch.linewidth": 0.9,
    })


def rule_bar(ax, y, width, height, left=0, **kw):
    """Grid-rule bar: white fill with grey hatch and outline (readable without color)."""
    return ax.barh(y, width, height, left=left, color="white", edgecolor=RULE, hatch=HATCH, linewidth=1.1, **kw)


def model_bar(ax, y, width, height, left=0, **kw):
    """Model bar: solid blue."""
    return ax.barh(y, width, height, left=left, color=MODEL, **kw)


def minus(x, fmt="{:+.3f}"):
    """Signed number with a true minus sign."""
    return fmt.format(x).replace("-", "−")


def save(fig, folder, name):
    """Save a final view as PNG (200+ dpi) and show it in the notebook."""
    folder = Path(folder)
    folder.mkdir(parents=True, exist_ok=True)
    fig.savefig(folder / f"{name}.png", dpi=DPI, bbox_inches="tight")
    plt.show()
