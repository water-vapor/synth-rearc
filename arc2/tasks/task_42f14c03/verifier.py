from collections import defaultdict

from arc2.core import *


def verify_42f14c03(I: Grid) -> Grid:
    x0 = objects(I, T, F, T)
    x1 = tuple(x0)
    x2 = []
    for x3 in x1:
        x4 = delta(x3)
        if len(x4) == ZERO:
            continue
        x5 = shift(x4, invert(ulcorner(x3)))
        x6 = fill(canvas(ZERO, shape(x3)), ONE, x5)
        x7 = tuple(order(objects(x6, T, F, T), ulcorner))
        if len(x7) == ZERO:
            continue
        x8 = defaultdict(list)
        for x9 in x1:
            if x9 == x3:
                continue
            x10 = normalize(toindices(x9))
            x8[x10].append(x9)
        x11 = T
        x12 = defaultdict(list)
        for x13 in x7:
            x14 = normalize(toindices(x13))
            x12[x14].append(x13)
        for x15, x16 in x12.items():
            if len(x8.get(x15, ())) < len(x16):
                x11 = F
                break
        if x11:
            x2.append((x3, x7, x8))
    x17 = x2[ZERO]
    x18 = x17[ZERO]
    x19 = x17[ONE]
    x20 = x17[TWO]
    x21 = canvas(color(x18), shape(x18))
    x22 = defaultdict(list)
    for x23 in x19:
        x24 = normalize(toindices(x23))
        x22[x24].append(x23)
    for x25 in x22:
        x26 = order(x22[x25], ulcorner)
        x27 = order(x20[x25], ulcorner)
        for x28, x29 in zip(x26, x27):
            x21 = fill(x21, color(x29), x28)
    return x21
