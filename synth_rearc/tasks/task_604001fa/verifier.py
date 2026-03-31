from synth_rearc.core import *


MARKER_MISSING_TOP_LEFT_604001fa = frozenset({(ZERO, ONE), (ONE, ZERO), (ONE, ONE)})
MARKER_MISSING_BOTTOM_RIGHT_604001fa = frozenset({(ZERO, ZERO), (ZERO, ONE), (ONE, ZERO)})
MARKER_MISSING_BOTTOM_LEFT_604001fa = frozenset({(ZERO, ZERO), (ZERO, ONE), (ONE, ONE)})


def verify_604001fa(I: Grid) -> Grid:
    x0 = objects(I, T, T, T)
    x1 = colorfilter(x0, ONE)
    x2 = colorfilter(x0, SEVEN)
    x3 = order(x1, ulcorner)
    x4 = order(x2, ulcorner)
    x5 = compose(toindices, normalize)
    x6 = matcher(x5, MARKER_MISSING_TOP_LEFT_604001fa)
    x7 = matcher(x5, MARKER_MISSING_BOTTOM_RIGHT_604001fa)
    x8 = matcher(x5, MARKER_MISSING_BOTTOM_LEFT_604001fa)
    x9 = lambda x: branch(x6(x), THREE, branch(x7(x), SIX, branch(x8(x), FOUR, EIGHT)))
    x10 = apply(x9, x4)
    x11 = pair(x10, x3)
    x12 = fork(recolor, first, last)
    x13 = mapply(x12, x11)
    x14 = canvas(ZERO, shape(I))
    x15 = paint(x14, x13)
    return x15
