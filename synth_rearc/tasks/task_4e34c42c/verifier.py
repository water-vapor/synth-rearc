from synth_rearc.core import *

from .helpers import assemble_fragments_4e34c42c, extract_fragments_4e34c42c


def verify_4e34c42c(
    I: Grid,
) -> Grid:
    x0 = extract_fragments_4e34c42c(I)
    x1 = x0[ZERO]
    x2 = x0[ONE]
    x3 = assemble_fragments_4e34c42c(x1, x2)
    return x3
