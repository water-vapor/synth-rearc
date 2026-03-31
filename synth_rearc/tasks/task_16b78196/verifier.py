from synth_rearc.core import *

from .helpers import render_output_16b78196


def verify_16b78196(
    I: Grid,
) -> Grid:
    x0 = render_output_16b78196(I)
    return x0
