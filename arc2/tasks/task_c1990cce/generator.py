from arc2.core import *


def generate_c1990cce(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    x0 = add(multiply(unifint(diff_lb, diff_ub, (ONE, 14)), TWO), ONE)
    x1 = choice(remove(ONE, interval(ZERO, TEN, ONE)))
    x2 = choice(remove(x1, remove(ONE, interval(ZERO, TEN, ONE))))
    x3 = halve(decrement(x0))
    x4 = canvas(x1, (ONE, x0))
    x5 = fill(x4, x2, initset((ZERO, x3)))
    x6 = decrement(x0)
    x7 = canvas(x1, (x0, x0))
    x8 = connect((ZERO, x3), (x3, ZERO))
    x9 = connect((ZERO, x3), (x3, x6))
    x10 = combine(x8, x9)
    x11 = fill(x7, x2, x10)
    x12 = ONE
    x13 = x11
    while True:
        x14 = subtract(x3, multiply(FOUR, x12))
        if x14 < -x6:
            break
        x15 = max(ZERO, invert(x14), add(double(x12), ONE))
        x16 = add(x15, x14)
        x17 = min(x6, subtract(x6, x14))
        x18 = add(x17, x14)
        x19 = connect((x15, x16), (x17, x18))
        x13 = fill(x13, ONE, x19)
        x12 = increment(x12)
    return {"input": x5, "output": x13}
