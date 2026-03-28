from synth_rearc.core import *


def generate_e7639916(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    x0 = unifint(diff_lb, diff_ub, (SIX, TEN))
    x1 = unifint(diff_lb, diff_ub, (SEVEN, 14))
    x2 = randint(ONE, THREE)
    x3 = randint(ONE, THREE)
    x4 = randint(ONE, THREE)
    x5 = randint(ONE, THREE)
    x6 = add(x0, add(x2, x3))
    x7 = add(x1, add(x4, x5))
    x8 = x2
    x9 = subtract(add(x8, x0), ONE)
    x10 = x4
    x11 = subtract(add(x10, x1), ONE)
    x12 = choice((ZERO, ONE, TWO, THREE))
    x13 = randint(add(x10, ONE), subtract(x11, ONE))
    x14 = randint(add(x8, ONE), subtract(x9, ONE))
    if x12 == ZERO:
        x15 = (x8, x10)
        x16 = (x9, x13)
        x17 = (x14, x11)
    elif x12 == ONE:
        x15 = (x8, x11)
        x16 = (x9, x13)
        x17 = (x14, x10)
    elif x12 == TWO:
        x15 = (x9, x10)
        x16 = (x8, x13)
        x17 = (x14, x11)
    else:
        x15 = (x9, x11)
        x16 = (x8, x13)
        x17 = (x14, x10)
    x18 = frozenset((x15, x16, x17))
    x19 = canvas(ZERO, (x6, x7))
    x20 = fill(x19, EIGHT, x18)
    x21 = box(x18)
    x22 = underfill(x20, ONE, x21)
    return {"input": x20, "output": x22}
