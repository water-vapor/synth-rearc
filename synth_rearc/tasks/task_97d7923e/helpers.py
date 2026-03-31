from __future__ import annotations

from synth_rearc.core import *


SelectorSpec97D7923E = tuple[Integer, Integer, Integer]
StemSpec97D7923E = tuple[Integer, Integer, Integer, Integer, Integer]


def _top_run_97d7923e(
    grid: Grid,
    col: Integer,
) -> tuple[Integer, ...]:
    x0 = []
    for x1 in range(height(grid)):
        if grid[x1][col] == ZERO:
            break
        x0.append(x1)
    return tuple(x0)


def _bottom_run_97d7923e(
    grid: Grid,
    col: Integer,
) -> tuple[Integer, ...]:
    x0 = []
    for x1 in range(decrement(height(grid)), NEG_ONE, NEG_ONE):
        if grid[x1][col] == ZERO:
            break
        x0.append(x1)
    x0.reverse()
    return tuple(x0)


def selector_specs_97d7923e(
    grid: Grid,
) -> tuple[SelectorSpec97D7923E, ...]:
    x0 = []
    x1 = width(grid)
    x2 = decrement(height(grid))
    for x3 in range(x1):
        x4 = _top_run_97d7923e(grid, x3)
        if len(x4) == ZERO:
            continue
        if x4[-1] == x2:
            continue
        x5 = tuple(grid[x6][x3] for x6 in x4)
        if len(set(x5)) != ONE:
            continue
        x0.append((x5[ZERO], len(x4), x3))
    return tuple(sorted(x0, key=lambda x6: (x6[TWO], x6[ZERO], x6[ONE])))


def stem_specs_97d7923e(
    grid: Grid,
) -> tuple[StemSpec97D7923E, ...]:
    x0 = []
    x1 = width(grid)
    for x2 in range(x1):
        x3 = _bottom_run_97d7923e(grid, x2)
        if len(x3) < THREE:
            continue
        x4 = tuple(grid[x5][x2] for x5 in x3)
        if x4[ZERO] != x4[-ONE]:
            continue
        x5 = x4[ONE:-ONE]
        if len(set(x5)) != ONE:
            continue
        if x5[ZERO] in (ZERO, x4[ZERO]):
            continue
        x0.append((x4[ZERO], x5[ZERO], x2, x3[ZERO], len(x3)))
    return tuple(sorted(x0, key=lambda x6: (x6[TWO], x6[THREE], x6[ZERO], x6[ONE])))


def selector_rank_map_97d7923e(
    grid: Grid,
) -> dict[Integer, Integer]:
    x0: dict[Integer, Integer] = {}
    for x1, x2, _ in selector_specs_97d7923e(grid):
        x3 = x0.get(x1, ZERO)
        x0[x1] = max(x2, x3)
    return x0


def ranked_stems_for_color_97d7923e(
    stems: tuple[StemSpec97D7923E, ...],
    color_value: Integer,
) -> tuple[StemSpec97D7923E, ...]:
    x0 = tuple(x1 for x1 in stems if x1[ZERO] == color_value)
    return tuple(sorted(x0, key=lambda x1: (invert(x1[FOUR]), x1[TWO])))


def selected_stems_97d7923e(
    grid: Grid,
) -> tuple[StemSpec97D7923E, ...]:
    x0 = selector_rank_map_97d7923e(grid)
    x1 = stem_specs_97d7923e(grid)
    x2 = []
    for x3, x4 in sorted(x0.items()):
        x5 = ranked_stems_for_color_97d7923e(x1, x3)
        if ZERO < x4 <= len(x5):
            x2.append(x5[decrement(x4)])
    return tuple(x2)


def stem_body_patch_97d7923e(
    stem: StemSpec97D7923E,
    grid_height: Integer,
) -> Indices:
    _, _, x0, x1, _ = stem
    return connect((increment(x1), x0), (subtract(grid_height, TWO), x0))


def paint_selected_stems_97d7923e(
    grid: Grid,
) -> Grid:
    x0 = grid
    x1 = height(grid)
    for x2 in selected_stems_97d7923e(grid):
        x3 = stem_body_patch_97d7923e(x2, x1)
        x0 = fill(x0, x2[ZERO], x3)
    return x0


def paint_selector_97d7923e(
    grid: Grid,
    color_value: Integer,
    col: Integer,
    run_height: Integer,
) -> Grid:
    x0 = connect((ZERO, col), (decrement(run_height), col))
    return fill(grid, color_value, x0)


def paint_stem_97d7923e(
    grid: Grid,
    color_value: Integer,
    body_value: Integer,
    col: Integer,
    top_row: Integer,
) -> Grid:
    x0 = decrement(height(grid))
    x1 = fill(grid, body_value, connect((top_row, col), (x0, col)))
    x2 = fill(x1, color_value, initset((top_row, col)))
    x3 = fill(x2, color_value, initset((x0, col)))
    return x3
