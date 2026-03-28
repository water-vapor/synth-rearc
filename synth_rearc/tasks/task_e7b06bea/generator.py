from synth_rearc.core import *


def generate_e7b06bea(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    cols = remove(FIVE, remove(ZERO, interval(ZERO, TEN, ONE)))
    while True:
        x0 = unifint(diff_lb, diff_ub, (ONE, FOUR))
        x1 = unifint(diff_lb, diff_ub, (TWO, THREE))
        x2 = unifint(diff_lb, diff_ub, (TWO, FIVE))
        x3 = max(THREE, x1 + ONE)
        x4 = min(15, 14 // x0 + ONE)
        if x3 > x4:
            continue
        x5 = randint(x3, x4)
        x6 = randint(ONE, x0)
        x7 = (x5 - ONE) * x0 + x6
        if x7 > 14:
            continue
        if x7 < FIVE:
            continue
        x8 = x2 + x1 + ONE
        x9 = sample(cols, x1)
        gi = canvas(ZERO, (x7, x8))
        x10 = connect(ORIGIN, astuple(decrement(x0), ZERO))
        gi = fill(gi, FIVE, x10)
        for x11, x12 in enumerate(x9):
            x13 = increment(x2 + x11)
            x14 = connect(astuple(ZERO, x13), astuple(decrement(x7), x13))
            gi = fill(gi, x12, x14)
        go = canvas(ZERO, (x7, x8))
        go = fill(go, FIVE, x10)
        for x15 in range(x7):
            x16 = divide(x15, x0)
            x17 = x16 % x1
            x18 = x9[x17]
            x19 = astuple(x15, x2)
            go = fill(go, x18, initset(x19))
        return {"input": gi, "output": go}
