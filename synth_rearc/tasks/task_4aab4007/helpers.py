from synth_rearc.core import *


GRID_SIZE_4AAB4007 = 28


def residue_patch_4aab4007(
    height: Integer,
    width: Integer,
    period: Integer,
    residue: Integer,
):
    return frozenset(
        (i, j)
        for i in range(THREE, height)
        for j in range(THREE, width)
        if i + j >= NINE and (i + j - NINE) % period == residue
    )


def render_output_4aab4007(cycle: tuple[int, ...]) -> Grid:
    x0 = canvas(ONE, (GRID_SIZE_4AAB4007, GRID_SIZE_4AAB4007))
    x1 = interval(TWO, GRID_SIZE_4AAB4007, ONE)
    x2 = product(frozenset({TWO}), x1)
    x3 = product(x1, frozenset({TWO}))
    x4 = fill(x0, FOUR, combine(x2, x3))
    x5 = fill(x4, THREE, frozenset({(THREE, THREE)}))
    x6 = fill(x5, TWO, frozenset({(THREE, FOUR), (FOUR, THREE)}))
    x7 = fill(x6, ONE, frozenset({(THREE, FIVE), (FIVE, THREE)}))
    x8 = fill(x7, cycle[-ONE], frozenset({(FOUR, FOUR)}))
    x9 = x8
    for x10, x11 in enumerate(cycle):
        x12 = residue_patch_4aab4007(GRID_SIZE_4AAB4007, GRID_SIZE_4AAB4007, len(cycle), x10)
        x9 = fill(x9, x11, x12)
    return x9


def full_cycle_visible_4aab4007(
    grid: Grid,
    period: Integer,
) -> Boolean:
    x0 = set()
    for i, row in enumerate(grid):
        for j, value in enumerate(row):
            if value == ZERO or i < THREE or j < THREE:
                continue
            if i == FOUR and j == FOUR:
                x0.add(period - ONE)
                continue
            if i + j < NINE:
                continue
            x0.add((i + j - NINE) % period)
    return len(x0) == period
