from arc2.core import *


def verify_817e6c09(I: Grid) -> Grid:
    x0 = objects(I, T, F, T)
    x1 = height(I)
    x2 = rbind(multiply, x1)
    x3 = compose(x2, leftmost)
    x4 = fork(add, x3, uppermost)
    x5 = order(x0, x4)
    x6 = decrement(size(x5))
    x7 = I
    for x8, x9 in enumerate(x5):
        x10 = subtract(x6, x8)
        if even(x10):
            x11 = recolor(EIGHT, x9)
            x7 = paint(x7, x11)
    return x7
