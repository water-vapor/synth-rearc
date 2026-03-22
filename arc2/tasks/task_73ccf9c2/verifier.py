from arc2.core import *


def verify_73ccf9c2(I: Grid) -> Grid:
    x0 = objects(I, T, T, T)
    x1 = normalize
    x2 = compose(vmirror, x1)
    x3 = fork(equality, x1, x2)
    x4 = compose(flip, x3)
    x5 = extract(x0, x4)
    x6 = subgrid(x5, I)
    return x6
