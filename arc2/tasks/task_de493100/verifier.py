from arc2.core import *


def verify_de493100(I: Grid) -> Grid:
    x0 = ofcolor(I, SEVEN)
    x1 = ulcorner(x0)
    x2 = shape(x0)
    x3 = shape(I)
    x4 = canvas(SEVEN, x3)
    x5 = vmirror(I)
    x6 = asobject(x5)
    x7 = shift(x6, ZERO_BY_TWO)
    x8 = paint(x4, x7)
    x9 = crop(x8, x1, x2)
    x10 = hmirror(I)
    x11 = asobject(x10)
    x12 = shift(x11, TWO_BY_ZERO)
    x13 = paint(x4, x12)
    x14 = crop(x13, x1, x2)
    x15 = dmirror(I)
    x16 = crop(x15, x1, x2)
    x17 = ofcolor(x9, SEVEN)
    x18 = toobject(x17, x14)
    x19 = paint(x9, x18)
    x20 = ofcolor(x19, SEVEN)
    x21 = toobject(x20, x16)
    x22 = paint(x19, x21)
    return x22
