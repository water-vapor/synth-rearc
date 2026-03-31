from synth_rearc.core import *

from .helpers import transform_grid_271d71e2


def verify_271d71e2(I: Grid) -> Grid:
    x0 = I
    x1 = transform_grid_271d71e2(x0)
    return x1
