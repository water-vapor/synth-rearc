from arc2.core import *


def verify_b5bb5719(I: Grid) -> Grid:
    x0 = combine(ofcolor(I, TWO), ofcolor(I, FIVE))
    x1 = leftmost(x0)
    x2 = rightmost(x0)
    x3 = height(I)
    x4 = I
    x5 = interval(ONE, x3, ONE)
    for x6 in x5:
        x7 = add(x1, decrement(x6))
        x8 = subtract(x2, increment(x6))
        if greater(x7, x8):
            break
        x9 = astuple(decrement(x6), x7)
        x10 = astuple(decrement(x6), x8)
        x11 = connect(x9, x10)
        x12 = intersection(ofcolor(x4, TWO), x11)
        x13 = intersection(ofcolor(x4, FIVE), x11)
        x14 = shift(x12, UNITY)
        x15 = shift(x13, UNITY)
        x4 = fill(x4, FIVE, x14)
        x4 = fill(x4, TWO, x15)
    return x4
