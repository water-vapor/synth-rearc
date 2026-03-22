from arc2.core import *

from .helpers import cluster_markers_896d5239, fit_cluster_triangle_896d5239


def verify_896d5239(I: Grid) -> Grid:
    x0 = ofcolor(I, THREE)
    x1 = cluster_markers_896d5239(x0)
    x2 = shape(I)
    x3 = I
    for x4 in x1:
        x5, x6, x7, x8, x9 = fit_cluster_triangle_896d5239(x4, x2)
        x10 = difference(x8, x4)
        x3 = fill(x3, EIGHT, x10)
    return x3
