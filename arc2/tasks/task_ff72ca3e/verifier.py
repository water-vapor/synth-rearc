from arc2.core import *

from .helpers import nearest_marker_distance_ff72ca3e, square_patch_ff72ca3e


def verify_ff72ca3e(I: Grid) -> Grid:
    x0 = ofcolor(I, FOUR)
    x1 = ofcolor(I, FIVE)
    x2 = canvas(ZERO, shape(I))
    for x3 in x0:
        x4 = nearest_marker_distance_ff72ca3e(x3, x1)
        x5 = decrement(x4)
        x6 = square_patch_ff72ca3e(x3, x5)
        x2 = fill(x2, TWO, x6)
    x7 = paint(x2, recolor(FIVE, x1))
    x8 = paint(x7, recolor(FOUR, x0))
    return x8
