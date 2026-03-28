from synth_rearc.core import *


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


def verify_fd4b2b02(I: Grid) -> Grid:
    x0 = objects(I, T, F, T)
    x1 = first(x0)
    x2 = uppermost(x1)
    x3 = leftmost(x1)
    x4 = height(x1)
    x5 = width(x1)
    x6 = color(x1)
    x7 = add(height(I), width(I))
    x8 = _extend_ray_fd4b2b02(I, x2, x3, x4, x5, x6, -ONE, -ONE, x7)
    x9 = _extend_ray_fd4b2b02(x8, x2, x3, x4, x5, x6, -ONE, ONE, x7)
    x10 = _extend_ray_fd4b2b02(x9, x2, x3, x4, x5, x6, ONE, -ONE, x7)
    x11 = _extend_ray_fd4b2b02(x10, x2, x3, x4, x5, x6, ONE, ONE, x7)
    return x11
