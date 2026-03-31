from synth_rearc.core import *

from .helpers import infer_cross_center_k_da515329, render_output_da515329


def verify_da515329(
    I: Grid,
) -> Grid:
    x0 = shape(I)
    x1 = infer_cross_center_k_da515329(I)
    x2 = x1[ZERO]
    x3 = x1[ONE]
    x4 = render_output_da515329(x0, x2, x3)
    return x4
