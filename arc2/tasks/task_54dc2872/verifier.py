from arc2.core import *


def verify_54dc2872(I: Grid) -> Grid:
    x0 = objects(I, F, F, T)
    x1 = matcher(numcolors, ONE)
    x2 = sfilter(x0, x1)
    x3 = sizefilter(x2, ONE)
    x4 = compose(flip, x1)
    x5 = sfilter(x0, x4)
    x6 = canvas(ZERO, shape(I))
    x7 = frozenset()
    x8 = x6
    for x9 in x5:
        x10 = leastcolor(x9)
        x11 = colorfilter(x3, x10)
        if size(x11) == ZERO:
            x8 = paint(x8, x9)
            continue
        x12 = first(x11)
        x7 = insert(x12, x7)
        x13 = ulcorner(x12)
        x14 = difference(corners(x9), toindices(x9))
        x15 = first(x14)
        x16 = add(ulcorner(x9), lrcorner(x9))
        x17 = subtract(x16, x15)
        x18 = subtract(x13, x17)
        x19 = shift(x9, x18)
        x8 = paint(x8, x19)
    x20 = difference(x3, x7)
    x21 = merge(x20)
    x22 = paint(x8, x21)
    return x22
