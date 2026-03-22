from arc2.core import *


def verify_73182012(I: Grid) -> Grid:
    x0 = ofcolor(I, ZERO)
    x1 = difference(asindices(I), x0)
    x2 = ulcorner(x1)
    x3 = halve(shape(x1))
    x4 = crop(I, x2, x3)
    return x4
