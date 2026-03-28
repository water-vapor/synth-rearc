from synth_rearc.core import *


def generate_fc754716(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    cols = interval(ONE, TEN, ONE)
    h = add(double(unifint(diff_lb, diff_ub, (ONE, 14))), ONE)
    w = add(double(unifint(diff_lb, diff_ub, (ONE, 14))), ONE)
    col = choice(cols)
    gi = canvas(ZERO, (h, w))
    cen = astuple(halve(h), halve(w))
    gi = fill(gi, col, {cen})
    go = canvas(ZERO, (h, w))
    go = fill(go, col, box(asindices(go)))
    return {"input": gi, "output": go}
