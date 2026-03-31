from synth_rearc.core import *

from .helpers import solve_hidden_rectangles_a6f40cea


def verify_a6f40cea(
    I: Grid,
) -> Grid:
    x0 = solve_hidden_rectangles_a6f40cea(I)
    return x0
