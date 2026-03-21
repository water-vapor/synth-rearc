from arc2.core import *

from .helpers import base_grid_97239e3d
from .helpers import region_patch_97239e3d


def _marker_region_97239e3d(
    x: Object,
) -> Object:
    x0 = uppermost(x)
    x1 = leftmost(x)
    x2 = lowermost(x)
    x3 = rightmost(x)
    x4 = multiply(divide(x0, FOUR), FOUR)
    x5 = multiply(divide(x1, FOUR), FOUR)
    x6 = multiply(divide(add(x2, THREE), FOUR), FOUR)
    x7 = multiply(divide(add(x3, THREE), FOUR), FOUR)
    x8 = divide(x4, FOUR)
    x9 = decrement(divide(x6, FOUR))
    x10 = divide(x5, FOUR)
    x11 = decrement(divide(x7, FOUR))
    x12 = region_patch_97239e3d(x8, x9, x10, x11)
    x13 = color(x)
    x14 = recolor(x13, x12)
    return x14


def verify_97239e3d(I: Grid) -> Grid:
    x0 = base_grid_97239e3d()
    x1 = replace(I, EIGHT, ZERO)
    x2 = fgpartition(x1)
    x3 = mapply(_marker_region_97239e3d, x2)
    x4 = paint(x0, x3)
    return x4
