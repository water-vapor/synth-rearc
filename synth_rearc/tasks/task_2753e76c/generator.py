from __future__ import annotations

from synth_rearc.core import *

from .verifier import verify_2753e76c


GRID_SHAPE_2753E76C = (16, 16)
TASK_COLORS_2753E76C = (ONE, TWO, THREE, FOUR, EIGHT)
COUNT_PATTERNS_2753E76C = (
    (THREE, TWO, ONE),
    (FOUR, THREE, TWO, ONE),
    (FOUR, THREE, TWO, ONE),
    (FOUR, THREE, TWO),
    (FOUR, THREE, ONE),
    (FOUR, TWO, ONE),
    (FIVE, FOUR, TWO),
    (FIVE, FOUR, TWO),
    (FIVE, FOUR, ONE),
    (FIVE, THREE, TWO, ONE),
    (FIVE, THREE, TWO, ONE),
    (FIVE, THREE, TWO),
    (FIVE, THREE, ONE),
    (FIVE, TWO, ONE),
)


def _rect_patch_2753e76c(
    top: Integer,
    left: Integer,
    height_: Integer,
    width_: Integer,
) -> frozenset[tuple[int, int]]:
    return frozenset(
        (i, j)
        for i in range(top, top + height_)
        for j in range(left, left + width_)
    )


def _moat_patch_2753e76c(
    top: Integer,
    left: Integer,
    height_: Integer,
    width_: Integer,
) -> frozenset[tuple[int, int]]:
    return frozenset(
        (i, j)
        for i in range(top - ONE, top + height_ + ONE)
        for j in range(left - ONE, left + width_ + ONE)
        if 0 <= i < GRID_SHAPE_2753E76C[ZERO] and 0 <= j < GRID_SHAPE_2753E76C[ONE]
    )


def _output_from_pairs_2753e76c(
    pairs: tuple[tuple[int, int], ...],
) -> Grid:
    x0 = max(x1 for _, x1 in pairs)
    x2 = []
    for x3, x4 in pairs:
        x5 = canvas(ZERO, (ONE, x0))
        x6 = connect((ZERO, subtract(x0, x4)), (ZERO, decrement(x0)))
        x7 = fill(x5, x3, x6)
        x2.append(x7)
    x8 = x2[ZERO]
    for x9 in x2[ONE:]:
        x8 = vconcat(x8, x9)
    return x8


def _side_options_2753e76c(total_objects: Integer) -> tuple[int, ...]:
    if total_objects >= TEN:
        return (TWO, TWO, TWO, THREE, THREE, THREE, FOUR, FOUR)
    if total_objects >= EIGHT:
        return (TWO, TWO, THREE, THREE, THREE, FOUR, FOUR, FIVE)
    return (TWO, TWO, THREE, THREE, FOUR, FOUR, FIVE, FIVE)


def _sample_specs_2753e76c(
    pairs: tuple[tuple[int, int], ...],
) -> tuple[dict[str, int], ...]:
    x0 = sum(x1 for _, x1 in pairs)
    x2 = _side_options_2753e76c(x0)
    x3 = []
    for x4, x5 in pairs:
        for _ in range(x5):
            x6 = choice(x2)
            x7 = choice(x2)
            x3.append(
                {
                    "color": x4,
                    "height": x6,
                    "width": x7,
                    "area": x6 * x7,
                }
            )
    shuffle(x3)
    x3.sort(key=lambda x8: x8["area"], reverse=True)
    return tuple(x3)


def _place_specs_2753e76c(
    specs: tuple[dict[str, int], ...],
) -> Grid | None:
    x0 = canvas(ZERO, GRID_SHAPE_2753E76C)
    x1 = frozenset()
    for x2 in specs:
        x3 = x2["height"]
        x4 = x2["width"]
        x5 = []
        for x6 in range(GRID_SHAPE_2753E76C[ZERO] - x3 + ONE):
            for x7 in range(GRID_SHAPE_2753E76C[ONE] - x4 + ONE):
                x8 = _rect_patch_2753e76c(x6, x7, x3, x4)
                if x8 & x1:
                    continue
                x5.append((x8, x6, x7))
        if len(x5) == ZERO:
            return None
        x9, x10, x11 = choice(tuple(x5))
        x0 = fill(x0, x2["color"], x9)
        x1 = x1 | _moat_patch_2753e76c(x10, x11, x3, x4)
    return x0


def generate_2753e76c(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = choice(COUNT_PATTERNS_2753E76C)
        x1 = sample(TASK_COLORS_2753E76C, len(x0))
        x2 = tuple((x3, x4) for x3, x4 in zip(x1, x0))
        x3 = _sample_specs_2753e76c(x2)
        x4 = _place_specs_2753e76c(x3)
        if x4 is None:
            continue
        x5 = objects(x4, T, F, T)
        x6 = tuple(
            size(colorfilter(x5, x7))
            for x7 in tuple(x8 for x8, _ in x2)
        )
        if x6 != x0:
            continue
        x7 = sum(x8["area"] >= NINE for x8 in x3)
        if x7 == ZERO:
            continue
        x8 = _output_from_pairs_2753e76c(x2)
        if verify_2753e76c(x4) != x8:
            continue
        return {"input": x4, "output": x8}
