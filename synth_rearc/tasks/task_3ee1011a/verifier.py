from synth_rearc.core import *


def verify_3ee1011a(I: Grid) -> Grid:
    x0 = objects(I, T, F, T)
    x1 = order(
        x0,
        lambda x2: (
            invert(size(x2)),
            color(x2),
            uppermost(x2),
            leftmost(x2),
        ),
    )
    x2 = size(first(x1))
    x3 = canvas(ZERO, (x2, x2))
    x4 = x3
    for x5, x6 in zip(interval(ZERO, size(x1), ONE), x1):
        x7 = subtract(x2, increment(x5))
        x8 = backdrop(frozenset({(x5, x5), (x7, x7)}))
        x4 = fill(x4, color(x6), x8)
    return x4
