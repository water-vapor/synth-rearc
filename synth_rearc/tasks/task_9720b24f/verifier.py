from synth_rearc.core import *

from .helpers import intruder_indices_9720b24f


def verify_9720b24f(I: Grid) -> Grid:
    x0 = intruder_indices_9720b24f(I)
    x1 = fill(I, ZERO, x0)
    return x1
