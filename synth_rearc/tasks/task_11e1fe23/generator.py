from synth_rearc.core import *


COLORS = remove(FIVE, remove(ZERO, interval(ZERO, TEN, ONE)))
MARGIN_BOUNDS = (ONE, THREE)
SIDE_OPTIONS = (SEVEN, SEVEN, NINE)


def generate_11e1fe23(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    side = choice(SIDE_OPTIONS)
    top = unifint(diff_lb, diff_ub, MARGIN_BOUNDS)
    bottom = unifint(diff_lb, diff_ub, MARGIN_BOUNDS)
    left = unifint(diff_lb, diff_ub, MARGIN_BOUNDS)
    right = unifint(diff_lb, diff_ub, MARGIN_BOUNDS)
    h = top + side + bottom
    w = left + side + right
    loci = top + side - ONE
    locj = left + side - ONE
    gi = canvas(ZERO, (h, w))
    x0 = frozenset({(top, left), (loci, locj)})
    x1 = sample(totuple(corners(x0)), THREE)
    x2 = sample(COLORS, THREE)
    x3 = frozenset((value, index) for value, index in zip(x2, x1))
    gi = paint(gi, x3)
    x4 = center(x0)
    x5 = initset(x4)
    x6 = frozenset((value, add(x4, position(x5, initset(index)))) for value, index in x3)
    go = paint(gi, x6)
    go = fill(go, FIVE, x5)
    return {"input": gi, "output": go}
