from arc2.core import *


def verify_8abad3cf(I: Grid) -> Grid:
    x0 = palette(I)
    x1 = remove(SEVEN, x0)
    x2 = totuple(x1)
    x3 = lbind(colorcount, I)
    x4 = order(x2, x3)
    x5 = last(x4)
    x6 = colorcount(I, x5)
    x7 = int(x6 ** 0.5)
    x8 = x4[-2]
    x9 = colorcount(I, x8)
    x10 = int(x9 ** 0.5)
    x11 = greater(size(x4), TWO)
    x12 = canvas(x5, (x7, x7))
    x13 = branch(x11, THREE, ONE)
    x14 = add(x10, x13)
    x15 = canvas(SEVEN, (x7, x14))
    x16 = subtract(x7, x10)
    x17 = branch(x11, TWO, ZERO)
    x18 = interval(x16, x7, ONE)
    x19 = interval(x17, add(x17, x10), ONE)
    x20 = product(x18, x19)
    x21 = fill(x15, x8, x20)
    x22 = x4[-3] if x11 else SEVEN
    x23 = branch(x11, frozenset({(subtract(x7, ONE), ZERO)}), frozenset())
    x24 = fill(x21, x22, x23)
    x25 = hconcat(x24, x12)
    return x25
