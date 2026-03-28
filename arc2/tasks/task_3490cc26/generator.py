from arc2.core import *

from .helpers import (
    PATH_COLOR_3490CC26,
    SOURCE_COLOR_3490CC26,
    TARGET_COLOR_3490CC26,
    block_cells_3490cc26,
    block_loc_3490cc26,
    block_object_3490cc26,
    connector_indices_3490cc26,
    extract_blocks_3490cc26,
    next_visible_block_3490cc26,
    visible_gap_3490cc26,
)


MIN_SIDE_3490CC26 = 16
MAX_SIDE_3490CC26 = 30
MAX_CHAIN_BLOCKS_3490CC26 = 10
MAX_DISTRACTORS_3490CC26 = 3
MAX_BRANCH_DISTRACTORS_3490CC26 = 3
BUILD_TRIES_3490CC26 = 300
EXTEND_TRIES_3490CC26 = 80
DISTRACTOR_TRIES_3490CC26 = 200
BRANCH_TRIES_3490CC26 = 240
DIRECTIONS_3490CC26 = (UP, DOWN, LEFT, RIGHT)


def _in_bounds_3490cc26(
    loc: IntegerTuple,
    dims: IntegerTuple,
) -> bool:
    x0, x1 = loc
    x2, x3 = dims
    return 0 <= x0 < x2 - ONE and 0 <= x1 < x3 - ONE


def _step_loc_3490cc26(
    loc: IntegerTuple,
    direction: IntegerTuple,
    gap: Integer,
) -> IntegerTuple:
    x0, x1 = loc
    x2, x3 = direction
    x4 = add(gap, TWO)
    return (add(x0, multiply(x2, x4)), add(x1, multiply(x3, x4)))


def _gap_limit_3490cc26(
    loc: IntegerTuple,
    direction: IntegerTuple,
    dims: IntegerTuple,
) -> Integer:
    x0, x1 = loc
    x2, x3 = dims
    if direction == UP:
        return subtract(x0, TWO)
    if direction == DOWN:
        return subtract(subtract(x2, x0), FOUR)
    if direction == LEFT:
        return subtract(x1, TWO)
    return subtract(subtract(x3, x1), FOUR)


def _blocked_cells_3490cc26(
    cells: Indices,
) -> Indices:
    x0 = set(cells)
    for x1 in cells:
        x0 |= dneighbors(x1)
    return frozenset(x0)


def _choice_profile_3490cc26(
    gi: Grid,
) -> tuple[tuple[IntegerTuple, ...], tuple[Integer, ...], Indices]:
    x0 = extract_blocks_3490cc26(gi)
    x1 = first(tuple(x2 for x2 in x0 if color(x2) == SOURCE_COLOR_3490CC26))
    x2 = [block_loc_3490cc26(x1)]
    x3 = {x1}
    x4 = x1
    x5 = frozenset()
    x6 = []
    while True:
        x7 = tuple(x8 for x8 in x0 if x8 not in x3)
        x8 = tuple(
            x9
            for x9 in x7
            if visible_gap_3490cc26(x4, x9, x0) is not None
        )
        x6.append(len(x8))
        x7 = next_visible_block_3490cc26(x4, x7, x0)
        if x7 is None:
            break
        x5 = combine(x5, connector_indices_3490cc26(x4, x7))
        x3.add(x7)
        x4 = x7
        x2.append(block_loc_3490cc26(x7))
    return tuple(x2), tuple(x6), x5


def _walk_chain_3490cc26(
    gi: Grid,
) -> tuple[tuple[IntegerTuple, ...], Indices]:
    x0, _, x1 = _choice_profile_3490cc26(gi)
    return x0, x1


def _render_input_3490cc26(
    dims: IntegerTuple,
    chain_locs: tuple[IntegerTuple, ...],
    distractor_locs: tuple[IntegerTuple, ...],
) -> Grid:
    x0 = canvas(ZERO, dims)
    x1 = fill(x0, SOURCE_COLOR_3490CC26, block_cells_3490cc26(first(chain_locs)))
    x2 = tuple(chain_locs[ONE:]) + distractor_locs
    for x3 in x2:
        x1 = fill(x1, TARGET_COLOR_3490CC26, block_cells_3490cc26(x3))
    return x1


