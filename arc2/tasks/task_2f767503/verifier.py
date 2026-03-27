from arc2.core import *


def verify_2f767503(I: Grid) -> Grid:
    x0 = ofcolor(I, FIVE)
    x1 = center(x0)
    x2 = ofcolor(I, NINE)
    x3 = position(x2, x0)
    x4 = shoot(x1, x3)
    x5 = objects(I, T, F, T)
    x6 = colorfilter(x5, FOUR)
    x7 = I
    for x8 in x6:
        x9 = intersection(x4, toindices(x8))
        if size(x9) != ZERO:
            x7 = fill(x7, SEVEN, x8)
    return x7
