from synth_rearc.core import *

from .helpers import apply_path_3e6067c3
from .helpers import extract_state_3e6067c3
from .helpers import recover_path_3e6067c3


def verify_3e6067c3(
    I: Grid,
) -> Grid:
    x0 = extract_state_3e6067c3(I)
    x1, _ = recover_path_3e6067c3(I, x0)
    x2 = tuple(x0.blocks[x3] for x3 in x1)
    x3 = apply_path_3e6067c3(I, x2)
    return x3
