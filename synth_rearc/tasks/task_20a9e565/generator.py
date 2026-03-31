from synth_rearc.core import *

from .helpers import (
    MODE_A_20A9E565,
    MODE_B_20A9E565,
    MODE_C_20A9E565,
    MODE_D_20A9E565,
    MODE_IDS_20A9E565,
    generate_mode_a_20a9e565,
    generate_mode_b_20a9e565,
    generate_mode_c_20a9e565,
    generate_mode_d_20a9e565,
    generate_mode_e_20a9e565,
)


def generate_20a9e565(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    x0 = choice(MODE_IDS_20A9E565)
    if x0 == MODE_A_20A9E565:
        x1 = generate_mode_a_20a9e565(diff_lb, diff_ub)
        return x1
    if x0 == MODE_B_20A9E565:
        x1 = generate_mode_b_20a9e565(diff_lb, diff_ub)
        return x1
    if x0 == MODE_C_20A9E565:
        x1 = generate_mode_c_20a9e565(diff_lb, diff_ub)
        return x1
    if x0 == MODE_D_20A9E565:
        x1 = generate_mode_d_20a9e565(diff_lb, diff_ub)
        return x1
    x1 = generate_mode_e_20a9e565(diff_lb, diff_ub)
    return x1
