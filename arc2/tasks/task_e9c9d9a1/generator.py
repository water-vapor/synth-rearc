from arc2.core import *


def _sample_bands_e9c9d9a1(
    diff_lb: float,
    diff_ub: float,
    nbands: Integer,
    outer_bounds: tuple[int, int],
    inner_bounds: tuple[int, int],
) -> tuple[Integer, ...]:
    bands = [unifint(diff_lb, diff_ub, outer_bounds)]
    for _ in range(nbands - TWO):
        bands.append(unifint(diff_lb, diff_ub, inner_bounds))
    bands.append(unifint(diff_lb, diff_ub, outer_bounds))
    return tuple(bands)


def _line_positions_e9c9d9a1(
    bands: tuple[Integer, ...],
) -> tuple[Integer, ...]:
    locs = []
    offset = ZERO
    for band in bands[:-ONE]:
        offset += band
        locs.append(offset)
        offset += ONE
    return tuple(locs)


def _render_output_e9c9d9a1(
    gi: Grid,
    row_lines: tuple[Integer, ...],
    col_lines: tuple[Integer, ...],
) -> Grid:
    x0 = interval(ZERO, first(row_lines), ONE)
    x1 = interval(increment(last(row_lines)), height(gi), ONE)
    x2 = interval(ZERO, first(col_lines), ONE)
    x3 = interval(increment(last(col_lines)), width(gi), ONE)
    go = fill(gi, TWO, product(x0, x2))
    go = fill(go, FOUR, product(x0, x3))
    go = fill(go, ONE, product(x1, x2))
    go = fill(go, EIGHT, product(x1, x3))
    for x4, x5 in zip(row_lines, row_lines[ONE:]):
        x6 = interval(increment(x4), x5, ONE)
        for x7, x8 in zip(col_lines, col_lines[ONE:]):
            x9 = interval(increment(x7), x8, ONE)
            go = fill(go, SEVEN, product(x6, x9))
    return go


def generate_e9c9d9a1(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        nrowbands = choice((THREE, FOUR, FOUR, FIVE))
        ncolbands = choice((THREE, THREE, FOUR, FIVE))
        row_bands = _sample_bands_e9c9d9a1(diff_lb, diff_ub, nrowbands, (TWO, SIX), (TWO, SIX))
        col_bands = _sample_bands_e9c9d9a1(diff_lb, diff_ub, ncolbands, (ONE, FIVE), (TWO, FOUR))
        h = sum(row_bands) + nrowbands - ONE
        w = sum(col_bands) + ncolbands - ONE
        if not (14 <= h <= 20 and 12 <= w <= 18):
            continue
        gi = canvas(ZERO, (h, w))
        row_lines = _line_positions_e9c9d9a1(row_bands)
        col_lines = _line_positions_e9c9d9a1(col_bands)
        for x0 in row_lines:
            gi = fill(gi, THREE, hfrontier((x0, ZERO)))
        for x1 in col_lines:
            gi = fill(gi, THREE, vfrontier((ZERO, x1)))
        x2 = frontiers(gi)
        x3 = sfilter(x2, hline)
        x4 = sfilter(x2, vline)
        if size(x3) != nrowbands - ONE:
            continue
        if size(x4) != ncolbands - ONE:
            continue
        if mostcolor(gi) != ZERO:
            continue
        go = _render_output_e9c9d9a1(gi, row_lines, col_lines)
        return {"input": gi, "output": go}
