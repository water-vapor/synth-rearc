from synth_rearc.core import *

from .helpers import motif_to_color_009d5c81


def verify_009d5c81(I: Grid) -> Grid:
    x0 = objects(I, T, T, T)
    x1 = colorfilter(x0, ONE)
    x2 = first(x1)
    x3 = subgrid(x2, I)
    x4 = motif_to_color_009d5c81(x3)
    x5 = replace(I, EIGHT, x4)
    x6 = cover(x5, x2)
    return x6
