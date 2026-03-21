from arc2.core import *


def verify_a934301b(I: Grid) -> Grid:
    x0 = objects(I, F, F, T)
    x1 = rbind(colorcount, EIGHT)
    x2 = rbind(greater, ONE)
    x3 = compose(x2, x1)
    x4 = mfilter(x0, x3)
    x5 = cover(I, x4)
    return x5
