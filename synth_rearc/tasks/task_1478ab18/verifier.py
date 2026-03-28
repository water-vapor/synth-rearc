from synth_rearc.core import *


def verify_1478ab18(I: Grid) -> Grid:
    x0 = ofcolor(I, FIVE)
    x1 = tuple(x0)
    x2 = tuple(
        (a, b)
        for a in x1
        for b in x1
        if a < b and abs(a[0] - b[0]) == abs(a[1] - b[1])
    )
    x3 = lambda x: size(connect(first(x), last(x)))
    x4 = argmax(x2, x3)
    x5 = first(x4)
    x6 = last(x4)
    x7 = astuple(first(x5), last(x6))
    x8 = astuple(first(x6), last(x5))
    x9 = branch(contained(x7, x0), x8, x7)
    x10 = connect(x5, x6)
    x11 = connect(x5, x9)
    x12 = connect(x6, x9)
    x13 = combine(x10, x11)
    x14 = combine(x12, x13)
    x15 = fill(I, EIGHT, x14)
    x16 = fill(x15, FIVE, x0)
    return x16
