from synth_rearc.core import *


def verify_342dd610(I: Grid) -> Grid:
    x0 = canvas(EIGHT, shape(I))
    x1 = ofcolor(I, ONE)
    x2 = shift(x1, RIGHT)
    x3 = recolor(ONE, x2)
    x4 = paint(x0, x3)
    x5 = ofcolor(I, TWO)
    x6 = shift(x5, double(LEFT))
    x7 = recolor(TWO, x6)
    x8 = paint(x4, x7)
    x9 = ofcolor(I, SEVEN)
    x10 = shift(x9, double(UP))
    x11 = recolor(SEVEN, x10)
    x12 = paint(x8, x11)
    x13 = ofcolor(I, NINE)
    x14 = shift(x13, double(DOWN))
    x15 = recolor(NINE, x14)
    x16 = paint(x12, x15)
    return x16
