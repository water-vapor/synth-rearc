from arc2.core import *

from .verifier import verify_6bcdb01e


LEFT_TURNS_6BCDB01E = {
    RIGHT: UP,
    UP: LEFT,
    LEFT: DOWN,
    DOWN: RIGHT,
}

RIGHT_TURNS_6BCDB01E = {
    RIGHT: DOWN,
    DOWN: LEFT,
    LEFT: UP,
    UP: RIGHT,
}

SLASH_REFLECTIONS_6BCDB01E = {
    RIGHT: UP,
    UP: RIGHT,
    LEFT: DOWN,
    DOWN: LEFT,
}

BACKSLASH_REFLECTIONS_6BCDB01E = {
    RIGHT: DOWN,
    DOWN: RIGHT,
    LEFT: UP,
    UP: LEFT,
}

SIZE_OPTIONS_6BCDB01E = (FIVE, FIVE, SIX, SEVEN, SEVEN, EIGHT, EIGHT, NINE)
SIDE_DIRECTIONS_6BCDB01E = (RIGHT, LEFT, DOWN, UP)


def _advance_6bcdb01e(
    loc: IntegerTuple,
    direction: IntegerTuple,
    steps: int = ONE,
) -> IntegerTuple:
    return (loc[0] + direction[0] * steps, loc[1] + direction[1] * steps)


def _inside_6bcdb01e(
    size_value: int,
    loc: IntegerTuple,
) -> bool:
    return ZERO <= loc[0] < size_value and ZERO <= loc[1] < size_value


def _distance_to_border_6bcdb01e(
    size_value: int,
    loc: IntegerTuple,
    direction: IntegerTuple,
) -> int:
    if direction == UP:
        return loc[0]
    if direction == DOWN:
        return size_value - ONE - loc[0]
    if direction == LEFT:
        return loc[1]
    return size_value - ONE - loc[1]


def _segment_6bcdb01e(
    loc: IntegerTuple,
    direction: IntegerTuple,
    steps: int,
) -> tuple[IntegerTuple, ...]:
    return tuple(_advance_6bcdb01e(loc, direction, k) for k in range(ONE, steps + ONE))


def _seed_cells_6bcdb01e(
    size_value: int,
    direction: IntegerTuple,
    anchor: int,
) -> tuple[IntegerTuple, IntegerTuple]:
    if direction == RIGHT:
        return ((anchor, ZERO), (anchor, ONE))
    if direction == LEFT:
        return ((anchor, size_value - ONE), (anchor, size_value - TWO))
    if direction == DOWN:
        return ((ZERO, anchor), (ONE, anchor))
    return ((size_value - ONE, anchor), (size_value - TWO, anchor))


def _mirror_kind_6bcdb01e(
    direction: IntegerTuple,
    new_direction: IntegerTuple,
) -> str:
    if SLASH_REFLECTIONS_6BCDB01E[direction] == new_direction:
        return "slash"
    return "backslash"


def _partner_offsets_6bcdb01e(
    mirror_kind: str,
) -> tuple[IntegerTuple, IntegerTuple]:
    if mirror_kind == "slash":
        return (UP_RIGHT, DOWN_LEFT)
    return (NEG_UNITY, UNITY)


def _free_segment_6bcdb01e(
    cells: tuple[IntegerTuple, ...],
    path_cells: set[IntegerTuple],
    reflectors: set[IntegerTuple],
) -> bool:
    return all(cell not in path_cells and cell not in reflectors for cell in cells)


