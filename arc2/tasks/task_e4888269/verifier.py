from arc2.core import *


def verify_e4888269(I: Grid) -> Grid:
    x0 = mostcolor(I)
    x1 = difference(asindices(I), ofcolor(I, x0))
    x2 = fill(canvas(ZERO, shape(I)), ONE, x1)
    x3 = objects(x2, T, F, T)
    x4 = frozenset()
    for x5 in x3:
        x6 = height(x5)
        x7 = width(x5)
        x8 = toobject(x5, I)
        x9 = astuple(x6, x7)
        if (
            size(x5) == multiply(x6, x7)
            and contained(TWO, x9)
            and greater(size(x5), FOUR)
            and greater(size(palette(x8)), ONE)
        ):
            x4 = insert(x5, x4)
    x10 = argmax(x4, size)
    x11 = argmax(remove(x10, x3), size)
    x12 = subgrid(x10, I)
    x13 = tuple()
    if width(x10) == TWO:
        for x14 in x12:
            x13 = x13 + ((x14[ZERO], x14[ONE]),)
    else:
        for x14 in range(width(x12)):
            x13 = x13 + (((x12[ZERO][x14], x12[ONE][x14]),))
    x14 = toobject(x10, I)
    x15 = toobject(x11, I)
    x16 = I
    for x17, x18 in x13:
        x16 = replace(x16, x17, x18)
        x16 = paint(x16, x15)
        x16 = paint(x16, x14)
    return x16
