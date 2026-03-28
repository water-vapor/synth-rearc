from synth_rearc.core import *


def generate_0b17323b(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        side = unifint(diff_lb, diff_ub, (15, 30))
        start = unifint(diff_lb, diff_ub, (ZERO, side - FOUR))
        maxstep = (side - ONE - start) // THREE
        if maxstep < ONE:
            continue
        step = unifint(diff_lb, diff_ub, (ONE, maxstep))
        maxpts = (side - ONE - start) // step + ONE
        x0 = interval(ZERO, THREE, ONE)
        x1 = lbind(multiply, step)
        x2 = apply(x1, x0)
        x3 = lbind(add, start)
        x4 = apply(x3, x2)
        x5 = pair(x4, x4)
        x6 = interval(THREE, maxpts, ONE)
        x7 = apply(x1, x6)
        x8 = apply(x3, x7)
        x9 = pair(x8, x8)
        gi = canvas(ZERO, (side, side))
        gi = fill(gi, ONE, x5)
        go = fill(gi, TWO, x9)
        if colorcount(go, TWO) == ZERO:
            continue
        return {"input": gi, "output": go}
