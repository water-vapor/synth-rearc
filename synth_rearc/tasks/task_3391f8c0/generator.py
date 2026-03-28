from synth_rearc.core import *

from .helpers import (
    NONZERO_COLORS_3391F8C0,
    PROTOTYPE_LIBRARY_3391F8C0,
    render_scene_3391f8c0,
    sample_family_counts_3391f8c0,
    sample_layout_3391f8c0,
)


def generate_3391f8c0(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0, x1 = sample(PROTOTYPE_LIBRARY_3391F8C0, TWO)
        x2, x3 = sample(NONZERO_COLORS_3391F8C0, TWO)
        x4, x5 = sample_family_counts_3391f8c0(diff_lb, diff_ub)
        x6 = max(height(x0), height(x1))
        x7 = max(width(x0), width(x1))
        x8 = sample_layout_3391f8c0(diff_lb, diff_ub, x6, x7, x4 + x5)
        if x8 is None:
            continue
        x9, x10, x11 = x8
        x12 = list(x11)
        shuffle(x12)
        x13 = tuple(sorted(x12[:x4]))
        x14 = tuple(sorted(x12[x4:]))
        x15 = render_scene_3391f8c0(x9, x10, x2, x0, x13, x3, x1, x14)
        x16 = render_scene_3391f8c0(x9, x10, x2, x0, x14, x3, x1, x13)
        return {"input": x15, "output": x16}
