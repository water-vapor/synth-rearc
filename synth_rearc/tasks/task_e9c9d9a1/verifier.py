from synth_rearc.core import *


def verify_e9c9d9a1(I: Grid) -> Grid:
    x0 = frontiers(I)
    x1 = order(sfilter(x0, hline), uppermost)
    x2 = order(sfilter(x0, vline), leftmost)
    x3 = first(x1)
    x4 = last(x1)
    x5 = first(x2)
    x6 = last(x2)
    x7 = uppermost(x3)
    x8 = lowermost(x4)
    x9 = leftmost(x5)
    x10 = rightmost(x6)
    x11 = interval(ZERO, x7, ONE)
    x12 = interval(increment(x8), height(I), ONE)
    x13 = interval(ZERO, x9, ONE)
    x14 = interval(increment(x10), width(I), ONE)
    x15 = product(x11, x13)
    x16 = product(x11, x14)
    x17 = product(x12, x13)
    x18 = product(x12, x14)
    x19 = I
    for x20, x21 in zip((TWO, FOUR, ONE, EIGHT), (x15, x16, x17, x18)):
        x19 = fill(x19, x20, x21)
    x22 = x19
    for x23, x24 in zip(x1, x1[ONE:]):
        x25 = interval(increment(uppermost(x23)), uppermost(x24), ONE)
        for x26, x27 in zip(x2, x2[ONE:]):
            x28 = interval(increment(leftmost(x26)), leftmost(x27), ONE)
            x22 = fill(x22, SEVEN, product(x25, x28))
    return x22
