from synth_rearc.core import *


TURN_RIGHT_PATCH_E6DE6E8F = frozenset({(ZERO, ONE), (ONE, ZERO), (ONE, ONE)})
TURN_LEFT_PATCH_E6DE6E8F = frozenset({(ZERO, ZERO), (ONE, ZERO), (ONE, ONE)})
STRAIGHT_PATCH_E6DE6E8F = frozenset({(ZERO, ZERO), (ONE, ZERO)})

PATCH_TO_STEP_E6DE6E8F = {
    TURN_RIGHT_PATCH_E6DE6E8F: NEG_ONE,
    STRAIGHT_PATCH_E6DE6E8F: ZERO,
    TURN_LEFT_PATCH_E6DE6E8F: ONE,
}


def verify_e6de6e8f(I: Grid) -> Grid:
    x0 = objects(I, T, F, F)
    x1 = colorfilter(x0, TWO)
    x2 = order(x1, leftmost)
    x3 = apply(compose(normalize, toindices), x2)
    x4 = tuple(PATCH_TO_STEP_E6DE6E8F[patch] for patch in x3)
    x5 = [THREE]
    for x6 in x4:
        x5.append(x5[-ONE] + x6)
        if x6 == ZERO:
            x5.append(x5[-ONE])
    x7 = tuple(x5[:EIGHT])
    x8 = canvas(ZERO, (EIGHT, SEVEN))
    x9 = fill(x8, THREE, initset((ZERO, THREE)))
    x10 = x9
    for x11, (x12, x13) in enumerate(zip(x7, x7[ONE:]), start=ONE):
        x14 = connect((x11, x12), (x11, x13))
        x10 = fill(x10, TWO, x14)
    return x10
