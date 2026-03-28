from synth_rearc.core import *

from .verifier import verify_1d61978c


GRID_SIZE_1D61978C = 16
GRID_SHAPE_1D61978C = (GRID_SIZE_1D61978C, GRID_SIZE_1D61978C)
DIAGONAL_DIRECTIONS_1D61978C = {
    "backslash": UNITY,
    "slash": DOWN_LEFT,
}
SEGMENT_COUNT_POOL_1D61978C = (ONE, ONE, ONE, TWO, TWO, TWO, THREE, THREE)


def _segment_1d61978c(
    start: IntegerTuple,
    direction: IntegerTuple,
    length: Integer,
) -> Indices:
    x0 = add(start, multiply(direction, subtract(length, ONE)))
    return connect(start, x0)


def _all_neighbors_1d61978c(
    patch: Indices,
) -> Indices:
    x0 = set()
    for x1 in patch:
        for x2 in neighbors(x1):
            x0.add(x2)
    return frozenset(x0)


def _sample_segment_1d61978c(
    direction_name: str,
    length: Integer,
) -> Indices:
    x0 = DIAGONAL_DIRECTIONS_1D61978C[direction_name]
    x1 = subtract(length, ONE)
    x2 = subtract(GRID_SIZE_1D61978C, length)
    if equality(direction_name, "backslash"):
        x3 = randint(ZERO, x2)
        x4 = randint(ZERO, x2)
        x5 = astuple(x3, x4)
        return _segment_1d61978c(x5, x0, length)
    x6 = randint(ZERO, x2)
    x7 = randint(x1, decrement(GRID_SIZE_1D61978C))
    x8 = astuple(x6, x7)
    return _segment_1d61978c(x8, x0, length)


def _partition_total_1d61978c(
    total: Integer,
    segment_count: Integer,
) -> Tuple[int, ...]:
    x0 = [TWO for _ in range(segment_count)]
    x1 = subtract(total, multiply(TWO, segment_count))
    while positive(x1):
        x2 = randint(ZERO, decrement(segment_count))
        x0[x2] = increment(x0[x2])
        x1 = decrement(x1)
    shuffle(x0)
    return tuple(x0)


def _add_family_1d61978c(
    occupied: Indices,
    direction_name: str,
    lengths: Tuple[int, ...],
) -> Indices | None:
    x0 = set()
    x1 = set(occupied)
    for x2 in lengths:
        x3 = ZERO
        x4 = 120
        x5 = F
        while x3 < x4:
            x3 = increment(x3)
            x6 = _sample_segment_1d61978c(direction_name, x2)
            x7 = _all_neighbors_1d61978c(x6)
            if x7 & x1:
                continue
            x0 |= set(x6)
            x1 |= set(x7)
            x5 = T
            break
        if flip(x5):
            return None
    return frozenset(x0)


def generate_1d61978c(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = choice(("backslash", "slash"))
        x1 = branch(equality(x0, "backslash"), "slash", "backslash")
        x2 = choice(SEGMENT_COUNT_POOL_1D61978C)
        x3 = choice(SEGMENT_COUNT_POOL_1D61978C)
        x4 = multiply(TWO, x2)
        x5 = multiply(TWO, x3)
        x6 = unifint(diff_lb, diff_ub, (x4, min(12, add(GRID_SIZE_1D61978C, multiply(TWO, decrement(x2))))))
        x7 = max(add(x6, ONE), x5)
        x8 = min(18, add(GRID_SIZE_1D61978C, multiply(TWO, decrement(x3))))
        if greater(x7, x8):
            continue
        x9 = unifint(diff_lb, diff_ub, (x7, x8))
        x10 = _partition_total_1d61978c(x6, x2)
        x11 = _partition_total_1d61978c(x9, x3)
        x12 = _add_family_1d61978c(frozenset(), x0, x10)
        if x12 is None:
            continue
        x13 = _add_family_1d61978c(x12, x1, x11)
        if x13 is None:
            continue
        x14 = canvas(SEVEN, GRID_SHAPE_1D61978C)
        x15 = combine(x12, x13)
        x16 = fill(x14, FIVE, x15)
        x17 = fill(x16, TWO, x12)
        x18 = fill(x17, EIGHT, x13)
        if verify_1d61978c(x16) != x18:
            continue
        return {"input": x16, "output": x18}
