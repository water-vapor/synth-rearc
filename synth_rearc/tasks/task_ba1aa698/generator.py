from synth_rearc.core import *

from .helpers import (
    HEIGHT_BA1AA698,
    INNER_WIDTH_CHOICES_BA1AA698,
    MOTIF_PATCHES_BA1AA698,
    NONZERO_COLORS_BA1AA698,
    PANEL_COUNT_BOUNDS_BA1AA698,
    assemble_input_ba1aa698,
    build_panel_ba1aa698,
    motif_choices_ba1aa698,
)


STEP_BOUNDS_BA1AA698 = (ONE, THREE)


def _sample_border_case_ba1aa698() -> Boolean:
    return randint(ZERO, FOUR) == ZERO


def _sample_colors_ba1aa698(
    border_case: Boolean,
) -> Tuple:
    x0 = choice(NONZERO_COLORS_BA1AA698)
    x1 = choice(tuple(x2 for x2 in NONZERO_COLORS_BA1AA698 if x2 != x0))
    if border_case:
        return x0, x1, x0
    x2 = tuple(x3 for x3 in NONZERO_COLORS_BA1AA698 if x3 not in (x0, x1))
    return x0, x1, choice(x2)


def _sample_layout_ba1aa698(
    diff_lb: float,
    diff_ub: float,
) -> Tuple:
    while True:
        x0 = _sample_border_case_ba1aa698()
        x1 = unifint(diff_lb, diff_ub, PANEL_COUNT_BOUNDS_BA1AA698)
        x2 = FOUR if x0 else choice(INNER_WIDTH_CHOICES_BA1AA698)
        x3 = MOTIF_PATCHES_BA1AA698[ONE] if x0 else choice(motif_choices_ba1aa698(x2))
        x4, x5, x6 = _sample_colors_ba1aa698(x0)
        x7 = unifint(diff_lb, diff_ub, STEP_BOUNDS_BA1AA698)
        x8 = ONE if x0 else choice((NEG_ONE, ONE))
        x9 = multiply(x7, x8)
        x10 = branch(x0, sign(x9), ZERO)
        x11 = height(x3)
        x12 = HEIGHT_BA1AA698 - x11 - TWO
        x13 = randint(TWO, x12)
        x14 = x13 - x1 * x9 - x10
        x15 = tuple(x14 + x16 * x9 for x16 in range(x1))
        if min(x15) < TWO or max(x15) > x12:
            continue
        return x2, x3, x4, x5, x6, x15, x13


def generate_ba1aa698(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0, x1, x2, x3, x4, x5, x6 = _sample_layout_ba1aa698(diff_lb, diff_ub)
        x7 = tuple(build_panel_ba1aa698(HEIGHT_BA1AA698, x0, x2, x3, x1, x4, x8) for x8 in x5)
        x8 = assemble_input_ba1aa698(x7)
        x9 = build_panel_ba1aa698(HEIGHT_BA1AA698, x0, x2, x3, x1, x4, x6)
        if x8 == x9:
            continue
        return {"input": x8, "output": x9}
