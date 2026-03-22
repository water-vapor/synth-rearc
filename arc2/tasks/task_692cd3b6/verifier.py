from arc2.core import *

from .helpers import (
    connector_directions_692cd3b6,
    frame_records_692cd3b6,
    monotone_reach_692cd3b6,
    sign_692cd3b6,
)


def verify_692cd3b6(I: Grid) -> Grid:
    x0 = frame_records_692cd3b6(I)
    x1 = first(x0)
    x2 = last(x0)
    x3 = last(x1)
    x4 = last(x2)
    x5 = subtract(x4, x3)
    x6 = sign_692cd3b6(x5[0])
    x7 = sign_692cd3b6(x5[1])
    x8 = tuple(x9 for x9 in ((x6, ZERO), (ZERO, x7)) if x9 != ORIGIN)
    x9 = tuple(invert(x10) for x10 in x8)
    x10 = monotone_reach_692cd3b6(I, (x3,), x8)
    x11 = monotone_reach_692cd3b6(I, (x4,), x9)
    x12 = intersection(x10, x11)
    x13 = connector_directions_692cd3b6(x1, x4)
    x14 = monotone_reach_692cd3b6(I, (x1[1],), x13)
    x15 = monotone_reach_692cd3b6(I, insert(x3, x12), tuple(invert(x16) for x16 in x13))
    x16 = intersection(x14, x15)
    x17 = connector_directions_692cd3b6(x2, x3)
    x18 = monotone_reach_692cd3b6(I, (x2[1],), x17)
    x19 = monotone_reach_692cd3b6(I, insert(x4, x12), tuple(invert(x20) for x20 in x17))
    x20 = intersection(x18, x19)
    x21 = combine(x12, x16)
    x22 = combine(x21, x20)
    x23 = fill(I, FOUR, x22)
    return x23
