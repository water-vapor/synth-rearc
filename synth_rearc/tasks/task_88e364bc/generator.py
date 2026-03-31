from __future__ import annotations

from synth_rearc.core import *

from .verifier import verify_88e364bc


ORTHO_DIRECTIONS_88E364BC = (UP, RIGHT, DOWN, LEFT)
DIAGONAL_DIRECTIONS_88E364BC = ((ONE, ONE), (ONE, NEG_ONE), (NEG_ONE, NEG_ONE), (NEG_ONE, ONE))


def _east_template_88e364bc(
    main_color: Integer,
    aux_color: Integer,
) -> Grid:
    x0 = canvas(main_color, (FIVE, FIVE))
    x1 = frozenset({(ONE, ONE), (ONE, TWO), (THREE, ONE), (THREE, TWO)})
    x2 = frozenset({(ONE, THREE), (THREE, THREE)})
    x3 = fill(x0, aux_color, x1)
    x4 = fill(x3, TWO, x2)
    return x4


def _southeast_template_88e364bc(
    main_color: Integer,
    aux_color: Integer,
) -> Grid:
    x0 = canvas(main_color, (SIX, SEVEN))
    x1 = frozenset({(ONE, THREE), (TWO, ONE), (TWO, FOUR), (THREE, TWO)})
    x2 = frozenset({(THREE, FIVE), (FOUR, THREE)})
    x3 = fill(x0, aux_color, x1)
    x4 = fill(x3, TWO, x2)
    return x4


def _template_88e364bc(
    main_color: Integer,
    aux_color: Integer,
    direction: IntegerTuple,
) -> Grid:
    if direction in ORTHO_DIRECTIONS_88E364BC:
        x0 = _east_template_88e364bc(main_color, aux_color)
        if direction == RIGHT:
            return x0
        if direction == DOWN:
            return rot90(x0)
        if direction == LEFT:
            return rot180(x0)
        return rot270(x0)
    x1 = _southeast_template_88e364bc(main_color, aux_color)
    if direction == (ONE, ONE):
        return x1
    if direction == (ONE, NEG_ONE):
        return rot90(x1)
    if direction == (NEG_ONE, NEG_ONE):
        return rot180(x1)
    return rot270(x1)


def _contact_direction_88e364bc(
    direction: IntegerTuple,
) -> IntegerTuple:
    if ZERO in direction:
        return direction
    return (ZERO, ONE if direction[ONE] > ZERO else NEG_ONE)


def _random_path_patch_88e364bc(
    diff_lb: float,
    diff_ub: float,
) -> Indices:
    x0 = unifint(diff_lb, diff_ub, (SEVEN, 11))
    x1 = {(randint(TWO, add(x0, ONE)), randint(TWO, add(x0, ONE)))}
    for _ in range(unifint(diff_lb, diff_ub, (SIX, TEN))):
        x2 = choice(tuple(x1))
        x3 = choice(ORTHO_DIRECTIONS_88E364BC)
        x4 = unifint(diff_lb, diff_ub, (TWO, FIVE))
        x5 = add(x2, multiply(x3, x4))
        x6 = connect(x2, x5)
        if not all(ONE <= i < add(x0, THREE) and ONE <= j < add(x0, THREE) for i, j in x6):
            continue
        x1 |= set(x6)
    for _ in range(choice((ZERO, ONE, ONE, TWO))):
        x7 = choice(tuple(x1))
        x8 = choice(ORTHO_DIRECTIONS_88E364BC)
        x9 = unifint(diff_lb, diff_ub, (ONE, THREE))
        x10 = add(x7, multiply(x8, x9))
        x11 = connect(x7, x10)
        if not all(ONE <= i < add(x0, THREE) and ONE <= j < add(x0, THREE) for i, j in x11):
            continue
        x1 |= set(x11)
    x12 = frozenset(x1)
    if size(x12) < TEN:
        return _random_path_patch_88e364bc(diff_lb, diff_ub)
    return normalize(x12)


def _pad_88e364bc(
    patch: Indices,
) -> Indices:
    x0 = set(patch)
    for x1 in patch:
        x0 |= neighbors(x1)
    return frozenset(x0)


def _nonzero_indices_88e364bc(
    grid: Grid,
) -> Indices:
    return frozenset((i, j) for i, row in enumerate(grid) for j, value in enumerate(row) if value != ZERO)


