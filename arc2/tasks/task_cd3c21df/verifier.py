from arc2.core import *


def verify_cd3c21df(I: Grid) -> Grid:
    x0 = objects(I, F, F, T)
    x1 = totuple(x0)
    x2 = apply(normalize, x1)
    x3 = leastcommon(x2)
    x4 = mostcolor(I)
    x5 = shape(x3)
    x6 = canvas(x4, x5)
    x7 = paint(x6, x3)
    return x7
