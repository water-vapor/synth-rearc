from synth_rearc.core import *


MAX_DIM_71E489B6 = 30
MIN_DIM_71E489B6 = 14

ZERO_INTERIOR_SHAPES_71E489B6 = (
    frozenset({(0, 0)}),
    frozenset({(0, 0), (0, 1)}),
    frozenset({(0, 0), (1, 0)}),
    frozenset({(0, 0), (1, 1)}),
    frozenset({(0, 0), (1, 0), (1, 1)}),
    frozenset({(0, 0), (0, 1), (1, 1)}),
    frozenset({(0, 0), (1, 1), (2, 2)}),
    frozenset({(0, 2), (1, 1), (2, 0)}),
)


def blank_grid_71e489b6(
    dims,
    value,
):
    return [[value for _ in range(dims[1])] for _ in range(dims[0])]


def freeze_grid_71e489b6(
    grid,
):
    return tuple(tuple(row) for row in grid)


def paint_cells_71e489b6(
    grid,
    cells,
    value,
):
    h = len(grid)
    w = len(grid[0])
    for i, j in cells:
        if 0 <= i < h and 0 <= j < w:
            grid[i][j] = value


def paint_rect_71e489b6(
    grid,
    top,
    left,
    height,
    width,
    value,
):
    for i in range(top, top + height):
        for j in range(left, left + width):
            grid[i][j] = value


def orth_neighbors_71e489b6(
    cell,
):
    i, j = cell
    return ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1))


def border_sides_71e489b6(
    cells,
    dims,
):
    h, w = dims
    sides = 0
    if any(i == 0 for i, _ in cells):
        sides += 1
    if any(i == h - 1 for i, _ in cells):
        sides += 1
    if any(j == 0 for _, j in cells):
        sides += 1
    if any(j == w - 1 for _, j in cells):
        sides += 1
    return sides


def halo_cells_71e489b6(
    cells,
    dims,
):
    h, w = dims
    halo = set()
    for i, j in cells:
        for di in (-1, 0, 1):
            for dj in (-1, 0, 1):
                ni = i + di
                nj = j + dj
                if 0 <= ni < h and 0 <= nj < w and (ni, nj) not in cells:
                    halo.add((ni, nj))
    return frozenset(halo)


def supported_cells_71e489b6(
    grid,
    value,
):
    h = len(grid)
    w = len(grid[0])
    supported = set()
    for i in range(h - 1):
        for j in range(w - 1):
            if (
                grid[i][j] == value
                and grid[i + 1][j] == value
                and grid[i][j + 1] == value
                and grid[i + 1][j + 1] == value
            ):
                supported |= {(i, j), (i + 1, j), (i, j + 1), (i + 1, j + 1)}
    return frozenset(supported)


def unsupported_components_71e489b6(
    grid,
    value,
):
    h = len(grid)
    w = len(grid[0])
    supported = supported_cells_71e489b6(grid, value)
    unsupported = {
        (i, j)
        for i in range(h)
        for j in range(w)
        if grid[i][j] == value and (i, j) not in supported
    }
    remaining = set(unsupported)
    components = []
    while remaining:
        start = next(iter(remaining))
        stack = [start]
        component = {start}
        remaining.remove(start)
        while stack:
            cell = stack.pop()
            i, j = cell
            for di in (-1, 0, 1):
                for dj in (-1, 0, 1):
                    if di == 0 and dj == 0:
                        continue
                    neighbor = (i + di, j + dj)
                    if neighbor in remaining:
                        remaining.remove(neighbor)
                        component.add(neighbor)
                        stack.append(neighbor)
        attachments = set()
        for cell in component:
            for neighbor in orth_neighbors_71e489b6(cell):
                ni, nj = neighbor
                if 0 <= ni < h and 0 <= nj < w and grid[ni][nj] == value and neighbor not in component:
                    attachments.add(neighbor)
        components.append(
            {
                "cells": frozenset(component),
                "attachments": frozenset(attachments),
                "border_sides": border_sides_71e489b6(component, (h, w)),
            }
        )
    return tuple(components)


def selected_zero_cells_71e489b6(
    grid,
):
    kept = set()
    for component in unsupported_components_71e489b6(grid, ZERO):
        x0 = size(component["attachments"])
        x1 = component["border_sides"]
        x2 = size(component["cells"])
        if x0 <= ONE and not (x1 >= TWO and x2 > ONE):
            kept |= component["cells"]
    return frozenset(kept)


def selected_one_cells_71e489b6(
    grid,
    halo,
):
    removed = set()
    for component in unsupported_components_71e489b6(grid, ONE):
        x0 = size(component["attachments"])
        x1 = component["cells"]
        if x0 <= ONE and x1.isdisjoint(halo):
            removed |= x1
    return frozenset(removed)


def normalize_shape_71e489b6(
    shape,
):
    mini = min(i for i, _ in shape)
    minj = min(j for _, j in shape)
    return frozenset((i - mini, j - minj) for i, j in shape)


def shape_variants_71e489b6(
    shape,
):
    variants = set()
    current = tuple(shape)
    for _ in range(4):
        rotated = tuple((j, -i) for i, j in current)
        current = rotated
        variants.add(normalize_shape_71e489b6(current))
        mirrored = tuple((i, -j) for i, j in current)
        variants.add(normalize_shape_71e489b6(mirrored))
    variants.add(normalize_shape_71e489b6(shape))
    return tuple(variants)


def random_partition_71e489b6(
    total,
    parts,
    minimum,
):
    values = [minimum for _ in range(parts)]
    slack = total - minimum * parts
    for _ in range(slack):
        values[randint(0, parts - 1)] += 1
    return tuple(values)
