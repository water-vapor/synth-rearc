from synth_rearc.core import *

from .helpers import SIDES_80A900E0, cell_map_in_bounds_80a900e0
from .helpers import checkerboard_80a900e0, motif_cell_map_80a900e0
from .helpers import paint_cell_map_80a900e0
from .helpers import render_output_80a900e0


NON_BG_COLORS_80A900E0 = tuple(range(TWO, TEN))


def _segment_values_80a900e0(
    axis_values: tuple[Integer, ...],
) -> tuple[Integer, ...]:
    x0 = choice((THREE, THREE, THREE, TWO, TWO))
    if x0 == THREE:
        return axis_values
    return axis_values[:TWO] if choice((T, F)) else axis_values[ONE:]


def _segment_color_map_80a900e0(
    sides: tuple[str, ...],
    center_color: Integer,
) -> dict[str, Integer]:
    x0 = tuple(color for color in NON_BG_COLORS_80A900E0 if color != center_color)
    x1 = {}
    if "left" in sides and "right" in sides and uniform(0.0, 1.0) < 0.5:
        x2 = choice(x0)
        x1["left"] = x2
        x1["right"] = x2
    if "top" in sides and "bottom" in sides and uniform(0.0, 1.0) < 0.5:
        x2 = choice(x0)
        x1["top"] = x2
        x1["bottom"] = x2
    for side in sides:
        if side not in x1:
            x1[side] = choice(x0)
    return x1


def _candidate_segments_80a900e0(
    us: tuple[Integer, ...],
    vs: tuple[Integer, ...],
    center_color: Integer,
) -> tuple[tuple[str, Integer, tuple[Integer, ...]], ...]:
    x0 = randint(TWO, FOUR)
    x1 = tuple(sample(SIDES_80A900E0, x0))
    x2 = _segment_color_map_80a900e0(x1, center_color)
    x3 = []
    for side in SIDES_80A900E0:
        if side not in x1:
            continue
        x4 = vs if side in ("left", "right") else us
        x5 = _segment_values_80a900e0(x4)
        x3.append((side, x2[side], x5))
    return tuple(x3)


def _sample_uv_ranges_80a900e0(
    dims: IntegerTuple,
) -> tuple[Integer, ...] | None:
    x0, x1 = dims
    x2 = tuple(range(-x1 + ONE, x0, TWO))
    x3 = tuple(range(ZERO, add(add(x0, x1), -ONE), TWO))
    if len(x2) == ZERO or len(x3) == ZERO:
        return None
    for _ in range(80):
        x4 = choice(x3)
        x5 = choice(x2)
        x6 = (x4, x4 + TWO, x4 + FOUR)
        x7 = (x5, x5 + TWO, x5 + FOUR)
        return x6, x7
    return None


def _sample_motif_grid_80a900e0(
    dims: IntegerTuple,
) -> tuple[Grid, Grid] | None:
    x0 = checkerboard_80a900e0(dims)
    for _ in range(400):
        x1 = _sample_uv_ranges_80a900e0(dims)
        if x1 is None:
            return None
        x2, x3 = x1
        x4 = choice(NON_BG_COLORS_80A900E0)
        x5 = _candidate_segments_80a900e0(x2, x3, x4)
        x6 = motif_cell_map_80a900e0(x2, x3, x4, x5)
        if not cell_map_in_bounds_80a900e0(x6, dims):
            continue
        x7 = paint_cell_map_80a900e0(x0, x6)
        x8 = render_output_80a900e0(x7)
        if x7 == x8:
            continue
        return x7, x8
    return None


def generate_80a900e0(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = randint(18, 30)
        x1 = randint(18, 30)
        x2 = (x0, x1)
        x3 = _sample_motif_grid_80a900e0(x2)
        if x3 is None:
            continue
        x4, x5 = x3
        if x5 == x4:
            continue
        return {"input": x4, "output": x5}
