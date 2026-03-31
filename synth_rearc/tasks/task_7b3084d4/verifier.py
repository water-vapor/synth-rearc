from synth_rearc.core import *

from .helpers import synthesize_output_7b3084d4


def verify_7b3084d4(I: Grid) -> Grid:
    x0 = synthesize_output_7b3084d4(I)
    return x0
