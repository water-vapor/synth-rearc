from synth_rearc.core import *


def clockwise_border_30f42897(
    dims: IntegerTuple,
) -> tuple[IntegerTuple, ...]:
    x0, x1 = dims
    x2 = tuple((ZERO, x3) for x3 in range(x1))
    x3 = tuple((x4, x1 - ONE) for x4 in range(ONE, x0))
    x4 = tuple((x0 - ONE, x5) for x5 in range(x1 - TWO, NEG_ONE, NEG_ONE))
    x5 = tuple((x6, ZERO) for x6 in range(x0 - TWO, ZERO, NEG_ONE))
    return x2 + x3 + x4 + x5


def border_lookup_30f42897(
    dims: IntegerTuple,
) -> dict[IntegerTuple, Integer]:
    x0 = clockwise_border_30f42897(dims)
    return {
        x1: x2
        for x2, x1 in enumerate(x0)
    }


def cyclic_run_start_30f42897(
    ranks: tuple[Integer, ...],
    perimeter: Integer,
) -> Integer:
    if len(ranks) == ZERO:
        return ZERO
    x0 = tuple(sorted(ranks))
    if len(x0) == ONE:
        return x0[ZERO]
    x1 = tuple(
        (x0[(x2 + ONE) % len(x0)] - x0[x2]) % perimeter
        for x2 in range(len(x0))
    )
    x2 = max(range(len(x1)), key=lambda x3: x1[x3])
    return x0[(x2 + ONE) % len(x0)]


def run_segment_30f42897(
    dims: IntegerTuple,
    start: Integer,
    length: Integer,
) -> Indices:
    x0 = clockwise_border_30f42897(dims)
    x1 = len(x0)
    if length == ZERO:
        return frozenset()
    return frozenset(
        x0[(start + x2) % x1]
        for x2 in range(length)
    )


def repeated_run_30f42897(
    dims: IntegerTuple,
    start: Integer,
    length: Integer,
) -> Indices:
    x0 = clockwise_border_30f42897(dims)
    x1 = len(x0)
    if length == ZERO:
        return frozenset()
    x2 = double(length)
    return frozenset(
        x4
        for x3, x4 in enumerate(x0)
        if ((x3 - start) % x1) % x2 < length
    )
