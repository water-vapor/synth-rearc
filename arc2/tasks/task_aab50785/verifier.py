from arc2.core import *


def verify_aab50785(I: Grid) -> Grid:
    x0 = astuple(TWO, TWO)
    x1 = canvas(EIGHT, x0)
    x2 = asobject(x1)
    x3 = occurrences(I, x2)
    x4 = order({x5[0] for x5 in x3}, identity)
    x5 = ()
    for x6 in x4:
        x7 = order(tuple(x8[1] for x8 in x3 if x8[0] == x6), identity)
        if greater(size(x7), ONE):
            x8 = first(x7)
            x9 = last(x7)
            x10 = add(x8, TWO)
            x11 = subtract(x9, x10)
            x12 = astuple(x6, x10)
            x13 = astuple(TWO, x11)
            x14 = crop(I, x12, x13)
            x5 = vconcat(x5, x14)
    return x5
