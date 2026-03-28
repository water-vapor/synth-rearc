from synth_rearc.core import *


MARGIN_BOUNDS_B7FB29BC = (ONE, SIX)


def generate_b7fb29bc(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    x0 = unifint(diff_lb, diff_ub, (THREE, SIX))
    x1 = increment(double(x0))
    x2 = unifint(diff_lb, diff_ub, MARGIN_BOUNDS_B7FB29BC)
    x3 = unifint(diff_lb, diff_ub, MARGIN_BOUNDS_B7FB29BC)
    x4 = unifint(diff_lb, diff_ub, MARGIN_BOUNDS_B7FB29BC)
    x5 = unifint(diff_lb, diff_ub, MARGIN_BOUNDS_B7FB29BC)
    x6 = x2 + x1 + x3
    x7 = x4 + x1 + x5
    x8 = canvas(ZERO, (x6, x7))
    x9 = astuple(x2, x4)
    x10 = astuple(x2 + x1 - ONE, x4 + x1 - ONE)
    x11 = box(frozenset({x9, x10}))
    x12 = randint(ONE, x1 - TWO)
    x13 = randint(ONE, x1 - TWO)
    x14 = add(x9, astuple(x12, x13))
    x15 = initset(x14)
    gi = fill(x8, THREE, x11)
    gi = fill(gi, THREE, x15)
    x16 = delta(x11)
    go = gi
    x17 = x15
    x18 = ONE
    while True:
        x17 = outbox(x17)
        x19 = intersection(x17, x16)
        if size(x19) == ZERO:
            break
        x20 = FOUR if x18 % TWO == ONE else TWO
        go = fill(go, x20, x19)
        x18 += ONE
    return {"input": gi, "output": go}
