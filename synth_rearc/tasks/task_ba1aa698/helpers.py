from synth_rearc.core import *


HEIGHT_BA1AA698 = 16
PANEL_COUNT_BOUNDS_BA1AA698 = (THREE, FOUR)
INNER_WIDTH_CHOICES_BA1AA698 = (FOUR, FIVE)
MOTIF_PATCHES_BA1AA698 = (
    frozenset({(ZERO, ZERO), (ZERO, ONE)}),
    frozenset({(ZERO, ZERO), (ZERO, ONE), (ONE, ZERO), (ONE, ONE)}),
    frozenset({(ZERO, ZERO), (ZERO, TWO), (ONE, ZERO), (ONE, ONE), (ONE, TWO)}),
    frozenset({(ZERO, ZERO), (ZERO, ONE), (ZERO, TWO), (ONE, ONE)}),
)
NONZERO_COLORS_BA1AA698 = (ONE, TWO, THREE, FOUR, FIVE, SIX, SEVEN, EIGHT, NINE)


def split_panels_ba1aa698(
    grid: Grid,
) -> Tuple:
    x0 = height(grid)
    x1 = tuple(j for j in range(width(grid)) if len({grid[i][j] for i in range(x0)}) == ONE)
    return tuple(crop(grid, (ZERO, x2), (x0, x3 - x2 + ONE)) for x2, x3 in zip(x1[:-1], x1[1:]))


def panel_background_ba1aa698(
    panel: Grid,
) -> Integer:
    return mostcolor(trim(panel))


def motif_object_ba1aa698(
    panel: Grid,
) -> Object:
    x0 = panel_background_ba1aa698(panel)
    x1 = trim(panel)
    return frozenset(
        (x4, (x2 + ONE, x3 + ONE))
        for x2, x5 in enumerate(x1)
        for x3, x4 in enumerate(x5)
        if x4 != x0
    )


def blank_panel_ba1aa698(
    panel: Grid,
) -> Grid:
    x0 = panel_background_ba1aa698(panel)
    x1 = motif_object_ba1aa698(panel)
    return fill(panel, x0, x1)


def predict_next_top_ba1aa698(
    rows: Tuple,
    motif: Object,
    border_color: Integer,
) -> Integer:
    x0 = rows[ONE] - rows[ZERO]
    x1 = rows[-ONE] + x0
    x2 = equality(color(motif), border_color)
    x3 = branch(x2, sign(x0), ZERO)
    return x1 + x3


def paint_motif_at_top_ba1aa698(
    panel: Grid,
    motif: Object,
    top: Integer,
) -> Grid:
    x0 = shift(normalize(motif), (top, leftmost(motif)))
    return paint(panel, x0)


def build_panel_ba1aa698(
    height_: Integer,
    inner_width: Integer,
    border_color: Integer,
    bg_color: Integer,
    motif_patch: Indices,
    motif_color: Integer,
    top: Integer,
) -> Grid:
    x0 = canvas(bg_color, (height_, inner_width + TWO))
    x1 = fill(x0, border_color, box(asindices(x0)))
    x2 = ONE + (inner_width - width(motif_patch)) // TWO
    x3 = shift(recolor(motif_color, motif_patch), (top, x2))
    return paint(x1, x3)


def assemble_input_ba1aa698(
    panels: Tuple,
) -> Grid:
    x0 = first(panels)
    for x1 in panels[ONE:]:
        x2 = crop(x1, (ZERO, ONE), (height(x1), width(x1) - ONE))
        x0 = hconcat(x0, x2)
    return x0


def motif_choices_ba1aa698(
    inner_width: Integer,
) -> Tuple:
    return tuple(x0 for x0 in MOTIF_PATCHES_BA1AA698 if width(x0) <= inner_width)
