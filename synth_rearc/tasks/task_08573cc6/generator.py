from __future__ import annotations

from synth_rearc.core import *

from .helpers import render_spiral_08573cc6
from .verifier import verify_08573cc6


DRAW_COLORS_08573cc6 = remove(ONE, remove(ZERO, interval(ZERO, TEN, ONE)))


def _make_input_08573cc6(
    dimensions: IntegerTuple,
    marker: IntegerTuple,
    hcolor: Integer,
    vcolor: Integer,
) -> Grid:
    x0 = canvas(ZERO, dimensions)
    x1 = fill(x0, hcolor, frozenset({ORIGIN}))
    x2 = fill(x1, vcolor, frozenset({(ZERO, ONE)}))
    x3 = fill(x2, ONE, frozenset({marker}))
    return x3


def _good_output_08573cc6(
    grid: Grid,
    hcolor: Integer,
    vcolor: Integer,
) -> Boolean:
    x0 = colorcount(grid, hcolor)
    x1 = colorcount(grid, vcolor)
    return x0 >= FOUR and x1 >= THREE


def generate_08573cc6(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = unifint(diff_lb, diff_ub, (TEN, 15))
        x1 = (x0, x0)
        x2 = choice(DRAW_COLORS_08573cc6)
        x3 = choice(remove(x2, DRAW_COLORS_08573cc6))
        x4 = max(THREE, x0 // THREE)
        x5 = min(x0 - THREE, x0 // TWO + TWO)
        x6 = unifint(diff_lb, diff_ub, (x4, x5))
        x7 = unifint(diff_lb, diff_ub, (x4 - ONE, x5))
        x8 = (x6, x7)
        x9 = _make_input_08573cc6(x1, x8, x2, x3)
        x10 = render_spiral_08573cc6(x1, x8, x2, x3)
        if not _good_output_08573cc6(x10, x2, x3):
            continue
        if verify_08573cc6(x9) != x10:
            continue
        return {"input": x9, "output": x10}
