from synth_rearc.core import *

from .helpers import transform_grid_dd6b8c4b


def verify_dd6b8c4b(
    I: Grid,
) -> Grid:
    x0 = transform_grid_dd6b8c4b(I)
    return x0
