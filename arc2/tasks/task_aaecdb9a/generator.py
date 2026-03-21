from arc2.core import *

from .helpers import (
    GRID_SHAPE_AAECDB9A,
    SUMMARY_COLORS_AAECDB9A,
    compose_output_aaecdb9a,
    place_patch_aaecdb9a,
    sample_component_counts_aaecdb9a,
    sample_component_patch_aaecdb9a,
)
from .verifier import verify_aaecdb9a


def generate_aaecdb9a(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = sample_component_counts_aaecdb9a(diff_lb, diff_ub)
        x1 = []
        for x2 in SUMMARY_COLORS_AAECDB9A:
            x3 = x0[x2]
            for _ in range(x3):
                x4 = sample_component_patch_aaecdb9a(x3)
                x1.append((x2, x4))
        shuffle(x1)
        x1 = sorted(x1, key=lambda x5: len(x5[ONE]), reverse=True)
        x5 = canvas(SEVEN, GRID_SHAPE_AAECDB9A)
        x6 = frozenset()
        x7 = T
        for x8, x9 in x1:
            x10, x6 = place_patch_aaecdb9a(x6, x9)
            if x10 is None:
                x7 = F
                break
            x5 = fill(x5, x8, x10)
        if x7 == F:
            continue
        x11 = compose_output_aaecdb9a(x0)
        if verify_aaecdb9a(x5) != x11:
            continue
        return {"input": x5, "output": x11}
