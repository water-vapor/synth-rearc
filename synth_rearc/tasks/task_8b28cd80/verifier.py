from synth_rearc.core import *

from .helpers import spiral_mask_8b28cd80


def verify_8b28cd80(I: Grid) -> Grid:
    x0 = objects(I, T, F, T)
    x1 = first(x0)
    x2 = color(x1)
    x3 = ulcorner(x1)
    x4 = height(I)
    x5 = width(I)
    x6 = subtract(multiply(x4, FOUR), THREE)
    x7 = subtract(multiply(x5, FOUR), THREE)
    x8 = spiral_mask_8b28cd80((x6, x7))
    x9, x10 = x3
    x11 = multiply(subtract(decrement(x4), x9), FOUR)
    x12 = multiply(subtract(decrement(x5), x10), FOUR)
    x13 = crop(x8, (x11, x12), (x6, x7))
    x14 = ofcolor(x13, ONE)
    x15 = canvas(ZERO, (x6, x7))
    x16 = fill(x15, x2, x14)
    return x16
