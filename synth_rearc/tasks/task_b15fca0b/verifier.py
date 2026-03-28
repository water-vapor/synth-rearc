from synth_rearc.core import *

from .helpers import passable_cells_b15fca0b, shortest_path_union_cells_b15fca0b


def verify_b15fca0b(
    I: Grid,
) -> Grid:
    x0 = tuple(sorted(ofcolor(I, TWO)))
    x1 = x0[ZERO]
    x2 = x0[ONE]
    x3 = passable_cells_b15fca0b(I)
    x4 = ofcolor(I, ZERO)
    x5 = shape(I)
    x6, _ = shortest_path_union_cells_b15fca0b(x3, x4, x1, x2, x5)
    x7 = fill(I, FOUR, x6)
    return x7
