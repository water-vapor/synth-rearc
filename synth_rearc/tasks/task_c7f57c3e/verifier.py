from synth_rearc.core import *

from .helpers import describe_objects_c7f57c3e, render_signature_c7f57c3e


def verify_c7f57c3e(I: Grid) -> Grid:
    x0 = describe_objects_c7f57c3e(I)
    x1 = tuple(x2["signature"] for x2 in x0)
    x2 = mostcommon(x1)
    x3 = leastcommon(x1)
    x4 = canvas(mostcolor(I), shape(I))
    for x5 in x0:
        x6 = x3 if equality(x5["signature"], x2) else x2
        x7 = render_signature_c7f57c3e(x5, x6)
        x4 = paint(x4, x7)
    return x4
