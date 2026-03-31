from synth_rearc.core import *

from .helpers import extension_patch_3dc255db
from .helpers import pointing_endpoint_3dc255db
from .helpers import _major_minor_patches_3dc255db


def verify_3dc255db(
    I: Grid,
) -> Grid:
    x0 = objects(I, F, T, T)
    x1 = I
    for x2 in x0:
        x3 = numcolors(x2)
        if flip(equality(x3, TWO)):
            continue
        x4, x5, x6, x7 = _major_minor_patches_3dc255db(x2)
        x8, x9 = pointing_endpoint_3dc255db(x6)
        x10 = extension_patch_3dc255db(x9, x8, len(x7))
        x1 = fill(x1, ZERO, x7)
        x1 = fill(x1, x5, x10)
    return x1
