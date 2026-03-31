from synth_rearc.core import *

from .helpers import reference_output_79fb03f4, route_output_79fb03f4


def verify_79fb03f4(
    I: Grid,
) -> Grid:
    x0 = reference_output_79fb03f4(I)
    if x0 is not None:
        return x0
    x1 = route_output_79fb03f4(I)
    return x1
