from synth_rearc.core import *

from .verifier import verify_5e6bbc0b


DIM_BOUNDS_5E6BBC0B = (THREE, 18)


def _checkerboard_5e6bbc0b(
    h: Integer,
    w: Integer,
    start: Integer,
) -> Grid:
    return tuple(tuple((start + i + j) % TWO for j in range(w)) for i in range(h))


def _rowwise_output_5e6bbc0b(
    grid: Grid,
    row: Integer,
    left: Boolean,
) -> Grid:
    x0 = height(grid)
    x1 = width(grid)
    x2 = canvas(ZERO, (x0, x1))
    for x3 in range(x0):
        x4 = sum(ONE for x5 in range(x1) if grid[x3][x5] != ZERO)
        x6 = (
            frozenset((x3, x5) for x5 in range(x4))
            if left
            else frozenset((x3, x5) for x5 in range(x1 - x4, x1))
        )
        x2 = fill(x2, ONE, x6)
    x7 = sum(ONE for x8 in range(x1) if grid[row][x8] != ZERO)
    x9 = (
        frozenset((row, x8) for x8 in range(x7, x7 + x7 - ONE))
        if left
        else frozenset((row, x8) for x8 in range(x1 - x7 - x7 + ONE, x1 - x7))
    )
    x10 = (row, ZERO) if left else (row, x1 - ONE)
    x2 = fill(x2, NINE, x9)
    x2 = fill(x2, EIGHT, frozenset({x10}))
    return x2


def _colwise_output_5e6bbc0b(
    grid: Grid,
    col: Integer,
    top: Boolean,
) -> Grid:
    x0 = height(grid)
    x1 = width(grid)
    x2 = canvas(ZERO, (x0, x1))
    for x3 in range(x1):
        x4 = sum(ONE for x5 in range(x0) if grid[x5][x3] != ZERO)
        x6 = (
            frozenset((x5, x3) for x5 in range(x4))
            if top
            else frozenset((x5, x3) for x5 in range(x0 - x4, x0))
        )
        x2 = fill(x2, ONE, x6)
    x7 = sum(ONE for x8 in range(x0) if grid[x8][col] != ZERO)
    x9 = (
        frozenset((x8, col) for x8 in range(x7, x7 + x7 - ONE))
        if top
        else frozenset((x8, col) for x8 in range(x0 - x7 - x7 + ONE, x0 - x7))
    )
    x10 = (ZERO, col) if top else (x0 - ONE, col)
    x2 = fill(x2, NINE, x9)
    x2 = fill(x2, EIGHT, frozenset({x10}))
    return x2


def generate_5e6bbc0b(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while T:
        x0 = choice((T, F))
        x1 = unifint(diff_lb, diff_ub, DIM_BOUNDS_5E6BBC0B)
        x2 = unifint(diff_lb, diff_ub, DIM_BOUNDS_5E6BBC0B)
        if x0:
            x3 = randint(ONE, x1 - TWO)
            x4 = choice((ZERO, x2 - ONE))
            x5 = ONE if (x3 + x4) % TWO == ZERO else ZERO
            gi = _checkerboard_5e6bbc0b(x1, x2, x5)
            gi = fill(gi, EIGHT, frozenset({(x3, x4)}))
            go = _rowwise_output_5e6bbc0b(gi, x3, equality(x4, ZERO))
        else:
            x3 = choice((ZERO, x1 - ONE))
            x4 = randint(ONE, x2 - TWO)
            x5 = ONE if (x3 + x4) % TWO == ZERO else ZERO
            gi = _checkerboard_5e6bbc0b(x1, x2, x5)
            gi = fill(gi, EIGHT, frozenset({(x3, x4)}))
            go = _colwise_output_5e6bbc0b(gi, x4, equality(x3, ZERO))
        if verify_5e6bbc0b(gi) != go:
            continue
        return {"input": gi, "output": go}
