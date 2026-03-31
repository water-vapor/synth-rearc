from synth_rearc.core import *

from .helpers import mutate_centers_2b83f449
from .helpers import render_input_2b83f449
from .helpers import render_output_2b83f449
from .helpers import sample_even_holes_2b83f449


def generate_2b83f449(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        odd_row_count = unifint(diff_lb, diff_ub, (5, 9))
        height = odd_row_count * TWO + ONE
        width = unifint(diff_lb, diff_ub, (15, 22))
        odd_rows: list[tuple[int, ...]] = []
        previous: tuple[int, ...] | None = None
        for idx in range(odd_row_count):
            allow_empty = idx not in (ZERO, odd_row_count - ONE)
            centers = mutate_centers_2b83f449(width, previous, allow_empty=allow_empty)
            odd_rows.append(centers)
            if centers:
                previous = centers
        if sum(ONE for centers in odd_rows if centers) < THREE:
            continue
        even_holes = sample_even_holes_2b83f449(height, width)
        gi = render_input_2b83f449(height, width, tuple(odd_rows), even_holes)
        go = render_output_2b83f449(gi)
        if colorcount(go, THREE) == ZERO or colorcount(go, SIX) == ZERO:
            continue
        if gi == go:
            continue
        return {"input": gi, "output": go}
