from arc2.core import *


def verify_e729b7be(I: Grid) -> Grid:
    x0 = rot180(I)
    x1 = asobject(x0)
    x2 = underpaint(I, x1)
    return x2
