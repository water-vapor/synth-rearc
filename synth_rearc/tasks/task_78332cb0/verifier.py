from synth_rearc.core import *

from .helpers import _assemble_output_78332cb0, _split_panels_78332cb0


def verify_78332cb0(
    I: Grid,
) -> Grid:
    x0 = _split_panels_78332cb0(I)
    x1 = _assemble_output_78332cb0(x0)
    return x1
