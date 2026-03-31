from synth_rearc.core import *


def verify_f931b4a8(I: Grid) -> Grid:
    x0 = vsplit(I, TWO)
    x1 = first(x0)
    x2 = last(x0)
    x3 = hsplit(x1, TWO)
    x4 = hsplit(x2, TWO)
    x5 = first(x3)
    x6 = last(x3)
    x7 = first(x4)
    x8 = last(x4)
    x9 = matcher(first, ZERO)
    x10 = compose(flip, x9)
    x11 = asobject(x5)
    x12 = sfilter(x11, x10)
    x13 = size(x12)
    x14 = asobject(x6)
    x15 = sfilter(x14, x10)
    x16 = size(x15)
    x17 = palette(x8)
    x18 = contained(ZERO, x17)
    x19 = remove(ZERO, x17)
    x20 = greater(size(x19), ZERO)
    x21 = both(x18, x20)
    if x21:
        x22 = tuple(tuple(replace(x8, ZERO, x23) for x23 in x24) for x24 in x7)
        x25 = tuple()
        for x26 in x22:
            x27 = first(x26)
            for x28 in x26[ONE:]:
                x27 = hconcat(x27, x28)
            x25 = x25 + (x27,)
        x29 = first(x25)
        for x30 in x25[ONE:]:
            x29 = vconcat(x29, x30)
    else:
        x29 = x7
    x31 = astuple(x13, x16)
    x32 = crop(x29, ORIGIN, x31)
    return x32
