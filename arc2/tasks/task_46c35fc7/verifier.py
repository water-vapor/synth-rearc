from arc2.core import *


def verify_46c35fc7(I: Grid) -> Grid:
    x0 = objects(I, F, F, T)
    x1 = mostcolor(I)
    x2 = shape(I)
    x3 = canvas(x1, x2)
    for x4 in x0:
        x5 = ulcorner(x4)
        x6 = crop(I, x5, (THREE, THREE))
        x7 = x6[ZERO][TWO]
        x8 = x6[ONE][ZERO]
        x9 = x6[TWO][TWO]
        x10 = x6[TWO][ONE]
        x11 = x6[ONE][ONE]
        x12 = x6[ZERO][ONE]
        x13 = x6[ZERO][ZERO]
        x14 = x6[ONE][TWO]
        x15 = x6[TWO][ZERO]
        x16 = (
            (x7, x8, x9),
            (x10, x11, x12),
            (x13, x14, x15),
        )
        x17 = asobject(x16)
        x18 = shift(x17, x5)
        x3 = paint(x3, x18)
    return x3