def _build_chain_3490cc26(
    dims: IntegerTuple,
    n_blocks: Integer,
) -> tuple[IntegerTuple, ...] | None:
    x0, x1 = dims
    for _ in range(BUILD_TRIES_3490CC26):
        x2 = (randint(ZERO, subtract(x0, TWO)), randint(ZERO, subtract(x1, TWO)))
        x3 = [x2]
        x4 = set(block_cells_3490cc26(x2))
        x5 = set()
        x6 = _blocked_cells_3490cc26(block_cells_3490cc26(x2))
        x7 = None
        x8 = T
        while len(x3) < n_blocks:
            x9 = [x10 for x10 in DIRECTIONS_3490CC26 if x10 != invert(x7)] if x7 is not None else list(DIRECTIONS_3490CC26)
            shuffle(x9)
            x10 = F
            for _ in range(EXTEND_TRIES_3490CC26):
                x11 = x9[randint(ZERO, subtract(len(x9), ONE))]
                x12 = _gap_limit_3490cc26(last(x3), x11, dims)
                if x12 < ONE:
                    continue
                x13 = randint(ONE, min(NINE, x12))
                x14 = _step_loc_3490cc26(last(x3), x11, x13)
                if not _in_bounds_3490cc26(x14, dims):
                    continue
                x15 = block_cells_3490cc26(x14)
                if any(x16 in x6 for x16 in x15):
                    continue
                x16 = block_object_3490cc26(TARGET_COLOR_3490CC26, last(x3))
                x17 = block_object_3490cc26(TARGET_COLOR_3490CC26, x14)
                x18 = connector_indices_3490cc26(x16, x17)
                if len(x18) == ZERO:
                    continue
                if any(x19 in x4 for x19 in x18):
                    continue
                if any(x19 in x5 for x19 in x18):
                    continue
                x3.append(x14)
                x4 |= set(x15)
                x5 |= set(x18)
                x6 |= set(_blocked_cells_3490cc26(x15))
                x7 = x11
                x10 = T
                break
            if not x10:
                x8 = F
                break
        if x8:
            return tuple(x3)
    return None


def _direction_3490cc26(
    start: IntegerTuple,
    end: IntegerTuple,
) -> IntegerTuple:
    x0, x1 = start
    x2, x3 = end
    if x0 == x2:
        return LEFT if x3 < x1 else RIGHT
    return UP if x2 < x0 else DOWN


def _desired_branch_steps_3490cc26(
    chain_locs: tuple[IntegerTuple, ...],
) -> Integer:
    x0 = len(chain_locs)
    if x0 >= EIGHT:
        return TWO
    if x0 >= SIX:
        return randint(ONE, TWO)
    return ONE


def _place_branch_distractors_3490cc26(
    dims: IntegerTuple,
    chain_locs: tuple[IntegerTuple, ...],
    reserved_cells: Indices,
    reserved_lines: Indices,
    branch_target: Integer,
) -> tuple[tuple[IntegerTuple, ...], Indices] | None:
    x0 = []
    x1 = set(reserved_cells)
    x2 = set(reserved_lines)
    x3 = set()
    for x4 in chain_locs:
        x3 |= set(block_cells_3490cc26(x4))
    x4 = _render_input_3490cc26(dims, chain_locs, tuple(x0))
    _, x5, _ = _choice_profile_3490cc26(x4)
    x6 = sum(x7 > ONE for x7 in x5)
    if x6 >= branch_target:
        return tuple(x0), frozenset(x2)
    for _ in range(MAX_BRANCH_DISTRACTORS_3490CC26):
        if x6 >= branch_target:
            break
        x7 = F
        for _ in range(BRANCH_TRIES_3490CC26):
            x8 = randint(ZERO, subtract(len(chain_locs), TWO))
            x9 = chain_locs[x8]
            x10 = chain_locs[increment(x8)]
            x11 = _direction_3490cc26(x9, x10)
            x12 = abs(x9[ZERO] - x10[ZERO]) + abs(x9[ONE] - x10[ONE]) - TWO
            x13 = [x14 for x14 in DIRECTIONS_3490CC26 if x14 != x11]
            shuffle(x13)
            x14 = x13[ZERO]
            x15 = _gap_limit_3490cc26(x9, x14, dims)
            x16 = add(x12, ONE)
            if x15 < x16:
                continue
            x17 = randint(x16, x15)
            x18 = _step_loc_3490cc26(x9, x14, x17)
            if not _in_bounds_3490cc26(x18, dims):
                continue
            x19 = block_cells_3490cc26(x18)
            if any(x20 in x1 for x20 in x19):
                continue
            if any(x20 in x2 for x20 in x19):
                continue
            x20 = block_object_3490cc26(TARGET_COLOR_3490CC26, x9)
            x21 = block_object_3490cc26(TARGET_COLOR_3490CC26, x18)
            x22 = connector_indices_3490cc26(x20, x21)
            if len(x22) == ZERO:
                continue
            if any(x23 in x3 for x23 in x22):
                continue
            if any(x23 in x2 for x23 in x22):
                continue
            x23 = tuple(x0) + (x18,)
            x24 = _render_input_3490cc26(dims, chain_locs, x23)
            x25, x26, _ = _choice_profile_3490cc26(x24)
            x27 = sum(x28 > ONE for x28 in x26)
            if x25 != chain_locs:
                continue
            if x27 <= x6:
                continue
            x0.append(x18)
            x1 |= set(_blocked_cells_3490cc26(x19))
            x2 |= set(x22)
            x3 |= set(x19)
            x6 = x27
            x7 = T
            break
        if not x7:
            break
    if x6 < branch_target:
        return None
    return tuple(x0), frozenset(x2)


