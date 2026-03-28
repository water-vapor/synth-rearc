from arc2.core import *


def verify_3cd86f4f(I: Grid) -> Grid:
    x0 = height(I)
    x1 = vsplit(I, x0)
    x2 = decrement(x0)
    x3 = interval(x2, NEG_ONE, NEG_ONE)
    x4 = interval(ZERO, x0, ONE)
    x5 = lbind(astuple, ONE)
    x6 = lbind(canvas, ZERO)
    x7 = compose(x6, x5)
    x8 = apply(x7, x3)
    x9 = papply(hconcat, x8, x1)
    x10 = apply(x7, x4)
    x11 = papply(hconcat, x9, x10)
    x12 = merge(x11)
    return x12
