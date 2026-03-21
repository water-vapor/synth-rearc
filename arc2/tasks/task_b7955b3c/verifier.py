from arc2.core import *


def verify_b7955b3c(I: Grid) -> Grid:
    x0 = partition(I)
    x1 = sfilter(x0, lambda x2: color(x2) != EIGHT)
    x2 = tuple((color(x3), toindices(x3), backdrop(x3)) for x3 in x1)
    x3 = {x4: x6 for x4, x5, x6 in x2}
    x4 = {x5: size(x7) for x5, x6, x7 in x2}
    x5 = {x6: set() for x6, x7, x8 in x2}
    for x6, x7, x8 in x2:
        for x9, x10, x11 in x2:
            if x6 != x9 and size(intersection(x7, x11)) > ZERO:
                x5[x9].add(x6)
    x12 = {x13: ZERO for x13 in x5}
    for x13, x14 in x5.items():
        for x15 in x14:
            x12[x15] += ONE
    x16 = sorted((x17 for x17, x18 in x12.items() if x18 == ZERO), key=lambda x19: (-x4[x19], x19))
    x20 = ()
    while x16:
        x21 = x16[0]
        x16 = x16[1:]
        x20 = x20 + (x21,)
        for x22 in sorted(x5[x21], key=lambda x23: (-x4[x23], x23)):
            x12[x22] -= ONE
            if x12[x22] == ZERO:
                x16.append(x22)
        x16 = sorted(x16, key=lambda x24: (-x4[x24], x24))
    x25 = replace(I, EIGHT, x20[0])
    for x26 in x20[1:]:
        x25 = fill(x25, x26, x3[x26])
    return x25
