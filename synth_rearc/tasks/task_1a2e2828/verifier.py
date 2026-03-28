from synth_rearc.core import *


def verify_1a2e2828(I: Grid) -> Grid:
    x0 = frontiers(I)
    x1 = first(x0)
    x2 = color(x1)
    x3 = canvas(x2, UNITY)
    return x3
