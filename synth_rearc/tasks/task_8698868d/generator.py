from __future__ import annotations

from synth_rearc.core import *

from .helpers import ORIENTATION_POOL_8698868D
from .helpers import assemble_output_8698868d
from .helpers import build_family_example_8698868d


def _sample_family_size_8698868d(
    diff_lb: float,
    diff_ub: float,
) -> Integer:
    x0 = unifint(diff_lb, diff_ub, (0, 2))
    return (2, 4, 6)[x0]


def generate_8698868d(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    x0 = _sample_family_size_8698868d(diff_lb, diff_ub)
    x1 = build_family_example_8698868d(x0)
    x2 = choice(ORIENTATION_POOL_8698868D)
    x3 = x2(x1)
    x4 = assemble_output_8698868d(x3)
    return {"input": x3, "output": x4}
