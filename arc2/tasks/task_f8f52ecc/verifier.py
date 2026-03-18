from arc2.core import *

from .helpers import route_f8f52ecc


def verify_f8f52ecc(I: Grid) -> Grid:
    x0 = difference(palette(I), frozenset({ONE, EIGHT}))
    x1 = ofcolor(I, EIGHT)
    x2 = I
    for x3 in order(x0, identity):
        x4 = order(ofcolor(I, x3), identity)
        for x5, x6 in zip(x4, x4[ONE:]):
            x7 = route_f8f52ecc(x5, x6, x1)
            x2 = fill(x2, x3, x7)
    return x2
