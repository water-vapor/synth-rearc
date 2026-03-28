from synth_rearc.core import *

from .helpers import (
    PATH_COLOR_3490CC26,
    SOURCE_COLOR_3490CC26,
    connector_indices_3490cc26,
    extract_blocks_3490cc26,
    next_visible_block_3490cc26,
)


def verify_3490cc26(I: Grid) -> Grid:
    x0 = extract_blocks_3490cc26(I)
    x1 = tuple(x2 for x2 in x0 if color(x2) == SOURCE_COLOR_3490CC26)
    x2 = first(x1)
    x3 = x2
    x4 = {x2}
    x5 = I
    while True:
        x6 = tuple(x7 for x7 in x0 if x7 not in x4)
        x7 = next_visible_block_3490cc26(x3, x6, x0)
        if x7 is None:
            break
        x8 = connector_indices_3490cc26(x3, x7)
        x5 = fill(x5, PATH_COLOR_3490CC26, x8)
        x4.add(x7)
        x3 = x7
    return x5
