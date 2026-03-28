from synth_rearc.core import *


def verify_9110e3c5(I: Grid) -> Grid:
    x0 = interval(ONE, FOUR, ONE)
    x1 = lbind(colorcount, I)
    x2 = order(x0, x1)
    x3 = last(x2)
    x4 = canvas(ZERO, (THREE, THREE))
    x5 = frozenset({(ZERO, TWO), (ONE, ZERO), (ONE, ONE), (TWO, ONE)})
    x6 = fill(x4, EIGHT, x5)
    x7 = frozenset({(ONE, ZERO), (ONE, ONE), (ONE, TWO)})
    x8 = fill(x4, EIGHT, x7)
    x9 = frozenset({(ZERO, ONE), (ZERO, TWO), (ONE, ONE), (TWO, ONE)})
    x10 = fill(x4, EIGHT, x9)
    x11 = equality(x3, ONE)
    x12 = branch(x11, x6, x8)
    x13 = equality(x3, THREE)
    x14 = branch(x13, x10, x12)
    return x14
