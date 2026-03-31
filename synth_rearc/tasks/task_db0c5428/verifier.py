from synth_rearc.core import *


def verify_db0c5428(I: Grid) -> Grid:
    x0 = objects(I, F, F, T)
    x1 = argmax(x0, size)
    x2 = ulcorner(x1)
    x3 = subgrid(x1, I)
    x4 = mostcolor(I)
    x5 = mostcolor(x3)
    x6 = vsplit(x3, THREE)
    x7 = tuple(hsplit(x8, THREE) for x8 in x6)
    x8 = x7[ZERO][ZERO]
    x9 = x7[ZERO][ONE]
    x10 = x7[ZERO][TWO]
    x11 = x7[ONE][ZERO]
    x12 = x7[ONE][TWO]
    x13 = x7[TWO][ZERO]
    x14 = x7[TWO][ONE]
    x15 = x7[TWO][TWO]
    x16 = (
        (x8[TWO][TWO], x9[TWO][ONE], x10[TWO][ZERO]),
        (x11[ONE][TWO], x5, x12[ONE][ZERO]),
        (x13[ZERO][TWO], x14[ZERO][ONE], x15[ZERO][ZERO]),
    )
    x17 = canvas(x4, shape(x8))
    x18 = hconcat(hconcat(hconcat(hconcat(x15, x17), x14), x17), x13)
    x19 = hconcat(hconcat(hconcat(hconcat(x17, x8), x9), x10), x17)
    x20 = hconcat(hconcat(hconcat(hconcat(x12, x11), x16), x12), x11)
    x21 = hconcat(hconcat(hconcat(hconcat(x17, x13), x14), x15), x17)
    x22 = hconcat(hconcat(hconcat(hconcat(x10, x17), x9), x17), x8)
    x23 = vconcat(vconcat(x18, x19), vconcat(vconcat(x20, x21), x22))
    x24 = shift(asobject(x23), subtract(x2, shape(x8)))
    x25 = paint(I, x24)
    return x25
