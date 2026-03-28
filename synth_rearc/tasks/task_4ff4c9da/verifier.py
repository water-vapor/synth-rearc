from synth_rearc.core import *

from .helpers import (
    _col_bands_4ff4c9da,
    _row_bands_4ff4c9da,
    _tile_signature_4ff4c9da,
)


def verify_4ff4c9da(I: Grid) -> Grid:
    x0 = mostcolor(I)
    x1 = _row_bands_4ff4c9da(I)
    x2 = _col_bands_4ff4c9da(I)
    x3 = frozenset()
    x4 = []
    for x5, x6 in x1:
        for x7, x8 in x2:
            x9 = crop(I, (x5, x7), (x6 - x5, x8 - x7))
            x10, x11, x12 = _tile_signature_4ff4c9da(x9, x0)
            if len(x10) > ZERO:
                x3 = combine(x3, initset(x10))
            x4.append(((x5, x7), x11, x12))
    x13 = I
    for x14, x15, x16 in x4:
        if len(x15) == ZERO:
            continue
        if x16 not in x3:
            continue
        x17 = shift(x15, x14)
        x13 = fill(x13, EIGHT, x17)
    return x13
