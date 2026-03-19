from arc2.core import *


def verify_15660dd6(I: Grid) -> Grid:
    x0 = height(I)
    x1 = subtract(x0, FOUR)
    x2 = divide(x1, THREE)
    x3 = width(I)
    x4 = increment(x2)
    x5 = subtract(x3, ONE)
    x6 = divide(x5, x4)
    x7 = []
    x8 = []
    for x9 in range(THREE):
        x10 = add(ONE, multiply(x9, x4))
        x11 = crop(I, (x10, ZERO), (x2, x3))
        x12 = index(x11, ORIGIN)
        x13 = tuple(crop(x11, (ZERO, add(ONE, multiply(x14, x4))), (x2, x2)) for x14 in range(x6))
        x7.append(x12)
        x8.append(x13)
    x15 = []
    for x16 in range(x6):
        x17 = tuple(x8[x18][x16] for x18 in range(THREE))
        x19 = tuple(x17.count(x20) for x20 in x17)
        x21 = x19.index(ONE)
        x22 = x19.index(TWO)
        x23 = x17[x22]
        x24 = tuple(value for value in palette(x17[x21]) if value not in (ONE, EIGHT))
        x25 = x24[ZERO]
        x26 = replace(x23, ONE, x7[x21])
        x27 = replace(x26, TWO, x25)
        x15.append(x27)
    x28 = x15[ZERO]
    x29 = canvas(EIGHT, (x2, ONE))
    for x30 in x15[ONE:]:
        x28 = hconcat(hconcat(x28, x29), x30)
    return x28
