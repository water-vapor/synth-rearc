from synth_rearc.core import *

from .helpers import (
    PATTERN_BITS_BY_ACTIVE_COUNT_EEE78D87,
    pattern_patch_eee78d87,
    render_output_from_bits_eee78d87,
)


def generate_eee78d87(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    colors = tuple(value for value in range(TEN) if value not in (SEVEN, NINE))
    x0 = unifint(diff_lb, diff_ub, (ONE, THREE))
    x1 = choice(PATTERN_BITS_BY_ACTIVE_COUNT_EEE78D87[x0])
    x2 = choice(colors)
    x3 = randint(ZERO, THREE)
    x4 = randint(ZERO, THREE)
    x5 = shift(pattern_patch_eee78d87(x1), (x3, x4))
    x6 = canvas(SEVEN, (SIX, SIX))
    x7 = fill(x6, x2, x5)
    x8 = render_output_from_bits_eee78d87(x1, SEVEN)
    return {"input": x7, "output": x8}
