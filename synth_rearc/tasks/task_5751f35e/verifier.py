from synth_rearc.core import *


def _centered_box_5751f35e(
    I: Grid,
    obj: Object,
) -> Indices:
    x0 = decrement(height(I))
    x1 = decrement(width(I))
    x2 = min(uppermost(obj), subtract(x0, lowermost(obj)))
    x3 = min(leftmost(obj), subtract(x1, rightmost(obj)))
    x4 = astuple(x2, x3)
    x5 = astuple(subtract(x0, x2), subtract(x1, x3))
    x6 = frozenset({x4, x5})
    return backdrop(x6)


def verify_5751f35e(
    I: Grid,
) -> Grid:
    x0 = partition(I)
    x1 = colorfilter(x0, ZERO)
    x2 = remove(first(x1), x0)
    x3 = order(
        x2,
        lambda x4: height(_centered_box_5751f35e(I, x4)) * width(_centered_box_5751f35e(I, x4)),
    )[::-ONE]
    x4 = canvas(ZERO, shape(I))
    for x5 in x3:
        x6 = color(x5)
        x7 = _centered_box_5751f35e(I, x5)
        x4 = fill(x4, x6, x7)
    return x4
