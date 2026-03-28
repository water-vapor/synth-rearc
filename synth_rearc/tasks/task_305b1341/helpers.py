from __future__ import annotations

from synth_rearc.core import *


Pair305b1341 = tuple[int, int]


def legend_pairs_305b1341(
    grid: Grid,
) -> tuple[Pair305b1341, ...]:
    x0 = []
    for x1 in range(height(grid)):
        x2 = index(grid, (x1, ZERO))
        x3 = index(grid, (x1, ONE))
        if x2 == ZERO or x3 == ZERO:
            break
        x0.append((x2, x3))
    return tuple(x0)


def marker_patch_305b1341(
    grid: Grid,
    color_value: Integer,
    legend_height: Integer,
) -> Indices:
    return frozenset(
        x0
        for x0 in ofcolor(grid, color_value)
        if not (x0[ZERO] < legend_height and x0[ONE] < TWO)
    )


def region_patches_305b1341(
    marker_patch: Indices,
    dims: tuple[int, int],
) -> tuple[Indices, Indices]:
    if len(marker_patch) == ZERO:
        return frozenset(), frozenset()
    x0, x1 = dims
    x2 = uppermost(marker_patch)
    x3 = lowermost(marker_patch)
    x4 = leftmost(marker_patch)
    x5 = rightmost(marker_patch)
    x6 = range(max(ZERO, x2 - ONE), min(x0, x3 + TWO))
    x7 = range(max(ZERO, x4 - ONE), min(x1, x5 + TWO))
    x8 = frozenset((x9, x10) for x9 in x6 for x10 in x7)
    x11 = frozenset(
        (x9, x10)
        for x9 in x6
        for x10 in x7
        if x9 % TWO == x2 % TWO and x10 % TWO == x4 % TWO
    )
    return x8, x11


def paint_region_305b1341(
    grid: Grid,
    marker_patch: Indices,
    color_value: Integer,
    fill_value: Integer,
) -> Grid:
    x0, x1 = region_patches_305b1341(marker_patch, shape(grid))
    x2 = fill(grid, fill_value, x0)
    x3 = fill(x2, color_value, x1)
    return x3
