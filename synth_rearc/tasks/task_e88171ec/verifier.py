from synth_rearc.core import *

from .helpers import largest_zero_rectangle_bounds_e88171ec, rectangle_interior_e88171ec


def verify_e88171ec(I: Grid) -> Grid:
    x0, x1 = largest_zero_rectangle_bounds_e88171ec(I)
    x2 = rectangle_interior_e88171ec(x0, x1)
    x3 = fill(I, EIGHT, x2)
    return x3
