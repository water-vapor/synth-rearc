from arc2.core import *


def _slide_object_6ad5bdfd(
    x0: Object,
    x1: Indices,
    x2: IntegerTuple,
) -> Object:
    x3 = x0
    while True:
        x4 = shift(x3, x2)
        x5 = toindices(x4)
        x6 = intersection(x5, x1)
        if len(x6) > ZERO:
            return x3
        x3 = x4


def verify_6ad5bdfd(I: Grid) -> Grid:
    x0 = ofcolor(I, TWO)
    x1 = vline(x0)
    x2 = equality(leftmost(x0), ZERO)
    x3 = equality(uppermost(x0), ZERO)
    x4 = branch(x2, LEFT, RIGHT)
    x5 = branch(x3, UP, DOWN)
    x6 = branch(x1, x4, x5)
    x7 = compose(invert, rightmost)
    x8 = branch(x2, leftmost, x7)
    x9 = compose(invert, lowermost)
    x10 = branch(x3, uppermost, x9)
    x11 = branch(x1, x8, x10)
    x12 = replace(I, TWO, ZERO)
    x13 = objects(x12, T, F, T)
    x14 = order(x13, x11)
    x15 = canvas(ZERO, shape(I))
    x16 = fill(x15, TWO, x0)
    x17 = x0
    x18 = x16
    for x19 in x14:
        x20 = _slide_object_6ad5bdfd(x19, x17, x6)
        x17 = combine(x17, toindices(x20))
        x18 = paint(x18, x20)
    return x18
