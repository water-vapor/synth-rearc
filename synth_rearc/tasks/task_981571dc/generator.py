from synth_rearc.core import *

from .helpers import (
    BLOCK_COUNT_981571DC,
    EXAMPLE_BLOCK_BANKS_981571DC,
    assemble_block_matrix_981571dc,
    mask_with_reflections_981571dc,
    sample_block_matrix_981571dc,
    sample_reflected_rectangles_981571dc,
    zero_count_981571dc,
)
from .verifier import verify_981571dc


ZERO_COUNT_BOUNDS_981571DC = (28, 128)


def generate_981571dc(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = choice(EXAMPLE_BLOCK_BANKS_981571DC)
        x1, x2 = x0
        x3 = sample_block_matrix_981571dc(x1, x2)
        x4 = tuple(x3[x5][x5] for x5 in range(BLOCK_COUNT_981571DC))
        x5 = tuple(
            x3[x6][x7]
            for x6 in range(BLOCK_COUNT_981571DC)
            for x7 in range(x6 + ONE, BLOCK_COUNT_981571DC)
        )
        if len(set(x4)) < THREE:
            continue
        if len(set(x5)) < SIX:
            continue
        x6 = assemble_block_matrix_981571dc(x3)
        if numcolors(x6) < FIVE:
            continue
        x7 = sample_reflected_rectangles_981571dc(diff_lb, diff_ub)
        x8 = mask_with_reflections_981571dc(x6, x7)
        x9 = zero_count_981571dc(x8)
        if x9 < ZERO_COUNT_BOUNDS_981571DC[ZERO] or x9 > ZERO_COUNT_BOUNDS_981571DC[ONE]:
            continue
        if x8 == x6:
            continue
        if verify_981571dc(x8) != x6:
            continue
        return {"input": x8, "output": x6}
