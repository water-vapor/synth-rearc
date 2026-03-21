from __future__ import annotations

from collections import deque

from arc2.core import *


def passable_cells_b15fca0b(
    I: Grid,
) -> Indices:
    x0, x1 = shape(I)
    return frozenset((x2, x3) for x2 in range(x0) for x3 in range(x1) if I[x2][x3] != ONE)


def bfs_distances_b15fca0b(
    passable: Indices,
    dims: IntegerTuple,
    start: IntegerTuple,
) -> dict[IntegerTuple, Integer]:
    x0, x1 = dims
    x2 = deque((start,))
    x3 = {start: ZERO}
    while len(x2) > ZERO:
        x4 = x2.popleft()
        for x5 in dneighbors(x4):
            x6, x7 = x5
            if not (ZERO <= x6 < x0 and ZERO <= x7 < x1):
                continue
            if x5 not in passable or x5 in x3:
                continue
            x3[x5] = x3[x4] + ONE
            x2.append(x5)
    return x3


def shortest_path_union_cells_b15fca0b(
    passable: Indices,
    zeros: Indices,
    start: IntegerTuple,
    goal: IntegerTuple,
    dims: IntegerTuple,
) -> tuple[Indices, Integer]:
    x0 = bfs_distances_b15fca0b(passable, dims, start)
    x1 = bfs_distances_b15fca0b(passable, dims, goal)
    x2 = x0[goal]
    x3 = frozenset(x4 for x4 in zeros if x0.get(x4, 999) + x1.get(x4, 999) == x2)
    return x3, x2
