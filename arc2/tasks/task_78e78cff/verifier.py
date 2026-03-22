from arc2.core import *


def verify_78e78cff(I: Grid) -> Grid:
    x0 = mostcolor(I)
    x1 = palette(I)
    x2 = remove(x0, x1)
    x3 = lbind(colorcount, I)
    x4 = argmin(x2, x3)
    x5 = other(x2, x4)
    x6 = first(ofcolor(I, x4))
    x7 = last(x6)
    x8 = height(I)
    x9 = width(I)
    x10 = tuple(x11 for x11 in range(x8) if contained(x5, I[x11]))
    x11 = minimum(x10)
    x12 = maximum(x10)
    x13 = []
    for x14 in range(x8):
        if x14 < x11:
            x15 = I[x11]
        elif x14 > x12:
            x15 = I[x12]
        else:
            x15 = I[x14]
        x16 = tuple(x17 for x17, x18 in enumerate(x15) if x18 == x5)
        if len(x16) == ZERO:
            x17 = frozenset((x14, x18) for x18 in range(x9))
        else:
            x18 = tuple(x19 for x19 in x16 if x19 < x7)
            x19 = tuple(x20 for x20 in x16 if x20 >= x7)
            if len(x18) > ZERO and len(x19) > ZERO:
                x20 = max(x18)
                x21 = min(x19)
                x17 = frozenset((x14, x22) for x22 in range(x20 + ONE, x21))
            elif len(x18) > ZERO:
                x20 = max(x18)
                x17 = frozenset((x14, x21) for x21 in range(x20 + ONE, x9))
            else:
                x20 = min(x19)
                x17 = frozenset((x14, x21) for x21 in range(x20))
        x13.append(x17)
    x14 = frozenset().union(*x13)
    x15 = underfill(I, x4, x14)
    return x15
