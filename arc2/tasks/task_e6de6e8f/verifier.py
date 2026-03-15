from arc2.core import *


TURN_RIGHT_PATCH_E6DE6E8F = frozenset({(ZERO, ONE), (ONE, ZERO), (ONE, ONE)})
TURN_LEFT_PATCH_E6DE6E8F = frozenset({(ZERO, ZERO), (ONE, ZERO), (ONE, ONE)})
STRAIGHT_PATCH_E6DE6E8F = frozenset({(ZERO, ZERO), (ONE, ZERO)})

PATCH_TO_STEP_E6DE6E8F = {
    TURN_RIGHT_PATCH_E6DE6E8F: NEG_ONE,
    STRAIGHT_PATCH_E6DE6E8F: ZERO,
    TURN_LEFT_PATCH_E6DE6E8F: ONE,
}


def verify_e6de6e8f(I: Grid) -> Grid:
    x0 = mostcolor(I)
    x1 = other(palette(I), x0)
    x2 = (x0 + ONE) % TEN
    x3 = (x0 + TWO) % TEN
    x4 = branch(equality(x2, x1), x3, x2)
    x5 = objects(I, T, F, F)
    x6 = colorfilter(x5, x0)
    x7 = order(x6, leftmost)
    x8 = apply(compose(normalize, toindices), x7)
    x9 = tuple(PATCH_TO_STEP_E6DE6E8F[patch] for patch in x8)
    x10 = [THREE]
    for x11 in x9:
        x10.append(x10[-ONE] + x11)
        if x11 == ZERO:
            x10.append(x10[-ONE])
    x12 = tuple(x10[:EIGHT])
    x13 = canvas(x1, (EIGHT, SEVEN))
    x14 = fill(x13, x4, initset((ZERO, THREE)))
    x15 = x14
    for x16, (x17, x18) in enumerate(zip(x12, x12[ONE:]), start=ONE):
        x19 = connect((x16, x17), (x16, x18))
        x15 = fill(x15, x0, x19)
    return x15
