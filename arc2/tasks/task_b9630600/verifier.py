from arc2.core import *

from .helpers import (
    build_candidate_edges_b9630600,
    draw_edge_b9630600,
    is_room_outline_b9630600,
    kruskal_edges_b9630600,
    room_bbox_b9630600,
)


def verify_b9630600(
    I: Grid,
) -> Grid:
    x0 = objects(I, T, F, T)
    x1 = sfilter(x0, is_room_outline_b9630600)
    x2 = order(x1, ulcorner)
    x3 = tuple(room_bbox_b9630600(x4) for x4 in x2)
    x4 = build_candidate_edges_b9630600(x3)
    x5 = kruskal_edges_b9630600(x4, len(x3))
    x6 = I
    for x7 in x5:
        x6 = draw_edge_b9630600(x6, x3, x7)
    return x6
