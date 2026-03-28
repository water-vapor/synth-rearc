from arc2.core import *


def verify_48634b99(I: Grid) -> Grid:
    x0 = objects(I, F, F, T)
    x1 = argmax(x0, rbind(colorcount, NINE))
    x2 = replace(I, NINE, EIGHT)
    x3 = size(x1)
    x4 = extract(x0, lambda x: both(equality(size(x), add(x3, TWO)), equality(colorcount(x, NINE), ZERO)))
    x5 = ofcolor(I, NINE)
    x6 = equality(uppermost(x5), uppermost(x1))
    x7 = divide(size(x4), TWO)
    x8 = branch(x6, uppermost(x4), subtract(add(lowermost(x4), ONE), x7))
    x9 = leftmost(x4)
    x10 = frozenset((i, x9) for i in range(x8, add(x8, x7)))
    x11 = fill(x2, NINE, x10)
    return x11
