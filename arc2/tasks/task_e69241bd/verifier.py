from arc2.core import *


def verify_e69241bd(I: Grid) -> Grid:
    x0 = ofcolor(I, ZERO)
    x1 = fill(canvas(FIVE, shape(I)), ONE, x0)
    x2 = colorfilter(objects(x1, T, F, F), ONE)
    x3 = I
    for x4 in x2:
        x5 = toindices(x4)
        x6 = mapply(dneighbors, x5)
        x7 = difference(x6, x5)
        x8 = toobject(x7, I)
        x9 = palette(x8)
        x10 = difference(x9, initset(ZERO))
        x11 = difference(x10, initset(FIVE))
        if size(x11) == ONE:
            x12 = first(x11)
            x3 = fill(x3, x12, x5)
    return x3
