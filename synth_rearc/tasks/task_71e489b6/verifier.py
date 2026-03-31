from synth_rearc.core import *

from .helpers import halo_cells_71e489b6
from .helpers import selected_one_cells_71e489b6
from .helpers import selected_zero_cells_71e489b6


def verify_71e489b6(
    I: Grid,
) -> Grid:
    x0 = selected_zero_cells_71e489b6(I)
    x1 = halo_cells_71e489b6(x0, shape(I))
    x2 = selected_one_cells_71e489b6(I, x1)
    x3 = fill(I, ZERO, x2)
    x4 = fill(x3, SEVEN, x1)
    x5 = fill(x4, ZERO, x0)
    return x5
