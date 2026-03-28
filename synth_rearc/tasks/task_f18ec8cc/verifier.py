from synth_rearc.core import *

from .helpers import concat_strips_f18ec8cc, split_vertical_strips_f18ec8cc


def verify_f18ec8cc(I: Grid) -> Grid:
    x0 = split_vertical_strips_f18ec8cc(I)
    x1 = x0[1:] + x0[:1]
    x2 = apply(last, x1)
    x3 = concat_strips_f18ec8cc(x2)
    return x3
