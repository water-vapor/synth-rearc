from __future__ import annotations

from collections import deque

from synth_rearc.core import *


def legend_component_dbff022c(
    grid: Grid,
) -> Object:
    x0 = objects(grid, F, F, T)
    x1 = tuple(
        sorted(
            (
                x2
                for x2 in x0
                if (
                    bordering(x2, grid)
                    and numcolors(x2) > ONE
                    and size(x2) == height(x2) * width(x2)
                    and (height(x2) == TWO or width(x2) == TWO)
                )
            ),
            key=lambda obj: (size(obj), uppermost(obj), leftmost(obj)),
        )
    )
    if len(x1) == ZERO:
        raise ValueError("missing dbff022c legend")
    return x1[ZERO]


def legend_cells_dbff022c(
    grid: Grid,
) -> Indices:
    return toindices(legend_component_dbff022c(grid))


def legend_mapping_dbff022c(
    grid: Grid,
) -> tuple[tuple[Integer, Integer], ...]:
    x0 = legend_component_dbff022c(grid)
    x1 = uppermost(x0)
    x2 = lowermost(x0)
    x3 = leftmost(x0)
    x4 = rightmost(x0)
    x5 = height(x0) == TWO and (x1 == ZERO or x2 == len(grid) - ONE)
    x6 = []
    if x5:
        x7 = x1 if x1 == ZERO else x2
        x8 = x2 if x1 == ZERO else x1
        for x9 in range(x3, x4 + ONE):
            x6.append((grid[x7][x9], grid[x8][x9]))
    else:
        x7 = x3 if x3 == ZERO else x4
        x8 = x4 if x3 == ZERO else x3
        for x9 in range(x1, x2 + ONE):
            x6.append((grid[x9][x7], grid[x9][x8]))
    return tuple(x6)


def hole_regions_dbff022c(
    patch: Patch,
) -> tuple[Indices, ...]:
    x0 = toindices(patch)
    if len(x0) == ZERO:
        return tuple()
    x1 = backdrop(x0) - x0
    x2 = set(x1)
    x3 = []
    while len(x2) > ZERO:
        x4 = x2.pop()
        x5 = deque([x4])
        x6 = {x4}
        x7 = False
        while len(x5) > ZERO:
            x8 = x5.popleft()
            i, j = x8
            if i in (uppermost(x0), lowermost(x0)) or j in (leftmost(x0), rightmost(x0)):
                x7 = True
            for x9 in dneighbors(x8):
                if x9 in x2:
                    x2.remove(x9)
                    x6.add(x9)
                    x5.append(x9)
        if not x7:
            x3.append(frozenset(x6))
    return tuple(sorted(x3, key=lambda region: (size(region), uppermost(region), leftmost(region))))


def hole_indices_dbff022c(
    patch: Patch,
) -> Indices:
    x0 = hole_regions_dbff022c(patch)
    return merge(x0) if len(x0) > ZERO else frozenset()


def connected_dbff022c(
    patch: Patch,
) -> Boolean:
    x0 = toindices(patch)
    if len(x0) == ZERO:
        return F
    x1 = next(iter(x0))
    x2 = deque([x1])
    x3 = {x1}
    while len(x2) > ZERO:
        x4 = x2.popleft()
        for x5 in dneighbors(x4):
            if x5 in x0 and x5 not in x3:
                x3.add(x5)
                x2.append(x5)
    return len(x3) == len(x0)
