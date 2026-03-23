from arc2.core import *


def verify_2b9ef948(I: Grid) -> Grid:
    x0 = objects(I, F, F, T)
    x1 = sizefilter(x0, NINE)
    x2 = extract(x1, square)
    x3 = other(x0, x2)
    x4 = leastcolor(x2)
    x5 = center(x2)
    x6 = extract(x3, matcher(first, x4))
    x7 = last(x6)
    x8 = extract(x3, matcher(first, FOUR))
    x9 = last(x8)
    x10 = subtract(x9, x7)
    x11 = add(x5, x10)
    x12 = shoot(x11, UNITY)
    x13 = shoot(x11, NEG_UNITY)
    x14 = combine(x12, x13)
    x15 = shoot(x11, UP_RIGHT)
    x16 = shoot(x11, DOWN_LEFT)
    x17 = combine(x14, x15)
    x18 = combine(x17, x16)
    x19 = shift(box(frozenset({ORIGIN, TWO_BY_TWO})), subtract(x11, UNITY))
    x20 = combine(x18, x19)
    x21 = difference(x20, initset(x11))
    x22 = canvas(x4, shape(I))
    x23 = fill(x22, FOUR, x21)
    return x23
