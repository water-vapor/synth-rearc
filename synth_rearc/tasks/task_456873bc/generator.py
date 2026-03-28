from synth_rearc.core import *


def generate_456873bc(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = unifint(diff_lb, diff_ub, (THREE, FOUR))
        x1 = choice((False, True))
        x2 = randint(ZERO, x0 - ONE)
        x3 = tuple((x4, x5) for x4 in interval(ZERO, x0, ONE) for x5 in interval(ZERO, x0, ONE))
        x4 = unifint(diff_lb, diff_ub, (x0 + TWO, x0 * x0 - x0))
        x5 = frozenset(sample(x3, x4))
        x6 = {x7[0] for x7 in x5}
        x7 = {x8[1] for x8 in x5}
        if size(x6) != x0 or size(x7) != x0:
            continue
        x8 = tuple(x9 for x9 in x5 if (x9[1] if x1 else x9[0]) == x2)
        x9 = size(x8)
        x10 = x4 - x9
        if not (ONE <= x9 <= max(ONE, x0 - TWO)):
            continue
        if x10 < max(THREE, x0):
            continue
        x11 = add(multiply(x0, x0), decrement(x0))
        x12 = increment(x0)
        x13 = canvas(ZERO, (x11, x11))
        for x14 in x5:
            if (x14[1] if x1 else x14[0]) == x2:
                continue
            x15 = multiply(x14, x12)
            x16 = shift(x5, x15)
            x13 = fill(x13, TWO, x16)
        x17 = multiply(x2, x12)
        if x1:
            x18 = frozenset((x19, x20) for x19 in range(x11) for x20 in range(x17, x17 + x0))
        else:
            x18 = frozenset((x19, x20) for x19 in range(x17, x17 + x0) for x20 in range(x11))
        x19 = fill(x13, THREE, x18)
        x20 = canvas(ZERO, (x11, x11))
        for x21 in x5:
            x22 = multiply(x21, x12)
            x23 = shift(x5, x22)
            x20 = fill(x20, TWO, x23)
            x24 = add(x21, x22)
            x20 = fill(x20, EIGHT, initset(x24))
        return {"input": x19, "output": x20}
