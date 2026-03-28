from synth_rearc.core import *


def verify_bf89d739(I: Grid) -> Grid:
    x0 = ofcolor(I, TWO)
    x1 = order(x0, identity)
    x2 = []
    for x3 in x1:
        for x4 in x1:
            x5 = flip(equality(x3, x4))
            x6 = either(equality(x3[0], x4[0]), equality(x3[1], x4[1]))
            if both(x5, x6):
                x2.append((x3, x4))
    x7 = tuple(x2)
    x8 = argmax(x7, lambda x9: manhattan(initset(first(x9)), initset(last(x9))))
    x9 = first(x8)
    x10 = last(x8)
    x11 = connect(x9, x10)
    x12 = equality(x9[0], x10[0])
    x13 = remove(x9, x0)
    x14 = remove(x10, x13)
    x15 = x11
    for x16 in x14:
        x17 = branch(x12, astuple(x9[0], x16[1]), astuple(x16[0], x9[1]))
        x18 = connect(x16, x17)
        x15 = combine(x15, x18)
    x19 = underfill(I, THREE, x15)
    return x19
