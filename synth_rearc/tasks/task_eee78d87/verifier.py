from synth_rearc.core import *

from .helpers import pattern_bits_from_stencil_eee78d87, render_output_from_bits_eee78d87


def verify_eee78d87(
    I: Grid,
) -> Grid:
    x0 = mostcolor(I)
    x1 = palette(I)
    x2 = other(x1, x0)
    x3 = ofcolor(I, x2)
    x4 = ulcorner(x3)
    x5 = crop(I, x4, (THREE, THREE))
    x6 = pattern_bits_from_stencil_eee78d87(x5, x0)
    x7 = render_output_from_bits_eee78d87(x6, x0)
    return x7
