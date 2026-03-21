from arc2.core import *


FG_COLORS_AC0C2AC3 = remove(SEVEN, interval(ZERO, TEN, ONE))
RADIUS_OPTIONS_AC0C2AC3 = (THREE, FOUR, FIVE, SIX)


def _square_patch_ac0c2ac3(center_loc: IntegerTuple, radius: Integer) -> Indices:
    x0 = astuple(radius, radius)
    x1 = subtract(center_loc, x0)
    x2 = add(center_loc, x0)
    x3 = insert(x1, initset(x2))
    return backdrop(x3)


def _ring_patch_ac0c2ac3(center_loc: IntegerTuple, radius: Integer) -> Indices:
    x0 = astuple(radius, radius)
    x1 = subtract(center_loc, x0)
    x2 = add(center_loc, x0)
    x3 = insert(x1, initset(x2))
    return box(x3)


def generate_ac0c2ac3(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    x0 = unifint(diff_lb, diff_ub, (first(RADIUS_OPTIONS_AC0C2AC3), last(RADIUS_OPTIONS_AC0C2AC3)))
    x1 = add(double(x0), ONE)
    x2 = astuple(x0, x0)
    x3 = tuple(sample(FG_COLORS_AC0C2AC3, add(x0, ONE)))
    x4 = canvas(SEVEN, (x1, x1))
    x5 = fill(x4, x3[ZERO], initset(x2))
    for x6 in interval(ONE, add(x0, ONE), ONE):
        x7 = _ring_patch_ac0c2ac3(x2, x6)
        x8 = choice(totuple(x7))
        x5 = fill(x5, x3[x6], initset(x8))
    x9 = canvas(SEVEN, (x1, x1))
    x10 = x9
    for x11 in interval(x0, NEG_ONE, NEG_ONE):
        x12 = _square_patch_ac0c2ac3(x2, x11)
        x10 = fill(x10, x3[x11], x12)
    return {"input": x5, "output": x10}
