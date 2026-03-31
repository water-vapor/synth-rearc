from synth_rearc.core import *

from .helpers import transform_grid_b6f77b65


def verify_b6f77b65(
    I: Grid,
) -> Grid:
    x0 = transform_grid_b6f77b65(I)
    return x0
