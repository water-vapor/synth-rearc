from arc2.core import *


def verify_d56f2372(I: Grid) -> Grid:
    x0 = fgpartition(I)
    x1 = fork(equality, identity, vmirror)
    x2 = extract(x0, x1)
    x3 = subgrid(x2, I)
    return x3
