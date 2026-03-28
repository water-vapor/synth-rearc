from synth_rearc.core import *


def generate_770cc55f(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    half_bounds = (FOUR, SEVEN)
    width_bounds = (FOUR, SEVEN)
    colopts = remove(TWO, remove(FOUR, interval(ONE, TEN, ONE)))
    x0 = unifint(diff_lb, diff_ub, half_bounds)
    x1 = add(double(x0), ONE)
    x2 = unifint(diff_lb, diff_ub, width_bounds)
    x3 = choice(colopts)
    x4 = choice((True, False))
    x5 = unifint(diff_lb, diff_ub, (THREE, x2))
    x6 = unifint(diff_lb, diff_ub, (TWO, max(TWO, decrement(x5))))
    x7 = branch(x4, x5, x6)
    x8 = branch(x4, x6, x5)
    while True:
        x9 = randint(ZERO, x2 - x7)
        x10 = randint(ZERO, x2 - x8)
        x11 = x9 + x7 - ONE
        x12 = x10 + x8 - ONE
        x13 = max(x9, x10)
        x14 = min(x11, x12)
        if x13 <= x14:
            break
    x15 = canvas(ZERO, (x1, x2))
    x16 = decrement(x2)
    x17 = connect((x0, ZERO), (x0, x16))
    x18 = connect((ZERO, x9), (ZERO, x11))
    x19 = decrement(x1)
    x20 = connect((x19, x10), (x19, x12))
    x21 = fill(x15, TWO, x17)
    x22 = fill(x21, x3, x18)
    x23 = fill(x22, x3, x20)
    x24 = branch(x4, interval(ONE, x0, ONE), interval(x0 + ONE, x19, ONE))
    x25 = interval(x13, x14 + ONE, ONE)
    x26 = product(x24, x25)
    x27 = fill(x23, FOUR, x26)
    return {"input": x23, "output": x27}
