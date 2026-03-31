from synth_rearc.core import *

from .helpers import DRAW_COLOR_DA515329, make_input_da515329, render_output_da515329
from .verifier import verify_da515329


def generate_da515329(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = choice((ONE, TWO, THREE, FOUR))
        x1 = max(SIX, multiply(THREE, x0))
        x2 = unifint(diff_lb, diff_ub, (x1, 15))
        x3 = double(x2)
        x4 = (x3, x3)
        x5 = x0 + TWO
        x6 = x3 - x0 - THREE
        if x5 > x6:
            continue
        x7 = unifint(diff_lb, diff_ub, (x5, x6))
        x8 = unifint(diff_lb, diff_ub, (x5, x6))
        x9 = (x7, x8)
        x10 = make_input_da515329(x4, x9, x0)
        x11 = render_output_da515329(x4, x9, x0)
        if colorcount(x11, DRAW_COLOR_DA515329) < x3 + x3:
            continue
        if verify_da515329(x10) != x11:
            continue
        return {"input": x10, "output": x11}
