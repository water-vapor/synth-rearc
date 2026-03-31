from synth_rearc.core import *

from .helpers import bar_patch_cb2d8a2c, trace_path_cb2d8a2c


def verify_cb2d8a2c(
    I: Grid,
) -> Grid:
    x0 = bar_patch_cb2d8a2c(I)
    x1 = trace_path_cb2d8a2c(I)
    x2 = fill(I, TWO, x0)
    x3 = fill(x2, THREE, x1)
    return x3
