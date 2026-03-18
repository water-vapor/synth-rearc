from arc2.core import *


def _segment_bounds(rows: tuple[int, ...], height: int) -> tuple[tuple[int, ...], tuple[int, ...]]:
    mids = tuple((a + b) // TWO for a, b in zip(rows, rows[ONE:]))
    starts = (ZERO,) + tuple(a + ONE for a in mids)
    ends = mids + (height - ONE,)
    return starts, ends


def _segment_sizes(rows: tuple[int, ...], height: int) -> tuple[int, ...]:
    starts, ends = _segment_bounds(rows, height)
    return tuple(b - a + ONE for a, b in zip(starts, ends))


def _render_output(rows: tuple[int, ...], colors: tuple[int, ...], shape_: tuple[int, int]) -> Grid:
    h, w = shape_
    right = w - ONE
    bottom = h - ONE
    starts, ends = _segment_bounds(rows, h)
    go = canvas(ZERO, shape_)
    for color_, start, end, row in zip(colors, starts, ends, rows):
        border = product(interval(start, end + ONE, ONE), (ZERO, right))
        full = connect((row, ZERO), (row, right))
        go = fill(go, color_, border)
        go = fill(go, color_, full)
    top = connect((ZERO, ZERO), (ZERO, right))
    bottomline = connect((bottom, ZERO), (bottom, right))
    go = fill(go, colors[ZERO], top)
    go = fill(go, colors[NEG_ONE], bottomline)
    return go


def _sample_rows(count: int) -> tuple[int, ...]:
    rowspace = interval(ONE, 14, ONE)
    while True:
        rows = tuple(sorted(sample(rowspace, count)))
        gaps = tuple(b - a for a, b in zip(rows, rows[ONE:]))
        if len(gaps) > ZERO and min(gaps) < TWO:
            continue
        segsizes = _segment_sizes(rows, 15)
        if min(segsizes) < THREE:
            continue
        if max(segsizes) > SEVEN:
            continue
        return rows


def generate_0f63c0b9(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    count = unifint(diff_lb, diff_ub, (THREE, FOUR))
    rows = _sample_rows(count)
    colors = tuple(sample(remove(ZERO, interval(ZERO, TEN, ONE)), count))
    cols = tuple(sample(interval(ZERO, 15, ONE), count))
    gi = canvas(ZERO, (15, 15))
    for row, col, color_ in zip(rows, cols, colors):
        gi = fill(gi, color_, initset(astuple(row, col)))
    go = _render_output(rows, colors, (15, 15))
    return {"input": gi, "output": go}
