from synth_rearc.core import *


def verify_929ab4e9(
    I: Grid,
) -> Grid:
    x0 = ofcolor(I, TWO)
    x1 = dmirror(I)
    x2 = toobject(x0, x1)
    x3 = paint(I, x2)
    x4 = ofcolor(x3, TWO)
    x5 = hmirror(x3)
    x6 = toobject(x4, x5)
    x7 = paint(x3, x6)
    return x7
