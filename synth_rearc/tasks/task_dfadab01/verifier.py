from synth_rearc.core import *

from .helpers import assemble_output_dfadab01


def verify_dfadab01(
    I: Grid,
) -> Grid:
    x0 = assemble_output_dfadab01(I)
    return x0
