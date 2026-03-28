from collections import deque

from synth_rearc.core import *


def rectangle_region_4b6b68e5(
    top: Integer,
    left: Integer,
    height_value: Integer,
    width_value: Integer,
) -> Indices:
    return backdrop(
        frozenset(
            {
                (top, left),
                (top + height_value - ONE, left + width_value - ONE),
            }
        )
    )


def boundary_cells_4b6b68e5(
    patch: Patch,
) -> Indices:
    x0 = toindices(patch)
    return frozenset(
        x1
        for x1 in x0
        if any(x2 not in x0 for x2 in dneighbors(x1))
    )


def enclosed_cells_4b6b68e5(
    patch: Patch,
) -> Indices:
    x0 = toindices(patch)
    if len(x0) == ZERO:
        return frozenset()
    x1 = uppermost(x0)
    x2 = leftmost(x0)
    x3 = lowermost(x0)
    x4 = rightmost(x0)
    x5 = {
        (x6, x7)
        for x6 in range(x1, x3 + ONE)
        for x7 in range(x2, x4 + ONE)
    }
    x8 = x5 - set(x0)
    x9 = deque(
        x10
        for x10 in x8
        if x10[0] in (x1, x3) or x10[1] in (x2, x4)
    )
    x11 = set(x9)
    while len(x9) > ZERO:
        x12 = x9.popleft()
        for x13 in dneighbors(x12):
            if x13 in x8 and x13 not in x11:
                x11.add(x13)
                x9.append(x13)
    return frozenset(x8 - x11)
