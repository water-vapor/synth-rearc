from synth_rearc.core import *


def verify_e4941b18(I: Grid) -> Grid:
    x0 = ofcolor(I, FIVE)
    x1 = ofcolor(I, TWO)
    x2 = ofcolor(I, EIGHT)
    x3 = leftmost(x1)
    x4 = leftmost(x2)
    x5 = branch(greater(x3, x4), decrement(leftmost(x0)), increment(rightmost(x0)))
    x6 = astuple(lowermost(x0), x5)
    x7 = fill(I, SEVEN, x1)
    x8 = fill(x7, SEVEN, x2)
    x9 = fill(x8, TWO, x2)
    x10 = fill(x9, EIGHT, initset(x6))
    return x10
