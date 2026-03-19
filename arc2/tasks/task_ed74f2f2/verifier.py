from arc2.core import *


def verify_ed74f2f2(I: Grid) -> Grid:
    x0 = objects(I, T, T, T)
    x1 = order(x0, leftmost)
    x2 = first(x1)
    x3 = last(x1)
    x4 = subgrid(x2, I)
    x5 = subgrid(x3, I)
    x6 = index(x4, ORIGIN)
    x7 = index(x4, ZERO_BY_TWO)
    x8 = equality(x6, FIVE)
    x9 = equality(x7, FIVE)
    x10 = branch(x8, branch(x9, ONE, TWO), THREE)
    x11 = replace(x5, FIVE, x10)
    return x11
