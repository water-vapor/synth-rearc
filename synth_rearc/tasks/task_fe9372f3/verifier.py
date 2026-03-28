from synth_rearc.core import *


def verify_fe9372f3(I: Grid) -> Grid:
    x0 = ofcolor(I, TWO)
    x1 = centerofmass(x0)
    x2 = shoot(x1, UNITY)
    x3 = shoot(x1, NEG_UNITY)
    x4 = shoot(x1, UP_RIGHT)
    x5 = shoot(x1, DOWN_LEFT)
    x6 = combine(x2, x3)
    x7 = combine(x4, x5)
    x8 = combine(x6, x7)
    x9 = underfill(I, ONE, x8)
    x10 = hfrontier(x1)
    x11 = vfrontier(x1)
    x12 = combine(x10, x11)
    x13 = underfill(x9, EIGHT, x12)
    x14 = interval(FOUR, 30, THREE)
    x15 = (UP, DOWN, LEFT, RIGHT)
    x16 = frozenset(add(x1, multiply(x17, x18)) for x17 in x14 for x18 in x15)
    x19 = fill(x13, FOUR, x16)
    return x19
