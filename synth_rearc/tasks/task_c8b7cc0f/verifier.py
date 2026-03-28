from synth_rearc.core import *


def verify_c8b7cc0f(I: Grid) -> Grid:
    x0 = ofcolor(I, ONE)
    x1 = backdrop(x0)
    x2 = palette(I)
    x3 = remove(ZERO, x2)
    x4 = other(x3, ONE)
    x5 = ofcolor(I, x4)
    x6 = intersection(x1, x5)
    x7 = size(x6)
    x8 = frozenset((x9 // THREE, x9 % THREE) for x9 in range(x7))
    x9 = canvas(ZERO, (THREE, THREE))
    x10 = fill(x9, x4, x8)
    return x10
