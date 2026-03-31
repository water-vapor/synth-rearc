from synth_rearc.core import *

from .helpers import selected_stems_97d7923e
from .helpers import stem_body_patch_97d7923e


def verify_97d7923e(
    I: Grid,
) -> Grid:
    x0 = selected_stems_97d7923e(I)
    x1 = I
    x2 = height(I)
    for x3 in x0:
        x4 = stem_body_patch_97d7923e(x3, x2)
        x1 = fill(x1, x3[ZERO], x4)
    return x1
