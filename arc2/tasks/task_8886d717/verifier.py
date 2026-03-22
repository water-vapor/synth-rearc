from arc2.core import *


def verify_8886d717(I: Grid) -> Grid:
    x0 = ofcolor(I, EIGHT)
    x1 = ofcolor(I, TWO)
    x2 = frontiers(I)
    x3 = extract(x2, matcher(color, NINE))
    if hline(x3):
        x4 = branch(equality(uppermost(x3), ZERO), UP, DOWN)
    else:
        x4 = branch(equality(leftmost(x3), ZERO), LEFT, RIGHT)
    x5 = compose(lbind(adjacent, x1), initset)
    x6 = sfilter(x0, x5)
    x7 = difference(x0, x6)
    x8 = fill(I, TWO, x6)
    x9 = fill(x8, SEVEN, x7)
    x10 = fill(x9, EIGHT, x7)
    x11 = shift(x7, x4)
    x12 = fill(x10, EIGHT, x11)
    return x12
