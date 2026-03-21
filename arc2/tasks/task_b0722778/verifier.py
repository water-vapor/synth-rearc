from arc2.core import *


def verify_b0722778(I: Grid) -> Grid:
    x0 = interval(ZERO, height(I), THREE)
    x1 = size(x0)
    x2 = {}
    for x3 in x0:
        x4 = crop(I, (x3, ZERO), (TWO, TWO))
        x5 = crop(I, (x3, THREE), (TWO, TWO))
        x6 = crop(I, (x3, SEVEN), (TWO, TWO))
        x7 = vmirror(x4)
        x8 = rot90(x4)
        x9 = rot270(x4)
        if x7 == x5:
            x10 = vmirror(x6)
        elif x8 == x5:
            x10 = rot90(x6)
        elif x9 == x5:
            x10 = rot270(x6)
        else:
            x11 = {}
            for x12, x13 in zip(x4, x5):
                for x14, x15 in zip(x12, x13):
                    x16 = x11.get(x14)
                    if x16 is None:
                        x11[x14] = x15
                    elif x16 != x15:
                        raise ValueError("inconsistent recolor relation")
            x10 = tuple(tuple(x11[x17] for x17 in x18) for x18 in x6)
        x2[x3] = x10
    x19 = []
    for x20, x21 in enumerate(x0):
        x19.extend(x2[x21])
        if x20 != x1 - ONE:
            x19.append((ZERO, ZERO))
    return tuple(x19)