def _trace_spec_6bcdb01e(
    size_value: int,
    direction: IntegerTuple,
    anchor: int,
    target_turns: int,
) -> tuple[tuple[IntegerTuple, ...], frozenset[IntegerTuple]] | None:
    x0, x1 = _seed_cells_6bcdb01e(size_value, direction, anchor)
    x2 = [x0, x1]
    x3 = {x0, x1}
    x4: set[IntegerTuple] = set()
    x5 = x1
    x6 = direction
    x7 = ZERO
    while True:
        x8 = _distance_to_border_6bcdb01e(size_value, x5, x6)
        x9 = _segment_6bcdb01e(x5, x6, x8)
        x10 = x8 >= TWO and _free_segment_6bcdb01e(x9, x3, x4)
        if x7 >= THREE and x10 and x7 >= target_turns:
            x2.extend(x9)
            return tuple(x2), frozenset(x4)
        x11 = []
        x12 = [LEFT_TURNS_6BCDB01E[x6], RIGHT_TURNS_6BCDB01E[x6]]
        shuffle(x12)
        x13 = x8 - ONE
        if x13 >= TWO:
            x14 = list(range(TWO, x13 + ONE))
            shuffle(x14)
            for x15 in x12:
                x16 = _mirror_kind_6bcdb01e(x6, x15)
                x17 = list(_partner_offsets_6bcdb01e(x16))
                shuffle(x17)
                for x18 in x14:
                    x19 = _segment_6bcdb01e(x5, x6, x18)
                    if not _free_segment_6bcdb01e(x19, x3, x4):
                        continue
                    x20 = x19[-ONE]
                    x21 = _advance_6bcdb01e(x20, x6)
                    if not _inside_6bcdb01e(size_value, x21):
                        continue
                    if x21 in x3 or x21 in x4:
                        continue
                    x22 = (
                        _advance_6bcdb01e(x21, UP_RIGHT),
                        _advance_6bcdb01e(x21, DOWN_LEFT),
                        _advance_6bcdb01e(x21, NEG_UNITY),
                        _advance_6bcdb01e(x21, UNITY),
                    )
                    if any(x23 in x4 for x23 in x22):
                        continue
                    for x23 in x17:
                        x24 = _advance_6bcdb01e(x21, x23)
                        if not _inside_6bcdb01e(size_value, x24):
                            continue
                        if x24 in x3 or x24 in x4:
                            continue
                        x11.append((x18, x15, x21, x24, x19))
        if not x11:
            if x10 and x7 >= THREE:
                x2.extend(x9)
                return tuple(x2), frozenset(x4)
            return None
        x25, x26, x27, x28, x29 = choice(x11)
        del x25
        x2.extend(x29)
        x3.update(x29)
        x4.add(x27)
        x4.add(x28)
        x5 = x29[-ONE]
        x6 = x26
        x7 += ONE


def _add_noise_6bcdb01e(
    size_value: int,
    path_cells: frozenset[IntegerTuple],
    reflectors: frozenset[IntegerTuple],
) -> frozenset[IntegerTuple]:
    x0 = {
        (i, j)
        for i in range(size_value)
        for j in range(size_value)
        if (i, j) not in path_cells and (i, j) not in reflectors
    }
    x1 = set()
    for x2 in path_cells:
        x1.update(dneighbors(x2))
    x3 = tuple(x0.difference(x1))
    if len(x3) == ZERO:
        return frozenset()
    x4 = randint(ZERO, min(TWO, len(x3)))
    if x4 == ZERO:
        return frozenset()
    return frozenset(sample(x3, x4))


def generate_6bcdb01e(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    del diff_lb
    del diff_ub
    while True:
        x0 = choice(SIZE_OPTIONS_6BCDB01E)
        x1 = choice(SIDE_DIRECTIONS_6BCDB01E)
        x2 = randint(ONE, x0 - TWO)
        x3 = randint(THREE, min(SIX, x0))
        x4 = _trace_spec_6bcdb01e(x0, x1, x2, x3)
        if x4 is None:
            continue
        x5, x6 = x4
        x7 = frozenset(x5)
        x8 = _add_noise_6bcdb01e(x0, x7, x6)
        x9 = fill(canvas(SEVEN, (x0, x0)), EIGHT, combine(x6, x8))
        x10 = fill(x9, THREE, initset(x5[ZERO]))
        x10 = fill(x10, THREE, initset(x5[ONE]))
        x11 = fill(x9, THREE, x7)
        if x10 == x11:
            continue
        if verify_6bcdb01e(x10) != x11:
            continue
        return {"input": x10, "output": x11}
