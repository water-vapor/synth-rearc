from collections import Counter, defaultdict

from synth_rearc.core import *


def verify_247ef758(I: Grid) -> Grid:
    x0 = height(I)
    x1 = width(I)
    x2 = None
    for x3 in range(x1):
        x4 = tuple(I[x5][x3] for x5 in range(x0))
        x5 = equality(size(dedupe(x4)), ONE)
        x6 = first(x4)
        if both(x5, x6 != ZERO):
            x2 = x3
            break
    x7 = crop(I, astuple(ZERO, ZERO), astuple(x0, x2))
    x8 = crop(I, astuple(ZERO, increment(x2)), astuple(x0, subtract(x1, increment(x2))))
    x9 = tuple(x8[ZERO])
    x10 = tuple(x8[decrement(x0)])
    x11 = tuple(x12[ZERO] for x12 in x8)
    x12 = tuple(x13[decrement(width(x8))] for x13 in x8)
    x13 = x9 + x10 + x11 + x12
    x14 = Counter(x13).most_common(ONE)[ZERO][ZERO]
    x15 = decrement(width(x8))
    x16 = defaultdict(tuple)
    for x17, x18 in enumerate(x9):
        x19 = both(x17 != ZERO, x17 != x15)
        x20 = x18 != x14
        if both(x19, x20):
            x16[x18] = x16[x18] + (add(increment(x2), x17),)
    x21 = decrement(x0)
    x22 = defaultdict(tuple)
    for x23, x24 in enumerate(x11):
        x25 = both(x23 != ZERO, x23 != x21)
        x26 = x24 != x14
        if both(x25, x26):
            x22[x24] = x22[x24] + (x23,)
    x27 = objects(x7, T, T, T)
    x28 = tuple(sorted(x27, key=lambda x29: (-uppermost(x29), -leftmost(x29))))
    x30 = I
    for x31 in x28:
        x32 = color(x31)
        if both(x32 in x16, x32 in x22):
            x30 = fill(x30, ZERO, x31)
    for x33 in x28:
        x34 = color(x33)
        if not both(x34 in x16, x34 in x22):
            continue
        x35 = center(x33)
        for x36 in x22[x34]:
            for x37 in x16[x34]:
                x38 = shift(x33, subtract(astuple(x36, x37), x35))
                x30 = paint(x30, x38)
    return x30
