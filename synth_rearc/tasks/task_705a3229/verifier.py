from synth_rearc.core import *


def verify_705a3229(I: Grid) -> Grid:
    x0 = objects(I, T, F, T)
    x1 = order(x0, ulcorner)
    x2 = height(I)
    x3 = width(I)
    x4 = decrement(x2)
    x5 = decrement(x3)
    x6 = I
    for x7 in x1:
        x8 = color(x7)
        x9 = ulcorner(x7)
        x10 = first(x9)
        x11 = last(x9)
        x12 = subtract(x4, x10)
        x13 = subtract(x5, x11)
        x14 = greater(x10, x12)
        x15 = branch(x14, DOWN, UP)
        x16 = shoot(x9, x15)
        x17 = greater(x11, x13)
        x18 = branch(x17, RIGHT, LEFT)
        x19 = shoot(x9, x18)
        x20 = combine(x16, x19)
        x6 = fill(x6, x8, x20)
    return x6
