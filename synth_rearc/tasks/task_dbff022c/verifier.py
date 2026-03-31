from synth_rearc.core import *

from .helpers import hole_indices_dbff022c
from .helpers import legend_cells_dbff022c
from .helpers import legend_mapping_dbff022c


def verify_dbff022c(
    I: Grid,
) -> Grid:
    x0 = mostcolor(I)
    x1 = legend_cells_dbff022c(I)
    x2 = dict(legend_mapping_dbff022c(I))
    x3 = fill(I, x0, x1)
    x4 = fgpartition(x3)
    x5 = I
    for x6 in x4:
        x7 = color(x6)
        if x7 not in x2:
            continue
        x8 = hole_indices_dbff022c(x6)
        if len(x8) == ZERO:
            continue
        x5 = fill(x5, x2[x7], x8)
    return x5
