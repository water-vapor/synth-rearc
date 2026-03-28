from synth_rearc.core import *


def _binary_block_be03b35f(
    diff_lb: float,
    diff_ub: float,
    bounds: IntegerTuple,
) -> Grid:
    x0 = canvas(ZERO, TWO_BY_TWO)
    x1 = totuple(asindices(x0))
    x2 = unifint(diff_lb, diff_ub, bounds)
    x3 = sample(x1, x2)
    x4 = fill(x0, ONE, x3)
    return x4


def generate_be03b35f(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    x0 = canvas(ZERO, astuple(TWO, ONE))
    x1 = canvas(ZERO, astuple(ONE, FIVE))
    x2 = canvas(TWO, TWO_BY_TWO)
    while True:
        x3 = _binary_block_be03b35f(diff_lb, diff_ub, astuple(ONE, THREE))
        x4 = _binary_block_be03b35f(diff_lb, diff_ub, astuple(ONE, THREE))
        x5 = _binary_block_be03b35f(diff_lb, diff_ub, astuple(TWO, THREE))
        x6 = initset(x3)
        x7 = insert(x4, x6)
        x8 = insert(x5, x7)
        if size(x8) != THREE:
            continue
        x9 = add(colorcount(x3, ONE), colorcount(x4, ONE))
        if x9 < FOUR or x9 > SIX:
            continue
        x10 = hconcat(x3, x0)
        x11 = hconcat(x10, x4)
        x12 = hconcat(x5, x0)
        x13 = hconcat(x12, x2)
        x14 = vconcat(x11, x1)
        gi = vconcat(x14, x13)
        go = rot90(x5)
        return {"input": gi, "output": go}
