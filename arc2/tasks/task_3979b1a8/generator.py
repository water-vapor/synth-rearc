from arc2.core import *


INPUT_SIZES_3979B1A8 = (FIVE, SEVEN, NINE, 11, 13, 15)
COLORS_3979B1A8 = remove(ZERO, interval(ZERO, TEN, ONE))


def _cycle_line_3979b1a8(
    length: Integer,
    cycle: Tuple[Integer, ...],
) -> Tuple[Integer, ...]:
    return tuple(cycle[idx % THREE] for idx in range(length))


def _build_output_3979b1a8(
    gi: Grid,
    cycle: Tuple[Integer, ...],
) -> Grid:
    x0 = height(gi)
    x1 = width(gi)
    x2 = _cycle_line_3979b1a8(x1, cycle)
    x3 = repeat(x2, x0)
    x4 = _cycle_line_3979b1a8(x0, cycle)
    x5 = apply(rbind(repeat, x1), x4)
    x6 = tuple(
        tuple(cycle[(max(x7, x8) + (x7 == x8)) % THREE] for x8 in range(x1))
        for x7 in range(x0)
    )
    x7 = hconcat(gi, x3)
    x8 = hconcat(x5, x6)
    x9 = vconcat(x7, x8)
    return x9


def generate_3979b1a8(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    x0 = unifint(diff_lb, diff_ub, (ZERO, len(INPUT_SIZES_3979B1A8) - ONE))
    x1 = INPUT_SIZES_3979B1A8[x0]
    x2 = tuple(sample(COLORS_3979B1A8, THREE))
    x3 = x2[ZERO]
    x4 = x2[ONE]
    x5 = x2[TWO]
    x6 = canvas(x4, (x1, x1))
    x7 = corners(asindices(x6))
    x8 = fill(x6, x3, x7)
    x9 = center(asindices(x8))
    x10 = insert(x9, dneighbors(x9))
    gi = fill(x8, x5, x10)
    go = _build_output_3979b1a8(gi, (x3, x5, x4))
    return {"input": gi, "output": go}
