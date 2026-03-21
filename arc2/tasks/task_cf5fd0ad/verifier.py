from arc2.core import *


def verify_cf5fd0ad(I: Grid) -> Grid:
    x0 = hconcat(I, I)
    x1 = vconcat(x0, x0)
    x2 = rot90(I)
    x3 = hconcat(x2, x2)
    x4 = vconcat(x3, x3)
    x5 = rot180(I)
    x6 = hconcat(x5, x5)
    x7 = vconcat(x6, x6)
    x8 = rot270(I)
    x9 = hconcat(x8, x8)
    x10 = vconcat(x9, x9)
    x11 = hconcat(x7, x4)
    x12 = hconcat(x10, x1)
    x13 = vconcat(x11, x12)
    return x13
