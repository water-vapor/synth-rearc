from __future__ import annotations

from synth_rearc.core import *

from .helpers import (
    AVAILABLE_COLORS_D59B0160,
    TEMPLATES_D59B0160,
    apply_clue_block_d59b0160,
    choose_bad_slots_d59b0160,
    decorate_region_d59b0160,
    rect_patch_d59b0160,
    sample_clue_positions_d59b0160,
    sample_region_bounds_d59b0160,
)


def generate_d59b0160(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = canvas(SEVEN, (16, 16))
        x1 = tuple(sample(AVAILABLE_COLORS_D59B0160, THREE))
        x2 = sample_clue_positions_d59b0160()
        x3 = apply_clue_block_d59b0160(x0, x1, x2)
        x4 = choice(TEMPLATES_D59B0160)
        x5 = choose_bad_slots_d59b0160(len(x4))
        x6 = x3
        x7 = []
        for x8, x9 in enumerate(x4):
            x10 = sample_region_bounds_d59b0160(x9)
            if x8 in x5:
                x11 = AVAILABLE_COLORS_D59B0160
                x6 = decorate_region_d59b0160(x6, x10, x1, x11, diff_lb, diff_ub)
                x7.append(x10)
                continue
            x11 = choice((ZERO, ONE, ONE, TWO))
            x12 = tuple(sample(x1, x11))
            x13 = tuple(x14 for x14 in AVAILABLE_COLORS_D59B0160 if x14 in x12 or x14 not in x1)
            x14 = len(x12) == ZERO
            x6 = decorate_region_d59b0160(
                x6,
                x10,
                x12,
                x13,
                diff_lb,
                diff_ub,
                allow_blank=x14 or choice((False, False, True)),
            )
        x15 = x6
        for x16 in x7:
            x17 = rect_patch_d59b0160(x16)
            x15 = fill(x15, SEVEN, x17)
        if x6 == x15:
            continue
        return {"input": x6, "output": x15}
