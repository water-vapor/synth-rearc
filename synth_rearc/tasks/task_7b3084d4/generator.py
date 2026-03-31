from __future__ import annotations

from synth_rearc.core import *

from .helpers import COLOR_POOL_7B3084D4
from .helpers import place_corner_objects_in_input_7b3084d4
from .helpers import sample_output_and_corner_grids_7b3084d4
from .verifier import verify_7b3084d4


def generate_7b3084d4(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = unifint(diff_lb, diff_ub, (FOUR, 14))
        x1 = tuple(sample(COLOR_POOL_7B3084D4, FOUR))
        x2 = sample_output_and_corner_grids_7b3084d4(x0, x1)
        if x2 is None:
            continue
        x3, x4 = x2
        x5 = place_corner_objects_in_input_7b3084d4(x4)
        if x5 is None:
            continue
        if x5 == x3:
            continue
        try:
            x6 = verify_7b3084d4(x5)
        except Exception:
            continue
        if x6 != x3:
            continue
        return {"input": x5, "output": x3}
