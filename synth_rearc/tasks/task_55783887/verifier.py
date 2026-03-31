from synth_rearc.core import *


def verify_55783887(I: Grid) -> Grid:
    x0 = ofcolor(I, ONE)
    x1 = ofcolor(I, SIX)
    x2 = frozenset(
        (a, b)
        for a in x0
        for b in x0
        if a < b and b[0] - a[0] == b[1] - a[1]
    )
    x3 = frozenset(
        (a, b)
        for a in x0
        for b in x0
        if a < b and b[0] - a[0] == a[1] - b[1]
    )
    x4 = apply(lambda x: connect(first(x), last(x)), x2)
    x5 = apply(lambda x: connect(first(x), last(x)), x3)
    x6 = combine(merge(x4), merge(x5))
    x7 = underfill(I, ONE, x6)
    x8 = intersection(x1, merge(x4))
    x9 = intersection(x1, merge(x5))
    x10 = apply(lambda x: combine(shoot(x, UP_RIGHT), shoot(x, DOWN_LEFT)), x8)
    x11 = apply(lambda x: combine(shoot(x, NEG_UNITY), shoot(x, UNITY)), x9)
    x12 = recolor(SIX, combine(merge(x10), merge(x11)))
    x13 = paint(x7, x12)
    return x13
