from arc2.core import *


def verify_c1990cce(I: Grid) -> Grid:
    x0 = width(I)
    x1 = mostcolor(I)
    x2 = other(palette(I), x1)
    x3 = leftmost(ofcolor(I, x2))
    x4 = decrement(x0)
    x5 = canvas(x1, (x0, x0))
    x6 = connect((ZERO, x3), (x3, ZERO))
    x7 = connect((ZERO, x3), (x3, x4))
    x8 = combine(x6, x7)
    x9 = fill(x5, x2, x8)
    x10 = ONE
    x11 = x9
    while True:
        x12 = subtract(x3, multiply(FOUR, x10))
        if x12 < -x4:
            break
        x13 = max(ZERO, invert(x12), add(double(x10), ONE))
        x14 = add(x13, x12)
        x15 = min(x4, subtract(x4, x12))
        x16 = add(x15, x12)
        x17 = connect((x13, x14), (x15, x16))
        x11 = fill(x11, ONE, x17)
        x10 = increment(x10)
    return x11
