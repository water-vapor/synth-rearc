from arc2.core import *

from .helpers import (
    adjacent_seven_dirs_f1bcbc2c,
    connected_components_f1bcbc2c,
    corridor_cells_f1bcbc2c,
    is_straight_dirs_f1bcbc2c,
)


def verify_f1bcbc2c(I: Grid) -> Grid:
    x0 = corridor_cells_f1bcbc2c(I)
    x1 = connected_components_f1bcbc2c(x0)
    x2 = argmax(x1, size)
    x3 = ofcolor(I, NINE)
    x4 = size(x3) == ONE
    x5 = x2
    if x4:
        x6 = first(totuple(x3))
        x7 = x6 in x2
        if x7:
            x8 = adjacent_seven_dirs_f1bcbc2c(I, x6)
            x9 = is_straight_dirs_f1bcbc2c(x8)
            if not x9:
                x10 = remove(x6, x2)
                x11 = connected_components_f1bcbc2c(x10)
                x12 = min(x11, key=lambda x: (uppermost(x), leftmost(x), -len(x)))
                x5 = x12
    x13 = fill(I, EIGHT, x5)
    return x13
