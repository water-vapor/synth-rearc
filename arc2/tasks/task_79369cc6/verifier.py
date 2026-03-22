from arc2.core import *


TEMPLATE_TRANSFORMS_79369CC6 = (
    identity,
    rot90,
    rot180,
    rot270,
    hmirror,
    vmirror,
    dmirror,
    cmirror,
)


def verify_79369cc6(I: Grid) -> Grid:
    x0 = height(I)
    x1 = width(I)
    x2 = astuple(THREE, THREE)
    x3 = interval(ZERO, subtract(x0, TWO), ONE)
    x4 = interval(ZERO, subtract(x1, TWO), ONE)
    x5 = None
    x6 = None
    for x7 in x3:
        for x8 in x4:
            x9 = crop(I, astuple(x7, x8), x2)
            x10 = palette(x9)
            x11 = both(contained(FOUR, x10), contained(SIX, x10))
            if flip(x11):
                continue
            x12 = []
            x13 = set()
            for x14 in TEMPLATE_TRANSFORMS_79369CC6:
                x15 = x14(x9)
                x16 = ofcolor(x15, SIX)
                x17 = tuple(sorted(x16))
                if x17 in x13:
                    continue
                x13.add(x17)
                x18 = ofcolor(x15, FOUR)
                x12.append((x16, x18))
            x19 = ZERO
            for x20 in x3:
                for x21 in x4:
                    x22 = crop(I, astuple(x20, x21), x2)
                    x23 = ofcolor(x22, SIX)
                    for x24, x25 in x12:
                        x26 = equality(x23, x24)
                        if flip(x26):
                            continue
                        x27 = F
                        for x28 in x25:
                            x29 = index(x22, x28)
                            x30 = equality(x29, FOUR)
                            if flip(x30):
                                x27 = T
                                break
                        if x27:
                            x19 = increment(x19)
                        break
            x31 = greater(x19, ZERO)
            if flip(x31):
                continue
            x32 = colorcount(x9, FOUR)
            x33 = colorcount(x9, SIX)
            x34 = (min(x32, x33), -x7, x32, -x8)
            if x6 is None or x34 > x6:
                x5 = x9
                x6 = x34
    if x5 is None:
        return I
    x35 = []
    x36 = set()
    for x37 in TEMPLATE_TRANSFORMS_79369CC6:
        x38 = x37(x5)
        x39 = ofcolor(x38, SIX)
        x40 = tuple(sorted(x39))
        if x40 in x36:
            continue
        x36.add(x40)
        x41 = ofcolor(x38, FOUR)
        x35.append((x39, x41))
    x42 = I
    for x43 in x3:
        for x44 in x4:
            x45 = crop(I, astuple(x43, x44), x2)
            x46 = ofcolor(x45, SIX)
            for x47, x48 in x35:
                x49 = equality(x46, x47)
                if flip(x49):
                    continue
                x50 = shift(x48, astuple(x43, x44))
                x42 = fill(x42, FOUR, x50)
                break
    return x42
