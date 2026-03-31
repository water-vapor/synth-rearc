from synth_rearc.core import *


def verify_581f7754(I: Grid) -> Grid:
    x0 = mostcolor(I)
    x1 = shape(I)
    x2 = height(I)
    x3 = width(I)
    x4 = objects(I, F, F, T)
    x5 = matcher(size, ONE)
    x6 = sfilter(x4, x5)
    x7 = rbind(bordering, I)
    x8 = sfilter(x6, x7)
    x9: dict[Integer, tuple[str, Integer]] = {}
    for x10 in x8:
        x11 = color(x10)
        x12 = centerofmass(x10)
        x13 = x12[0]
        x14 = x12[1]
        if either(equality(x13, ZERO), equality(x13, decrement(x2))):
            x9[x11] = ("col", x14)
        elif either(equality(x14, ZERO), equality(x14, decrement(x3))):
            x9[x11] = ("row", x13)
    x15 = canvas(x0, x1)
    for x16 in x4:
        x17 = None
        x18 = None
        if equality(size(x16), ONE):
            x17 = color(x16)
            x18 = centerofmass(x16)
        else:
            x19 = palette(x16)
            for x20 in x19:
                if equality(colorcount(x16, x20), ONE):
                    x17 = x20
                    break
            if x17 is not None:
                for x21, x22 in x16:
                    if x21 == x17:
                        x18 = x22
                        break
        x23 = (ZERO, ZERO)
        if both(x17 is not None, x17 in x9):
            x24, x25 = x9[x17]
            if x24 == "row":
                x23 = (subtract(x25, x18[0]), ZERO)
            else:
                x23 = (ZERO, subtract(x25, x18[1]))
        x26 = shift(x16, x23)
        x15 = paint(x15, x26)
    return x15
