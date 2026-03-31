from synth_rearc.core import *

from .helpers import (
    compose_input_bf45cf4b,
    render_output_bf45cf4b,
    sample_layout_bf45cf4b,
    sample_marker_patch_bf45cf4b,
    sample_tile_bf45cf4b,
)
from .verifier import verify_bf45cf4b


def generate_bf45cf4b(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = choice(interval(ZERO, TEN, ONE))
        x1 = sample_tile_bf45cf4b(diff_lb, diff_ub, x0)
        x2 = shape(x1)
        x3 = (
            unifint(diff_lb, diff_ub, (THREE, FIVE)),
            unifint(diff_lb, diff_ub, (THREE, FIVE)),
        )
        x4 = sample_marker_patch_bf45cf4b(diff_lb, diff_ub, x3)
        if x4 is None:
            continue
        x5 = tuple(x6 for x6 in interval(ZERO, TEN, ONE) if x6 not in palette(x1) | {x0})
        x6 = choice(x5)
        x7 = sample_layout_bf45cf4b(diff_lb, diff_ub, x2, x3)
        if x7 is None:
            continue
        x8, x9, x10 = x7
        x11 = compose_input_bf45cf4b(x8, x0, x1, x9, x4, x6, x10)
        x12 = render_output_bf45cf4b(x1, x4, x0)
        if verify_bf45cf4b(x11) != x12:
            continue
        return {"input": x11, "output": x12}
