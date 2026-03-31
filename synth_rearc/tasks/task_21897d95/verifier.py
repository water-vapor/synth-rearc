from synth_rearc.core import *

from .helpers import decode_clean_21897d95


def verify_21897d95(I: Grid) -> Grid:
    x0 = decode_clean_21897d95(I)
    x1 = dmirror(x0)
    return x1
