from arc2.core import *


def verify_2037f2c7(I: Grid) -> Grid:
    x0 = objects(I, F, F, T)
    x1 = totuple(x0)
    x2 = first(x1)
    x3 = last(x1)
    x4 = normalize(x2)
    x5 = normalize(x3)
    x6 = toindices(x4)
    x7 = toindices(x5)
    x8 = difference(x6, x7)
    x9 = difference(x7, x6)
    x10 = combine(x8, x9)
    x11 = combine(x6, x7)
    x12 = shape(x11)
    x13 = canvas(ZERO, x12)
    x14 = fill(x13, EIGHT, x10)
    x15 = subgrid(x10, x14)
    return x15
