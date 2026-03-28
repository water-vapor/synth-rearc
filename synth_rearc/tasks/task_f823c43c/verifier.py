from synth_rearc.core import *


def _is_vertical_period_f823c43c(
    grid: Grid,
    period: Integer,
) -> Boolean:
    h = height(grid)
    w = width(grid)
    for i in range(h - period):
        for j in range(w):
            a = grid[i][j]
            b = grid[i + period][j]
            if a != SIX and b != SIX and a != b:
                return F
    return T


def _is_horizontal_period_f823c43c(
    grid: Grid,
    period: Integer,
) -> Boolean:
    h = height(grid)
    w = width(grid)
    for i in range(h):
        for j in range(w - period):
            a = grid[i][j]
            b = grid[i][j + period]
            if a != SIX and b != SIX and a != b:
                return F
    return T


def _recover_tile_f823c43c(
    grid: Grid,
    row_period: Integer,
    col_period: Integer,
) -> Grid:
    h = height(grid)
    w = width(grid)
    signal = tuple(
        value
        for row in grid
        for value in row
        if value != SIX
    )
    fallback = mostcommon(signal)
    rows = []
    for i in range(row_period):
        row = []
        for j in range(col_period):
            votes = tuple(
                grid[ii][jj]
                for ii in range(i, h, row_period)
                for jj in range(j, w, col_period)
                if grid[ii][jj] != SIX
            )
            value = fallback if len(votes) == ZERO else mostcommon(votes)
            row.append(value)
        rows.append(tuple(row))
    return tuple(rows)


def verify_f823c43c(I: Grid) -> Grid:
    x0 = height(I)
    x1 = width(I)
    x2 = next(x3 for x3 in range(ONE, x0 + ONE) if _is_vertical_period_f823c43c(I, x3))
    x4 = next(x5 for x5 in range(ONE, x1 + ONE) if _is_horizontal_period_f823c43c(I, x5))
    x6 = _recover_tile_f823c43c(I, x2, x4)
    x7 = tuple(tuple(x6[i % x2][j % x4] for j in range(x1)) for i in range(x0))
    return x7
