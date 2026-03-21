from arc2.core import *


def verify_a59b95c0(I: Grid) -> Grid:
    x0 = numcolors(I)
    x1 = rbind(repeat, x0)
    x2 = compose(merge, x1)
    x3 = apply(x2, I)
    x4 = repeat(x3, x0)
    x5 = merge(x4)
    return x5
