from arc2.core import *

from .helpers import concat_strips_f18ec8cc, split_vertical_strips_f18ec8cc


def _ascending_pair_f18ec8cc(
    x0: tuple[Integer, Integer],
) -> Boolean:
    x1 = first(x0)
    x2 = last(x0)
    x3 = greater(x2, x1)
    return x3


def verify_f18ec8cc(I: Grid) -> Grid:
    x0 = split_vertical_strips_f18ec8cc(I)
    x1 = apply(first, x0)
    x2 = pair(x1, x1[1:])
    x3 = apply(_ascending_pair_f18ec8cc, x2)
    x4 = all(x3)
    x5 = branch(x4, tuple(reversed(x0)), x0[1:] + x0[:1])
    x6 = apply(last, x5)
    x7 = concat_strips_f18ec8cc(x6)
    return x7
