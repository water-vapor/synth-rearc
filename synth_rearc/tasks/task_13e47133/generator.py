from __future__ import annotations

from collections import Counter

from synth_rearc.core import *

from .helpers import component_cells_13e47133, convex_corners_13e47133, corner_diagonal_13e47133, render_output_13e47133


COLOR_POOL_13E47133 = tuple(range(TEN))
SEQUENCE_LENGTH_BAG_13E47133 = (ONE, ONE, TWO, TWO, TWO, THREE)


def _band_sizes_13e47133(
    count: Integer,
    diff_lb: float,
    diff_ub: float,
) -> tuple[Integer, ...] | None:
    for _ in range(80):
        x0 = tuple(unifint(diff_lb, diff_ub, (THREE, NINE)) for _ in range(count))
        x1 = sum(x0) + (count - ONE)
        if 15 <= x1 <= 30:
            return x0
    return None


def _band_bounds_13e47133(
    sizes: tuple[Integer, ...],
) -> tuple[tuple[Integer, Integer], ...]:
    out = []
    start = ZERO
    for size in sizes:
        stop = start + size - ONE
        out.append((start, stop))
        start = stop + TWO
    return tuple(out)


def _find_13e47133(
    parent: dict[IntegerTuple, IntegerTuple],
    node: IntegerTuple,
) -> IntegerTuple:
    root = node
    while parent[root] != root:
        root = parent[root]
    while parent[node] != node:
        nxt = parent[node]
        parent[node] = root
        node = nxt
    return root


def _union_13e47133(
    parent: dict[IntegerTuple, IntegerTuple],
    a: IntegerTuple,
    b: IntegerTuple,
) -> None:
    x0 = _find_13e47133(parent, a)
    x1 = _find_13e47133(parent, b)
    if x0 != x1:
        parent[x1] = x0


def _face_components_13e47133(
    nr: Integer,
    nc: Integer,
    diff_lb: float,
    diff_ub: float,
) -> dict[IntegerTuple, IntegerTuple] | None:
    x0 = {(i, j): (i, j) for i in range(nr) for j in range(nc)}
    x1 = []
    for i in range(nr):
        for j in range(nc):
            if i + ONE < nr:
                x1.append(((i, j), (i + ONE, j)))
            if j + ONE < nc:
                x1.append(((i, j), (i, j + ONE)))
    shuffle(x1)
    x2 = unifint(diff_lb, diff_ub, (max(ONE, len(x1) // FOUR), max(TWO, (2 * len(x1)) // THREE)))
    for x3, x4 in x1[:x2]:
        _union_13e47133(x0, x3, x4)
    x5 = {_find_13e47133(x0, node) for node in x0}
    if not (THREE <= len(x5) <= nr * nc - ONE):
        return None
    x6 = Counter(_find_13e47133(x0, node) for node in x0)
    if maximum(tuple(x6.values())) < TWO:
        return None
    return {node: _find_13e47133(x0, node) for node in x0}


def _grid_from_faces_13e47133(
    row_bounds: tuple[tuple[Integer, Integer], ...],
    col_bounds: tuple[tuple[Integer, Integer], ...],
    labels: dict[IntegerTuple, IntegerTuple],
    background: Integer,
    wall: Integer,
) -> Grid:
    x0 = row_bounds[-ONE][ONE] + ONE
    x1 = col_bounds[-ONE][ONE] + ONE
    x2 = canvas(background, (x0, x1))
    for i, (r0, r1) in enumerate(row_bounds[:-ONE]):
        x3 = r1 + ONE
        for j, (c0, c1) in enumerate(col_bounds):
            if labels[(i, j)] == labels[(i + ONE, j)]:
                continue
            x4 = frozenset((x3, c) for c in range(c0, c1 + ONE))
            x2 = fill(x2, wall, x4)
    for i, (r0, r1) in enumerate(row_bounds):
        for j, (c0, c1) in enumerate(col_bounds[:-ONE]):
            if labels[(i, j)] == labels[(i, j + ONE)]:
                continue
            x3 = c1 + ONE
            x4 = frozenset((r, x3) for r in range(r0, r1 + ONE))
            x2 = fill(x2, wall, x4)
    return x2


def _place_component_sequence_13e47133(
    grid: Grid,
    component: Indices,
    background: Integer,
    wall: Integer,
    palette: tuple[Integer, ...],
    diff_lb: float,
    diff_ub: float,
) -> Grid:
    x0 = convex_corners_13e47133(grid, component)
    x1 = []
    for x2, x3 in x0:
        x4 = corner_diagonal_13e47133(component, x2, x3)
        x1.append((len(x4), x2, x3, x4))
    x1 = tuple(sorted(x1, reverse=T))
    if len(x1) == ZERO:
        return grid
    x2 = x1[ZERO]
    x3 = choice(x1[: min(len(x1), THREE)])
    x4 = x3[THREE]
    if len(x4) == ONE and choice((T, F)):
        return grid
    x5 = choice(SEQUENCE_LENGTH_BAG_13E47133)
    x5 = min(x5, len(x4))
    if x5 == ZERO:
        return grid
    x6 = T if len(x4) > ONE and x5 > ONE and choice((T, F, F)) else F
    x7 = x5
    if x6 and x7 == ONE:
        x6 = F
    x8 = list(sample(tuple(value for value in palette if value not in (background, wall)), x7 - (ONE if x6 else ZERO)))
    x9 = [background] if x6 else []
    x9.extend(x8)
    x10 = grid
    for x11, x12 in zip(x4, x9):
        if x12 == background:
            continue
        x10 = fill(x10, x12, initset(x11))
    return x10


def _seed_grid_13e47133(
    grid: Grid,
    background: Integer,
    wall: Integer,
    diff_lb: float,
    diff_ub: float,
) -> Grid | None:
    x0 = tuple(value for value in COLOR_POOL_13E47133 if value not in (background, wall))
    x1 = list(component_cells_13e47133(grid, wall))
    shuffle(x1)
    x2 = grid
    x3 = ZERO
    x4 = ZERO
    for x5 in x1:
        x6 = x2
        x2 = _place_component_sequence_13e47133(x2, x5, background, wall, x0, diff_lb, diff_ub)
        if x2 != x6:
            x3 += ONE
            x7 = render_output_13e47133(x2)
            if x7 != x2:
                x4 += ONE
    if x3 < TWO or x4 < TWO:
        return None
    return x2


def generate_13e47133(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = unifint(diff_lb, diff_ub, (TWO, FOUR))
        x1 = unifint(diff_lb, diff_ub, (TWO, FOUR))
        x2 = _band_sizes_13e47133(x0, diff_lb, diff_ub)
        x3 = _band_sizes_13e47133(x1, diff_lb, diff_ub)
        if x2 is None or x3 is None:
            continue
        x4 = _face_components_13e47133(x0, x1, diff_lb, diff_ub)
        if x4 is None:
            continue
        x5, x6 = sample(COLOR_POOL_13E47133, TWO)
        x7 = _band_bounds_13e47133(x2)
        x8 = _band_bounds_13e47133(x3)
        x9 = _grid_from_faces_13e47133(x7, x8, x4, x5, x6)
        x10 = _seed_grid_13e47133(x9, x5, x6, diff_lb, diff_ub)
        if x10 is None:
            continue
        x11 = render_output_13e47133(x10)
        if x11 == x10:
            continue
        return {"input": x10, "output": x11}
