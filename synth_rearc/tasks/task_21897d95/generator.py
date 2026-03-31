from synth_rearc.core import *

from .helpers import decode_clean_21897d95, make_example_21897d95, transpose_grid_21897d95


def generate_21897d95(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = make_example_21897d95(diff_lb, diff_ub)
        x1 = decode_clean_21897d95(x0["input"])
        x2 = transpose_grid_21897d95(x1)
        if x1 != x0["clean"]:
            continue
        if x2 != x0["output"]:
            continue
        return {"input": x0["input"], "output": x0["output"]}
