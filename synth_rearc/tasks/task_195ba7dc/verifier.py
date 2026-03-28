from synth_rearc.core import *


def verify_195ba7dc(I: Grid) -> Grid:
    x0 = lefthalf(I)
    x1 = righthalf(I)
    x2 = cellwise(x0, x1, ONE)
    x3 = replace(x2, SEVEN, ONE)
    return x3
