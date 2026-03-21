from arc2.core import *


def verify_a8610ef7(I: Grid) -> Grid:
    x0 = hmirror(I)
    x1 = ofcolor(I, EIGHT)
    x2 = ofcolor(x0, EIGHT)
    x3 = intersection(x1, x2)
    x4 = difference(x1, x3)
    x5 = fill(I, TWO, x3)
    x6 = fill(x5, FIVE, x4)
    return x6