def _place_distractors_3490cc26(
    dims: IntegerTuple,
    reserved_cells: Indices,
    reserved_lines: Indices,
    n_distractors: Integer,
) -> tuple[IntegerTuple, ...] | None:
    x0, x1 = dims
    x2 = set(reserved_cells)
    x3 = set(reserved_lines)
    x4 = []
    for _ in range(n_distractors):
        x5 = F
        for _ in range(DISTRACTOR_TRIES_3490CC26):
            x6 = (randint(ZERO, subtract(x0, TWO)), randint(ZERO, subtract(x1, TWO)))
            x7 = block_cells_3490cc26(x6)
            if any(x8 in x2 for x8 in x7):
                continue
            if any(x8 in x3 for x8 in x7):
                continue
            x4.append(x6)
            x2 |= set(_blocked_cells_3490cc26(x7))
            x5 = T
            break
        if not x5:
            return None
    return tuple(x4)


def generate_3490cc26(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = unifint(diff_lb, diff_ub, (MIN_SIDE_3490CC26, MAX_SIDE_3490CC26))
        x1 = unifint(diff_lb, diff_ub, (MIN_SIDE_3490CC26, MAX_SIDE_3490CC26))
        x2 = (x0, x1)
        x3 = unifint(diff_lb, diff_ub, (TWO, MAX_CHAIN_BLOCKS_3490CC26))
        x4 = _build_chain_3490cc26(x2, x3)
        if x4 is None:
            continue
        x5 = set()
        x6 = set()
        for x7 in x4:
            x5 |= set(_blocked_cells_3490cc26(block_cells_3490cc26(x7)))
        for x7, x8 in zip(x4, x4[ONE:]):
            x9 = block_object_3490cc26(TARGET_COLOR_3490CC26, x7)
            x10 = block_object_3490cc26(TARGET_COLOR_3490CC26, x8)
            x6 |= set(connector_indices_3490cc26(x9, x10))
        x7 = _desired_branch_steps_3490cc26(x4)
        x8 = _place_branch_distractors_3490cc26(x2, x4, frozenset(x5), frozenset(x6), x7)
        if x8 is None:
            continue
        x9, x10 = x8
        for x11 in x9:
            x5 |= set(_blocked_cells_3490cc26(block_cells_3490cc26(x11)))
        x6 = set(x10)
        x11 = subtract(MAX_DISTRACTORS_3490CC26, len(x9))
        x12 = ZERO if x11 == ZERO else unifint(diff_lb, diff_ub, (ZERO, x11))
        x13 = _place_distractors_3490cc26(x2, frozenset(x5), frozenset(x6), x12)
        if x13 is None:
            continue
        gi = _render_input_3490cc26(x2, x4, x9 + x13)
        x14, x15, x16 = _choice_profile_3490cc26(gi)
        if x14 != x4:
            continue
        if sum(x17 > ONE for x17 in x15) < x7:
            continue
        go = fill(gi, PATH_COLOR_3490CC26, x16)
        return {"input": gi, "output": go}
