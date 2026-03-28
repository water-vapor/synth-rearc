from synth_rearc.core import *

from .helpers import has_diagonal_run_ecb67b6d


def verify_ecb67b6d(I: Grid) -> Grid:
    x0 = objects(I, T, T, F)
    x1 = colorfilter(x0, FIVE)
    x2 = sfilter(x1, has_diagonal_run_ecb67b6d)
    x3 = merge(x2)
    x4 = fill(I, EIGHT, x3)
    return x4
