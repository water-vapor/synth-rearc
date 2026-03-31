from synth_rearc.core import *

from .helpers import (
    classify_object_142ca369,
    color_groups_142ca369,
    output_cells_for_group_142ca369,
    paint_group_cells_142ca369,
)


def verify_142ca369(I: Grid) -> Grid:
    x0 = canvas(ZERO, shape(I))
    x1 = color_groups_142ca369(I)
    for x3, x4 in x1:
        x5 = []
        for x6, x7 in x1:
            if x6 == x3:
                continue
            for x8 in x7:
                if classify_object_142ca369(x8)[0] == "L":
                    continue
                x5.append(toindices(x8))
        x9 = frozenset(merge(tuple(x5))) if x5 else frozenset()
        x10 = output_cells_for_group_142ca369(x4, shape(I), blockers=x9)
        x0 = paint_group_cells_142ca369(x0, x3, x10)
    return x0
