from arc2.core import *


GRID_SIZE_996EC1F3 = 19


def _non_separator_colors_996ec1f3(separator: Integer) -> Tuple:
    return tuple(value for value in interval(ZERO, TEN, ONE) if value != separator)


def _render_output_996ec1f3(
    ul: Integer,
    separator: Integer,
    ur: Integer,
    ll: Integer,
    lr: Integer,
) -> Grid:
    x0 = canvas(separator, THREE_BY_THREE)
    x1 = fill(x0, ul, initset(ORIGIN))
    x2 = fill(x1, ur, initset(ZERO_BY_TWO))
    x3 = fill(x2, ll, initset(TWO_BY_ZERO))
    x4 = fill(x3, lr, initset(TWO_BY_TWO))
    return x4


def _quadrant_majorities_996ec1f3(
    grid: Grid,
    row: Integer,
    col: Integer,
) -> Tuple:
    x0 = increment(col)
    x1 = subtract(width(grid), x0)
    x2 = increment(row)
    x3 = subtract(height(grid), x2)
    x4 = crop(grid, ORIGIN, astuple(row, col))
    x5 = crop(grid, astuple(ZERO, x0), astuple(row, x1))
    x6 = crop(grid, astuple(x2, ZERO), astuple(x3, col))
    x7 = crop(grid, astuple(x2, x0), astuple(x3, x1))
    return (
        mostcolor(x4),
        mostcolor(x5),
        mostcolor(x6),
        mostcolor(x7),
    )


def generate_996ec1f3(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    x0 = decrement(GRID_SIZE_996EC1F3)
    while True:
        x1 = choice(interval(ZERO, TEN, ONE))
        x2 = _non_separator_colors_996ec1f3(x1)
        x3, x4, x5, x6 = sample(x2, FOUR)
        x7 = unifint(diff_lb, diff_ub, (SIX, 11))
        x8 = unifint(diff_lb, diff_ub, (SIX, TEN))
        x9 = tuple(
            tuple(choice(x2) for _ in range(GRID_SIZE_996EC1F3))
            for _ in range(GRID_SIZE_996EC1F3)
        )
        x10 = fill(x9, x1, hfrontier(astuple(x7, ZERO)))
        x11 = fill(x10, x1, vfrontier(astuple(ZERO, x8)))
        x12 = interval(ONE, decrement(x7), ONE)
        x13 = interval(ONE, decrement(x8), ONE)
        x14 = product(x12, x13)
        x15 = fill(x11, x3, x14)
        x16 = interval(add(x8, TWO), x0, ONE)
        x17 = product(x12, x16)
        x18 = fill(x15, x4, x17)
        x19 = interval(add(x7, TWO), x0, ONE)
        x20 = product(x19, x13)
        x21 = fill(x18, x5, x20)
        x22 = product(x19, x16)
        x23 = fill(x21, x6, x22)
        x24 = _quadrant_majorities_996ec1f3(x23, x7, x8)
        x25 = (x3, x4, x5, x6)
        if x24 != x25:
            continue
        x26 = _render_output_996ec1f3(x3, x1, x4, x5, x6)
        return {"input": x23, "output": x26}
