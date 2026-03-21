from arc2.core import *


def _band_c4d1a9ae(
    I: Grid,
    obj: Object,
) -> Indices:
    x0 = decrement(height(I))
    x1 = leftmost(obj)
    x2 = rightmost(obj)
    x3 = frozenset({(ZERO, x1), (x0, x2)})
    return backdrop(x3)


def verify_c4d1a9ae(
    I: Grid,
) -> Grid:
    x0 = mostcolor(I)
    x1 = ofcolor(I, x0)
    x2 = order(
        fgpartition(I),
        lambda x3: (leftmost(x3), rightmost(x3), color(x3)),
    )
    x3 = tuple(color(x4) for x4 in x2)
    x4 = x3[ONE:] + x3[:ONE]
    x5 = I
    for x6, x7 in zip(x2, x4):
        x8 = _band_c4d1a9ae(I, x6)
        x9 = intersection(x1, x8)
        x5 = fill(x5, x7, x9)
    return x5
