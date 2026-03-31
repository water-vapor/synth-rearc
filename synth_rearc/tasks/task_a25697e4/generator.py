from synth_rearc.core import *

from .helpers import generate_template_input_a25697e4
from .verifier import verify_a25697e4


def generate_a25697e4(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = generate_template_input_a25697e4(diff_lb, diff_ub)
        x1 = verify_a25697e4(x0)
        if x0 == x1:
            continue
        return {"input": x0, "output": x1}