def _place_patch_88e364bc(
    grid: Grid,
    patch: Indices,
) -> Indices | None:
    x0 = normalize(patch)
    x1 = height(x0)
    x2 = width(x0)
    x3 = len(grid)
    x4 = len(grid[ZERO])
    x5 = _pad_88e364bc(_nonzero_indices_88e364bc(grid))
    for _ in range(200):
        x6 = randint(ZERO, subtract(x3, x1))
        x7 = randint(ZERO, subtract(x4, x2))
        x8 = shift(x0, (x6, x7))
        x9 = toindices(x8)
        if x9 & x5:
            continue
        return x9
    return None


def _template_anchor_88e364bc(
    dims: IntegerTuple,
    corner_name: str,
    grid_dims: IntegerTuple,
) -> IntegerTuple:
    x0, x1 = dims
    x2, x3 = grid_dims
    if corner_name == "ul":
        return (ZERO, ZERO)
    if corner_name == "ur":
        return (ZERO, subtract(x3, x1))
    if corner_name == "ll":
        return (subtract(x2, x0), ZERO)
    return (subtract(x2, x0), subtract(x3, x1))


def _marker_candidates_88e364bc(
    grid: Grid,
    patch: Indices,
    direction: IntegerTuple,
) -> tuple[tuple[IntegerTuple, tuple[IntegerTuple, ...]], ...]:
    x0 = []
    x1 = _contact_direction_88e364bc(direction)
    for x2 in patch:
        x3 = subtract(x2, x1)
        if index(grid, x3) != ZERO:
            continue
        x4 = []
        x5 = subtract(x3, direction)
        while index(grid, x5) == ZERO:
            x4.append(x5)
            x5 = subtract(x5, direction)
        if len(x4) == ZERO:
            continue
        x0.append((x3, tuple(x4)))
    return tuple(dedupe(tuple(x0)))


def _choose_markers_88e364bc(
    candidates: tuple[tuple[IntegerTuple, tuple[IntegerTuple, ...]], ...],
    amount: Integer,
) -> tuple[tuple[IntegerTuple, IntegerTuple], ...]:
    x0 = list(candidates)
    shuffle(x0)
    x1 = []
    x2 = set()
    for x3, x4 in x0:
        if x3 in x2:
            continue
        x5 = [x6 for x6 in x4 if x6 not in x2]
        if len(x5) == ZERO:
            continue
        x7 = max(ONE, len(x5) // TWO)
        x8 = choice(x5[-x7:])
        x1.append((x8, x3))
        x2.add(x3)
        x2.add(x8)
        if len(x1) == amount:
            break
    return tuple(x1)


def _paint_template_88e364bc(
    grid: Grid,
    template: Grid,
    anchor: IntegerTuple,
) -> Grid:
    x0 = asobject(template)
    x1 = shift(x0, anchor)
    x2 = paint(grid, x1)
    return x2


def generate_88e364bc(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = (20, 20)
        x1 = canvas(ZERO, x0)
        x2 = choice((ONE, ONE, TWO))
        x3 = [color for color in range(ONE, TEN) if color not in (TWO, FOUR)]
        shuffle(x3)
        x4 = []
        x5 = ("ul", "ur", "ll", "lr")
        x6 = list(x5)
        shuffle(x6)
        x7 = list(ORTHO_DIRECTIONS_88E364BC + DIAGONAL_DIRECTIONS_88E364BC)
        shuffle(x7)
        x8 = True
        for x9 in range(x2):
            x10 = x3.pop()
            x11 = x3.pop()
            x12 = x7.pop()
            x13 = _template_88e364bc(x10, x11, x12)
            x14 = _template_anchor_88e364bc(shape(x13), x6.pop(), x0)
            x1 = _paint_template_88e364bc(x1, x13, x14)
            x15 = _random_path_patch_88e364bc(diff_lb, diff_ub)
            x16 = _place_patch_88e364bc(x1, x15)
            if x16 is None:
                x8 = False
                break
            x1 = fill(x1, x10, x16)
            x4.append((x10, x12, x16))
        if not x8:
            continue
        x20 = x1
        x21 = x1
        for x22, x23, x24 in x4:
            x25 = choice((ONE, TWO, TWO, THREE))
            x26 = _marker_candidates_88e364bc(x1, x24, x23)
            x27 = _choose_markers_88e364bc(x26, x25)
            if len(x27) < ONE:
                x8 = False
                break
            x28 = frozenset(x29 for x29, _ in x27)
            x29 = frozenset(x30 for _, x30 in x27)
            x20 = fill(x20, FOUR, x28)
            x21 = fill(x21, FOUR, x29)
        if not x8:
            continue
        if x20 == x21:
            continue
        if verify_88e364bc(x20) != x21:
            continue
        return {"input": x20, "output": x21}
