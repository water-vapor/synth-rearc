from arc2.core import *


def verify_b7999b51(I: Grid) -> Grid:
    x0 = fgpartition(I)
    x1 = order(x0, lambda x: (-height(x), leftmost(x), uppermost(x), color(x)))
    x2 = maximum(apply(height, x1))
    x3 = size(x1)
    x4 = canvas(ZERO, (x2, x3))
    x5 = x4
    for x6, x7 in enumerate(x1):
        x8 = decrement(height(x7))
        x9 = connect((ZERO, x6), (x8, x6))
        x10 = recolor(color(x7), x9)
        x5 = paint(x5, x10)
    return x5
