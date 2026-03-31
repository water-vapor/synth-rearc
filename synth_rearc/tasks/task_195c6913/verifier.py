from synth_rearc.core import *

from .helpers import extract_task_parts_195c6913
from .helpers import trace_paths_195c6913


def verify_195c6913(
    I: Grid,
) -> Grid:
    x0, x1, x2, x3, x4, x5 = extract_task_parts_195c6913(I)
    x6 = trace_paths_195c6913(x0, x1, x2, x3, x5)
    return x6
