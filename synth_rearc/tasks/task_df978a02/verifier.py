from synth_rearc.core import *

from .helpers import (
    cap_patch_df978a02,
    direction_df978a02,
    foreground_focus_df978a02,
    tip_cell_df978a02,
)


def verify_df978a02(
    I: Grid,
) -> Grid:
    x0 = mostcolor(I)
    x1 = objects(I, T, T, T)
    x2 = foreground_focus_df978a02(x1)
    x3 = argmax(x1, size)
    x4 = I
    for x5 in x1:
        x6 = direction_df978a02(x5, x2)
        if x5 == x3:
            x7 = cap_patch_df978a02(x5, x6)
            x4 = fill(x4, color(x5), x7)
        else:
            x7 = tip_cell_df978a02(x5, x6)
            x8 = frozenset({x7})
            x4 = fill(x4, x0, x8)
    return x4
