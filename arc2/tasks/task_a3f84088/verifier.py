from arc2.core import *


def verify_a3f84088(I: Grid) -> Grid:
    x0 = objects(I, T, F, F)
    x1 = colorfilter(x0, FIVE)
    x2 = argmax(x1, size)
    x3 = subtract(height(x2), TWO)
    x4 = divide(add(x3, ONE), TWO)
    x5 = equality(x3, SEVEN)
    x6 = branch(x5, decrement(x4), x4)
    x7 = I
    x8 = x2
    x9 = (TWO, FIVE, ZERO, FIVE)
    for x10 in range(x6):
        x8 = inbox(x8)
        x11 = x9[x10 % FOUR]
        x7 = fill(x7, x11, x8)
    return x7
