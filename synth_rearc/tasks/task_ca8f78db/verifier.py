from synth_rearc.core import *

from .helpers import (
    is_pattern_row_ca8f78db,
    recover_cycle_ca8f78db,
    render_wallpaper_ca8f78db,
)


def verify_ca8f78db(
    I: Grid,
) -> Grid:
    x0 = height(I)
    x1 = tuple(x2 for x2 in range(x0) if is_pattern_row_ca8f78db(I[x2]))
    x2 = x1[ZERO] % TWO
    x3 = recover_cycle_ca8f78db(I, x1)
    x4 = render_wallpaper_ca8f78db(x3, x0, width(I), x2)
    return x4
