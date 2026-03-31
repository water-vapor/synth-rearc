from synth_rearc.core import *

from .helpers import build_example_79fb03f4
from .verifier import verify_79fb03f4


def generate_79fb03f4(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = build_example_79fb03f4(diff_lb, diff_ub)
        if verify_79fb03f4(x0["input"]) != x0["output"]:
            continue
        return x0
