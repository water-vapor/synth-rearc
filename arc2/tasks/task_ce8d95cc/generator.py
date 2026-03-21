from arc2.core import *


COLORS_CE8D95CC = (ONE, TWO, THREE, FOUR, FIVE, SIX, SEVEN, EIGHT, NINE)


def _positive_composition_ce8d95cc(
    total: Integer,
    parts: Integer,
) -> tuple[Integer, ...]:
    if parts == ONE:
        return (total,)
    x0 = sorted(sample(range(ONE, total), parts - ONE))
    x1 = (ZERO,) + tuple(x0)
    x2 = tuple(x0) + (total,)
    return tuple(x4 - x3 for x3, x4 in zip(x1, x2))


def _stripe_positions_ce8d95cc(
    gaps: tuple[Integer, ...],
) -> tuple[Integer, ...]:
    x0 = []
    x1 = gaps[ZERO]
    for x2 in gaps[ONE:]:
        x0.append(x1)
        x1 += increment(x2)
    return tuple(x0)


def _render_stripes_ce8d95cc(
    shape_: tuple[Integer, Integer],
    row_positions: tuple[Integer, ...],
    row_colors: tuple[Integer, ...],
    col_positions: tuple[Integer, ...],
    col_colors: tuple[Integer, ...],
) -> Grid:
    x0 = canvas(ZERO, shape_)
    for x1, x2 in zip(col_positions, col_colors):
        x0 = fill(x0, x2, vfrontier((ZERO, x1)))
    for x3, x4 in zip(row_positions, row_colors):
        x0 = fill(x0, x4, hfrontier((x3, ZERO)))
    return x0


def generate_ce8d95cc(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = choice((TWO, TWO, THREE))
        x1 = choice((ONE, TWO, TWO, THREE, THREE, FOUR))
        x2 = unifint(diff_lb, diff_ub, (10, 13))
        x3 = unifint(diff_lb, diff_ub, (9, 13))
        x4 = increment(x0)
        x5 = increment(x1)
        x6 = subtract(x2, x0)
        x7 = subtract(x3, x1)
        if greater(x4, x6) or greater(x5, x7):
            continue

        x8 = _positive_composition_ce8d95cc(x6, x4)
        x9 = _positive_composition_ce8d95cc(x7, x5)
        x10 = _stripe_positions_ce8d95cc(x8)
        x11 = _stripe_positions_ce8d95cc(x9)
        x12 = tuple(interval(ONE, increment(double(x0)), TWO))
        x13 = tuple(interval(ONE, increment(double(x1)), TWO))
        x14 = sample(COLORS_CE8D95CC, add(x0, x1))
        x15 = tuple(x14[:x0])
        x16 = tuple(x14[x0:])

        gi = _render_stripes_ce8d95cc((x2, x3), x10, x15, x11, x16)
        go = _render_stripes_ce8d95cc((increment(double(x0)), increment(double(x1))), x12, x15, x13, x16)
        return {"input": gi, "output": go}
