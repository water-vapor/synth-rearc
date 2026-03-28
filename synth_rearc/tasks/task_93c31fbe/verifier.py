from synth_rearc.core import *

from .helpers import find_boxes_93c31fbe, reflect_points_93c31fbe


def verify_93c31fbe(
    I: Grid,
) -> Grid:
    x0 = ofcolor(I, ONE)
    x1 = fill(I, ZERO, x0)
    x2 = find_boxes_93c31fbe(I)
    x3 = frozenset()
    for x4 in x2:
        r0, c0, r1, c1 = x4
        x5 = frozenset((i, j) for i, j in x0 if r0 <= i <= r1 and c0 <= j <= c1)
        x6 = reflect_points_93c31fbe(x5, x4)
        x3 = combine(x3, x5)
        x3 = combine(x3, x6)
    x7 = fill(x1, ONE, x3)
    return x7
