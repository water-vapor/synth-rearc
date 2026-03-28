from arc2.core import *


def verify_342ae2ed(I: Grid) -> Grid:
    x0 = objects(I, T, F, T)
    x1 = palette(I)
    x2 = mostcolor(I)
    x3 = remove(x2, x1)
    x4 = order(x3, identity)
    x5 = I
    x6 = fork(connect, first, last)
    x7 = matcher(size, ZERO)
    x8 = compose(flip, x7)
    for x9 in x4:
        x10 = colorfilter(x0, x9)
        x11 = order(x10, ulcorner)
        x12 = first(x11)
        x13 = last(x11)
        x14 = corners(x12)
        x15 = corners(x13)
        x16 = product(x14, x15)
        x17 = apply(x6, x16)
        x18 = sfilter(x17, x8)
        x19 = combine(toindices(x12), toindices(x13))
        x20 = rbind(difference, x19)
        x21 = compose(size, x20)
        x22 = argmin(x18, x21)
        x5 = fill(x5, x9, x22)
    return x5
