from synth_rearc.core import *

from .helpers import assemble_output_cbebaa4b


def verify_cbebaa4b(
    I: Grid,
) -> Grid:
    x0 = assemble_output_cbebaa4b(I)
    return x0
