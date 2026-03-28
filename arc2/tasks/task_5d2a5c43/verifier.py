from arc2.core import *


def verify_5d2a5c43(I: Grid) -> Grid:
    x0 = lefthalf(I)
    x1 = righthalf(I)
    x2 = cellwise(x0, x1, FOUR)
    x3 = replace(x2, FOUR, EIGHT)
    return x3
