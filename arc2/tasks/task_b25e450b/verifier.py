from arc2.core import *

from .helpers import (
    corridor_b25e450b,
    move_to_opposite_border_b25e450b,
    sort_key_b25e450b,
)


def verify_b25e450b(
    I: Grid,
) -> Grid:
    x0 = objects(I, T, F, F)
    x1 = colorfilter(x0, ZERO)
    x2 = sfilter(x1, lambda x: bordering(x, I))
    x3 = tuple(sorted(x2, key=sort_key_b25e450b))
    x4 = tuple(move_to_opposite_border_b25e450b(x5, shape(I)) for x5 in x3)
    x5 = merge(tuple(corridor_b25e450b(x6, x7) for x6, x7 in zip(x3, x4)))
    x6 = fill(I, SEVEN, x5)
    x7 = merge(x4)
    x8 = paint(x6, x7)
    return x8
