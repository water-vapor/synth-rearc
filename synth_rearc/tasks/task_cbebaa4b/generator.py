from synth_rearc.core import *

from .helpers import (
    choose_output_layout_cbebaa4b,
    render_layout_cbebaa4b,
    scatter_input_layout_cbebaa4b,
)


def generate_cbebaa4b(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        shape, output_layout = choose_output_layout_cbebaa4b(diff_lb, diff_ub)
        input_layout = scatter_input_layout_cbebaa4b(shape, output_layout)
        if input_layout is None:
            continue
        gi = render_layout_cbebaa4b(shape, input_layout)
        go = render_layout_cbebaa4b(shape, output_layout)
        if gi == go:
            continue
        return {"input": gi, "output": go}
