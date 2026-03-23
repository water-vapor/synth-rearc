from arc2.core import *


def verify_2601afb7(I: Grid) -> Grid:
    x0 = objects(I, T, F, T)
    x1 = order(x0, leftmost)
    x2 = apply(leftmost, x1)
    x3 = apply(uppermost, x1)
    x4 = apply(color, x1)
    x5 = x3[ONE:] + x3[:ONE]
    x6 = x4[-ONE:] + x4[:-ONE]
    x7 = decrement(height(I))
    x8 = repeat(x7, size(x2))
    x9 = pair(x5, x2)
    x10 = pair(x8, x2)
    x11 = papply(connect, x9, x10)
    x12 = mpapply(recolor, x6, x11)
    x13 = canvas(mostcolor(I), shape(I))
    x14 = paint(x13, x12)
    return x14
