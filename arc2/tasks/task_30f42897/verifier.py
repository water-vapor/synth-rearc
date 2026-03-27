from arc2.core import *

from .helpers import (
    border_lookup_30f42897,
    cyclic_run_start_30f42897,
    repeated_run_30f42897,
)


def verify_30f42897(I: Grid) -> Grid:
    x0 = mostcolor(I)
    x1 = other(palette(I), x0)
    x2 = shape(I)
    x3 = border_lookup_30f42897(x2)
    x4 = tuple(sorted(
        x3[x5]
        for x5 in ofcolor(I, x1)
        if x5 in x3
    ))
    if len(x4) == ZERO:
        return I
    x5 = cyclic_run_start_30f42897(x4, len(x3))
    x6 = repeated_run_30f42897(x2, x5, len(x4))
    x7 = fill(I, x1, x6)
    return x7
