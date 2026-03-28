from arc2.core import *


def verify_4df5b0ae(I: Grid) -> Grid:
    x0 = shape(I)
    x1 = mostcolor(I)
    x2 = decrement(x0)
    x3 = matcher(ulcorner, ORIGIN)
    x4 = matcher(lrcorner, x2)
    x5 = fork(both, x3, x4)
    x6 = compose(flip, x5)
    x7 = objects(I, T, F, T)
    x8 = sfilter(x7, x6)
    x9 = order(x8, lambda x: (size(x), uppermost(x), leftmost(x), color(x)))
    x10 = canvas(x1, x0)
    x11 = ZERO
    for x12 in x9:
        x13 = normalize(x12)
        x14 = astuple(subtract(first(x0), height(x13)), x11)
        x15 = shift(x13, x14)
        x10 = paint(x10, x15)
        x11 = add(x11, width(x13))
    return x10
