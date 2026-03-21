from arc2.core import *


def verify_d282b262(I: Grid) -> Grid:
    x0 = objects(I, F, F, T)
    x1 = order(x0, lambda x: (rightmost(x), leftmost(x), uppermost(x), lowermost(x)))
    x2 = width(I)
    x3 = canvas(ZERO, shape(I))
    x4 = ()
    for x5 in x1[::-1]:
        x6 = subtract(subtract(x2, ONE), rightmost(x5))
        x7 = {}
        for _, x8 in x5:
            x9 = x7.get(x8[0], -ONE)
            if x8[1] > x9:
                x7[x8[0]] = x8[1]
        for x10 in x4:
            x11 = {}
            for _, x12 in x10:
                x13 = x11.get(x12[0], x2)
                if x12[1] < x13:
                    x11[x12[0]] = x12[1]
            for x14, x15 in x7.items():
                if x14 in x11:
                    x16 = subtract(subtract(x11[x14], x15), ONE)
                    x6 = minimum((x6, x16))
        x17 = shift(x5, (ZERO, x6))
        x3 = paint(x3, x17)
        x4 = x4 + (x17,)
    return x3
