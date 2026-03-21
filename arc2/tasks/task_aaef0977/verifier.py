from arc2.core import *


CYCLE_AAEF0977 = (THREE, FOUR, ZERO, FIVE, TWO, EIGHT, NINE, SIX, ONE)


def verify_aaef0977(I: Grid) -> Grid:
    x0 = first(fgpartition(I))
    x1 = ulcorner(x0)
    x2 = color(x0)
    x3 = CYCLE_AAEF0977.index(x2)
    x4 = frozenset(
        (CYCLE_AAEF0977[(x3 + manhattan(initset(x1), initset(x5))) % len(CYCLE_AAEF0977)], x5)
        for x5 in asindices(I)
    )
    x5 = canvas(ZERO, shape(I))
    x6 = paint(x5, x4)
    return x6
