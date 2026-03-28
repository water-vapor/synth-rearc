from synth_rearc.core import *

from .helpers import packed_rectangles_db615bd4


def verify_db615bd4(I: Grid) -> Grid:
    x0 = mostcolor(I)
    x1 = fgpartition(I)
    x2 = argmax(x1, size)
    x3 = remove(x2, x1)
    x4 = argmax(x3, compose(size, backdrop))
    x5 = remove(x4, x3)
    x6 = order(x5, uppermost if portrait(x4) else leftmost)
    x7 = I
    for x8 in x6:
        x7 = fill(x7, x0, x8)
    x9 = fill(x7, x0, backdrop(x4))
    x10 = fill(x9, color(x4), box(x4))
    x11 = tuple(shape(backdrop(x12)) for x12 in x6)
    x12 = packed_rectangles_db615bd4(x4, x11)
    x13 = apply(color, x6)
    x14 = x10
    for x15, x16 in zip(x13, x12):
        x14 = fill(x14, x15, x16)
    return x14
