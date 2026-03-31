from __future__ import annotations

from collections import Counter

from synth_rearc.core import *


LAYOUTS_800D221B = (
    ("ne", "sw", "se"),
    ("nw", "sw", "se"),
    ("nw", "ne", "sw"),
    ("nw", "ne", "se"),
    ("nw", "ne", "sw", "se"),
    ("nw", "ne", "sw", "se", "e"),
    ("nw", "ne", "sw", "se", "w"),
)


def freeze_grid_800d221b(
    grid: list[list[Integer]],
) -> Grid:
    return tuple(tuple(row) for row in grid)


def neighbors4_800d221b(
    cell: IntegerTuple,
) -> tuple[IntegerTuple, ...]:
    i, j = cell
    return ((i - ONE, j), (i + ONE, j), (i, j - ONE), (i, j + ONE))


def in_bounds_800d221b(
    cell: IntegerTuple,
    dims: IntegerTuple,
) -> Boolean:
    h, w = dims
    i, j = cell
    return both(ZERO <= i < h, ZERO <= j < w)


def connected_components_800d221b(
    cells: set[IntegerTuple] | frozenset[IntegerTuple],
    dims: IntegerTuple,
) -> tuple[frozenset[IntegerTuple], ...]:
    remaining = set(cells)
    comps: list[frozenset[IntegerTuple]] = []
    while remaining:
        start = remaining.pop()
        frontier = [start]
        comp = {start}
        while frontier:
            cell = frontier.pop()
            for nb in neighbors4_800d221b(cell):
                if nb in remaining and in_bounds_800d221b(nb, dims):
                    remaining.remove(nb)
                    frontier.append(nb)
                    comp.add(nb)
        comps.append(frozenset(comp))
    return tuple(comps)


def monochrome_centers_800d221b(
    grid: Grid,
    value: Integer,
) -> tuple[IntegerTuple, ...]:
    h = len(grid)
    w = len(grid[ZERO])
    out = []
    for i in range(ONE, subtract(h, ONE)):
        for j in range(ONE, subtract(w, ONE)):
            if all(
                grid[ii][jj] == value
                for ii in range(i - ONE, i + TWO)
                for jj in range(j - ONE, j + TWO)
            ):
                out.append((i, j))
    return tuple(out)


def separator_color_800d221b(
    grid: Grid,
    bg: Integer | None = None,
) -> Integer:
    x0 = mostcolor(grid) if bg is None else bg
    x1 = difference(palette(grid), initset(x0))
    x2 = tuple(x1)
    x3 = tuple(monochrome_centers_800d221b(grid, x4) for x4 in x2)
    x4 = tuple(x5 for x5, x6 in pair(x2, x3) if len(x6) == ONE)
    return x4[ZERO]


def separator_center_800d221b(
    grid: Grid,
    sep: Integer,
) -> IntegerTuple:
    return monochrome_centers_800d221b(grid, sep)[ZERO]


def separator_block_800d221b(
    center: IntegerTuple,
) -> frozenset[IntegerTuple]:
    i, j = center
    return frozenset((ii, jj) for ii in range(i - ONE, i + TWO) for jj in range(j - ONE, j + TWO))


def foreground_components_800d221b(
    grid: Grid,
    bg: Integer,
    sep: Integer,
) -> tuple[frozenset[IntegerTuple], ...]:
    h = len(grid)
    w = len(grid[ZERO])
    x0 = {
        (i, j)
        for i in range(h)
        for j in range(w)
        if grid[i][j] != bg and grid[i][j] != sep
    }
    return connected_components_800d221b(x0, (h, w))


def branch_components_800d221b(
    grid: Grid,
    sep: Integer,
    center: IntegerTuple,
) -> tuple[frozenset[IntegerTuple], ...]:
    h = len(grid)
    w = len(grid[ZERO])
    x0 = ofcolor(grid, sep)
    x1 = separator_block_800d221b(center)
    x2 = difference(x0, x1)
    return connected_components_800d221b(set(x2), (h, w))


def component_index_800d221b(
    comps: tuple[frozenset[IntegerTuple], ...],
) -> dict[IntegerTuple, Integer]:
    out = {}
    for idx, comp in enumerate(comps):
        for cell in comp:
            out[cell] = idx
    return out


def dominant_color_for_cells_800d221b(
    grid: Grid,
    cells: frozenset[IntegerTuple] | set[IntegerTuple],
) -> Integer:
    x0 = Counter(grid[i][j] for i, j in cells)
    return x0.most_common(ONE)[ZERO][ZERO]


def adjacent_component_ids_800d221b(
    cells: frozenset[IntegerTuple] | set[IntegerTuple],
    index_by_cell: dict[IntegerTuple, Integer],
    dims: IntegerTuple,
) -> tuple[Integer, ...]:
    out = []
    for cell in cells:
        for nb in neighbors4_800d221b(cell):
            if not in_bounds_800d221b(nb, dims):
                continue
            if nb in index_by_cell:
                out.append(index_by_cell[nb])
    return tuple(out)


def line_cells_800d221b(
    start: IntegerTuple,
    end: IntegerTuple,
) -> frozenset[IntegerTuple]:
    if start[ZERO] == end[ZERO]:
        i = start[ZERO]
        left = min(start[ONE], end[ONE])
        right = max(start[ONE], end[ONE])
        return frozenset((i, j) for j in range(left, right + ONE))
    j = start[ONE]
    top = min(start[ZERO], end[ZERO])
    bottom = max(start[ZERO], end[ZERO])
    return frozenset((i, j) for i in range(top, bottom + ONE))


def l_path_800d221b(
    start: IntegerTuple,
    end: IntegerTuple,
    order: str,
) -> frozenset[IntegerTuple]:
    if order == "hv":
        corner = (start[ZERO], end[ONE])
    else:
        corner = (end[ZERO], start[ONE])
    return combine(line_cells_800d221b(start, corner), line_cells_800d221b(corner, end))


def slot_target_800d221b(
    center: IntegerTuple,
    slot: str,
) -> IntegerTuple:
    i, j = center
    targets = {
        "nw": (i - TWO, j - ONE),
        "ne": (i - TWO, j + ONE),
        "sw": (i + TWO, j - ONE),
        "se": (i + TWO, j + ONE),
        "e": (i, j + TWO),
        "w": (i, j - TWO),
    }
    return targets[slot]


def count_exact_sep_candidates_800d221b(
    grid: Grid,
    bg: Integer,
    sep: Integer,
) -> Integer:
    x0 = difference(difference(palette(grid), initset(bg)), initset(sep))
    return sum(len(monochrome_centers_800d221b(grid, x1)) == ONE for x1 in x0)
