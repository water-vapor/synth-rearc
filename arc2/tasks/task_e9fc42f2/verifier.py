from arc2.core import *

from .helpers import assemble_tiles_e9fc42f2


def verify_e9fc42f2(I: Grid) -> Grid:
    x0 = objects(I, F, F, T)
    x1 = tuple(
        sorted(
            x0,
            key=lambda x2: (uppermost(x2), leftmost(x2), height(x2), width(x2)),
        )
    )
    x3 = tuple(subgrid(x4, I) for x4 in x1)
    x5 = assemble_tiles_e9fc42f2(x3)
    return x5
