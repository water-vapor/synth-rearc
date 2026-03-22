from arc2.core import *


def verify_85b81ff1(I: Grid) -> Grid:
    x0 = hsplit(I, FIVE)
    x1 = rbind(colorcount, ZERO)
    x2 = chain(invert, x1, righthalf)
    x3 = order(x0, x2)
    x4 = height(I)
    x5 = crop(I, astuple(ZERO, TWO), astuple(x4, ONE))
    x6 = first(x3)
    for x7 in x3[ONE:]:
        x6 = hconcat(x6, x5)
        x6 = hconcat(x6, x7)
    return x6
