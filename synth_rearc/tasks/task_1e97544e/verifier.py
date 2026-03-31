from synth_rearc.core import *

from .helpers import build_output_1e97544e


def verify_1e97544e(I: Grid) -> Grid:
    x0 = remove(ZERO, palette(I))
    x1 = maximum(x0)
    x2 = ZERO
    x3 = ZERO
    x4 = shape(I)
    for x5 in range(x4[0]):
        for x6 in range(x4[1]):
            x7 = index(I, (x5, x6))
            if x7 == ZERO:
                continue
            x2 = x7
            x3 = x6 if x5 <= x6 else x6 + ONE
            break
        if x2 != ZERO:
            break
    x8 = ((x2 - ONE - x3) % x1) + ONE
    x9 = build_output_1e97544e(x8, x1, x4)
    return x9
