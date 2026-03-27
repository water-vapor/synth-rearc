from arc2.core import *


def verify_62b74c02(I: Grid) -> Grid:
    x0 = difference(asindices(I), ofcolor(I, ZERO))
    x1 = subgrid(x0, I)
    x2 = astuple(height(x1), ONE)
    x3 = crop(x1, ORIGIN, x2)
    x4 = subtract(width(I), double(width(x1)))
    x5 = hupscale(x3, x4)
    x6 = hconcat(x1, x5)
    x7 = hconcat(x6, x1)
    return x7
