from synth_rearc.core import *


def verify_256b0a75(I: Grid) -> Grid:
    x0 = ofcolor(I, EIGHT)
    x1 = ulcorner(x0)
    x2 = lrcorner(x0)
    x3 = box(x0)
    x4 = difference(corners(x3), x0)
    x5 = first(x4)
    x6 = index(I, x5)
    x7 = height(I)
    x8 = width(I)
    x9, x10 = x1
    x11, x12 = x2
    x13 = frozenset(
        (x14, x15)
        for x14 in range(x7)
        for x15 in range(x8)
        if x9 <= x14 <= x11 or x10 <= x15 <= x12
    )
    x14 = fill(I, x6, x13)
    x15 = fill(x14, EIGHT, x3)
    x16 = []
    for x17, x18 in enumerate(I):
        for x19, x20 in enumerate(x18):
            if x20 in (ZERO, EIGHT):
                continue
            if x9 <= x17 <= x11 and x10 <= x19 <= x12:
                continue
            x16.append((x17, x19, x20))
    x21 = {}
    x22 = {}
    x23 = {}
    x24 = {}
    for x25, x26, x27 in x16:
        if x9 <= x25 <= x11:
            if x26 < x10:
                x21.setdefault(x25, []).append((x26, x27))
            elif x26 > x12:
                x22.setdefault(x25, []).append((x26, x27))
        elif x10 <= x26 <= x12:
            if x25 < x9:
                x23.setdefault(x26, []).append((x25, x27))
            elif x25 > x11:
                x24.setdefault(x26, []).append((x25, x27))
    x28 = x15
    for x29, x30 in x21.items():
        x31 = sorted(x30, reverse=True)
        x32 = len(x31)
        for x33 in range(x32):
            x34, x35 = x31[x33]
            x36 = x31[x33 + 1][0] if x33 + 1 < x32 else -1
            x37 = connect((x29, x36 + 1), (x29, x34))
            x28 = fill(x28, x35, x37)
    for x38, x39 in x22.items():
        x40 = sorted(x39)
        x41 = len(x40)
        for x42 in range(x41):
            x43, x44 = x40[x42]
            x45 = x40[x42 + 1][0] if x42 + 1 < x41 else x8
            x46 = connect((x38, x43), (x38, x45 - 1))
            x28 = fill(x28, x44, x46)
    for x47, x48 in x23.items():
        x49 = sorted(x48, reverse=True)
        x50 = len(x49)
        for x51 in range(x50):
            x52, x53 = x49[x51]
            x54 = x49[x51 + 1][0] if x51 + 1 < x50 else -1
            x55 = connect((x54 + 1, x47), (x52, x47))
            x28 = fill(x28, x53, x55)
    for x56, x57 in x24.items():
        x58 = sorted(x57)
        x59 = len(x58)
        for x60 in range(x59):
            x61, x62 = x58[x60]
            x63 = x58[x60 + 1][0] if x60 + 1 < x59 else x7
            x64 = connect((x61, x56), (x63 - 1, x56))
            x28 = fill(x28, x62, x64)
    return x28
