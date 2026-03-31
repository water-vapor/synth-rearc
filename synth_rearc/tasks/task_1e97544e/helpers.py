from __future__ import annotations

from synth_rearc.core import *


GRID_SHAPE_1E97544E = (23, 23)


def build_output_1e97544e(
    start_color: Integer,
    period: Integer,
    dims: IntegerTuple = GRID_SHAPE_1E97544E,
) -> Grid:
    x0, x1 = dims
    x2 = tuple(((start_color - ONE + x3) % period) + ONE for x3 in range(x1))
    x4 = []
    for x5 in range(x0):
        x6 = []
        for x7 in range(x1):
            x8 = x7 if x5 <= x7 else min(x7 + ONE, x1 - ONE)
            x6.append(x2[x8])
        x4.append(tuple(x6))
    return tuple(x4)


def rect_indices_1e97544e(
    loc: IntegerTuple,
    dims: IntegerTuple,
) -> Indices:
    x0, x1 = loc
    x2, x3 = dims
    return frozenset((x4, x5) for x4 in range(x0, x0 + x2) for x5 in range(x1, x1 + x3))
