from synth_rearc.core import *


def verify_cb227835(I: Grid) -> Grid:
    x0 = order(ofcolor(I, EIGHT), identity)
    x1 = first(x0)
    x2 = last(x0)
    x3 = subtract(x2, x1)
    x4 = first(x3)
    x5 = last(x3)
    x6 = sign(x5)
    x7 = multiply(x5, x6)
    x8 = greater(x7, x4)
    x9 = branch(x8, subtract(x7, x4), subtract(x4, x7))
    x10 = branch(x8, astuple(ZERO, multiply(x6, x9)), astuple(x9, ZERO))
    x11 = add(x1, x10)
    x12 = subtract(x2, x10)
    x13 = connect(x11, x2)
    x14 = connect(x1, x12)
    x15 = connect(x1, x11)
    x16 = connect(x12, x2)
    x17 = combine(x13, x14)
    x18 = combine(x15, x16)
    x19 = combine(x17, x18)
    x20 = difference(x19, ofcolor(I, EIGHT))
    x21 = fill(I, THREE, x20)
    return x21
