from __future__ import annotations

from synth_rearc.core import *

from .helpers import render_output_abc82100
from .helpers import side_anchor_abc82100


PALETTE_ABC82100 = tuple(x0 for x0 in interval(ONE, TEN, ONE) if x0 != EIGHT)
POINT_ABC82100 = frozenset({(ZERO, ZERO)})
LINE3_H_ABC82100 = frozenset({(ZERO, ZERO), (ZERO, ONE), (ZERO, TWO)})
LINE3_V_ABC82100 = frozenset({(ZERO, ZERO), (ONE, ZERO), (TWO, ZERO)})
WEDGE_ABC82100 = frozenset({(ZERO, ONE), (ONE, ZERO), (TWO, ONE)})
DIAMOND4_ABC82100 = frozenset({(ZERO, ONE), (ONE, ZERO), (ONE, TWO), (TWO, ONE)})
ELBOW4_ABC82100 = frozenset({(ZERO, ONE), (ONE, ZERO), (ONE, ONE), (TWO, ONE)})
BIG_DOWN_ABC82100 = frozenset(
    {
        (ZERO, THREE),
        (ONE, TWO),
        (ONE, FOUR),
        (TWO, ONE),
        (TWO, FIVE),
        (THREE, ZERO),
        (THREE, SIX),
        (FOUR, ONE),
        (FOUR, FIVE),
        (FIVE, TWO),
        (FIVE, FOUR),
        (SIX, THREE),
    }
)
BIG_UP_ABC82100 = frozenset(
    {
        (ZERO, ZERO),
        (ZERO, FOUR),
        (ONE, ONE),
        (ONE, THREE),
        (TWO, TWO),
        (THREE, ONE),
        (THREE, THREE),
        (FOUR, ZERO),
        (FOUR, FOUR),
    }
)
MOTIF_LIBRARY_ABC82100 = (
    (POINT_ABC82100, LEFT),
    (POINT_ABC82100, LEFT),
    (LINE3_H_ABC82100, LEFT),
    (LINE3_H_ABC82100, LEFT),
    (LINE3_V_ABC82100, LEFT),
    (WEDGE_ABC82100, RIGHT),
    (WEDGE_ABC82100, RIGHT),
    (WEDGE_ABC82100, RIGHT),
    (DIAMOND4_ABC82100, LEFT),
    (DIAMOND4_ABC82100, LEFT),
    (ELBOW4_ABC82100, LEFT),
    (ELBOW4_ABC82100, LEFT),
    (BIG_DOWN_ABC82100, DOWN),
    (BIG_UP_ABC82100, UP),
)
PAYLOAD_LIBRARY_ABC82100 = (
    frozenset({(ZERO, ZERO), (ZERO, ONE), (ZERO, TWO), (ZERO, THREE), (ZERO, FOUR)}),
    frozenset({(ZERO, ZERO), (ZERO, TWO), (ZERO, FOUR), (ZERO, SIX), (ZERO, EIGHT)}),
    frozenset({(ZERO, ZERO), (ONE, ZERO), (TWO, ZERO), (THREE, ZERO), (FOUR, ZERO)}),
    frozenset({(ZERO, ZERO), (TWO, ZERO), (FOUR, ZERO), (SIX, ZERO)}),
    frozenset({(ZERO, ONE), (ONE, ZERO), (TWO, ONE), (THREE, ZERO), (FOUR, ONE)}),
    frozenset({(ZERO, TWO), (TWO, ZERO), (TWO, FOUR), (FOUR, TWO)}),
    frozenset({(ZERO, ZERO), (ONE, TWO), (TWO, ONE), (THREE, THREE)}),
    frozenset({(ZERO, ZERO), (ONE, ZERO), (TWO, ZERO), (THREE, ZERO), (FOUR, ZERO), (FIVE, ZERO), (SIX, ZERO)}),
)
PRESERVED_LIBRARY_ABC82100 = (
    frozenset({(ZERO, ZERO)}),
    frozenset({(ZERO, ZERO), (ZERO, ONE)}),
    frozenset({(ZERO, ZERO), (ONE, ZERO), (TWO, ZERO)}),
    frozenset({(ZERO, ZERO), (ONE, ONE)}),
)


