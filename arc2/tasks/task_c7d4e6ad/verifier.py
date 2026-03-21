from arc2.core import *


def verify_c7d4e6ad(I: Grid) -> Grid:
    x0 = fgpartition(I)
    x1 = matcher(color, FIVE)
    x2 = extract(x0, x1)
    x3 = toindices(x2)
    x4 = compose(flip, x1)
    x5 = sfilter(x0, x4)
    x6 = compose(lbind(mapply, hfrontier), toindices)
    x7 = compose(rbind(intersection, x3), x6)
    x8 = fork(recolor, color, x7)
    x9 = apply(x8, x5)
    x10 = merge(x9)
    x11 = paint(I, x10)
    return x11
