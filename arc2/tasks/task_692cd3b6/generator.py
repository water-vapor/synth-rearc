from arc2.core import *

from .helpers import (
    DIHEDRAL_TRANSFORMS_692cd3b6,
    connector_directions_692cd3b6,
    frame_cells_692cd3b6,
    monotone_reach_692cd3b6,
    sign_692cd3b6,
)


FrameRecord692cd3b6 = tuple[IntegerTuple, IntegerTuple, IntegerTuple]


def _frame_record_692cd3b6(
    center: IntegerTuple,
    direction: IntegerTuple,
) -> FrameRecord692cd3b6:
    x0 = add(center, direction)
    x1 = add(x0, direction)
    return (center, x0, x1)


def _bridge_patch_692cd3b6(
    I: Grid,
    a: FrameRecord692cd3b6,
    b: FrameRecord692cd3b6,
) -> Indices:
    x0 = a[2]
    x1 = b[2]
    x2 = subtract(x1, x0)
    x3 = sign_692cd3b6(x2[0])
    x4 = sign_692cd3b6(x2[1])
    x5 = tuple(x6 for x6 in ((x3, ZERO), (ZERO, x4)) if x6 != ORIGIN)
    x6 = tuple(invert(x7) for x7 in x5)
    x7 = monotone_reach_692cd3b6(I, (x0,), x5)
    x8 = monotone_reach_692cd3b6(I, (x1,), x6)
    x9 = intersection(x7, x8)
    x10 = connector_directions_692cd3b6(a, x1)
    x11 = monotone_reach_692cd3b6(I, (a[1],), x10)
    x12 = monotone_reach_692cd3b6(I, insert(x0, x9), tuple(invert(x13) for x13 in x10))
    x13 = intersection(x11, x12)
    x14 = connector_directions_692cd3b6(b, x0)
    x15 = monotone_reach_692cd3b6(I, (b[1],), x14)
    x16 = monotone_reach_692cd3b6(I, insert(x1, x9), tuple(invert(x17) for x17 in x14))
    x17 = intersection(x15, x16)
    return combine(combine(x9, x13), x17)


def generate_692cd3b6(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = randint(ZERO, FOUR)
        x1 = randint(TWO, SIX)
        x2 = randint(x0 + SIX, 13)
        x3 = randint(x1 + SIX, 14)
        x4 = _frame_record_692cd3b6((x0 + TWO, x1), UP)
        x5 = _frame_record_692cd3b6((x2, x3 - TWO), RIGHT)
        x6 = canvas(ZERO, (15, 15))
        x6 = paint(x6, frame_cells_692cd3b6(x4[0], UP))
        x6 = paint(x6, frame_cells_692cd3b6(x5[0], RIGHT))
        x7 = _bridge_patch_692cd3b6(x6, x4, x5)
        x8 = fill(x6, FOUR, x7)
        x9 = choice(DIHEDRAL_TRANSFORMS_692cd3b6)
        x10 = x9(x6)
        x11 = x9(x8)
        return {"input": x10, "output": x11}
