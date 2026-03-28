from synth_rearc.core import *


def generate_759f3fd3(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    x0 = unifint(diff_lb, diff_ub, (FIVE, 15))
    x1 = double(x0)
    x2 = multiply(x1, UNITY)
    x3 = canvas(ZERO, x2)
    x4 = randint(THREE, x1 - FOUR)
    x5 = randint(THREE, x1 - FOUR)
    x6 = decrement(x1)
    x7 = connect(astuple(x4, ZERO), astuple(x4, x6))
    x8 = connect(astuple(ZERO, x5), astuple(x6, x5))
    x9 = combine(x7, x8)
    x10 = fill(x3, THREE, x9)
    x11 = initset((x4, x5))
    x12 = increment(x1)
    x13 = interval(TWO, x12, TWO)
    x14 = lbind(power, outbox)
    x15 = apply(x14, x13)
    x16 = rapply(x15, x11)
    x17 = frozenset(merge(x16))
    x18 = underfill(x10, FOUR, x17)
    return {"input": x10, "output": x18}
