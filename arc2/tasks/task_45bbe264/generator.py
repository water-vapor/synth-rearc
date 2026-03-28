from arc2.core import *

from .verifier import verify_45bbe264


Seed45bbe264 = tuple[int, int, int]
GRID_BOUNDS_45BBE264 = (13, 17)
SEED_COUNTS_45BBE264 = (TWO, TWO, THREE, THREE)
ALLOWED_COLORS_45BBE264 = (ONE, THREE, FOUR, FIVE, SEVEN, EIGHT)


def _sample_axis_45bbe264(
    dim: int,
    count: int,
) -> tuple[int, ...]:
    x0 = tuple(range(ONE, dim - ONE))
    while True:
        x1 = tuple(sample(x0, count))
        x2 = tuple(sorted(x1))
        x3 = tuple(x2[i + ONE] - x2[i] for i in range(len(x2) - ONE))
        if all(x4 > ONE for x4 in x3):
            return x1


def _render_input_45bbe264(
    dim: int,
    seeds: tuple[Seed45bbe264, ...],
) -> Grid:
    x0 = canvas(ZERO, (dim, dim))
    x1 = frozenset((x4, (x2, x3)) for x2, x3, x4 in seeds)
    x2 = paint(x0, x1)
    return x2


def _render_output_45bbe264(
    dim: int,
    seeds: tuple[Seed45bbe264, ...],
) -> Grid:
    x0 = canvas(ZERO, (dim, dim))
    x1 = x0
    for x2, x3, x4 in seeds:
        x5 = astuple(x2, x3)
        x6 = recolor(x4, hfrontier(x5))
        x7 = recolor(x4, vfrontier(x5))
        x8 = combine(x6, x7)
        x1 = paint(x1, x8)
    x9 = tuple(x10 for x10, _, _ in seeds)
    x10 = tuple(x11 for _, x11, _ in seeds)
    x11 = frozenset((x12, x13) for x12, x13, _ in seeds)
    x12 = difference(product(x9, x10), x11)
    x13 = fill(x1, TWO, x12)
    x14 = frozenset((x17, (x15, x16)) for x15, x16, x17 in seeds)
    x15 = paint(x13, x14)
    return x15


def generate_45bbe264(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = unifint(diff_lb, diff_ub, GRID_BOUNDS_45BBE264)
        x1 = choice(SEED_COUNTS_45BBE264)
        x2 = _sample_axis_45bbe264(x0, x1)
        x3 = _sample_axis_45bbe264(x0, x1)
        x4 = tuple(sample(ALLOWED_COLORS_45BBE264, x1))
        x5 = tuple((x6, x7, x8) for x6, x7, x8 in zip(x2, x3, x4))
        x6 = _render_input_45bbe264(x0, x5)
        x7 = _render_output_45bbe264(x0, x5)
        if verify_45bbe264(x6) != x7:
            continue
        return {"input": x6, "output": x7}
