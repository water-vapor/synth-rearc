from arc2.core import *

from .helpers import compose_tiles_6350f1f4, split_tiles_6350f1f4


def verify_6350f1f4(I: Grid) -> Grid:
    x0 = split_tiles_6350f1f4(I)
    x1 = tuple(x2 for x3 in x0 for x2 in x3)
    x2 = next(x3 for x3 in x1 if ZERO not in palette(x3) and numcolors(x3) == TWO)
    x3 = mostcolor(x2)
    x4 = canvas(x3, shape(x2))
    x5 = tuple(
        tuple(x4 if contained(x3, palette(x6)) else x2 for x6 in x7)
        for x7 in x0
    )
    x6 = compose_tiles_6350f1f4(x5)
    return x6
