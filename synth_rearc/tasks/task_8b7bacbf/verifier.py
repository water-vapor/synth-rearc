from synth_rearc.core import *

from .helpers import transform_grid_8b7bacbf


def verify_8b7bacbf(I: Grid) -> Grid:
    x0 = I
    x1 = transform_grid_8b7bacbf(x0)
    return x1