def _normalize_indices_abc82100(
    patch: Indices,
) -> Indices:
    return shift(patch, (-uppermost(patch), -leftmost(patch)))


def _rot90_indices_abc82100(
    patch: Indices,
) -> Indices:
    x0 = height(patch)
    return frozenset((j, subtract(x0, increment(i))) for i, j in patch)


def _rotate_indices_abc82100(
    patch: Indices,
    turns: Integer,
) -> Indices:
    x0 = patch
    for _ in range(turns % FOUR):
        x0 = _normalize_indices_abc82100(_rot90_indices_abc82100(x0))
    return x0


def _rotate_direction_abc82100(
    direction: IntegerTuple,
    turns: Integer,
) -> IntegerTuple:
    x0 = (UP, RIGHT, DOWN, LEFT)
    x1 = x0.index(direction)
    return x0[(x1 + turns) % FOUR]


def _random_offset_abc82100(
    patch: Indices,
    dims: IntegerTuple,
) -> IntegerTuple | None:
    x0, x1 = dims
    x2 = -uppermost(patch)
    x3 = subtract(x0, increment(lowermost(patch)))
    x4 = -leftmost(patch)
    x5 = subtract(x1, increment(rightmost(patch)))
    if x2 > x3 or x4 > x5:
        return None
    return (randint(x2, x3), randint(x4, x5))


def _shifted_indices_abc82100(
    patch: Indices,
    offset: IntegerTuple,
) -> Indices:
    return frozenset((i + offset[ZERO], j + offset[ONE]) for i, j in patch)


def _legend_local_abc82100(
    component: Indices,
    anchor: IntegerTuple,
    direction: IntegerTuple,
) -> Indices:
    x0 = add(anchor, direction)
    x1 = add(x0, direction)
    return component | frozenset({x0, x1})


def _bbox_halo_abc82100(
    patch: Indices,
    dims: IntegerTuple,
    pad: Integer,
) -> Indices:
    x0, x1 = dims
    x2 = max(ZERO, uppermost(patch) - pad)
    x3 = max(ZERO, leftmost(patch) - pad)
    x4 = min(subtract(x0, ONE), lowermost(patch) + pad)
    x5 = min(subtract(x1, ONE), rightmost(patch) + pad)
    return frozenset((i, j) for i in range(x2, increment(x4)) for j in range(x3, increment(x5)))


def _stamped_output_abc82100(
    payload_cells: Indices,
    component: Indices,
    anchor: IntegerTuple,
    dims: IntegerTuple,
) -> Indices:
    x0, x1 = dims
    x2 = set()
    for x3 in payload_cells:
        x4 = subtract(x3, anchor)
        for x5 in component:
            x6 = add(x5, x4)
            if 0 <= x6[ZERO] < x0 and 0 <= x6[ONE] < x1:
                x2.add(x6)
    return frozenset(x2)


def _paint_indices_abc82100(
    grid: Grid,
    color_value: Integer,
    patch: Indices,
) -> Grid:
    return fill(grid, color_value, patch)


