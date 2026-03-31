from synth_rearc.core import *

from .helpers import component_cells_13e47133, component_cycle_13e47133, rectangle_depths_13e47133, wall_color_13e47133


def verify_13e47133(
    I: Grid,
) -> Grid:
    x0 = wall_color_13e47133(I)
    x1 = [list(row) for row in I]
    x2 = component_cells_13e47133(I, x0)
    for x3 in x2:
        x4 = component_cycle_13e47133(I, x3)
        x5 = rectangle_depths_13e47133(x3)
        for x6, x7 in x5.items():
            i, j = x6
            x1[i][j] = x4[x7 % len(x4)]
    x8 = tuple(tuple(row) for row in x1)
    return x8
