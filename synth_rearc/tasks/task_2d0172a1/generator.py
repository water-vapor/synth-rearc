from synth_rearc.core import *

from .helpers import (
    ARCHETYPES_2D0172A1,
    COLOR_POOL_2D0172A1,
    MODES_2D0172A1,
    pad_binary_input_2d0172a1,
    recolor_binary_grid_2d0172a1,
    transform_binary_grid_2d0172a1,
)


def generate_2d0172a1(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    x0 = choice(ARCHETYPES_2D0172A1)
    x1 = choice(MODES_2D0172A1)
    x2 = choice(COLOR_POOL_2D0172A1)
    x3 = choice(tuple(x4 for x4 in COLOR_POOL_2D0172A1 if x4 != x2))
    x4 = transform_binary_grid_2d0172a1(x0.input_grid, x1)
    x5 = transform_binary_grid_2d0172a1(x0.output_grid, x1)
    x6 = height(x4)
    x7 = width(x4)
    x8 = max(x6, 20)
    x9 = max(x7, 16)
    x10 = unifint(diff_lb, diff_ub, (x8, 30))
    x11 = unifint(diff_lb, diff_ub, (x9, 30))
    x12 = unifint(diff_lb, diff_ub, (ZERO, x10 - x6))
    x13 = unifint(diff_lb, diff_ub, (ZERO, x11 - x7))
    x14 = x10 - x6 - x12
    x15 = x11 - x7 - x13
    x16 = pad_binary_input_2d0172a1(x4, x2, x3, x12, x13, x14, x15)
    x17 = recolor_binary_grid_2d0172a1(x5, x2, x3)
    return {"input": x16, "output": x17}
