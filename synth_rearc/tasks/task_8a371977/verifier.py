from synth_rearc.core import *


def verify_8a371977(I: Grid) -> Grid:
    x0 = objects(I, T, F, F)
    x1 = colorfilter(x0, ZERO)
    x2 = argmin(x1, uppermost)
    x3 = argmax(x1, lowermost)
    x4 = argmin(x1, leftmost)
    x5 = argmax(x1, rightmost)
    x6 = uppermost(x2)
    x7 = lowermost(x3)
    x8 = leftmost(x4)
    x9 = rightmost(x5)
    x10 = matcher(uppermost, x6)
    x11 = matcher(lowermost, x7)
    x12 = matcher(leftmost, x8)
    x13 = matcher(rightmost, x9)
    x14 = fork(either, x10, x11)
    x15 = fork(either, x12, x13)
    x16 = fork(either, x14, x15)
    x17 = mfilter(x1, x16)
    x18 = compose(flip, x16)
    x19 = mfilter(x1, x18)
    x20 = fill(I, TWO, x17)
    x21 = fill(x20, THREE, x19)
    return x21
