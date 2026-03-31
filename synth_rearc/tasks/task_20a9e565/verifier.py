from synth_rearc.core import *

from .helpers import (
    MODE_A_20A9E565,
    MODE_B_20A9E565,
    MODE_C_20A9E565,
    MODE_D_20A9E565,
    detect_mode_20a9e565,
    solve_mode_a_20a9e565,
    solve_mode_b_20a9e565,
    solve_mode_c_20a9e565,
    solve_mode_d_20a9e565,
    solve_mode_e_20a9e565,
)


def verify_20a9e565(
    I: Grid,
) -> Grid:
    x0 = detect_mode_20a9e565(I)
    if x0 == MODE_A_20A9E565:
        x1 = solve_mode_a_20a9e565(I)
        return x1
    if x0 == MODE_B_20A9E565:
        x1 = solve_mode_b_20a9e565(I)
        return x1
    if x0 == MODE_C_20A9E565:
        x1 = solve_mode_c_20a9e565(I)
        return x1
    if x0 == MODE_D_20A9E565:
        x1 = solve_mode_d_20a9e565(I)
        return x1
    x1 = solve_mode_e_20a9e565(I)
    return x1
