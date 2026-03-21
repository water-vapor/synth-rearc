from arc2.core import *

from .helpers import matches_template_bd14c3bf


def verify_bd14c3bf(I: Grid) -> Grid:
    x0 = objects(I, T, F, F)
    x1 = colorfilter(x0, TWO)
    x2 = argmin(x1, ulcorner)
    x3 = subgrid(x2, I)
    x4 = colorfilter(x0, ONE)
    x5 = lambda x6: matches_template_bd14c3bf(subgrid(x6, I), x3)
    x6 = sfilter(x4, x5)
    x7 = merge(x6)
    x8 = fill(I, TWO, x7)
    return x8
