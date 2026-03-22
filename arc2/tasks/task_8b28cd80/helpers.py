from arc2.core import *


def spiral_mask_8b28cd80(
    window_shape: IntegerTuple,
) -> Grid:
    x0, x1 = window_shape
    x2 = subtract(double(x0), ONE)
    x3 = subtract(double(x1), ONE)
    x4 = canvas(ONE, (x2, x3))
    x5 = ZERO
    x6 = ONE
    x7 = subtract(x2, TWO)
    x8 = subtract(x3, TWO)
    while x5 <= x7 and x6 <= x8:
        x4 = fill(x4, ZERO, connect((x5, x6), (x7, x6)))
        x4 = fill(x4, ZERO, connect((x7, x6), (x7, x8)))
        x4 = fill(x4, ZERO, connect((x5 + ONE, x8), (x7, x8)))
        if x6 + TWO <= x8:
            x4 = fill(x4, ZERO, connect((x5 + ONE, x6 + TWO), (x5 + ONE, x8)))
        x5 += TWO
        x6 += TWO
        x7 -= TWO
        x8 -= TWO
    return x4
