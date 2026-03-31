from synth_rearc.core import *

from .helpers import generate_input_4a21e3da
from .verifier import verify_4a21e3da


def generate_4a21e3da(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    x0 = generate_input_4a21e3da(diff_lb, diff_ub)
    x1 = verify_4a21e3da(x0)
    return {"input": x0, "output": x1}
