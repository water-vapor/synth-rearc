from arc2.core import *

from .helpers import (
    adjacent_endpoint_arcs_753ea09b,
    dominant_fill_color_753ea09b,
    enclosed_cells_753ea09b,
    largest_two_eight_components_753ea09b,
)


def verify_753ea09b(I: Grid) -> Grid:
    x0 = mostcolor(I)
    x1 = dominant_fill_color_753ea09b(I)
    x2 = ofcolor(I, x1)
    x3 = largest_two_eight_components_753ea09b(x2)
    x4 = adjacent_endpoint_arcs_753ea09b(x3, shape(I))
    x5 = merge((x3[ZERO], x3[ONE], x4[ZERO], x4[ONE]))
    x6 = enclosed_cells_753ea09b(x5, shape(I))
    x7 = ofcolor(I, x0)
    x8 = intersection(x6, x7)
    x9 = fill(I, x1, x8)
    return x9
