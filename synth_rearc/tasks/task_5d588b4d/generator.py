from synth_rearc.core import *


COLORS_5D588B4D = remove(ZERO, interval(ZERO, TEN, ONE))


def generate_5d588b4d(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    x0 = choice(COLORS_5D588B4D)
    x1 = unifint(diff_lb, diff_ub, (THREE, EIGHT))
    x2 = interval(ONE, increment(x1), ONE)
    x3 = interval(decrement(x1), ZERO, NEG_ONE)
    x4 = combine(x2, x3)
    x5 = tuple(combine(repeat(x0, x6), (ZERO,)) for x6 in x4)
    x6 = merge(x5)[:-1]
    x7 = add(divide(decrement(size(x6)), SEVEN), ONE)
    x8 = unifint(diff_lb, diff_ub, (max(FIVE, x1, x7), 23))
    x9 = add(divide(decrement(size(x6)), x8), ONE)
    x10 = unifint(diff_lb, diff_ub, (max(SEVEN, x9), 13))
    x11 = canvas(ZERO, astuple(x10, x8))
    x12 = frozenset((ZERO, x13) for x13 in interval(ZERO, x1, ONE))
    x14 = fill(x11, x0, x12)
    x15 = canvas(ZERO, astuple(x9, x8))
    x16 = frozenset(
        astuple(divide(x17, x8), x17 % x8)
        for x17, x18 in enumerate(x6)
        if equality(x18, x0)
    )
    x19 = fill(x15, x0, x16)
    return {"input": x14, "output": x19}
