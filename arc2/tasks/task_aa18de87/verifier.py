from arc2.core import *


def verify_aa18de87(I: Grid) -> Grid:
    x0 = ofcolor(I, ZERO)
    x1 = difference(asindices(I), x0)
    x2 = order({x3[0] for x3 in x1}, identity)
    x3 = I
    for x4 in x2:
        x5 = tuple(x6[1] for x6 in x1 if x6[0] == x4)
        if greater(size(x5), ONE):
            x6 = connect((x4, minimum(x5)), (x4, maximum(x5)))
            x7 = intersection(x6, x0)
            x3 = fill(x3, TWO, x7)
    return x3
