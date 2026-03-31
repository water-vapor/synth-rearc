from synth_rearc.core import *


def _is_vertical_period_e95e3d8e(
    grid: Grid,
    period: Integer,
) -> Boolean:
    x0 = height(grid)
    x1 = width(grid)
    for x2 in range(x0 - period):
        for x3 in range(x1):
            x4 = grid[x2][x3]
            x5 = grid[x2 + period][x3]
            if x4 != ZERO and x5 != ZERO and x4 != x5:
                return F
    return T


def _is_horizontal_period_e95e3d8e(
    grid: Grid,
    period: Integer,
) -> Boolean:
    x0 = height(grid)
    x1 = width(grid)
    for x2 in range(x0):
        for x3 in range(x1 - period):
            x4 = grid[x2][x3]
            x5 = grid[x2][x3 + period]
            if x4 != ZERO and x5 != ZERO and x4 != x5:
                return F
    return T


def _recover_tile_e95e3d8e(
    grid: Grid,
    row_period: Integer,
    col_period: Integer,
) -> Grid:
    x0 = height(grid)
    x1 = width(grid)
    x2 = tuple(x3 for x4 in grid for x3 in x4 if x3 != ZERO)
    x3 = mostcommon(x2)
    x4 = []
    for x5 in range(row_period):
        x6 = []
        for x7 in range(col_period):
            x8 = tuple(
                grid[x9][x10]
                for x9 in range(x5, x0, row_period)
                for x10 in range(x7, x1, col_period)
                if grid[x9][x10] != ZERO
            )
            x11 = x3 if len(x8) == ZERO else mostcommon(x8)
            x6.append(x11)
        x4.append(tuple(x6))
    return tuple(x4)


def verify_e95e3d8e(I: Grid) -> Grid:
    x0 = height(I)
    x1 = width(I)
    x2 = next(x3 for x3 in range(ONE, x0 + ONE) if _is_vertical_period_e95e3d8e(I, x3))
    x4 = next(x5 for x5 in range(ONE, x1 + ONE) if _is_horizontal_period_e95e3d8e(I, x5))
    x6 = _recover_tile_e95e3d8e(I, x2, x4)
    x7 = tuple(tuple(x6[x8 % x2][x9 % x4] for x9 in range(x1)) for x8 in range(x0))
    return x7