def _place_rule_abc82100(
    grid: Grid,
    dims: IntegerTuple,
    occupied_input: set[IntegerTuple],
    blocked_input: set[IntegerTuple],
    occupied_output: set[IntegerTuple],
    source_color: Integer,
    target_color: Integer,
) -> tuple[Grid, Indices, Indices, Indices] | None:
    for _ in range(300):
        x0, x1 = choice(MOTIF_LIBRARY_ABC82100)
        x2 = randint(ZERO, THREE)
        x3 = _rotate_indices_abc82100(x0, x2)
        x4 = _rotate_direction_abc82100(x1, x2)
        x5 = side_anchor_abc82100(x3, x4)
        x6 = choice(PAYLOAD_LIBRARY_ABC82100)
        x7 = _rotate_indices_abc82100(x6, randint(ZERO, THREE))
        if size(x3) >= NINE and len(x7) > FOUR:
            continue
        x8 = None
        x9 = None
        for _ in range(200):
            x10 = _random_offset_abc82100(x7, dims)
            if x10 is None:
                break
            x11 = _shifted_indices_abc82100(x7, x10)
            if len(x11 & frozenset(blocked_input)) > ZERO:
                continue
            x12 = _stamped_output_abc82100(x11, x3, x5, dims)
            if len(x12) == ZERO:
                continue
            if len(x12 & frozenset(occupied_output)) > ZERO:
                continue
            if len(x12) < max(ONE, size(x3) // TWO):
                continue
            x8 = x11
            x9 = x12
            break
        if x8 is None or x9 is None:
            continue
        x13 = _legend_local_abc82100(x3, x5, x4)
        for _ in range(200):
            x14 = _random_offset_abc82100(x13, dims)
            if x14 is None:
                break
            x15 = _shifted_indices_abc82100(x13, x14)
            x16 = _bbox_halo_abc82100(x15, dims, TWO)
            if len(x16 & frozenset(blocked_input | set(x8))) > ZERO:
                continue
            if len(x15 & x8) > ZERO:
                continue
            x17 = _shifted_indices_abc82100(x3, x14)
            x18 = add(x5, x14)
            x19 = add(x18, x4)
            x20 = add(x19, x4)
            x21 = grid
            x21 = _paint_indices_abc82100(x21, source_color, x8)
            x21 = _paint_indices_abc82100(x21, EIGHT, x17)
            x21 = _paint_indices_abc82100(x21, target_color, frozenset({x19}))
            x21 = _paint_indices_abc82100(x21, source_color, frozenset({x20}))
            return x21, x16, x8 | x15, x9
    return None


def _place_preserved_abc82100(
    grid: Grid,
    dims: IntegerTuple,
    occupied_input: set[IntegerTuple],
    blocked_input: set[IntegerTuple],
    occupied_output: set[IntegerTuple],
    color_value: Integer,
) -> tuple[Grid, Indices] | None:
    for _ in range(120):
        x0 = choice(PRESERVED_LIBRARY_ABC82100)
        x1 = _rotate_indices_abc82100(x0, randint(ZERO, THREE))
        x2 = _random_offset_abc82100(x1, dims)
        if x2 is None:
            continue
        x3 = _shifted_indices_abc82100(x1, x2)
        if len(x3 & frozenset(blocked_input)) > ZERO:
            continue
        if len(x3 & frozenset(occupied_output)) > ZERO:
            continue
        x4 = _paint_indices_abc82100(grid, color_value, x3)
        return x4, x3
    return None


def generate_abc82100(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = unifint(diff_lb, diff_ub, (12, 24))
        x1 = unifint(diff_lb, diff_ub, (12, 24))
        x2 = (x0, x1)
        x3 = canvas(ZERO, x2)
        x4 = min(FOUR, max(ONE, unifint(diff_lb, diff_ub, (ONE, FOUR))))
        x5 = list(PALETTE_ABC82100)
        shuffle(x5)
        if len(x5) < multiply(TWO, x4):
            continue
        x6 = tuple(x5[:x4])
        x7 = tuple(x5[x4:multiply(TWO, x4)])
        x8 = tuple(x5[multiply(TWO, x4):])
        x9: set[IntegerTuple] = set()
        x10: set[IntegerTuple] = set()
        x11: set[IntegerTuple] = set()
        x12 = True
        for x13, x14 in zip(x6, x7):
            x15 = _place_rule_abc82100(x3, x2, x9, x10, x11, x13, x14)
            if x15 is None:
                x12 = False
                break
            x3, x16, x17, x18 = x15
            x10 |= set(x16)
            x9 |= set(x17)
            x11 |= set(x18)
        if flip(x12):
            continue
        x19 = min(len(x8), choice((ZERO, ONE, ONE, TWO)))
        x20 = tuple(x8[:x19])
        x21 = True
        for x22 in x20:
            x23 = _place_preserved_abc82100(x3, x2, x9, x10, x11, x22)
            if x23 is None:
                x21 = False
                break
            x3, x24 = x23
            x9 |= set(x24)
            x11 |= set(x24)
        if flip(x21):
            continue
        x25 = render_output_abc82100(x3)
        if x25 == x3:
            continue
        return {
            "input": x3,
            "output": x25,
        }
