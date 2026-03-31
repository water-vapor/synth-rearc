from synth_rearc.core import *

from .helpers import pair_color_a47bf94d
from .helpers import paint_port_symbol_a47bf94d
from .helpers import port_pairs_a47bf94d
from .helpers import strip_payload_a47bf94d


def verify_a47bf94d(
    I: Grid,
) -> Grid:
    x0 = strip_payload_a47bf94d(I)
    x1 = port_pairs_a47bf94d(I)
    for x2 in x1:
        x3 = pair_color_a47bf94d(I, x2)
        if x3 == ZERO:
            continue
        x4, x5 = x2
        x6, x7 = x4
        x8, x9 = x5
        x0 = paint_port_symbol_a47bf94d(x0, x3, x6, x7)
        x0 = paint_port_symbol_a47bf94d(x0, x3, x8, x9)
    return x0
