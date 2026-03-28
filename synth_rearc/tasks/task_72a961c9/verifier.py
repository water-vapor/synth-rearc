from synth_rearc.core import *


def verify_72a961c9(I: Grid) -> Grid:
    x0 = ofcolor(I, TWO)
    x1 = ofcolor(I, EIGHT)
    x2 = lambda x3: connect(astuple(subtract(x3[0], FOUR), x3[1]), astuple(decrement(x3[0]), x3[1]))
    x3 = apply(x2, x0)
    x4 = lambda x5: connect(astuple(subtract(x5[0], THREE), x5[1]), astuple(decrement(x5[0]), x5[1]))
    x5 = apply(x4, x1)
    x6 = combine(merge(x3), merge(x5))
    x7 = fill(I, ONE, x6)
    x8 = apply(lambda x9: astuple(subtract(x9[0], FOUR), x9[1]), x0)
    x9 = fill(x7, TWO, x8)
    x10 = apply(lambda x11: astuple(subtract(x11[0], THREE), x11[1]), x1)
    x11 = fill(x9, EIGHT, x10)
    return x11
