from synth_rearc.core import *

from .helpers import assemble_output_446ef5d2, extract_task_state_446ef5d2


def verify_446ef5d2(
    I: Grid,
) -> Grid:
    x0 = extract_task_state_446ef5d2(I)
    x1 = x0["grid"]
    x2 = assemble_output_446ef5d2(x1)
    return x2
