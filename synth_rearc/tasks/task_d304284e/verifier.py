from synth_rearc.core import *


def verify_d304284e(I: Grid) -> Grid:
    x0 = ofcolor(I, SEVEN)
    x1 = width(x0)
    x2 = increment(x1)
    x3 = height(x0)
    x4 = increment(x3)
    x5 = canvas(ZERO, shape(I))
    x6 = interval(ZERO, increment(width(I)), ONE)
    x7 = interval(ONE, increment(height(I)), ONE)
    x8 = x5
    for x9 in x6:
        x10 = multiply(tojvec(x2), x9)
        x11 = branch(equality(x9 % THREE, TWO), SIX, SEVEN)
        x12 = shift(recolor(x11, x0), x10)
        x8 = paint(x8, x12)
        if x11 == SIX:
            for x13 in x7:
                x14 = multiply(toivec(x4), x13)
                x15 = shift(x12, x14)
                x8 = paint(x8, x15)
    return x8
