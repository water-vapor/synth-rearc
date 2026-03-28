from synth_rearc.core import *

from .helpers import candidate_outputs_0934a4d8


def verify_0934a4d8(I: Grid) -> Grid:
    x0 = candidate_outputs_0934a4d8(I)
    x1 = mostcommon(x0)
    return x1
