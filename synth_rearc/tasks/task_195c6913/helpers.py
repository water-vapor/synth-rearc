from __future__ import annotations

from collections import Counter

from synth_rearc.core import *


def _major_colors_195c6913(
    grid: Grid,
) -> tuple[Integer, Integer]:
    x0 = Counter(value for row in grid for value in row)
    x1 = tuple(color_value for color_value, _ in x0.most_common(TWO))
    if len(x1) != TWO:
        raise ValueError("expected two dominant colors")
    return x1


def _special_square_blocks_195c6913(
    grid: Grid,
) -> tuple[Object, ...]:
    x0, x1 = _major_colors_195c6913(grid)
    x2 = objects(grid, T, F, F)
    x3 = tuple(
        obj
        for obj in x2
        if color(obj) not in (x0, x1) and len(obj) == FOUR and square(obj)
    )
    if len(x3) < TWO:
        raise ValueError("expected motif blocks and a corner block")
    return tuple(sorted(x3, key=lambda obj: (uppermost(obj), leftmost(obj), color(obj))))


def extract_task_parts_195c6913(
    grid: Grid,
) -> tuple[Grid, tuple[Integer, ...], Integer, tuple[IntegerTuple, ...], Integer, Integer]:
    x0 = _special_square_blocks_195c6913(grid)
    x1 = minimum(apply(uppermost, x0))
    x2 = tuple(obj for obj in x0 if uppermost(obj) == x1)
    x3 = tuple(sorted(x2, key=leftmost))
    x4 = tuple(color(obj) for obj in x3)
    x5 = extract(x0, lambda obj: uppermost(obj) != x1)
    x6 = color(x5)
    x7, x8 = _major_colors_195c6913(grid)
    x9 = color(first(x3))
    x10 = tuple(
        sorted(
            (
                obj
                for obj in objects(grid, T, F, F)
                if color(obj) == x9 and len(obj) == ONE and leftmost(obj) == ZERO
            ),
            key=uppermost,
        )
    )
    x11 = tuple(ulcorner(obj) for obj in x10)
    if len(x11) == ZERO:
        raise ValueError("expected at least one left-edge seed")
    x12 = x11[0]
    x13 = grid[x12[0]][increment(x12[1])]
    x14 = x7 if x8 == x13 else x8
    x15 = grid
    for x16 in x3:
        x15 = fill(x15, x14, toindices(x16))
    x15 = fill(x15, x14, toindices(x5))
    for x17 in x11:
        x15 = fill(x15, x13, initset(x17))
    return x15, x4, x6, x11, x14, x13


def trace_paths_195c6913(
    base_grid: Grid,
    motif: tuple[Integer, ...],
    corner_color: Integer,
    starts: tuple[IntegerTuple, ...],
    band_color: Integer,
) -> Grid:
    x0 = [list(row) for row in base_grid]
    x1 = len(x0)
    x2 = len(x0[0])
    x3 = ((ZERO, ONE), (-ONE, ZERO))
    x4 = len(motif)
    for x5 in starts:
        x6, x7 = x5
        x8 = ZERO
        x9 = ZERO
        x0[x6][x7] = motif[x8]
        while True:
            x10, x11 = x3[x9]
            x12 = add(x6, x10)
            x13 = add(x7, x11)
            if not (ZERO <= x12 < x1 and ZERO <= x13 < x2):
                break
            if base_grid[x12][x13] != band_color:
                x0[x12][x13] = corner_color
                x9 = increment(x9) % TWO
                x14, x15 = x3[x9]
                x16 = add(x6, x14)
                x17 = add(x7, x15)
                if not (ZERO <= x16 < x1 and ZERO <= x17 < x2):
                    break
                if base_grid[x16][x17] != band_color:
                    break
                continue
            x6 = x12
            x7 = x13
            x8 = increment(x8) % x4
            x0[x6][x7] = motif[x8]
    return tuple(tuple(row) for row in x0)
