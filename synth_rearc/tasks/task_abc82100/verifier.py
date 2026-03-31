from synth_rearc.core import *

from .helpers import render_output_abc82100


def verify_abc82100(
    I: Grid,
) -> Grid:
    x0 = render_output_abc82100(I)
    return x0
