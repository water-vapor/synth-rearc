from arc2.core import *

from .helpers import extract_rooms, extract_wall_indices, room_color


def verify_e681b708(I: Grid) -> Grid:
    x0 = extract_wall_indices(I)
    x1 = extract_rooms(I, x0)
    x2 = ofcolor(I, ONE)
    x3 = I
    for x4 in x1:
        x5 = room_color(I, x4, x0)
        if x5 is None:
            continue
        x6 = intersection(x4, x2)
        x3 = fill(x3, x5, x6)
    return x3
