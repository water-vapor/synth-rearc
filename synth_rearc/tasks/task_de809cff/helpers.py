from __future__ import annotations

from collections import Counter

from synth_rearc.core import *


def dominant_colors_de809cff(
    grid: Grid,
) -> tuple[Integer, Integer]:
    x0 = Counter(x1 for x2 in grid for x1 in x2 if x1 != ZERO)
    x1, x2 = tuple(x3 for x3, _ in x0.most_common(TWO))
    return x1, x2


def other_color_de809cff(
    colors: tuple[Integer, Integer],
    color: Integer,
) -> Integer:
    return colors[ZERO] if colors[ONE] == color else colors[ONE]


def _connected_offsets_de809cff(
    offsets: tuple[tuple[Integer, Integer], ...],
) -> Boolean:
    if len(offsets) == ZERO:
        return F
    x0 = set(offsets)
    x1 = [next(iter(x0))]
    x2 = {x1[ZERO]}
    while len(x1) > ZERO:
        x3, x4 = x1.pop()
        for x5 in (-ONE, ZERO, ONE):
            for x6 in (-ONE, ZERO, ONE):
                if both(x5 == ZERO, x6 == ZERO):
                    continue
                x7 = (add(x3, x5), add(x4, x6))
                if both(x7 in x0, x7 not in x2):
                    x2.add(x7)
                    x1.append(x7)
    return len(x2) == len(x0)


def _center_signature_de809cff(
    grid: Grid,
    loc: tuple[Integer, Integer],
) -> tuple[Integer, Integer, Boolean] | None:
    x0, x1 = loc
    x2 = len(grid)
    x3 = len(grid[ZERO])
    x4 = []
    x5 = []
    for x6 in (-ONE, ZERO, ONE):
        for x7 in (-ONE, ZERO, ONE):
            if both(x6 == ZERO, x7 == ZERO):
                continue
            x8 = add(x0, x6)
            x9 = add(x1, x7)
            if not (ZERO <= x8 < x2 and ZERO <= x9 < x3):
                continue
            x10 = grid[x8][x9]
            if x10 == ZERO:
                continue
            x4.append(x10)
            x5.append((x6, x7, x10))
    if len(x4) == ZERO:
        return None
    x11 = Counter(x4).most_common(ONE)[ZERO]
    x12 = x11[ZERO]
    x13 = x11[ONE]
    x14 = tuple((x15, x16) for x15, x16, x17 in x5 if x17 == x12)
    x15 = _connected_offsets_de809cff(x14)
    return x12, x13, x15


def stamp_centers_de809cff(
    grid: Grid,
) -> tuple[tuple[Integer, Integer, Integer], ...]:
    x0 = len(grid)
    x1 = len(grid[ZERO])
    x2 = []
    for x3 in range(x0):
        for x4 in range(x1):
            if grid[x3][x4] != ZERO:
                continue
            x5 = _center_signature_de809cff(grid, (x3, x4))
            if x5 is None:
                continue
            x6, x7, x8 = x5
            if both(x7 >= FIVE, x8):
                x2.append((x3, x4, x6))
    return tuple(x2)


def stamp_footprint_de809cff(
    dims: tuple[Integer, Integer],
    center: tuple[Integer, Integer],
) -> frozenset[tuple[Integer, Integer]]:
    x0, x1 = dims
    x2, x3 = center
    x4 = set()
    for x5 in range(max(ZERO, subtract(x2, ONE)), min(x0, add(x2, TWO))):
        for x6 in range(max(ZERO, subtract(x3, ONE)), min(x1, add(x3, TWO))):
            x4.add((x5, x6))
    return frozenset(x4)


def covered_cells_de809cff(
    dims: tuple[Integer, Integer],
    centers: tuple[tuple[Integer, Integer, Integer], ...],
) -> frozenset[tuple[Integer, Integer]]:
    x0 = frozenset()
    for x1, x2, _ in centers:
        x3 = stamp_footprint_de809cff(dims, (x1, x2))
        x0 = frozenset(x0 | x3)
    return x0


