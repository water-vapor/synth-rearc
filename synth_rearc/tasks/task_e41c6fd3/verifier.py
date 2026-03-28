from synth_rearc.core import *


def verify_e41c6fd3(I: Grid) -> Grid:
    x0 = objects(I, T, F, T)
    x1 = matcher(color, EIGHT)
    x2 = extract(x0, x1)
    x3 = uppermost(x2)
    x4 = canvas(ZERO, shape(I))
    for x5 in x0:
        x6 = uppermost(x5)
        x7 = subtract(x3, x6)
        x8 = shift(x5, toivec(x7))
        x4 = paint(x4, x8)
    return x4
