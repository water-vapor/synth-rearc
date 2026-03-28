from synth_rearc.core import *


BLANK_ROW_25c199f5 = repeat(SEVEN, FIVE)
SEPARATOR_25c199f5 = canvas(SIX, (FIVE, ONE))

HEIGHT_TRIPLES_25c199f5 = (
    (ONE, ONE, ONE),
    (TWO, ONE, ONE),
    (THREE, ONE, ONE),
    (THREE, ONE, ONE),
    (ONE, THREE, ONE),
    (TWO, TWO, ONE),
)

MOTIFS_BY_HEIGHT_25c199f5 = {
    ONE: (
        ((0,),),
        ((0, 1),),
        ((0, 1, 2),),
        ((0, 1, 2, 3),),
        ((0, 1, 2, 3, 4),),
    ),
    TWO: (
        ((0, 1), (0, 1)),
        ((1,), (0, 1, 2)),
    ),
    THREE: (
        ((1,), (0, 1, 2), (1,)),
        ((0, 1, 2), (0, 2), (0, 1, 2)),
    ),
}


def _row_from_cols_25c199f5(cols: tuple[int, ...], color: Integer) -> tuple[int, ...]:
    row = [SEVEN] * FIVE
    for j in cols:
        row[j] = color
    return tuple(row)


def _paint_motif_25c199f5(
    motif: tuple[tuple[int, ...], ...],
    color: Integer,
    loc: tuple[Integer, Integer],
) -> tuple[Grid, tuple[tuple[int, ...], ...]]:
    panel = canvas(SEVEN, (FIVE, FIVE))
    top, left = loc
    rows = []
    for di, cols in enumerate(motif):
        shifted = tuple(left + j for j in cols)
        rows.append(_row_from_cols_25c199f5(shifted, color))
        patch = frozenset((top + di, j) for j in shifted)
        panel = fill(panel, color, patch)
    return panel, tuple(rows)


def _sample_panel_25c199f5(height_value: Integer, color: Integer) -> tuple[Grid, tuple[tuple[int, ...], ...]]:
    motif = choice(MOTIFS_BY_HEIGHT_25c199f5[height_value])
    motif_width = max(max(row) for row in motif) + ONE
    top = randint(ZERO, FIVE - height_value)
    left = randint(ZERO, FIVE - motif_width)
    return _paint_motif_25c199f5(motif, color, (top, left))


def generate_25c199f5(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    _ = diff_lb, diff_ub
    heights = choice(HEIGHT_TRIPLES_25c199f5)
    outer_color = choice((ONE, FIVE))
    middle_color = other((ONE, FIVE), outer_color)
    colors = (outer_color, middle_color, outer_color)
    panels = []
    rowsets = []
    for height_value, color in zip(heights, colors):
        panel, rows = _sample_panel_25c199f5(height_value, color)
        panels.append(panel)
        rowsets.append(rows)
    gi = hconcat(panels[0], SEPARATOR_25c199f5)
    gi = hconcat(gi, panels[1])
    gi = hconcat(gi, SEPARATOR_25c199f5)
    gi = hconcat(gi, panels[2])
    kept = rowsets[2] + rowsets[1] + rowsets[0]
    padding = repeat(BLANK_ROW_25c199f5, FIVE - len(kept))
    go = vconcat(padding, kept)
    return {"input": gi, "output": go}
