from synth_rearc.core import *

from .helpers import extract_sequence_136b0064
from .helpers import render_trace_136b0064


def verify_136b0064(I: Grid) -> Grid:
    x0 = ofcolor(I, FOUR)
    x1 = leftmost(x0)
    x2 = ulcorner(ofcolor(I, FIVE))
    x3 = subtract(x2, (ZERO, increment(x1)))
    x4 = extract_sequence_136b0064(I)
    x5 = canvas(ZERO, (height(I), x1))
    x6 = fill(x5, FIVE, initset(x3))
    x7 = render_trace_136b0064(x6, x3, x4)
    return x7
