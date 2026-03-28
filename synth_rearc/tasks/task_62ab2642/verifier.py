from synth_rearc.core import *


def verify_62ab2642(I: Grid) -> Grid:
    x0 = objects(I, T, F, F)
    x1 = colorfilter(x0, ZERO)
    x2 = argmin(x1, size)
    x3 = argmax(x1, size)
    x4 = fill(I, SEVEN, x2)
    x5 = fill(x4, EIGHT, x3)
    return x5
