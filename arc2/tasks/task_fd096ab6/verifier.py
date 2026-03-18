from arc2.core import *

from .helpers import completed_partition_fd096ab6


def verify_fd096ab6(I: Grid) -> Grid:
    x0 = shape(I)
    x1 = objects(I, T, T, T)
    x2 = argmax(x1, size)
    x3 = color(x2)
    x4 = toindices(x2)
    x5 = normalize(x4)
    x6 = fgpartition(I)
    x7 = merge(x6)
    x8 = toindices(x7)
    x9 = I
    for x10 in x6:
        x11 = color(x10)
        if equality(x11, x3):
            continue
        x12 = toindices(x10)
        x13 = difference(x8, x12)
        x14 = completed_partition_fd096ab6(x5, x12, x11, x0, x13)
        x9 = paint(x9, x14)
    return x9
