from synth_rearc.core import *


def verify_68bc2e87(I: Grid) -> Grid:
    x0 = fgpartition(I)
    x1 = {color(x2): x2 for x2 in x0}
    x2 = tuple(x1.keys())
    x3 = {x4: set() for x4 in x2}
    x4 = {x5: set() for x5 in x2}
    x5 = mostcolor(I)
    for x6 in x2:
        x7 = x1[x6]
        x8 = difference(box(x7), toindices(x7))
        for x9 in x8:
            x10 = index(I, x9)
            if x10 is None:
                continue
            if x10 == x5 or x10 == x6:
                continue
            if x10 not in x1:
                continue
            x3[x6].add(x10)
            x4[x10].add(x6)
    x11 = []
    x12 = set()
    while len(x11) < len(x2):
        x13 = tuple(
            sorted(
                x14
                for x14 in x2
                if x14 not in x12 and all(x15 in x12 for x15 in x4[x14])
            )
        )
        if len(x13) == ZERO:
            x13 = tuple(sorted(x14 for x14 in x2 if x14 not in x12))
        x16 = x13[ZERO]
        x11.append(x16)
        x12.add(x16)
    return tuple((x17,) for x17 in x11)
