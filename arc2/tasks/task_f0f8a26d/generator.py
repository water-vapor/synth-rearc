from arc2.core import *

from .verifier import verify_f0f8a26d


ACTIVE_COLORS_F0F8A26D = difference(interval(ZERO, TEN, ONE), frozenset({SEVEN}))
GRID_SIZES_F0F8A26D = (NINE, 11, 13)
LENGTH_POOL_F0F8A26D = (ONE, THREE, THREE, THREE, FIVE, FIVE, FIVE, SEVEN, SEVEN, NINE)


def _segment_cells_f0f8a26d(
    center_loc: IntegerTuple,
    length: Integer,
    vertical: Boolean,
) -> Indices:
    x0, x1 = center_loc
    x2 = halve(length)
    if vertical:
        return connect((x0 - x2, x1), (x0 + x2, x1))
    return connect((x0, x1 - x2), (x0, x1 + x2))


def _blocked_cells_f0f8a26d(
    cells: Indices,
    side: Integer,
) -> Indices:
    x0 = set(cells)
    for x1 in cells:
        for x2 in dneighbors(x1):
            if 0 <= x2[0] < side and 0 <= x2[1] < side:
                x0.add(x2)
    return frozenset(x0)


def _sample_segment_f0f8a26d(
    side: Integer,
    vertical: Boolean,
    singleton_only: Boolean,
    blocked: Indices,
) -> tuple[IntegerTuple, Integer, Boolean, Indices] | None:
    for _ in range(400):
        x0 = randint(ZERO, side - ONE)
        x1 = randint(ZERO, side - ONE)
        x2 = min(x0, x1, side - ONE - x0, side - ONE - x1)
        x3 = add(add(x2, x2), ONE)
        if singleton_only:
            x4 = (ONE,) if x3 >= ONE else tuple()
        else:
            x4 = tuple(x5 for x5 in LENGTH_POOL_F0F8A26D if ONE < x5 <= x3)
        if len(x4) == ZERO:
            continue
        x5 = choice(x4)
        x6 = (x0, x1)
        x7 = _segment_cells_f0f8a26d(x6, x5, vertical)
        if len(intersection(x7, blocked)) > ZERO:
            continue
        return (x6, x5, vertical, x7)
    return None


def generate_f0f8a26d(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = choice(GRID_SIZES_F0F8A26D)
        x1 = astuple(x0, x0)
        x2 = choice(ACTIVE_COLORS_F0F8A26D)
        x3 = unifint(diff_lb, diff_ub, (max(FOUR, x0 // TWO), min(TEN, x0 - THREE)))
        x4 = randint(ZERO, min(TWO, x3 - TWO))
        x5 = tuple()
        x6 = frozenset()
        x7 = True
        for x8 in range(x3):
            if x8 == ZERO:
                x9 = F
                x10 = F
            elif x8 == ONE:
                x9 = T
                x10 = F
            else:
                x9 = choice((T, F))
                x10 = greater(x8, x3 - x4 - ONE)
            x11 = _sample_segment_f0f8a26d(x0, x9, x10, x6)
            if x11 is None:
                x7 = False
                break
            x12 = x11[3]
            x5 = x5 + (x11[:3],)
            x6 = combine(x6, _blocked_cells_f0f8a26d(x12, x0))
        if not x7:
            continue
        x13 = canvas(SEVEN, x1)
        x14 = canvas(SEVEN, x1)
        for x15, x16, x17 in x5:
            x18 = _segment_cells_f0f8a26d(x15, x16, x17)
            x19 = _segment_cells_f0f8a26d(x15, x16, flip(x17))
            x13 = fill(x13, x2, x18)
            x14 = fill(x14, x2, x19)
        if x13 == x14:
            continue
        if len(objects(x13, T, F, T)) != x3:
            continue
        if verify_f0f8a26d(x13) != x14:
            continue
        return {"input": x13, "output": x14}
