from synth_rearc.core import *

from .helpers import legend_cells_9385bd28
from .helpers import legend_mapping_9385bd28


def verify_9385bd28(
    I: Grid,
) -> Grid:
    x0 = dict(legend_mapping_9385bd28(I))
    x1 = mostcolor(I)
    x2 = legend_cells_9385bd28(I)
    x3 = fill(I, x1, x2)
    x4 = objects(x3, T, F, T)
    x5 = {}
    for x6 in x4:
        x7 = color(x6)
        x8 = toindices(x6)
        if x7 not in x5:
            x5[x7] = []
        x5[x7].append(x8)
    x9 = tuple(
        sorted(
            (
                (
                    x10,
                    frozenset(index for x12 in x11 for index in x12),
                    tuple(x11),
                    x0[x10] if x10 in x0 else "missing",
                )
                for x10, x11 in x5.items()
            ),
            key=lambda item: (size(backdrop(item[1])), item[0]),
        )
    )
    x12 = I
    for _, x13, _, x14 in x9:
        if x14 == ZERO:
            x12 = fill(x12, x1, x13)
    for x13, x14, x15, x16 in x9:
        if either(x16 is None, either(x16 == ZERO, x16 == "missing")):
            continue
        x17 = backdrop(x14)
        if either(x16 == x13, x14 == x17):
            x12 = fill(x12, x16, x17)
        else:
            x18 = tuple(
                intersection(x17, backdrop(x19))
                for x18, x19, x20, x21 in x9
                if both(
                    x18 != x13,
                    both(
                        x21 is None,
                        any(len(intersection(x17, x22)) > ZERO for x22 in x20),
                    ),
                )
            )
            x19 = difference(x17, merge(x18)) if len(x18) > ZERO else x17
            x12 = underfill(x12, x16, x19)
    return x12
