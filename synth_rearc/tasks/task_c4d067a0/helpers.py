from __future__ import annotations

from synth_rearc.core import *


def block_patch_c4d067a0(
    top: Integer,
    left: Integer,
    side: Integer,
) -> Indices:
    return frozenset(
        (i, j)
        for i in range(top, top + side)
        for j in range(left, left + side)
    )


def paint_macro_c4d067a0(
    grid: Grid,
    matrix: Grid,
    bg: Integer,
    top: Integer,
    left: Integer,
    stride: Integer,
    side: Integer,
) -> Grid:
    x0 = grid
    for x1, x2 in enumerate(matrix):
        for x3, x4 in enumerate(x2):
            if x4 == bg:
                continue
            x5 = top + x1 * stride
            x6 = left + x3 * stride
            x7 = block_patch_c4d067a0(x5, x6, side)
            x0 = fill(x0, x4, x7)
    return x0


def paint_source_c4d067a0(
    grid: Grid,
    matrix: Grid,
    bg: Integer,
    top: Integer = ONE,
    left: Integer = ONE,
    stride: Integer = TWO,
) -> Grid:
    x0 = grid
    for x1, x2 in enumerate(matrix):
        for x3, x4 in enumerate(x2):
            if x4 == bg:
                continue
            x5 = top + x1 * stride
            x6 = left + x3 * stride
            x0 = fill(x0, x4, frozenset({(x5, x6)}))
    return x0
