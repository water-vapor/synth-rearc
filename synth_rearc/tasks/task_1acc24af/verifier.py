from synth_rearc.core import *

from .helpers import blue_slots_1acc24af, piece_matches_slot_1acc24af


def verify_1acc24af(I: Grid) -> Grid:
    x0 = objects(I, T, F, T)
    x1 = colorfilter(x0, ONE)
    x2 = merge(x1)
    x3 = colorfilter(x0, FIVE)
    x4 = blue_slots_1acc24af(x2)
    x5 = lbind(piece_matches_slot_1acc24af, x2)
    x6 = lbind(x5, x4)
    x7 = sfilter(x3, x6)
    x8 = merge(x7)
    x9 = fill(I, TWO, x8)
    return x9
