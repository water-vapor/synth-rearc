from synth_rearc.core import *

from .helpers import analyze_motif_80a900e0
from .helpers import extend_segment_80a900e0, motif_objects_80a900e0


def verify_80a900e0(
    I: Grid,
) -> Grid:
    x0 = motif_objects_80a900e0(I)
    x1 = I
    for x2 in x0:
        _, x3, x4, x5 = analyze_motif_80a900e0(x2)
        for x6, x7, x8 in x5:
            x1 = extend_segment_80a900e0(x1, I, x3, x4, x6, x7, x8)
    return x1
