from synth_rearc.core import *

from .helpers import build_example_4e34c42c
from .verifier import verify_4e34c42c


def generate_4e34c42c(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = build_example_4e34c42c(diff_lb, diff_ub)
        x1 = x0["input"]
        x2 = x0["output"]
        if verify_4e34c42c(x1) != x2:
            continue
        return x0
