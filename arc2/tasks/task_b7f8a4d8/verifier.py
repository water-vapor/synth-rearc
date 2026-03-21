from arc2.core import *


def verify_b7f8a4d8(I: Grid) -> Grid:
    x0 = difference(palette(I), initset(ZERO))
    x1 = lbind(colorcount, I)
    x2 = argmax(x0, x1)
    x3 = remove(x2, x0)
    x4 = argmax(x3, x1)
    x5 = remove(x4, x3)
    x6 = ofcolor(I, ZERO)
    x7 = I
    for x8 in x5:
        x9 = ofcolor(I, x8)
        x10 = {x11[0] for x11 in x9}
        for x11 in x10:
            x12 = tuple(x13[1] for x13 in x9 if x13[0] == x11)
            x13 = connect((x11, min(x12)), (x11, max(x12)))
            x14 = intersection(x13, x6)
            x7 = fill(x7, x8, x14)
        x15 = {x16[1] for x16 in x9}
        for x16 in x15:
            x17 = tuple(x18[0] for x18 in x9 if x18[1] == x16)
            x18 = connect((min(x17), x16), (max(x17), x16))
            x19 = intersection(x18, x6)
            x7 = fill(x7, x8, x19)
    return x7
