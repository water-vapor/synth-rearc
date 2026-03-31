from synth_rearc.core import *

from .helpers import detect_layout_5dbc8537, render_output_5dbc8537


def verify_5dbc8537(I: Grid) -> Grid:
    x0, x1, x2, x3 = detect_layout_5dbc8537(I)
    x4 = render_output_5dbc8537(x0, x1, x2, x3)
    return x4
