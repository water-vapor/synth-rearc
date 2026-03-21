from arc2.core import *


def verify_9b4c17c4(I: Grid) -> Grid:
    x0 = height(I)
    x1 = width(I)
    x2 = compose(lbind(remove, TWO), palette)
    x3 = vsplit(I, x0)
    x4 = apply(x2, x3)
    x5 = tuple(size(x6) == TWO for x6 in x4)
    x6 = any(x5)
    if x6:
        x7 = leftmost(ofcolor(I, ONE))
        x8 = leftmost(ofcolor(I, EIGHT))
        x9 = branch(greater(x7, x8), EIGHT, ONE)
        x10 = increment(rightmost(ofcolor(I, x9)))
        x11 = branch(equality(x9, ONE), EIGHT, ONE)
        x12 = []
        for x13 in I:
            x14 = colorcount((x13[:x10],), TWO)
            x15 = colorcount((x13[x10:],), TWO)
            x16 = branch(
                equality(x9, ONE),
                repeat(ONE, subtract(x10, x14)) + repeat(TWO, x14),
                repeat(TWO, x14) + repeat(EIGHT, subtract(x10, x14)),
            )
            x17 = subtract(x1, x10)
            x18 = branch(
                equality(x11, ONE),
                repeat(ONE, subtract(x17, x15)) + repeat(TWO, x15),
                repeat(TWO, x15) + repeat(EIGHT, subtract(x17, x15)),
            )
            x12.append(x16 + x18)
        x19 = tuple(x12)
        return x19
    x7 = uppermost(ofcolor(I, ONE))
    x8 = uppermost(ofcolor(I, EIGHT))
    x9 = branch(greater(x7, x8), EIGHT, ONE)
    x10 = increment(lowermost(ofcolor(I, x9)))
    x11 = branch(equality(x9, ONE), EIGHT, ONE)
    x12 = []
    for x13, x14 in enumerate(I):
        x15 = colorcount((x14,), TWO)
        x16 = branch(x13 < x10, x9, x11)
        x17 = branch(
            equality(x16, ONE),
            repeat(ONE, subtract(x1, x15)) + repeat(TWO, x15),
            repeat(TWO, x15) + repeat(EIGHT, subtract(x1, x15)),
        )
        x12.append(x17)
    x18 = tuple(x12)
    return x18
