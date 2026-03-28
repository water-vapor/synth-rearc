from arc2.core import *


GRID_SHAPE_5B6CBEF5 = astuple(FOUR, FOUR)
GRID_CELLS_5B6CBEF5 = totuple(asindices(canvas(ZERO, GRID_SHAPE_5B6CBEF5)))
NONZERO_COLORS_5B6CBEF5 = interval(ONE, TEN, ONE)


def generate_5b6cbef5(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = choice(NONZERO_COLORS_5B6CBEF5)
        x1 = unifint(diff_lb, diff_ub, (THREE, 11))
        x2 = frozenset(sample(GRID_CELLS_5B6CBEF5, x1))
        gi = fill(canvas(ZERO, GRID_SHAPE_5B6CBEF5), x0, x2)
        x3 = asobject(gi)
        x4 = rbind(multiply, FOUR)
        x5 = apply(x4, x2)
        x6 = lbind(shift, x3)
        x7 = mapply(x6, x5)
        go = paint(canvas(ZERO, multiply(GRID_SHAPE_5B6CBEF5, FOUR)), x7)
        return {"input": gi, "output": go}
