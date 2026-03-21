from arc2.core import *

from .helpers import render_templates_98c475bf


def verify_98c475bf(I: Grid) -> Grid:
    x0 = shape(I)
    x1 = canvas(ZERO, x0)
    x2 = index(I, ORIGIN)
    x3 = width(I)
    x4 = decrement(x3)
    x5 = fill(x1, x2, vfrontier(ORIGIN))
    x6 = fill(x5, x2, vfrontier(astuple(ZERO, x4)))
    x7 = tuple(
        (x8[1][1], x8[0])
        for x8 in enumerate(I)
        if x8[1][1] == x8[1][-2]
        and x8[1][1] not in (ZERO, x2)
        and x8[1].count(x8[1][1]) == TWO
    )
    x8 = render_templates_98c475bf(x7)
    x9 = paint(x6, x8)
    return x9
