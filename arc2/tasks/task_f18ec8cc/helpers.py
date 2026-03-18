from __future__ import annotations

from arc2.core import *


def split_vertical_strips_f18ec8cc(
    grid: Grid,
) -> tuple[tuple[Integer, Grid], ...]:
    x0 = width(grid)
    x1 = tuple(tuple(row[x2] for row in grid) for x2 in range(x0))
    x2 = apply(mostcommon, x1)
    if len(x2) == ZERO:
        return tuple()
    x3 = []
    x4 = ZERO
    for x5 in range(ONE, len(x2) + ONE):
        if x5 < len(x2) and equality(x2[x5], x2[x4]):
            continue
        x6 = tuple(tuple(row[x4:x5]) for row in grid)
        x3.append((x2[x4], x6))
        x4 = x5
    return tuple(x3)


def concat_strips_f18ec8cc(
    strips: tuple[Grid, ...],
) -> Grid:
    x0 = first(strips)
    for x1 in strips[1:]:
        x0 = hconcat(x0, x1)
    return x0
