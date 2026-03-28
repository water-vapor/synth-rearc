from __future__ import annotations

from itertools import combinations

from synth_rearc.core import *


PLUS_OFFSETS_14754a24 = (
    UP,
    LEFT,
    ORIGIN,
    RIGHT,
    DOWN,
)

DIAGONAL_OFFSETS_14754a24 = (
    NEG_UNITY,
    UP_RIGHT,
    DOWN_LEFT,
    UNITY,
)


def plus_patch_14754a24(
    center: IntegerTuple,
    dims: IntegerTuple,
) -> Indices:
    h, w = dims
    i, j = center
    return frozenset(
        (i + di, j + dj)
        for di, dj in PLUS_OFFSETS_14754a24
        if ZERO <= i + di < h and ZERO <= j + dj < w
    )


def valid_plus_center_14754a24(
    grid: Grid,
    center: IntegerTuple,
) -> Indices | None:
    dims = shape(grid)
    patch = plus_patch_14754a24(center, dims)
    if len(patch) < FOUR:
        return None
    values = tuple(index(grid, cell) for cell in patch)
    if any(value not in (FOUR, FIVE) for value in values):
        return None
    yellow = frozenset(cell for cell in patch if index(grid, cell) == FOUR)
    if not (TWO <= len(yellow) < len(patch)):
        return None
    h, w = dims
    for i, j in yellow:
        for di, dj in DIAGONAL_OFFSETS_14754a24:
            ni, nj = i + di, j + dj
            if ZERO <= ni < h and ZERO <= nj < w and index(grid, (ni, nj)) == FOUR and (ni, nj) not in patch:
                return None
    return frozenset(cell for cell in patch if index(grid, cell) == FIVE)


def _connected_subset_14754a24(patch: Indices) -> Boolean:
    start = first(patch)
    frontier = {start}
    seen = {start}
    while frontier:
        i, j = frontier.pop()
        for di in (-ONE, ZERO, ONE):
            for dj in (-ONE, ZERO, ONE):
                if di == ZERO and dj == ZERO:
                    continue
                cell = (i + di, j + dj)
                if cell in patch and cell not in seen:
                    seen.add(cell)
                    frontier.add(cell)
    return len(seen) == len(patch)


def plus_connected_subsets_14754a24(
    patch: Indices,
) -> tuple[Indices, ...]:
    cells = tuple(sorted(patch))
    subsets = []
    for n in range(TWO, len(cells)):
        for subset in combinations(cells, n):
            frozen = frozenset(subset)
            if _connected_subset_14754a24(frozen):
                subsets.append(frozen)
    return tuple(subsets)
