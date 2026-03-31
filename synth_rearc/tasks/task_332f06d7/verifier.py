from synth_rearc.core import *


def verify_332f06d7(I: Grid) -> Grid:
    x0 = ofcolor(I, ZERO)
    x1 = ofcolor(I, TWO)
    x2 = ulcorner(x0)
    x3 = shape(x1)
    x4 = replace(I, ZERO, ONE)
    x5 = replace(x4, TWO, ONE)
    x6 = set()
    x7 = height(I) - x3[0] + ONE
    x8 = width(I) - x3[1] + ONE
    for x9 in range(x7):
        for x10 in range(x8):
            x11 = crop(x5, (x9, x10), x3)
            if palette(x11) == initset(ONE):
                x6.add((x9, x10))
    x12 = {x2}
    x13 = [x2]
    x14 = ((ONE, ZERO), (NEG_ONE, ZERO), (ZERO, ONE), (ZERO, NEG_ONE))
    while len(x13) > ZERO:
        x15 = x13.pop()
        for x16 in x14:
            x17 = add(x15, x16)
            if x17 in x6 and x17 not in x12:
                x12.add(x17)
                x13.append(x17)
    x18 = []
    for x19 in x12:
        if x19 == x2:
            continue
        x20 = ZERO
        for x21 in x14:
            if add(x19, x21) in x12:
                x20 = increment(x20)
        if x20 == ONE:
            x18.append(x19)
    x22 = min(x18)
    x23 = fill(I, ONE, x0)
    x24 = interval(x22[0], x22[0] + x3[0], ONE)
    x25 = interval(x22[1], x22[1] + x3[1], ONE)
    x26 = product(x24, x25)
    x27 = fill(x23, ZERO, x26)
    return x27
