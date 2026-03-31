from synth_rearc.core import *

from .verifier import verify_929ab4e9


GRID_SIZE_929AB4E9 = 24
HALF_SIZE_929AB4E9 = 12
AVAILABLE_COLORS_929AB4E9 = tuple(remove(TWO, remove(ZERO, interval(ZERO, TEN, ONE))))
PATTERN_MODES_929AB4E9 = ("rings", "bands", "mix", "plaid")


def _symmetrize_quadrant_929ab4e9(
    grid: list[list[int]],
) -> Grid:
    for i in range(HALF_SIZE_929AB4E9):
        for j in range(i):
            grid[i][j] = grid[j][i]
    return tuple(tuple(row) for row in grid)


def _base_quadrant_929ab4e9(
    colors: tuple[int, ...],
    diff_lb: float,
    diff_ub: float,
) -> list[list[int]]:
    x0 = choice(PATTERN_MODES_929AB4E9)
    x1 = unifint(diff_lb, diff_ub, (ONE, FOUR))
    x2 = unifint(diff_lb, diff_ub, (ONE, FOUR))
    x3 = unifint(diff_lb, diff_ub, (ONE, FOUR))
    x4 = unifint(diff_lb, diff_ub, (ONE, FOUR))
    x5 = randint(ZERO, len(colors) - ONE)
    x6: list[list[int]] = []
    for i in range(HALF_SIZE_929AB4E9):
        x7 = []
        for j in range(HALF_SIZE_929AB4E9):
            x8 = max(i, j) // x1
            x9 = min(i, j) // x2
            x10 = abs(i - j) // x3
            x11 = (i + j) // x4
            if x0 == "rings":
                x12 = x5 + x8 + x10 + x11
            elif x0 == "bands":
                x12 = x5 + x8 + x9 + x10
            elif x0 == "plaid":
                x12 = x5 + x8 + x11 + (i % TWO) + (j % TWO)
            else:
                x12 = x5 + x8 + x9 + x10 + x11
            x13 = colors[x12 % len(colors)]
            x7.append(x13)
        x6.append(x7)
    return x6


def _decorate_quadrant_929ab4e9(
    grid: list[list[int]],
    colors: tuple[int, ...],
    diff_lb: float,
    diff_ub: float,
) -> Grid:
    x0 = unifint(diff_lb, diff_ub, (THREE, SIX))
    for _ in range(x0):
        x1 = choice(colors)
        x2 = choice(("rect", "diag", "box", "line"))
        if x2 == "rect":
            x3 = randint(ZERO, HALF_SIZE_929AB4E9 - THREE)
            x4 = randint(x3, HALF_SIZE_929AB4E9 - THREE)
            x5 = randint(ONE, min(FOUR, HALF_SIZE_929AB4E9 - x3))
            x6 = randint(ONE, min(FOUR, HALF_SIZE_929AB4E9 - x4))
            for i in range(x3, x3 + x5):
                for j in range(x4, x4 + x6):
                    grid[i][j] = x1
                    grid[j][i] = x1
        elif x2 == "diag":
            x3 = randint(ZERO, HALF_SIZE_929AB4E9 - TWO)
            x4 = randint(x3, min(HALF_SIZE_929AB4E9 - ONE, x3 + THREE))
            for i in range(HALF_SIZE_929AB4E9):
                for j in range(HALF_SIZE_929AB4E9):
                    if x3 <= abs(i - j) <= x4:
                        grid[i][j] = x1
        elif x2 == "box":
            x3 = randint(ZERO, HALF_SIZE_929AB4E9 - THREE)
            x4 = randint(x3 + ONE, HALF_SIZE_929AB4E9 - ONE)
            for i in range(x3, x4 + ONE):
                grid[x3][i] = x1
                grid[x4][i] = x1
                grid[i][x3] = x1
                grid[i][x4] = x1
        else:
            x3 = randint(ZERO, HALF_SIZE_929AB4E9 - ONE)
            for i in range(HALF_SIZE_929AB4E9):
                grid[x3][i] = x1
                grid[i][x3] = x1
    return _symmetrize_quadrant_929ab4e9(grid)


def _assemble_output_929ab4e9(
    quadrant: Grid,
) -> Grid:
    x0 = vmirror(quadrant)
    x1 = hconcat(quadrant, x0)
    x2 = hmirror(x1)
    x3 = vconcat(x1, x2)
    return x3


def _good_output_929ab4e9(
    grid: Grid,
) -> bool:
    x0 = len(set(grid))
    x1 = len(set(zip(*grid)))
    x2 = numcolors(grid)
    return x0 >= SIX and x1 >= SIX and x2 >= FOUR


def _paint_mask_929ab4e9(
    grid: Grid,
    mask: set[tuple[int, int]],
) -> Grid:
    x0 = [list(row) for row in grid]
    for i, j in mask:
        x0[i][j] = TWO
    return tuple(tuple(row) for row in x0)


def _sample_input_929ab4e9(
    output: Grid,
    diff_lb: float,
    diff_ub: float,
) -> Grid:
    for _ in range(400):
        x0 = unifint(diff_lb, diff_ub, (TWO, SIX))
        x1 = unifint(diff_lb, diff_ub, (TWO, SIX))
        x2 = randint(ZERO, GRID_SIZE_929AB4E9 - x0)
        x3 = randint(ZERO, GRID_SIZE_929AB4E9 - x1)
        x4 = {(i, j) for i in range(x2, x2 + x0) for j in range(x3, x3 + x1)}
        x5 = unifint(diff_lb, diff_ub, (ONE, THREE))
        for _ in range(x5):
            x6 = choice(tuple(x4))
            x7 = unifint(diff_lb, diff_ub, (ONE, FIVE))
            x8 = unifint(diff_lb, diff_ub, (ONE, FIVE))
            x9 = x6[0] - randint(ZERO, x7 - ONE)
            x10 = x6[1] - randint(ZERO, x8 - ONE)
            x11 = {
                (i, j)
                for i in range(x9, x9 + x7)
                for j in range(x10, x10 + x8)
                if 0 <= i < GRID_SIZE_929AB4E9 and 0 <= j < GRID_SIZE_929AB4E9
            }
            x4 |= x11
        x12 = len(x4)
        if x12 < 16 or x12 > 100:
            continue
        x13 = _paint_mask_929ab4e9(output, x4)
        if verify_929ab4e9(x13) != output:
            continue
        return x13
    raise RuntimeError("failed to sample a recoverable corruption mask for 929ab4e9")


def generate_929ab4e9(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = unifint(diff_lb, diff_ub, (FOUR, SIX))
        x1 = tuple(sample(AVAILABLE_COLORS_929AB4E9, x0))
        x2 = _base_quadrant_929ab4e9(x1, diff_lb, diff_ub)
        x3 = _decorate_quadrant_929ab4e9(x2, x1, diff_lb, diff_ub)
        go = _assemble_output_929ab4e9(x3)
        if not _good_output_929ab4e9(go):
            continue
        gi = _sample_input_929ab4e9(go, diff_lb, diff_ub)
        return {"input": gi, "output": go}
