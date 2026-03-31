from synth_rearc.core import *

from .helpers import extract_tiles_b5ca7ac4, pack_tiles_b5ca7ac4, render_tiles_b5ca7ac4


def verify_b5ca7ac4(I: Grid) -> Grid:
    x0 = mostcolor(I)
    x1 = extract_tiles_b5ca7ac4(I)
    x2 = pack_tiles_b5ca7ac4(x1, len(I[ZERO]))
    x3 = render_tiles_b5ca7ac4(x0, x2, shape(I))
    return x3
