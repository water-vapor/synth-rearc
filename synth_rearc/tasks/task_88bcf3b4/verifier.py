from synth_rearc.core import *

from .helpers import (
    chebyshev_distance_88bcf3b4,
    component_inventory_88bcf3b4,
    line_like_88bcf3b4,
    neighbors4_88bcf3b4,
    rerouted_path_88bcf3b4,
)


def verify_88bcf3b4(
    I: Grid,
) -> Grid:
    x0 = mostcolor(I)
    x1 = component_inventory_88bcf3b4(I)
    x2 = I
    x3 = set()
    for x4, _, x5 in x1:
        if not line_like_88bcf3b4(x5):
            continue
        for x6, x7, x8 in x1:
            if x6 == x4 or x6 in x3 or line_like_88bcf3b4(x8):
                continue
            x9 = tuple(
                (x10, x11)
                for x10 in x8
                for x11 in neighbors4_88bcf3b4(x10)
                if x11 in x5
            )
            if len(x9) == ZERO:
                continue
            x10 = None
            for x11, x12 in x9:
                for x13, _, x14 in x1:
                    if x13 in (x4, x6):
                        continue
                    x15 = (
                        chebyshev_distance_88bcf3b4(x11, x14),
                        len(x14),
                        x11,
                        x12,
                        x13,
                    )
                    if x10 is None or x15 < x10:
                        x10 = x15
            if x10 is None:
                continue
            _, _, x16, x17, x18 = x10
            x19 = x1[x18][2]
            x20 = (x17[0] - x16[0], x17[1] - x16[1])
            x21 = rerouted_path_88bcf3b4(x16, x19, len(x8), x20)
            x2 = fill(x2, x0, x8)
            x2 = fill(x2, x7, frozenset(x21))
            x3.add(x6)
    return x2
