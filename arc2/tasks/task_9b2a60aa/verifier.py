from arc2.core import *


def verify_9b2a60aa(I: Grid) -> Grid:
    x0 = objects(I, T, T, T)
    x1 = argmax(x0, size)
    x2 = remove(x1, x0)
    x3 = color(x1)
    x4 = extract(x2, matcher(color, x3))
    x5 = equality(size(apply(uppermost, x2)), ONE)
    x6 = normalize(x1)
    x7 = uppermost(x1)
    x8 = leftmost(x1)
    x9 = underpaint(I, recolor(x3, shift(x6, (x7, x8))))
    if x5:
        x10 = order(x2, leftmost)
        x11 = x10.index(x4)
        x12 = leftmost(x4)
        for x13, x14 in enumerate(x10):
            x15 = subtract(leftmost(x14), x12)
            x16 = multiply(subtract(x13, x11), TWO)
            x17 = add(x8, add(x15, x16))
            x18 = shift(x6, (x7, x17))
            x19 = recolor(color(x14), x18)
            x9 = underpaint(x9, x19)
        return x9
    x10 = order(x2, uppermost)
    x11 = x10.index(x4)
    x12 = uppermost(x4)
    for x13, x14 in enumerate(x10):
        x15 = subtract(uppermost(x14), x12)
        x16 = multiply(subtract(x13, x11), TWO)
        x17 = add(x7, add(x15, x16))
        x18 = shift(x6, (x17, x8))
        x19 = recolor(color(x14), x18)
        x9 = underpaint(x9, x19)
    return x9
