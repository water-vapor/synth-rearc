from synth_rearc.core import *

from .helpers import LIBRARY_POSITIONS_D8E07EB2
from .helpers import LIBRARY_TILES_D8E07EB2
from .helpers import is_complete_line_d8e07eb2
from .helpers import render_input_d8e07eb2
from .helpers import render_output_d8e07eb2


def generate_d8e07eb2(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    del diff_lb, diff_ub
    while True:
        x0 = choice((True, True, False, False, False))
        if x0:
            x1 = choice((True, False))
            x2 = choice(interval(ZERO, FOUR, ONE))
            if x1:
                x3 = tuple((x2, x4) for x4 in interval(ZERO, FOUR, ONE))
            else:
                x3 = tuple((x4, x2) for x4 in interval(ZERO, FOUR, ONE))
        else:
            x1 = choice((THREE, FOUR, FOUR, FOUR, FOUR))
            x2 = sample(LIBRARY_POSITIONS_D8E07EB2, x1)
            x3 = tuple(x2)
            if is_complete_line_d8e07eb2(x3):
                continue
        x4 = list(x3)
        shuffle(x4)
        x5 = [LIBRARY_TILES_D8E07EB2[x6][x7] for x6, x7 in x4]
        x6 = [None] * FOUR
        x7 = sample(interval(ZERO, FOUR, ONE), len(x5))
        for x8, x9 in zip(x7, x5):
            x6[x8] = x9
        x10 = render_input_d8e07eb2(tuple(x6))
        x11 = render_output_d8e07eb2(x10)
        return {"input": x10, "output": x11}
