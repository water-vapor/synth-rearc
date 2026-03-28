from synth_rearc.core import *


GRID_SHAPE_7EE1C6EA = astuple(TEN, TEN)
FRAME_SIDES_7EE1C6EA = (SIX, EIGHT, EIGHT)
COLOR_POOL_7EE1C6EA = remove(FIVE, remove(ZERO, interval(ZERO, TEN, ONE)))
FULL_GRID_7EE1C6EA = asindices(canvas(ZERO, GRID_SHAPE_7EE1C6EA))


def _frame_7ee1c6ea(side: int) -> Indices:
    top = divide(subtract(TEN, side), TWO)
    bottom = decrement(add(top, side))
    return box(frozenset({(top, top), (bottom, bottom)}))


def _paint_region_7ee1c6ea(
    grid: Grid,
    patch: Indices,
    acol: int,
    bcol: int,
    anum: int,
    bnum: int,
) -> Grid:
    x0 = frozenset(sample(totuple(patch), anum))
    x1 = difference(patch, x0)
    x2 = frozenset(sample(totuple(x1), bnum))
    x3 = fill(grid, acol, x0)
    x4 = fill(x3, bcol, x2)
    return x4


def _split_counts_7ee1c6ea(
    diff_lb: float,
    diff_ub: float,
    total: int,
    zero_bounds: tuple[int, int],
    min_each: int,
) -> tuple[int, int]:
    zero_lb, zero_ub = zero_bounds
    zero_ub = min(zero_ub, total - 2 * min_each)
    zeros = unifint(diff_lb, diff_ub, (zero_lb, zero_ub))
    rem = total - zeros
    anum = unifint(diff_lb, diff_ub, (min_each, rem - min_each))
    bnum = rem - anum
    return anum, bnum


def generate_7ee1c6ea(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        side = choice(FRAME_SIDES_7EE1C6EA)
        frame = _frame_7ee1c6ea(side)
        inner = backdrop(inbox(frame))
        outside = difference(FULL_GRID_7EE1C6EA, backdrop(frame))
        acol, bcol = sample(COLOR_POOL_7EE1C6EA, TWO)

        if side == SIX:
            outside_zero_bounds = (16, 28)
        else:
            outside_zero_bounds = (7, 14)

        inner_counts = _split_counts_7ee1c6ea(diff_lb, diff_ub, size(inner), (4, 10), TWO)
        outside_counts = _split_counts_7ee1c6ea(
            diff_lb, diff_ub, size(outside), outside_zero_bounds, FOUR
        )

        gi = canvas(ZERO, GRID_SHAPE_7EE1C6EA)
        gi = _paint_region_7ee1c6ea(gi, outside, acol, bcol, outside_counts[0], outside_counts[1])
        gi = fill(gi, FIVE, frame)
        gi = _paint_region_7ee1c6ea(gi, inner, acol, bcol, inner_counts[0], inner_counts[1])

        x0 = ulcorner(inner)
        x1 = crop(gi, x0, shape(inner))
        x2 = switch(x1, acol, bcol)
        x3 = shift(asobject(x2), x0)
        go = paint(gi, x3)

        return {"input": gi, "output": go}
