from synth_rearc.core import *

from .helpers import generate_input_b6f77b65, transform_grid_b6f77b65


def generate_b6f77b65(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    x0 = generate_input_b6f77b65(diff_lb, diff_ub)
    x1 = transform_grid_b6f77b65(x0)
    return {"input": x0, "output": x1}
