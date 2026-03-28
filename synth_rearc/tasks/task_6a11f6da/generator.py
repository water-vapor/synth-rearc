from synth_rearc.core import *

from .verifier import verify_6a11f6da


LAYER_SHAPE_6A11F6DA = (FIVE, FIVE)
CELL_OPTIONS_6A11F6DA = tuple(product(interval(ZERO, FIVE, ONE), interval(ZERO, FIVE, ONE)))
TOP_BOUNDS_6A11F6DA = (11, 15)
MIDDLE_BOUNDS_6A11F6DA = (9, 18)
BOTTOM_BOUNDS_6A11F6DA = (10, 15)


def _sample_layer_6a11f6da(
    diff_lb: float,
    diff_ub: float,
    color_value: Integer,
    bounds: tuple[Integer, Integer],
) -> Grid:
    x0 = unifint(diff_lb, diff_ub, bounds)
    x1 = frozenset(sample(CELL_OPTIONS_6A11F6DA, x0))
    x2 = canvas(ZERO, LAYER_SHAPE_6A11F6DA)
    x3 = fill(x2, color_value, x1)
    return x3


def _overlay_layers_6a11f6da(
    top: Grid,
    middle: Grid,
    bottom: Grid,
) -> Grid:
    x0 = canvas(ZERO, LAYER_SHAPE_6A11F6DA)
    x1 = fill(x0, EIGHT, ofcolor(middle, EIGHT))
    x2 = fill(x1, ONE, ofcolor(top, ONE))
    x3 = fill(x2, SIX, ofcolor(bottom, SIX))
    return x3


def generate_6a11f6da(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = _sample_layer_6a11f6da(diff_lb, diff_ub, ONE, TOP_BOUNDS_6A11F6DA)
        x1 = _sample_layer_6a11f6da(diff_lb, diff_ub, EIGHT, MIDDLE_BOUNDS_6A11F6DA)
        x2 = _sample_layer_6a11f6da(diff_lb, diff_ub, SIX, BOTTOM_BOUNDS_6A11F6DA)
        x3 = _overlay_layers_6a11f6da(x0, x1, x2)
        x4 = colorcount(x3, ZERO)
        x5 = colorcount(x3, ONE)
        x6 = colorcount(x3, EIGHT)
        x7 = colorcount(x3, SIX)
        if x4 < ONE or x4 > EIGHT:
            continue
        if x5 < THREE or x5 > TEN:
            continue
        if x6 < ONE or x6 > SIX:
            continue
        if x7 < EIGHT or x7 > 16:
            continue
        x8 = vconcat(vconcat(x0, x1), x2)
        if verify_6a11f6da(x8) != x3:
            continue
        return {"input": x8, "output": x3}
