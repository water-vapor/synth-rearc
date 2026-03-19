from arc2.core import *


def verify_17829a00(I: Grid) -> Grid:
    x0 = height(I)
    x1 = width(I)
    x2 = mostcolor(I)
    x3 = index(I, ORIGIN)
    x4 = index(I, (subtract(x0, ONE), ZERO))
    x5 = canvas(x2, (x0, x1))
    x6 = fill(x5, x3, hfrontier(ORIGIN))
    x7 = fill(x6, x4, hfrontier((subtract(x0, ONE), ZERO)))
    x8 = objects(I, T, T, T)
    x9 = x7
    for x10 in x8:
        x11 = color(x10)
        x12 = uppermost(x10)
        x13 = lowermost(x10)
        if both(equality(x11, x3), positive(x12)):
            x14 = shift(x10, (subtract(ONE, x12), ZERO))
            x9 = paint(x9, x14)
        elif both(equality(x11, x4), greater(subtract(x0, ONE), x13)):
            x15 = subtract(subtract(x0, TWO), x13)
            x16 = shift(x10, (x15, ZERO))
            x9 = paint(x9, x16)
            x17 = both(vline(x10), equality(rightmost(x10), subtract(x1, ONE)))
            x18 = greater(height(x10), TWO)
            if both(x17, x18):
                x19 = connect(
                    (uppermost(x10), subtract(x1, ONE)),
                    (subtract(x0, TWO), subtract(x1, ONE)),
                )
                x9 = fill(x9, x4, x19)
    return x9
