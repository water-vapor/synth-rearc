from arc2.core import *


def verify_f21745ec(I: Grid) -> Grid:
    x0 = fgpartition(I)
    x1 = compose(flip, fork(equality, size, compose(size, box)))
    x2 = extract(x0, x1)
    x3 = shape(x2)
    x4 = normalize(toindices(x2))
    x5 = matcher(shape, x3)
    x6 = sfilter(x0, x5)
    x7 = fork(recolor, color, compose(lbind(shift, x4), ulcorner))
    x8 = mapply(x7, x6)
    x9 = canvas(ZERO, shape(I))
    x10 = paint(x9, x8)
    return x10
