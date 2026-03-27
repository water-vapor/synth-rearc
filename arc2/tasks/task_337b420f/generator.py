from arc2.core import *

from .helpers import (
    NONZERO_NONBACKGROUND_COLORS_337B420F,
    OUTPUT_DIMS_337B420F,
    make_panel_337b420f,
    sample_distractor_337b420f,
    sample_major_patches_337b420f,
    stitch_panels_337b420f,
)


def generate_337b420f(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = sample_major_patches_337b420f(diff_lb, diff_ub)
        if x0 is None:
            continue
        x1 = []
        x2 = F
        for x3 in x0:
            x4 = sample_distractor_337b420f(x3, diff_lb, diff_ub)
            if x4 is None:
                x2 = T
                break
            x1.append(x4)
        if x2:
            continue
        x5 = sample(NONZERO_NONBACKGROUND_COLORS_337B420F, THREE)
        x6 = list(zip(x5, x0, x1))
        x7 = canvas(EIGHT, OUTPUT_DIMS_337B420F)
        x8 = sorted(x6, key=lambda x9: size(x9[1]), reverse=T)
        x9 = []
        for x10, x11, x12 in x8:
            x7 = fill(x7, x10, x11)
            x13 = make_panel_337b420f(x10, x11, x12)
            x9.append(x13)
        shuffle(x9)
        x14 = stitch_panels_337b420f(tuple(x9))
        return {"input": x14, "output": x7}
