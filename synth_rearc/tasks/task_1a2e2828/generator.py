from synth_rearc.core import *


COLORS_1A2E2828 = (ONE, TWO, THREE, FOUR, FIVE, SIX, SEVEN, EIGHT, NINE)


def _sample_axis_1a2e2828(
    diff_lb: float,
    diff_ub: float,
    nbands: Integer,
    thickness_bounds: tuple[int, int],
) -> tuple[tuple[Integer, ...], tuple[Integer, ...], Integer]:
    thicknesses = tuple(unifint(diff_lb, diff_ub, thickness_bounds) for _ in range(nbands))
    gaps = tuple(unifint(diff_lb, diff_ub, (ONE, TWO)) for _ in range(nbands - ONE))
    lead = unifint(diff_lb, diff_ub, (ONE, TWO))
    trail = unifint(diff_lb, diff_ub, (ONE, TWO))
    starts = []
    offset = lead
    for idx, thickness in enumerate(thicknesses):
        starts.append(offset)
        offset += thickness
        if idx < nbands - ONE:
            offset += gaps[idx]
    return tuple(starts), thicknesses, offset + trail


def _paint_row_band_1a2e2828(
    grid: Grid,
    spec: tuple[Integer, Integer, Integer],
) -> Grid:
    x0, x1, x2 = spec
    x3 = interval(x0, x0 + x1, ONE)
    x4 = interval(ZERO, width(grid), ONE)
    x5 = product(x3, x4)
    x6 = fill(grid, x2, x5)
    return x6


def _paint_col_band_1a2e2828(
    grid: Grid,
    spec: tuple[Integer, Integer, Integer],
) -> Grid:
    x0, x1, x2 = spec
    x3 = interval(ZERO, height(grid), ONE)
    x4 = interval(x0, x0 + x1, ONE)
    x5 = product(x3, x4)
    x6 = fill(grid, x2, x5)
    return x6


def _render_input_1a2e2828(
    shape_: tuple[Integer, Integer],
    row_specs: tuple[tuple[Integer, Integer, Integer], ...],
    col_specs: tuple[tuple[Integer, Integer, Integer], ...],
    winner_orient: str,
    winner_index: Integer,
) -> Grid:
    gi = canvas(ZERO, shape_)
    if winner_orient == "row":
        for idx, spec in enumerate(row_specs):
            if idx != winner_index:
                gi = _paint_row_band_1a2e2828(gi, spec)
        for spec in col_specs:
            gi = _paint_col_band_1a2e2828(gi, spec)
        return _paint_row_band_1a2e2828(gi, row_specs[winner_index])
    for idx, spec in enumerate(col_specs):
        if idx != winner_index:
            gi = _paint_col_band_1a2e2828(gi, spec)
    for spec in row_specs:
        gi = _paint_row_band_1a2e2828(gi, spec)
    return _paint_col_band_1a2e2828(gi, col_specs[winner_index])


def generate_1a2e2828(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        winner_orient = choice(("row", "col"))
        nrows = choice((ONE, TWO, TWO, THREE))
        ncols = choice((ONE, TWO, TWO, THREE))
        row_starts, row_thicknesses, h = _sample_axis_1a2e2828(diff_lb, diff_ub, nrows, (ONE, THREE))
        col_starts, col_widths, w = _sample_axis_1a2e2828(diff_lb, diff_ub, ncols, (ONE, TWO))
        if not (THREE <= h <= 11 and THREE <= w <= 13):
            continue
        colors = sample(COLORS_1A2E2828, nrows + ncols)
        row_colors = colors[:nrows]
        col_colors = colors[nrows:]
        row_specs = tuple((x0, x1, x2) for x0, x1, x2 in zip(row_starts, row_thicknesses, row_colors))
        col_specs = tuple((x0, x1, x2) for x0, x1, x2 in zip(col_starts, col_widths, col_colors))
        winner_index = randint(ZERO, nrows - ONE) if winner_orient == "row" else randint(ZERO, ncols - ONE)
        gi = _render_input_1a2e2828((h, w), row_specs, col_specs, winner_orient, winner_index)
        if mostcolor(gi) != ZERO:
            continue
        x0 = frontiers(gi)
        x1 = {color(obj) for obj in x0}
        winner_color = row_specs[winner_index][TWO] if winner_orient == "row" else col_specs[winner_index][TWO]
        if x1 != {winner_color}:
            continue
        go = canvas(winner_color, UNITY)
        return {"input": gi, "output": go}
