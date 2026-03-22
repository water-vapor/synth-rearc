from arc2.core import *

from .helpers import (
    CORNER_COLORS_85fa5666,
    paint_diagonal_ray_85fa5666,
    paint_input_block_85fa5666,
    rotated_corner_specs_from_colors_85fa5666,
)


def _frames_overlap_85fa5666(
    a: IntegerTuple,
    b: IntegerTuple,
) -> bool:
    x0, x1 = a
    x2, x3 = b
    return both(abs(subtract(x0, x2)) <= THREE, abs(subtract(x1, x3)) <= THREE)


def _sample_anchors_85fa5666(
    h: Integer,
    w: Integer,
    n: Integer,
) -> tuple[IntegerTuple, ...] | None:
    x0 = tuple(product(interval(ONE, subtract(h, TWO), ONE), interval(ONE, subtract(w, TWO), ONE)))
    x1 = tuple(sorted(x0))
    x2 = list(x1)
    shuffle(x2)
    x3: tuple[IntegerTuple, ...] = tuple()
    for x4 in x2:
        if all(not _frames_overlap_85fa5666(x4, x5) for x5 in x3):
            x3 = x3 + (x4,)
        if len(x3) == n:
            return tuple(sorted(x3))
    return None


def _build_output_85fa5666(
    dims: IntegerTuple,
    specs: tuple[tuple[IntegerTuple, tuple[int, int, int, int]], ...],
) -> Grid:
    x0 = canvas(ZERO, dims)
    for x1, _ in specs:
        x2, x3 = x1
        x0 = fill(
            x0,
            TWO,
            product(
                interval(x2, add(x2, TWO), ONE),
                interval(x3, add(x3, TWO), ONE),
            ),
        )
    for x1, x4 in specs:
        x5 = rotated_corner_specs_from_colors_85fa5666(x1, x4)
        for x6, x7, x8 in x5:
            x0 = paint_diagonal_ray_85fa5666(x0, x6, x8, x7)
    return x0


def generate_85fa5666(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = unifint(diff_lb, diff_ub, (EIGHT, 12))
        x1 = branch(choice((T, T, F)), x0, unifint(diff_lb, diff_ub, (EIGHT, 12)))
        x2 = minimum((THREE, divide(minimum((x0, x1)), FOUR)))
        x3 = choice(tuple(n for n in (ONE, ONE, TWO, TWO, THREE) if n <= x2))
        x4 = _sample_anchors_85fa5666(x0, x1, x3)
        if x4 is None:
            continue
        x5: tuple[tuple[IntegerTuple, tuple[int, int, int, int]], ...] = tuple()
        for x6 in x4:
            x7 = tuple(sample(CORNER_COLORS_85fa5666, FOUR))
            x5 = x5 + ((x6, x7),)
        x8 = canvas(ZERO, (x0, x1))
        for x9, x10 in x5:
            x8 = paint_input_block_85fa5666(x8, x9, x10)
        x11 = _build_output_85fa5666((x0, x1), x5)
        x12 = _build_output_85fa5666((x0, x1), tuple(reversed(x5)))
        if x11 != x12:
            continue
        return {"input": x8, "output": x11}
