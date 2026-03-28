from synth_rearc.core import *


def generate_0e671a1a(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    dims = (13, 13)
    coords = interval(ONE, 12, ONE)
    while True:
        rows = sample(coords, THREE)
        cols = sample(coords, THREE)
        p3 = astuple(rows[0], cols[0])
        p4 = astuple(rows[1], cols[1])
        p2 = astuple(rows[2], cols[2])
        leg34 = manhattan(initset(p3), initset(p4))
        leg42 = manhattan(initset(p4), initset(p2))
        targ34 = unifint(diff_lb, diff_ub, (11, 13))
        targ42 = unifint(diff_lb, diff_ub, (11, 13))
        if leg34 != targ34 or leg42 != targ42:
            continue
        gi = canvas(ZERO, dims)
        gi = fill(gi, THREE, initset(p3))
        gi = fill(gi, FOUR, initset(p4))
        gi = fill(gi, TWO, initset(p2))
        x0 = astuple(first(p4), last(p3))
        x1 = astuple(first(p2), last(p4))
        x2 = connect(p3, x0)
        x3 = connect(x0, p4)
        x4 = connect(p4, x1)
        x5 = connect(x1, p2)
        x6 = combine(x2, x3)
        x7 = combine(x4, x5)
        x8 = combine(x6, x7)
        x9 = combine(initset(p3), initset(p4))
        x10 = combine(x9, initset(p2))
        x11 = difference(x8, x10)
        go = fill(gi, FIVE, x11)
        return {"input": gi, "output": go}
