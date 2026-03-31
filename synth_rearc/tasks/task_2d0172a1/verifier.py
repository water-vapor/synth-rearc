from synth_rearc.core import *

from .helpers import reconstruct_picture_2d0172a1


def verify_2d0172a1(
    I: Grid,
) -> Grid:
    x0 = reconstruct_picture_2d0172a1(I)
    return x0
