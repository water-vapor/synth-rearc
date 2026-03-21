from arc2.core import *


def verify_bbb1b8b6(I: Grid) -> Grid:
    x0 = astuple(FOUR, FOUR)
    x1 = crop(I, ORIGIN, x0)
    x2 = crop(I, astuple(ZERO, FIVE), x0)
    x3 = ofcolor(x1, ZERO)
    x4 = difference(asindices(x2), ofcolor(x2, ZERO))
    x5 = equality(x3, x4)
    x6 = remove(ZERO, palette(x2))
    x7 = branch(equality(size(x6), ZERO), ZERO, first(x6))
    x8 = fill(x1, x7, x3)
    x9 = branch(x5, x8, x1)
    return x9
