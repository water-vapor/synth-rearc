from arc2.core import *


def verify_522fdd07(I: Grid) -> Grid:
    x0 = objects(I, T, F, T)
    x1 = canvas(SEVEN, shape(I))
    for x2 in x0:
        x3 = color(x2)
        x4 = size(x2)
        if equality(x4, ONE):
            x5, x6 = center(x2)
            x7 = interval(subtract(x5, FOUR), add(x5, FIVE), ONE)
            x8 = interval(subtract(x6, FOUR), add(x6, FIVE), ONE)
            x9 = product(x7, x8)
        else:
            x9 = difference(backdrop(x2), box(x2))
        x1 = fill(x1, x3, x9)
    return x1
