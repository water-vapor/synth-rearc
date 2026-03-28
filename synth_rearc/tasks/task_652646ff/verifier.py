from synth_rearc.core import *

from .helpers import clipped_diamond_patch_652646ff, diamond_block_652646ff


def verify_652646ff(
    I: Grid,
) -> Grid:
    x0 = mostcolor(I)
    x1 = order(remove(x0, palette(I)), identity)
    x2 = height(I)
    x3 = width(I)
    x4 = astuple(x2, x3)
    x5 = tuple()
    x6 = {}
    for x7 in x1:
        x8 = ofcolor(I, x7)
        x9 = tuple()
        for x10 in range(-FIVE, x2):
            for x11 in range(-FIVE, x3):
                x12 = astuple(x10, x11)
                x13 = clipped_diamond_patch_652646ff(x12, x4)
                if x8 <= x13:
                    x9 = x9 + (x12,)
        if len(x9) == ONE:
            x14 = x9[ZERO]
            x5 = x5 + (x7,)
            x6[x7] = clipped_diamond_patch_652646ff(x14, x4)
    x15 = {x16: frozenset() for x16 in x5}
    for x16 in x5:
        x17 = ofcolor(I, x16)
        for x18 in x5:
            if x16 == x18:
                continue
            if len(intersection(x17, x6[x18])) > ZERO:
                x15[x18] = insert(x16, x15[x18])
    x19 = tuple()
    x20 = x5
    while len(x20) > ZERO:
        x21 = frozenset(x20)
        x22 = tuple(x23 for x23 in x20 if len(intersection(x15[x23], x21)) == ZERO)
        if len(x22) == ZERO:
            raise ValueError("652646ff expected an acyclic overlap order")
        x19 = x19 + x22
        x20 = tuple(x24 for x24 in x20 if x24 not in x22)
    x25 = tuple(diamond_block_652646ff(x0, x26) for x26 in x19)
    x27 = x25[ZERO]
    for x28 in x25[ONE:]:
        x27 = vconcat(x27, x28)
    return x27
