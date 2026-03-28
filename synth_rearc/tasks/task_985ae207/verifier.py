from synth_rearc.core import *


def _motif_patch_985ae207(center: IntegerTuple) -> Indices:
    x0, x1 = center
    return frozenset((x0 + x2, x1 + x3) for x2 in range(-ONE, TWO) for x3 in range(-ONE, TWO))


def _bridge_centers_985ae207(
    source: IntegerTuple,
    target: IntegerTuple,
) -> tuple[IntegerTuple, ...]:
    x0, x1 = source
    x2, x3 = target
    if x0 == x2:
        x4 = THREE if x3 > x1 else -THREE
        return tuple((x0, x5) for x5 in range(x1, x3 + x4, x4))
    x4 = THREE if x2 > x0 else -THREE
    return tuple((x5, x1) for x5 in range(x0, x2 + x4, x4))


def verify_985ae207(I: Grid) -> Grid:
    x0 = objects(I, F, F, T)
    x1 = []
    for x2 in x0:
        x3 = palette(x2)
        x4 = equality(size(x3), TWO)
        x5 = equality(shape(x2), THREE_BY_THREE)
        x6 = equality(size(backdrop(x2)), NINE)
        if not both(x4, both(x5, x6)):
            continue
        x7 = mostcolor(x2)
        x8 = leastcolor(x2)
        x9 = equality(colorcount(x2, x7), EIGHT)
        x10 = equality(colorcount(x2, x8), ONE)
        if not both(x9, x10):
            continue
        x11 = uppermost(x2) + ONE
        x12 = leftmost(x2) + ONE
        x13 = (x11, x12)
        x1.append((x7, x8, x2, x13))
    x14 = objects(I, T, F, T)
    x15 = []
    for x16 in x14:
        x17 = toindices(x16)
        x18 = equality(x17, backdrop(x16))
        x19 = greater(size(x16), ONE)
        if not both(x18, x19):
            continue
        x20 = color(x16)
        x15.append((x20, x16))
    x21 = I
    for x22, x23, x24, x25 in x1:
        x26 = uppermost(x24)
        x27 = lowermost(x24)
        x28 = leftmost(x24)
        x29 = rightmost(x24)
        x30, x31 = x25
        x32 = None
        x33 = None
        for x34, x35 in x15:
            if x34 != x23:
                continue
            x36 = uppermost(x35)
            x37 = lowermost(x35)
            x38 = leftmost(x35)
            x39 = rightmost(x35)
            if x36 <= x30 <= x37:
                if x39 < x28:
                    x40 = x31 - x39
                    if positive(x40) and equality(x40 % THREE, ZERO):
                        if x33 is None or x40 < x33:
                            x32 = (x30, x39)
                            x33 = x40
                if x38 > x29:
                    x40 = x38 - x31
                    if positive(x40) and equality(x40 % THREE, ZERO):
                        if x33 is None or x40 < x33:
                            x32 = (x30, x38)
                            x33 = x40
            if x38 <= x31 <= x39:
                if x37 < x26:
                    x40 = x30 - x37
                    if positive(x40) and equality(x40 % THREE, ZERO):
                        if x33 is None or x40 < x33:
                            x32 = (x37, x31)
                            x33 = x40
                if x36 > x27:
                    x40 = x36 - x30
                    if positive(x40) and equality(x40 % THREE, ZERO):
                        if x33 is None or x40 < x33:
                            x32 = (x36, x31)
                            x33 = x40
        if x32 is None:
            continue
        x41 = _bridge_centers_985ae207(x25, x32)
        for x42 in x41:
            x43 = _motif_patch_985ae207(x42)
            x21 = fill(x21, x22, x43)
            x21 = fill(x21, x23, initset(x42))
    return x21
