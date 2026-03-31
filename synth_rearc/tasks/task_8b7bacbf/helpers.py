from __future__ import annotations

from synth_rearc.core import *


def _split_four_connected_8b7bacbf(
    patch: Indices,
) -> tuple[Indices, ...]:
    x0 = set(patch)
    x1: list[Indices] = []
    while len(x0) > ZERO:
        x2 = x0.pop()
        x3 = {x2}
        x4 = [x2]
        while len(x4) > ZERO:
            x5 = x4.pop()
            for x6 in dneighbors(x5):
                if x6 in x0:
                    x0.remove(x6)
                    x3.add(x6)
                    x4.append(x6)
        x1.append(frozenset(x3))
    return tuple(x1)


def _boundary_8b7bacbf(
    grid: Grid,
    region: Indices,
) -> Indices:
    x0, x1 = shape(grid)
    x2 = mostcolor(grid)
    x3 = set()
    for x4 in region:
        for x5 in dneighbors(x4):
            if (
                ZERO <= x5[ZERO] < x0
                and ZERO <= x5[ONE] < x1
                and x5 not in region
                and index(grid, x5) != x2
            ):
                x3.add(x5)
    return frozenset(x3)


def _marker_specs_8b7bacbf(
    grid: Grid,
) -> tuple[tuple[Integer, IntegerTuple, Integer, Indices], ...]:
    x0 = palette(grid) - initset(mostcolor(grid))
    x1 = []
    for x2 in sorted(x0):
        if colorcount(grid, x2) != ONE:
            continue
        x3 = first(colorfilter(objects(grid, True, False, True), x2))
        x4 = first(toindices(x3))
        x5 = {
            index(grid, x6)
            for x6 in dneighbors(x4)
            if index(grid, x6) not in (None, mostcolor(grid), x2)
        }
        if len(x5) != ONE:
            continue
        x6 = first(x5)
        x7 = extract(
            objects(grid, False, True, True),
            lambda x8: len(intersection(toindices(x8), toindices(x3))) > ZERO,
        )
        x1.append((x2, x4, x6, toindices(x7)))
    return tuple(x1)


def candidate_regions_8b7bacbf(
    grid: Grid,
) -> tuple[
    tuple[Integer, IntegerTuple, Integer, Indices, tuple[tuple[Indices, Indices], ...], tuple[Indices, ...]],
    ...,
]:
    x0 = mostcolor(grid)
    x1 = []
    for x2, x3, x4, x5 in _marker_specs_8b7bacbf(grid):
        x6: list[tuple[Indices, Indices]] = []
        for x7 in objects(grid, True, False, False):
            if color(x7) != x0 or bordering(x7, grid):
                continue
            x8 = toindices(x7)
            x9 = _boundary_8b7bacbf(grid, x8)
            x10 = {index(grid, x11) for x11 in x9}
            if len(x9) > ZERO and x9 <= x5 and len(x10) == ONE:
                x6.append((x8, x9))
        for x7 in objects(grid, True, True, True):
            x8 = color(x7)
            x9 = toindices(x7)
            if x8 in (x0, x2, x4) or not (x9 <= x5) or not bordering(x7, grid):
                continue
            x10 = {x11 for x11 in difference(backdrop(x7), x9) if index(grid, x11) == x0}
            for x11 in _split_four_connected_8b7bacbf(x10):
                if len(x11) == ONE:
                    continue
                x12 = _boundary_8b7bacbf(grid, x11)
                x13 = {index(grid, x14) for x14 in x12}
                if len(x12) > ZERO and x12 <= x5 and len(x13) == ONE:
                    x6.append((x11, x12))
        x7 = set()
        x8: list[tuple[Indices, Indices]] = []
        for x9, x10 in x6:
            x11 = tuple(sorted(x9))
            if x11 in x7:
                continue
            x7.add(x11)
            x8.append((x9, x10))
        x9 = tuple(
            toindices(x10)
            for x10 in colorfilter(objects(grid, True, True, True), x4)
            if toindices(x10) <= x5
        )
        x1.append((x2, x3, x4, x5, tuple(x8), x9))
    return tuple(x1)


def transform_grid_8b7bacbf(
    grid: Grid,
) -> Grid:
    x0 = grid
    x1 = candidate_regions_8b7bacbf(x0)
    x2 = x0
    for x3, x4, x5, x6, x7, x8 in x1:
        x9 = {
            x10
            for x10, x11 in enumerate(x8)
            if any(x12 in x11 for x12 in dneighbors(x4))
        }
        x10 = set()
        x11 = True
        while x11:
            x11 = False
            for x12, (x13, x14) in enumerate(x7):
                if x12 in x10:
                    continue
                if any(manhattan(x14, x8[x15]) <= TWO for x15 in x9):
                    x10.add(x12)
                    x11 = True
            for x12, x13 in enumerate(x8):
                if x12 in x9:
                    continue
                if any(manhattan(x8[x14], x13) <= THREE for x14 in x9) or any(
                    manhattan(x7[x14][ONE], x13) <= TWO for x14 in x10
                ):
                    x9.add(x12)
                    x11 = True
        x12 = frozenset()
        for x13 in x10:
            x12 = combine(x12, x7[x13][ZERO])
        x2 = fill(x2, x3, x12)
    return x2
