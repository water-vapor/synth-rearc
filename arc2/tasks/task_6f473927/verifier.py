from arc2.core import *


def verify_6f473927(I: Grid) -> Grid:
    x0 = vmirror(I)
    x1 = replace(x0, ZERO, EIGHT)
    x2 = replace(x1, TWO, ZERO)
    x3 = height(I)
    x4 = decrement(x3)
    x5 = width(I)
    x6 = decrement(x5)
    x7 = astuple(x4, ZERO)
    x8 = connect(ORIGIN, x7)
    x9 = ofcolor(I, TWO)
    x10 = intersection(x8, x9)
    x11 = size(x10)
    x12 = tojvec(x6)
    x13 = astuple(x4, x6)
    x14 = connect(x12, x13)
    x15 = intersection(x14, x9)
    x16 = size(x15)
    x17 = greater(x11, x16)
    x18 = hconcat(x2, I)
    x19 = hconcat(I, x2)
    x20 = branch(x17, x18, x19)
    return x20
