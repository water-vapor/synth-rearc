from synth_rearc.core import *

from .helpers import transform_grid_de809cff


def verify_de809cff(
    I: Grid,
) -> Grid:
    x0 = I
    x1 = transform_grid_de809cff(x0)
    return x1
