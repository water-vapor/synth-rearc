from arc2.core import *


def verify_d4c90558(I: Grid) -> Grid:
    x0 = replace(I, FIVE, ZERO)
    x1 = objects(x0, T, F, F)
    x2 = sfilter(x1, lambda x3: color(x3) != ZERO)
    x3 = order(
        x2,
        lambda x4: (
            colorcount(subgrid(x4, I), FIVE),
            color(x4),
            uppermost(x4),
            leftmost(x4),
        ),
    )
    x4 = apply(lambda x5: colorcount(subgrid(x5, I), FIVE), x3)
    x5 = maximum(x4)
    x6 = canvas(ZERO, (size(x3), x5))
    x7 = x6
    for x8, x9, x10 in zip(interval(ZERO, size(x3), ONE), x3, x4):
        x11 = connect((x8, ZERO), (x8, x10 - ONE))
        x7 = fill(x7, color(x9), x11)
    return x7
