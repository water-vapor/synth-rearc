from arc2.core import *


def verify_8fbca751(I: Grid) -> Grid:
    x0 = colorfilter(objects(I, T, F, T), EIGHT)
    x1 = list(x0)
    x2 = True
    while x2:
        x2 = False
        x3 = []
        for x4 in x1:
            x5 = False
            for x6, x7 in enumerate(x3):
                x8 = hmatching(x4, x7)
                x9 = vmatching(x4, x7)
                if either(x8, x9):
                    x3[x6] = combine(x7, x4)
                    x5 = True
                    x2 = True
                    break
            if not x5:
                x3.append(x4)
        x1 = x3
    x10 = I
    for x11 in x1:
        x12 = delta(x11)
        x10 = fill(x10, TWO, x12)
    return x10
