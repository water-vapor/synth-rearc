from arc2.core import *


def _fill_column_5207a7b5(
    grid: Grid,
    value: int,
    column: int,
    column_height: int,
) -> Grid:
    x0 = frozenset((i, column) for i in range(column_height))
    return fill(grid, value, x0)


def _render_output_5207a7b5(
    grid_height: int,
    grid_width: int,
    bar_column: int,
    bar_height: int,
) -> Grid:
    x0 = canvas(ZERO, (grid_height, grid_width))
    x1 = frozenset((i, bar_column) for i in range(bar_height))
    x2 = fill(x0, FIVE, x1)
    for x3 in range(ONE, add(bar_column, ONE)):
        x4 = subtract(bar_column, x3)
        x5 = min(grid_height, add(bar_height, multiply(TWO, x3)))
        x2 = _fill_column_5207a7b5(x2, EIGHT, x4, x5)
    for x6 in range(ONE, subtract(grid_width, bar_column)):
        x7 = subtract(bar_height, multiply(TWO, x6))
        if x7 <= ZERO:
            break
        x8 = add(bar_column, x6)
        x2 = _fill_column_5207a7b5(x2, SIX, x8, x7)
    return x2


def generate_5207a7b5(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    x0 = unifint(diff_lb, diff_ub, (FOUR, TEN))
    x1 = unifint(diff_lb, diff_ub, (TWO, EIGHT))
    x2 = unifint(diff_lb, diff_ub, (THREE, EIGHT))
    x3 = unifint(diff_lb, diff_ub, (NEG_ONE, THREE))
    x4 = add(add(x0, multiply(TWO, x1)), x3)
    x5 = add(add(x1, x2), ONE)
    x6 = canvas(ZERO, (x4, x5))
    x7 = frozenset((i, x1) for i in range(x0))
    x8 = fill(x6, FIVE, x7)
    x9 = _render_output_5207a7b5(x4, x5, x1, x0)
    return {"input": x8, "output": x9}
