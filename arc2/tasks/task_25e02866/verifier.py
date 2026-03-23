from arc2.core import *


def verify_25e02866(I: Grid) -> Grid:
    x0 = objects(I, F, F, T)
    x1 = first(x0)
    x2 = mostcolor(x1)
    x3 = shape(x1)
    x4 = canvas(x2, x3)
    x5 = compose(flip, matcher(first, x2))
    x6 = frozenset()
    for x7 in x0:
        x8 = normalize(x7)
        x9 = sfilter(x8, x5)
        x6 = combine(x6, x9)
    x10 = paint(x4, x6)
    return x10
