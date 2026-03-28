from synth_rearc.core import *

from .helpers import render_output_block_a57f2f04


def verify_a57f2f04(
    I: Grid,
) -> Grid:
    x0 = objects(I, F, F, T)
    x1 = order(x0, ulcorner)
    x2 = I
    for x3 in x1:
        x4 = subgrid(x3, I)
        x5 = render_output_block_a57f2f04(x4)
        x6 = shift(asobject(x5), ulcorner(x3))
        x2 = paint(x2, x6)
    return x2
