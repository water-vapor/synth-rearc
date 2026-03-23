from arc2.core import *


def verify_2072aba6(I: Grid) -> Grid:
    x0 = upscale(I, TWO)
    x1 = replace(x0, FIVE, ONE)
    x2 = ofcolor(x0, FIVE)
    x3 = fork(add, first, last)
    x4 = compose(flip, even)
    x5 = compose(x4, x3)
    x6 = sfilter(x2, x5)
    x7 = fill(x1, TWO, x6)
    return x7
