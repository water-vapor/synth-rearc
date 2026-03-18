from arc2.core import *


def _rect_patch_fd4b2b02(
    top: int,
    left: int,
    height_: int,
    width_: int,
):
    x0 = interval(top, add(top, height_), ONE)
    x1 = interval(left, add(left, width_), ONE)
    return product(x0, x1)


def _extend_ray_fd4b2b02(
    grid: Grid,
    top: int,
    left: int,
    height_: int,
    width_: int,
    color_: int,
    row_dir: int,
    col_dir: int,
    n_steps: int,
) -> Grid:
    x0 = grid
    x1 = top
    x2 = left
    x3 = height_
    x4 = width_
    x5 = color_
    for _ in range(n_steps):
        x1 = subtract(x1, x4) if row_dir == -ONE else add(x1, x3)
        x2 = subtract(x2, x3) if col_dir == -ONE else add(x2, x4)
        x3, x4 = x4, x3
        x5 = other((THREE, SIX), x5)
        x6 = _rect_patch_fd4b2b02(x1, x2, x3, x4)
        x0 = fill(x0, x5, x6)
    return x0


def _paint_pattern_fd4b2b02(
    grid: Grid,
    top: int,
    left: int,
    height_: int,
    width_: int,
    color_: int,
) -> Grid:
    x0 = add(height(grid), width(grid))
    x1 = _extend_ray_fd4b2b02(grid, top, left, height_, width_, color_, -ONE, -ONE, x0)
    x2 = _extend_ray_fd4b2b02(x1, top, left, height_, width_, color_, -ONE, ONE, x0)
    x3 = _extend_ray_fd4b2b02(x2, top, left, height_, width_, color_, ONE, -ONE, x0)
    x4 = _extend_ray_fd4b2b02(x3, top, left, height_, width_, color_, ONE, ONE, x0)
    return x4


def generate_fd4b2b02(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = unifint(diff_lb, diff_ub, (16, 26))
        x1 = choice((ONE, TWO))
        x2 = TWO if x1 == ONE else THREE
        x3 = unifint(diff_lb, diff_ub, (x2, FIVE))
        x4 = choice((T, F))
        x5 = x3 if x4 else x1
        x6 = x1 if x4 else x3
        x7 = choice((THREE, SIX))
        x8 = canvas(ZERO, (x0, x0))
        x9 = unifint(diff_lb, diff_ub, (ONE, subtract(subtract(x0, x5), ONE)))
        x10 = unifint(diff_lb, diff_ub, (ONE, subtract(subtract(x0, x6), ONE)))
        x11 = _rect_patch_fd4b2b02(x9, x10, x5, x6)
        x12 = fill(x8, x7, x11)
        x13 = _paint_pattern_fd4b2b02(x12, x9, x10, x5, x6, x7)
        x14 = add(colorcount(x13, THREE), colorcount(x13, SIX))
        x15 = multiply(x14, 100)
        x16 = multiply(x0, x0)
        x17 = greater(x15, multiply(x16, 10))
        x18 = greater(multiply(x16, 22), x15)
        x19 = both(greater(colorcount(x13, THREE), ZERO), greater(colorcount(x13, SIX), ZERO))
        x20 = both(x17, x18)
        if both(x19, x20):
            return {"input": x12, "output": x13}
