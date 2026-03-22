from arc2.core import *


def verify_8719f442(I: Grid) -> Grid:
    x0 = other(palette(I), ZERO)
    x1 = shape(I)
    x2 = halve(x1)
    x3 = subtract(double(x1), ONE)
    x4 = multiply(x1, x3)
    x5 = canvas(ZERO, x4)
    x6 = asobject(I)
    x7 = asobject(canvas(x0, x1))
    x8 = ofcolor(I, x0)
    x9 = x5
    for x10 in x8:
        x11 = subtract(x10, x2)
        x12 = sign(x11)
        x13 = add(x10, x2)
        if not equality(x12[ZERO], ZERO):
            x14 = add(x13, toivec(x12[ZERO]))
            x15 = multiply(x14, x1)
            x16 = shift(x6, x15)
            x9 = paint(x9, x16)
        if not equality(x12[ONE], ZERO):
            x17 = add(x13, tojvec(x12[ONE]))
            x18 = multiply(x17, x1)
            x19 = shift(x6, x18)
            x9 = paint(x9, x19)
    x20 = x9
    for x21 in x8:
        x22 = add(x21, x2)
        x23 = multiply(x22, x1)
        x24 = shift(x7, x23)
        x20 = paint(x20, x24)
    return x20
