from arc2.core import *


def _full_rows_4e7e0eb9(grid: Grid, value: int) -> tuple[int, ...]:
    return tuple(i for i, row in enumerate(grid) if all(cell == value for cell in row))


def _full_cols_4e7e0eb9(grid: Grid, value: int) -> tuple[int, ...]:
    h = len(grid)
    w = len(grid[ZERO])
    return tuple(j for j in range(w) if all(grid[i][j] == value for i in range(h)))


def _separator_color_4e7e0eb9(grid: Grid) -> int | None:
    x0 = tuple(sorted(value for value in palette(grid) if value not in (ZERO, FOUR)))
    x1: list[tuple[int, int, int]] = []
    for x2 in x0:
        x3 = _full_rows_4e7e0eb9(grid, x2)
        x4 = _full_cols_4e7e0eb9(grid, x2)
        if len(x3) + len(x4) > ZERO:
            x5 = minimum(x3 + x4)
            x1.append((len(x3) + len(x4), invert(x5), x2))
    if len(x1) == ZERO:
        return None
    return maximum(x1)[TWO]


def _bands_4e7e0eb9(indices: tuple[int, ...], limit: int) -> tuple[tuple[int, int], ...]:
    x0 = (-ONE,) + indices + (limit,)
    return tuple((a + ONE, b) for a, b in zip(x0, x0[ONE:]) if b - a > ONE)


def _solve_panel_4e7e0eb9(grid: Grid) -> Grid:
    x0 = _separator_color_4e7e0eb9(grid)
    if x0 is not None:
        x1 = _full_rows_4e7e0eb9(grid, x0)
        x2 = _full_cols_4e7e0eb9(grid, x0)
        x3 = _bands_4e7e0eb9(x1, len(grid))
        x4 = _bands_4e7e0eb9(x2, len(grid[ZERO]))
        x5 = grid
        for x6, x7 in x3:
            for x8, x9 in x4:
                x10 = crop(grid, (x6, x8), (x7 - x6, x9 - x8))
                x11 = _solve_panel_4e7e0eb9(x10)
                x12 = shift(asobject(x11), (x6, x8))
                x5 = paint(x5, x12)
        return x5
    x13 = _full_rows_4e7e0eb9(grid, FOUR)
    x14 = _full_cols_4e7e0eb9(grid, FOUR)
    x15 = len(x13)
    x16 = len(x14)
    if x15 == ONE and x16 == ZERO:
        return hmirror(grid)
    if x16 == ONE and x15 == ZERO:
        return vmirror(grid)
    x17 = tuple(sorted(value for value in palette(grid) if value not in (ZERO, ONE)))
    if len(x17) == ONE:
        return replace(grid, ONE, x17[ZERO])
    return grid


def verify_4e7e0eb9(I: Grid) -> Grid:
    x0 = _solve_panel_4e7e0eb9(I)
    return x0
