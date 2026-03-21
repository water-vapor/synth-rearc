from arc2.core import *


def verify_bf699163(I: Grid) -> Grid:
    x0 = fgpartition(I)
    x1 = colorfilter(x0, SEVEN)
    x2 = first(x1)
    x3 = backdrop(x2)
    x4 = objects(I, T, F, T)
    x5 = matcher(size, EIGHT)
    x6 = sfilter(x4, x5)
    x7 = compose(square, backdrop)
    x8 = sfilter(x6, x7)
    x9 = fork(equality, toindices, box)
    x10 = sfilter(x8, x9)

    def x11(x12: Object) -> Boolean:
        x13 = backdrop(x12)
        x14 = difference(x13, x3)
        x15 = center(x12)
        x16 = index(I, x15)
        return size(x14) == ZERO and x16 == FIVE

    x17 = extract(x10, x11)
    x18 = subgrid(x17, I)
    return x18
