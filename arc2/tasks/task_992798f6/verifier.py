from arc2.core import *


def verify_992798f6(
    I: Grid,
) -> Grid:
    x0 = first(ofcolor(I, TWO))
    x1 = first(ofcolor(I, ONE))
    x2 = subtract(x1, x0)
    x3 = sign(x2)
    x4 = add(x0, x3)
    x5 = astuple(first(x1), last(x4))
    x6 = initset(x4)
    x7 = initset(x5)
    x8 = manhattan(x6, x7)
    x9 = astuple(first(x4), last(x1))
    x10 = initset(x9)
    x11 = manhattan(x6, x10)
    x12 = greater(x8, x11)
    x13 = branch(x12, subtract(x8, x11), subtract(x11, x8))
    x14 = toivec(first(x3))
    x15 = tojvec(last(x3))
    x16 = branch(x12, x14, x15)
    x17 = multiply(x13, x16)
    x18 = add(x4, x17)
    x19 = connect(x4, x18)
    x20 = connect(x18, x1)
    x21 = combine(x19, x20)
    x22 = remove(x0, x21)
    x23 = remove(x1, x22)
    x24 = fill(I, THREE, x23)
    return x24
