from synth_rearc.core import *

from .helpers import trace_guides_36a08778


def verify_36a08778(
    I: Grid,
) -> Grid:
    x0 = ofcolor(I, SIX)
    x1 = size(x0)
    x2 = greater(x1, ZERO)
    x3 = trace_guides_36a08778(I)
    x4 = branch(x2, x3, I)
    return x4
