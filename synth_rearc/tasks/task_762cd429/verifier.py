from synth_rearc.core import *


def verify_762cd429(I: Grid) -> Grid:
    x0 = objects(I, F, F, T)
    x1 = first(x0)
    x2 = canvas(ZERO, shape(I))
    x3 = width(I)
    x4 = ZERO
    x5 = ONE
    x6 = x2
    while x4 < x3:
        x7 = upscale(x1, x5)
        x8 = astuple(subtract(ONE, x5), x4)
        x9 = shift(x7, x8)
        x6 = paint(x6, x9)
        x4 = add(x4, width(x7))
        x5 = double(x5)
    return x6
