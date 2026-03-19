from arc2.core import *


def verify_e7639916(I: Grid) -> Grid:
    x0 = ofcolor(I, EIGHT)
    x1 = box(x0)
    x2 = underfill(I, ONE, x1)
    return x2
