from arc2.core import *

from .helpers import align_to_corner_b74ca5d1, corner_map_b74ca5d1, expand_bbox_b74ca5d1


def verify_b74ca5d1(I: Grid) -> Grid:
    x0 = shape(I)
    x1 = corner_map_b74ca5d1(I)
    x2 = fgpartition(I)
    x3 = frozenset(x4 for x4 in x2 if color(x4) not in x1)
    x4 = I
    x5 = frozenset(x1)
    for x6 in x3:
        x7 = expand_bbox_b74ca5d1(x6, ONE, x0)
        x8 = frozenset((index(I, x9), x9) for x9 in x7 if index(I, x9) in x5)
        x9 = first(x8)
        x10 = first(x9)
        x11 = last(x9)
        x12 = color(x6)
        x13 = combine(toindices(x6), initset(x11))
        x14 = align_to_corner_b74ca5d1(x13, x1[x10], x0)
        x4 = fill(x4, x10, x6)
        x4 = fill(x4, x12, initset(x11))
        x4 = fill(x4, x10, x14)
    return x4
