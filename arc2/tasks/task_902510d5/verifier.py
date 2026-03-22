from arc2.core import *

from .helpers import (
    corner_cells_902510d5,
    corner_name_from_cell_902510d5,
    triangle_patch_902510d5,
)


def verify_902510d5(
    I: Grid,
) -> Grid:
    x0 = objects(I, T, T, T)
    x1 = argmax(x0, size)
    x2 = remove(x1, x0)
    x3 = sfilter(x2, matcher(size, ONE))
    x4 = corner_cells_902510d5(shape(I))
    x5 = extract(x3, lambda x: contained(first(toindices(x)), x4))
    x6 = first(toindices(x5))
    x7 = corner_name_from_cell_902510d5(x6, shape(I))
    x8 = remove(x5, x3)
    x9 = tuple(color(x10) for x10 in x8)
    x10 = mostcommon(x9)
    x11 = size(x8)
    x12 = triangle_patch_902510d5(x7, x11, shape(I))
    x13 = cover(I, merge(x2))
    x14 = fill(x13, x10, x12)
    return x14
