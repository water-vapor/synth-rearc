from synth_rearc.core import *


def verify_1efba499(I: Grid) -> Grid:
    x0 = mostcolor(I)
    x1 = fgpartition(I)
    x2 = argmax(x1, size)
    x3 = color(x2)
    x4 = toindices(x2)
    x5 = greater(width(x2), height(x2))
    x6 = height(I)
    x7 = width(I)
    x8 = {}
    if x5:
        for x9, x10 in x4:
            if x10 not in x8:
                x8[x10] = [x9, x9]
            else:
                if x9 < x8[x10][ZERO]:
                    x8[x10][ZERO] = x9
                if x9 > x8[x10][ONE]:
                    x8[x10][ONE] = x9
    else:
        for x9, x10 in x4:
            if x9 not in x8:
                x8[x9] = [x10, x10]
            else:
                if x10 < x8[x9][ZERO]:
                    x8[x9][ZERO] = x10
                if x10 > x8[x9][ONE]:
                    x8[x9][ONE] = x10
    x11 = I
    if x5:
        for x12, x13 in x8.items():
            x14, x15 = x13
            x16 = []
            x17 = []
            for x18 in range(x14):
                x19 = index(I, (x18, x12))
                if x19 not in (x0, x3):
                    x16.append((x18, x19))
            for x18 in range(x15 + ONE, x6):
                x19 = index(I, (x18, x12))
                if x19 not in (x0, x3):
                    x17.append((x18, x19))
            if x16 and x17:
                x20, x21 = x16[-ONE]
                x22, x23 = x17[ZERO]
                x24 = frozenset(((x20, x12), (x22, x12)))
                x11 = fill(x11, x0, x24)
                x11 = fill(x11, x23, frozenset(((x14 - ONE, x12),)))
                x11 = fill(x11, x21, frozenset(((x15 + ONE, x12),)))
    else:
        for x12, x13 in x8.items():
            x14, x15 = x13
            x16 = []
            x17 = []
            for x18 in range(x14):
                x19 = index(I, (x12, x18))
                if x19 not in (x0, x3):
                    x16.append((x18, x19))
            for x18 in range(x15 + ONE, x7):
                x19 = index(I, (x12, x18))
                if x19 not in (x0, x3):
                    x17.append((x18, x19))
            if x16 and x17:
                x20, x21 = x16[-ONE]
                x22, x23 = x17[ZERO]
                x24 = frozenset(((x12, x20), (x12, x22)))
                x11 = fill(x11, x0, x24)
                x11 = fill(x11, x23, frozenset(((x12, x14 - ONE),)))
                x11 = fill(x11, x21, frozenset(((x12, x15 + ONE),)))
    return x11
