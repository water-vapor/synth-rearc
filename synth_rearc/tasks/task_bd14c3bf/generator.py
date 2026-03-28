from synth_rearc.core import *

from .helpers import (
    SYMMETRIES_BD14C3BF,
    expand_binary_shape_bd14c3bf,
    matches_template_bd14c3bf,
    shape_indices_bd14c3bf,
)


TEMPLATE_SHAPES_BD14C3BF = (
    (
        (1, 0, 1),
        (1, 1, 1),
        (1, 0, 1),
    ),
    (
        (1, 1, 1),
        (1, 0, 0),
        (1, 1, 1),
    ),
    (
        (1, 1, 1),
        (1, 0, 1),
        (1, 1, 1),
    ),
    (
        (1, 1, 1, 1, 1),
        (1, 0, 1, 0, 1),
        (1, 1, 1, 1, 1),
    ),
)


def _repeat_factor_bd14c3bf() -> int:
    return choice((ONE, ONE, ONE, TWO, TWO))


def _sample_variant_bd14c3bf(template: Grid) -> Grid:
    x0 = choice(SYMMETRIES_BD14C3BF)(template)
    while True:
        x1 = tuple(_repeat_factor_bd14c3bf() for _ in range(len(x0)))
        x2 = tuple(_repeat_factor_bd14c3bf() for _ in range(len(x0[0])))
        x3 = expand_binary_shape_bd14c3bf(x0, x1, x2)
        if both(len(x3) <= SEVEN, len(x3[0]) <= SEVEN):
            return x3


def _sample_distractor_bd14c3bf(template: Grid) -> Grid:
    while True:
        x0 = choice(TEMPLATE_SHAPES_BD14C3BF)
        x1 = _sample_variant_bd14c3bf(x0)
        if not matches_template_bd14c3bf(x1, template):
            return x1


def _touches_existing_bd14c3bf(
    cells: Indices,
    occupied: set[IntegerTuple],
) -> bool:
    for cell in cells:
        if cell in occupied:
            return True
        if any(neighbor in occupied for neighbor in dneighbors(cell)):
            return True
    return False


def _place_shape_bd14c3bf(
    shape0: Grid,
    dims: tuple[int, int],
    occupied: set[IntegerTuple],
) -> IntegerTuple | None:
    x0 = len(shape0)
    x1 = len(shape0[0])
    x2 = [(i, j) for i in range(dims[0] - x0 + ONE) for j in range(dims[1] - x1 + ONE)]
    shuffle(x2)
    for x3 in x2:
        x4 = shape_indices_bd14c3bf(shape0, x3)
        if not _touches_existing_bd14c3bf(x4, occupied):
            return x3
    return None


def generate_bd14c3bf(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = choice(TEMPLATE_SHAPES_BD14C3BF)
        x1 = unifint(diff_lb, diff_ub, (15, 19))
        x2 = unifint(diff_lb, diff_ub, (15, 19))
        x3 = canvas(ZERO, (x1, x2))
        x4 = shape_indices_bd14c3bf(x0, ORIGIN)
        x5 = fill(x3, TWO, x4)
        x6 = x5
        x7 = set(x4)
        x8 = unifint(diff_lb, diff_ub, (2, 4))
        x9 = unifint(diff_lb, diff_ub, (2, 4))
        x10 = [(_sample_variant_bd14c3bf(x0), T) for _ in range(x8)]
        x11 = [(_sample_distractor_bd14c3bf(x0), F) for _ in range(x9)]
        x12 = x10 + x11
        shuffle(x12)
        x13 = F
        for x14, x15 in x12:
            x16 = _place_shape_bd14c3bf(x14, (x1, x2), x7)
            if x16 is None:
                x13 = T
                break
            x17 = shape_indices_bd14c3bf(x14, x16)
            x5 = fill(x5, ONE, x17)
            x18 = branch(x15, TWO, ONE)
            x6 = fill(x6, x18, x17)
            x7 |= set(x17)
        if x13:
            continue
        x19 = colorcount(x5, ZERO)
        x20 = colorcount(x5, ONE)
        if x19 <= x20:
            continue
        x21 = colorcount(x6, TWO)
        if x21 == size(x4):
            continue
        return {"input": x5, "output": x6}
