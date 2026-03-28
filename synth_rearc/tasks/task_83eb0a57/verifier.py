from synth_rearc.core import *

from .helpers import extract_fragments_83eb0a57, find_placements_83eb0a57, paint_fragment_83eb0a57


def verify_83eb0a57(
    I: Grid,
) -> Grid:
    x0 = extract_fragments_83eb0a57(I)
    x1 = x0[ZERO]
    x2 = x1
    for x3 in x0[ONE:]:
        x4 = find_placements_83eb0a57(x2, x3)
        if len(x4) != ONE:
            raise ValueError("83eb0a57 expected a unique fragment placement")
        x5 = x4[ZERO]
        x2 = paint_fragment_83eb0a57(x2, x3, x5)
    return x2