def _orthogonal_neighbors_de809cff(
    grid: Grid,
    loc: tuple[Integer, Integer],
) -> tuple[Integer | None, Integer | None, Integer | None, Integer | None]:
    x0, x1 = loc
    x2 = len(grid)
    x3 = len(grid[ZERO])
    x4 = []
    for x5, x6 in ((ONE, ZERO), (NEG_ONE, ZERO), (ZERO, ONE), (ZERO, NEG_ONE)):
        x7 = add(x0, x5)
        x8 = add(x1, x6)
        if 0 <= x7 < x2 and 0 <= x8 < x3:
            x4.append(grid[x7][x8])
        else:
            x4.append(None)
    return tuple(x4)


def _thin_cell_rewrite_de809cff(
    grid: Grid,
    loc: tuple[Integer, Integer],
    colors: tuple[Integer, Integer],
) -> Integer | None:
    x0 = grid[loc[ZERO]][loc[ONE]]
    if x0 == ZERO:
        return None
    x1 = _orthogonal_neighbors_de809cff(grid, loc)
    x2 = sum(x3 == x0 for x3 in x1)
    x3 = tuple(x4 for x4 in x1 if x4 != x0)
    if x2 == ZERO:
        return ZERO
    if x2 != ONE:
        return None
    if all(x4 in (ZERO, None) for x4 in x3):
        return ZERO
    x4 = other_color_de809cff(colors, x0)
    if both(x0 == colors[ZERO], all(x5 == x4 for x5 in x3)):
        return x4
    return None


def _secondary_pit_fill_de809cff(
    grid: Grid,
    loc: tuple[Integer, Integer],
    colors: tuple[Integer, Integer],
) -> Integer | None:
    x0 = grid[loc[ZERO]][loc[ONE]]
    if x0 != colors[ONE]:
        return None
    x1 = _orthogonal_neighbors_de809cff(grid, loc)
    x2 = sum(x3 == x0 for x3 in x1)
    if x2 != ONE:
        return None
    x3 = colors[ZERO]
    x4 = tuple(x5 for x5 in x1 if x5 != x0)
    if all(x5 == x3 for x5 in x4):
        return x3
    return None


def transform_grid_de809cff(
    grid: Grid,
) -> Grid:
    x0 = dominant_colors_de809cff(grid)
    x1 = stamp_centers_de809cff(grid)
    x2 = covered_cells_de809cff(shape(grid), x1)
    x3 = [list(x4) for x4 in grid]
    x4 = len(grid)
    x5 = len(grid[ZERO])
    for x6 in range(x4):
        for x7 in range(x5):
            if both(grid[x6][x7] != ZERO, (x6, x7) not in x2):
                x8 = _thin_cell_rewrite_de809cff(grid, (x6, x7), x0)
                if x8 is not None:
                    x3[x6][x7] = x8
    x6 = tuple(tuple(x7) for x7 in x3)
    for x7 in range(x4):
        for x8 in range(x5):
            if both(x6[x7][x8] != ZERO, (x7, x8) not in x2):
                x9 = _secondary_pit_fill_de809cff(x6, (x7, x8), x0)
                if x9 is not None:
                    x3[x7][x8] = x9
    for x7, x8, x9 in x1:
        x10 = other_color_de809cff(x0, x9)
        for x11 in range(max(ZERO, subtract(x7, ONE)), min(x4, add(x7, TWO))):
            for x12 in range(max(ZERO, subtract(x8, ONE)), min(x5, add(x8, TWO))):
                x3[x11][x12] = x10
    for x7, x8, _ in x1:
        x3[x7][x8] = EIGHT
    return tuple(tuple(x12) for x12 in x3)


def carvable_centers_de809cff(
    grid: Grid,
    color: Integer,
) -> tuple[tuple[Integer, Integer], ...]:
    x0 = []
    for x1 in range(len(grid)):
        for x2 in range(len(grid[ZERO])):
            if grid[x1][x2] != color:
                continue
            x3 = tuple(tuple(grid[x4][x5] if not both(x4 == x1, x5 == x2) else ZERO for x5 in range(len(grid[ZERO]))) for x4 in range(len(grid)))
            x4 = _center_signature_de809cff(x3, (x1, x2))
            if both(x4 is not None, x4[ZERO] == color):
                if both(x4[ONE] >= FIVE, x4[TWO]):
                    x0.append((x1, x2))
    return tuple(x0)


def rect_patch_de809cff(
    top: Integer,
    left: Integer,
    h: Integer,
    w: Integer,
) -> Indices:
    return frozenset((x0, x1) for x0 in range(top, add(top, h)) for x1 in range(left, add(left, w)))
