from synth_rearc.core import *


SOURCE_COLOR_3490CC26 = TWO
TARGET_COLOR_3490CC26 = EIGHT
PATH_COLOR_3490CC26 = SEVEN


def block_cells_3490cc26(
    loc: IntegerTuple,
) -> Indices:
    x0, x1 = loc
    return frozenset({
        (x0, x1),
        (x0, increment(x1)),
        (increment(x0), x1),
        (increment(x0), increment(x1)),
    })


def block_object_3490cc26(
    value: Integer,
    loc: IntegerTuple,
) -> Object:
    x0 = block_cells_3490cc26(loc)
    return frozenset((value, x1) for x1 in x0)


def extract_blocks_3490cc26(
    I: Grid,
) -> tuple[Object, ...]:
    x0 = objects(I, T, F, T)
    x1 = tuple(x2 for x2 in x0 if x2 and square(x2) and equality(size(x2), FOUR))
    return tuple(sorted(x1, key=ulcorner))


def block_loc_3490cc26(
    block: Object,
) -> IntegerTuple:
    return ulcorner(block)


def visible_gap_3490cc26(
    current: Object,
    candidate: Object,
    blocks: tuple[Object, ...],
) -> Integer | None:
    x0, x1 = ulcorner(current)
    x2, x3 = ulcorner(candidate)
    if x0 == x2:
        x4 = min(x1, x3)
        x5 = max(x1, x3)
        for x6 in blocks:
            if x6 == current or x6 == candidate:
                continue
            x7, x8 = ulcorner(x6)
            if x7 == x0 and x4 < x8 < x5:
                return None
        return subtract(subtract(x5, x4), TWO)
    if x1 == x3:
        x4 = min(x0, x2)
        x5 = max(x0, x2)
        for x6 in blocks:
            if x6 == current or x6 == candidate:
                continue
            x7, x8 = ulcorner(x6)
            if x8 == x1 and x4 < x7 < x5:
                return None
        return subtract(subtract(x5, x4), TWO)
    return None


def next_visible_block_3490cc26(
    current: Object,
    candidates: tuple[Object, ...],
    blocks: tuple[Object, ...],
) -> Object | None:
    x0 = []
    for x1 in candidates:
        x2 = visible_gap_3490cc26(current, x1, blocks)
        if x2 is None:
            continue
        x3 = ulcorner(x1)
        x0.append((x2, x3[ZERO], x3[ONE], x1))
    if len(x0) == ZERO:
        return None
    return min(x0)[-ONE]


def connector_indices_3490cc26(
    a: Object,
    b: Object,
) -> Indices:
    x0, x1 = ulcorner(a)
    x2, x3 = ulcorner(b)
    if x0 == x2:
        x4 = min(x1, x3)
        x5 = max(x1, x3)
        x6 = frozenset((x0, x7) for x7 in range(x4 + TWO, x5))
        x8 = frozenset((increment(x0), x7) for x7 in range(x4 + TWO, x5))
        return combine(x6, x8)
    if x1 == x3:
        x4 = min(x0, x2)
        x5 = max(x0, x2)
        x6 = frozenset((x7, x1) for x7 in range(x4 + TWO, x5))
        x8 = frozenset((x7, increment(x1)) for x7 in range(x4 + TWO, x5))
        return combine(x6, x8)
    return frozenset()
