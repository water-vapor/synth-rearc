from synth_rearc.core import *

from .helpers import (
    LABEL_GRIDS_3A25B0D8,
    choose_region_colors_3a25b0d8,
    choose_scales_3a25b0d8,
    compose_input_grid_3a25b0d8,
    expand_label_grid_3a25b0d8,
    render_label_grid_3a25b0d8,
    render_scaffold_3a25b0d8,
)
from .verifier import verify_3a25b0d8


def generate_3a25b0d8(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = choice(LABEL_GRIDS_3A25B0D8)
        x1 = choice(tuple(range(TEN)))
        x2 = choice(tuple(x3 for x3 in range(TEN) if x3 != x1))
        x3 = choose_region_colors_3a25b0d8(x0, x1, x2)
        x4 = choose_scales_3a25b0d8(x0, diff_lb, diff_ub)
        x5 = choose_scales_3a25b0d8(x0, diff_lb, diff_ub)
        x6 = expand_label_grid_3a25b0d8(x0, x4[ZERO], x4[ONE])
        x7 = expand_label_grid_3a25b0d8(x0, x5[ZERO], x5[ONE])
        x8 = render_label_grid_3a25b0d8(x6, x1, x2, x3)
        x9 = render_scaffold_3a25b0d8(x7, x1, x2)
        x10 = render_label_grid_3a25b0d8(x7, x1, x2, x3)
        x11 = compose_input_grid_3a25b0d8(x8, x9, x1)
        if x11 == x10:
            continue
        if verify_3a25b0d8(x11) != x10:
            continue
        return {"input": x11, "output": x10}
