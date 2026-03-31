from synth_rearc.core import *

from .helpers import build_example_64efde09
from .verifier import verify_64efde09


def generate_64efde09(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = build_example_64efde09(diff_lb, diff_ub)
        if verify_64efde09(x0["input"]) != x0["output"]:
            continue
        return x0
