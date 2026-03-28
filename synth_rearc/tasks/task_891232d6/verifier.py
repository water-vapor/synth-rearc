from synth_rearc.core import *


def _run_bounds_891232d6(
    grid: Grid,
    row: Integer,
    col: Integer,
) -> tuple[int, int]:
    x0 = width(grid)
    x1 = col
    while x1 > ZERO and grid[row][x1 - ONE] == SEVEN:
        x1 -= ONE
    x2 = col
    while x2 < x0 - ONE and grid[row][x2 + ONE] == SEVEN:
        x2 += ONE
    return (x1, x2)


def _trace_beam_891232d6(
    grid: Grid,
    output: list[list[int]],
    row: Integer,
    col: Integer,
) -> None:
    x0 = height(grid)
    x1 = width(grid)
    x2 = row
    x3 = col
    while ZERO <= x2 < x0 and ZERO <= x3 < x1:
        if x2 == ZERO:
            output[x2][x3] = SIX
            return
        if grid[x2 - ONE][x3] != SEVEN:
            output[x2][x3] = TWO
            x2 -= ONE
            continue
        x4 = x2 - ONE
        x5, x6 = _run_bounds_891232d6(grid, x4, x3)
        del x5
        x7 = x6 + ONE
        x8 = both(x7 < x1, all(grid[x2][x9] == ZERO for x9 in range(x3, x7 + ONE)))
        if x8:
            output[x4][x3] = EIGHT
            output[x2][x3] = FOUR
            for x9 in range(x3 + ONE, x6 + ONE):
                output[x2][x9] = TWO
            output[x2][x7] = THREE
            x2 = x4
            x3 = x7
            continue
        output[x2][x3] = SIX
        return


def verify_891232d6(I: Grid) -> Grid:
    x0 = [list(x1) for x1 in I]
    x1 = last(I)
    x2 = tuple(x3 for x3, x4 in enumerate(x1) if x4 == SIX)
    x3 = subtract(height(I), TWO)
    for x4 in x2:
        if x3 >= ZERO:
            _trace_beam_891232d6(I, x0, x3, x4)
    x5 = tuple(tuple(x6) for x6 in x0)
    return x5
