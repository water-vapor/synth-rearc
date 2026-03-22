from arc2.core import *


def verify_7d1f7ee8(I: Grid) -> Grid:
    x0 = objects(I, T, F, T)
    x1 = merge(x0)
    x2 = toindices(x1)
    x3 = lambda x: size(sfilter(x0, lambda y: backdrop(x) < backdrop(y))) == ZERO
    x4 = sfilter(x0, x3)
    x5 = lambda x: recolor(color(x), intersection(backdrop(x), x2))
    x6 = mapply(x5, x4)
    x7 = paint(I, x6)
    return x7
