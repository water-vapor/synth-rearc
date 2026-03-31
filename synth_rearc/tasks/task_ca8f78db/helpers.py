from __future__ import annotations

from synth_rearc.core import *


def row_signal_ca8f78db(
    row: tuple[Integer, ...],
) -> tuple[Integer, ...]:
    return tuple(x0 for x0 in row if x0 != ZERO)


def is_pattern_row_ca8f78db(
    row: tuple[Integer, ...],
) -> Boolean:
    return len(set(row_signal_ca8f78db(row))) > ONE


def _period_votes_ca8f78db(
    grid: Grid,
    rows: tuple[Integer, ...],
    offset: Integer,
    period: Integer,
) -> tuple[Integer, ...]:
    x0 = width(grid)
    return tuple(
        grid[x1][x2]
        for x1 in rows
        for x2 in range(offset, x0, period)
        if grid[x1][x2] != ZERO
    )


def is_valid_period_ca8f78db(
    grid: Grid,
    rows: tuple[Integer, ...],
    period: Integer,
) -> Boolean:
    for x0 in range(period):
        x1 = _period_votes_ca8f78db(grid, rows, x0, period)
        if len(x1) == ZERO or len(set(x1)) != ONE:
            return F
    return T


def recover_cycle_ca8f78db(
    grid: Grid,
    rows: tuple[Integer, ...],
) -> tuple[Integer, ...]:
    x0 = width(grid)
    x1 = next(
        x2
        for x2 in range(ONE, x0 + ONE)
        if is_valid_period_ca8f78db(grid, rows, x2)
    )
    return tuple(
        mostcommon(_period_votes_ca8f78db(grid, rows, x3, x1))
        for x3 in range(x1)
    )


def render_wallpaper_ca8f78db(
    cycle: tuple[Integer, ...],
    height_value: Integer,
    width_value: Integer,
    pattern_parity: Integer,
) -> Grid:
    x0 = repeat(cycle[ZERO], width_value)
    x1 = tuple(cycle[x2 % len(cycle)] for x2 in range(width_value))
    return tuple(
        x1 if x3 % TWO == pattern_parity else x0
        for x3 in range(height_value)
    )
