from synth_rearc.core import *


def verify_9f8de559(I: Grid) -> Grid:
    x0 = ofcolor(I, SIX)
    x1 = ofcolor(I, TWO)
    x2 = position(x0, x1)
    x3 = ulcorner(x1)
    x4 = shoot(add(x3, x2), x2)
    x5 = totuple(x4)
    x6 = lambda x: manhattan(initset(x3), initset(x))
    x7 = order(x5, x6)
    x8 = lbind(index, I)
    x9 = matcher(x8, SEVEN)
    x10 = compose(flip, x9)
    x11 = extract(x7, x10)
    x12 = fill(I, SEVEN, initset(x11))
    return x12
