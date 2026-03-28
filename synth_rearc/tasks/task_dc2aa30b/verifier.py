from synth_rearc.core import *

from .helpers import assemble_tiles_dc2aa30b, split_tiles_dc2aa30b


def verify_dc2aa30b(I: Grid) -> Grid:
    x0 = split_tiles_dc2aa30b(I)
    x1 = rbind(colorcount, TWO)
    x2 = order(x0, x1)
    x3 = (
        x2[TWO],
        x2[ONE],
        x2[ZERO],
        x2[FIVE],
        x2[FOUR],
        x2[THREE],
        x2[EIGHT],
        x2[SEVEN],
        x2[SIX],
    )
    x4 = assemble_tiles_dc2aa30b(x3)
    return x4
