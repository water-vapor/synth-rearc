from arc2.core import *

from .helpers import passable_cells_b15fca0b, shortest_path_union_cells_b15fca0b


TRANSFORMS_B15FCA0B = (
    identity,
    rot90,
    rot180,
    rot270,
    hmirror,
    vmirror,
    lambda x: hmirror(rot90(x)),
    lambda x: vmirror(rot90(x)),
)


def _odd_width_b15fca0b(
    width_: Integer,
) -> Integer:
    if width_ % TWO == ONE:
        return width_
    if width_ == NINE:
        return width_ - ONE
    return width_ + ONE


def _build_opposite_b15fca0b(
    diff_lb: float,
    diff_ub: float,
) -> Grid:
    x0 = unifint(diff_lb, diff_ub, (TWO, THREE))
    x1 = unifint(diff_lb, diff_ub, (FIVE, NINE))
    x2 = tuple(randint(ONE, TWO) for _ in range(x0 + ONE))
    x3 = sum(x2) + x0
    x4 = add(x3, randint(ZERO, ONE))
    x5 = canvas(ZERO, (x4, x1))
    x6 = ZERO
    for x7 in range(x0):
        x6 += x2[x7]
        x8 = randint(ONE, min(TWO, x1 - THREE))
        if x7 % TWO == ZERO:
            x9 = frozenset((x6, x10) for x10 in range(x8, x1))
        else:
            x9 = frozenset((x6, x10) for x10 in range(ZERO, x1 - x8))
        x5 = fill(x5, ONE, x9)
        x6 += ONE
    x11 = x3 - ONE
    x12 = {(ZERO, x1 - ONE), (x11, ZERO)}
    x13 = fill(x5, TWO, x12)
    return x13


def _build_same_side_b15fca0b(
    diff_lb: float,
    diff_ub: float,
) -> Grid:
    x0 = unifint(diff_lb, diff_ub, (FIVE, EIGHT))
    x1 = _odd_width_b15fca0b(unifint(diff_lb, diff_ub, (FIVE, NINE)))
    x2 = randint(ONE, min(TWO, x0 - ONE))
    x3 = x0 - x2 - ONE
    x4 = canvas(ZERO, (x0, x1))
    for x5 in range(ONE, x1 - ONE, TWO):
        x6 = frozenset((x7, x5) for x7 in range(ZERO, x3 + ONE))
        x4 = fill(x4, ONE, x6)
    x8 = {(ZERO, ZERO), (ZERO, x1 - ONE)}
    x9 = fill(x4, TWO, x8)
    return x9


def _output_b15fca0b(
    I: Grid,
) -> tuple[Grid, Indices, Integer]:
    x0 = tuple(sorted(ofcolor(I, TWO)))
    x1 = x0[ZERO]
    x2 = x0[ONE]
    x3 = passable_cells_b15fca0b(I)
    x4 = ofcolor(I, ZERO)
    x5 = shape(I)
    x6, x7 = shortest_path_union_cells_b15fca0b(x3, x4, x1, x2, x5)
    x8 = fill(I, FOUR, x6)
    return x8, x6, x7


def generate_b15fca0b(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    x0 = (_build_opposite_b15fca0b, _build_same_side_b15fca0b)
    while True:
        x1 = choice(x0)
        x2 = x1(diff_lb, diff_ub)
        x3 = choice(TRANSFORMS_B15FCA0B)
        x4 = x3(x2)
        x5, x6, x7 = _output_b15fca0b(x4)
        x8, x9 = shape(x4)
        x10 = len(x6)
        x11 = colorcount(x4, ONE)
        if maximum((x8, x9)) > TEN:
            continue
        if x10 < max(FOUR, min(x8, x9) - ONE):
            continue
        if multiply(THREE, x10) > multiply(TWO, multiply(x8, x9)):
            continue
        if x10 > multiply(TWO, add(x8, x9)):
            continue
        if x11 < TWO:
            continue
        if colorcount(x5, ZERO) == ZERO:
            continue
        if x7 < add(x8, x9):
            continue
        return {"input": x4, "output": x5}
