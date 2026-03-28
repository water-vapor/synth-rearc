from __future__ import annotations

from synth_rearc.core import *


SPIRAL_DIRECTIONS_08573cc6 = (
    (ZERO, NEG_ONE),
    (ONE, ZERO),
    (ZERO, ONE),
    (NEG_ONE, ZERO),
)


def render_spiral_08573cc6(
    dimensions: IntegerTuple,
    marker: IntegerTuple,
    hcolor: Integer,
    vcolor: Integer,
) -> Grid:
    x0 = canvas(ZERO, dimensions)
    x1 = fill(x0, ONE, frozenset({marker}))
    x2 = marker
    x3 = TWO
    x4 = ZERO
    while True:
        x5 = SPIRAL_DIRECTIONS_08573cc6[x4 % FOUR]
        x6 = hcolor if even(x4) else vcolor
        x7 = add(x2, multiply(x5, x3))
        x8 = remove(x2, connect(x2, x7))
        x1 = fill(x1, x6, x8)
        if not (ZERO <= x7[ZERO] < dimensions[ZERO] and ZERO <= x7[ONE] < dimensions[ONE]):
            return x1
        x2 = x7
        x3 += ONE
        x4 += ONE
