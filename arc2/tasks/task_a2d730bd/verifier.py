from arc2.core import *


def verify_a2d730bd(I: Grid) -> Grid:
    x0 = mostcolor(I)
    x1 = objects(I, T, F, T)
    x2 = remove(x0, palette(I))
    x3 = I
    for x4 in x2:
        x5 = colorfilter(x1, x4)
        x6 = argmax(x5, size)
        x7 = difference(x5, initset(x6))
        x8 = sizefilter(x7, ONE)
        x9 = uppermost(x6)
        x10 = lowermost(x6)
        x11 = leftmost(x6)
        x12 = rightmost(x6)
        for x13 in x8:
            x14 = ulcorner(x13)
            if x9 <= x14[0] <= x10:
                x15 = branch(
                    greater(x11, x14[1]),
                    astuple(x14[0], decrement(x11)),
                    astuple(x14[0], increment(x12)),
                )
            else:
                x15 = branch(
                    greater(x9, x14[0]),
                    astuple(decrement(x9), x14[1]),
                    astuple(increment(x10), x14[1]),
                )
            x16 = connect(x14, x15)
            x17 = combine(x16, dneighbors(x14))
            x18 = combine(x17, dneighbors(x15))
            x19 = remove(x14, x18)
            x3 = fill(x3, x0, x13)
            x3 = fill(x3, x4, x19)
    return x3
