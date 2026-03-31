from __future__ import annotations

from collections import deque

from synth_rearc.core import *


def rectangle_region_aa4ec2a5(
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


def connected_patch_aa4ec2a5(
    patch: Patch,
) -> Boolean:
    x0 = toindices(patch)
    if len(x0) == ZERO:
        return False
    x1 = first(x0)
    x2 = deque((x1,))
    x3 = {x1}
    while len(x2) > ZERO:
        x4 = x2.popleft()
        for x5 in dneighbors(x4):
            if x5 in x0 and x5 not in x3:
                x3.add(x5)
                x2.append(x5)
    return equality(len(x3), len(x0))


def enclosed_cells_aa4ec2a5(
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
    x6 = x5 - set(x0)
    x7 = deque(
        x8
        for x8 in x6
        if x8[ZERO] in (x1, x3) or x8[ONE] in (x2, x4)
    )
    x8 = set(x7)
    while len(x7) > ZERO:
        x9 = x7.popleft()
        for x10 in dneighbors(x9):
            if x10 in x6 and x10 not in x8:
                x8.add(x10)
                x7.append(x10)
    return frozenset(x6 - x8)


def halo8_aa4ec2a5(
    patch: Patch,
    grid_shape: IntegerTuple,
) -> Indices:
    x0 = toindices(patch)
    x1, x2 = grid_shape
    return frozenset(
        x3
        for x4 in x0
        for x3 in neighbors(x4)
        if 0 <= x3[ZERO] < x1 and 0 <= x3[ONE] < x2 and x3 not in x0
    )
