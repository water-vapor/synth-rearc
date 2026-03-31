from synth_rearc.core import *

from .helpers import parse_turns_e87109e9
from .helpers import render_output_e87109e9
from .helpers import strip_header_e87109e9


def verify_e87109e9(
    I: Grid,
) -> Grid:
    x0 = parse_turns_e87109e9(I)
    x1 = strip_header_e87109e9(I)
    x2 = render_output_e87109e9(x1, x0)
    return x2
