from arc2.core import *


def verify_ed98d772(I: Grid) -> Grid:
    x0 = rot270(I)
    x1 = hconcat(I, x0)
    x2 = rot180(I)
    x3 = rot90(I)
    x4 = hconcat(x2, x3)
    x5 = vconcat(x1, x4)
    return x5
