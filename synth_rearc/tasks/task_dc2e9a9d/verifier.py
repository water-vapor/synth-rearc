from synth_rearc.core import *

from .helpers import mirrored_copy_dc2e9a9d


def verify_dc2e9a9d(I: Grid) -> Grid:
    x0 = objects(I, T, F, T)
    x1 = I
    for x2 in x0:
        x3 = mirrored_copy_dc2e9a9d(x2)
        x1 = paint(x1, x3)
    return x1
