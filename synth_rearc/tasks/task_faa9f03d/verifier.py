from synth_rearc.core import *

from .helpers import solve_faa9f03d


def verify_faa9f03d(
    I: Grid,
) -> Grid:
    x0 = solve_faa9f03d(I)
    return x0
