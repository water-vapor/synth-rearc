from synth_rearc.core import *

from .helpers import mirror_object_7ed72f31
from .helpers import nearest_axis_7ed72f31


def verify_7ed72f31(I: Grid) -> Grid:
    x0 = objects(I, T, F, T)
    x1 = colorfilter(x0, TWO)
    x2 = difference(x0, x1)
    x3 = lambda x: nearest_axis_7ed72f31(x, x1)
    x4 = lambda x: mirror_object_7ed72f31(x, x3(x))
    x5 = apply(x4, x2)
    x6 = merge(x5)
    x7 = paint(I, x6)
    return x7
