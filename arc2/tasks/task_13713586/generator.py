from arc2.core import *

from .verifier import verify_13713586


RawSegment13713586 = tuple[Integer, Integer, Integer, Integer]


def _spaced_positions_13713586(
    limit: Integer,
    total: Integer,
) -> tuple[Integer, ...] | None:
    x0 = tuple(range(TWO, subtract(limit, TWO)))
    if len(x0) < total:
        return None
    for _ in range(200):
        x1 = tuple(sorted(sample(x0, total)))
        x2 = T
        for x3, x4 in zip(x1, x1[ONE:]):
            if x4 - x3 <= ONE:
                x2 = F
                break
        if x2:
            return x1
    return None


def _fresh_interval_13713586(
    span: Integer,
) -> tuple[Integer, Integer]:
    x0 = min(subtract(span, ONE), add(THREE, span // TWO))
    x1 = randint(TWO, x0)
    x2 = randint(ZERO, subtract(span, x1))
    x3 = add(x2, decrement(x1))
    return x2, x3


def _perturbed_interval_13713586(
    span: Integer,
    prior: tuple[Integer, Integer],
) -> tuple[Integer, Integer]:
    x0, x1 = prior
    for _ in range(50):
        x2 = randint(max(ZERO, x0 - TWO), min(subtract(span, TWO), x0 + TWO))
        x3 = max(add(x2, ONE), x1 - TWO)
        x4 = min(decrement(span), x1 + TWO)
        if x3 <= x4:
            return x2, randint(x3, x4)
    return _fresh_interval_13713586(span)


def _sample_intervals_13713586(
    span: Integer,
    total: Integer,
) -> tuple[tuple[Integer, Integer], ...]:
    x0 = tuple()
    for _ in range(total):
        if len(x0) > ZERO and choice((T, T, F)):
            x1 = _perturbed_interval_13713586(span, choice(x0))
        else:
            x1 = _fresh_interval_13713586(span)
        x0 = x0 + (x1,)
    return x0


def _base_grid_13713586(
    shape: IntegerTuple,
    side: Integer,
) -> Grid:
    x0, x1 = shape
    x2 = canvas(ZERO, shape)
    if side == ZERO:
        x3 = frozenset({(ZERO, ZERO), (ZERO, decrement(x1))})
    elif side == ONE:
        x3 = frozenset({(decrement(x0), ZERO), (decrement(x0), decrement(x1))})
    elif side == TWO:
        x3 = frozenset({(ZERO, ZERO), (decrement(x0), ZERO)})
    else:
        x3 = frozenset({(ZERO, decrement(x1)), (decrement(x0), decrement(x1))})
    return fill(x2, FIVE, backdrop(x3))


def _segment_patch_13713586(
    side: Integer,
    anchor: Integer,
    start: Integer,
    stop: Integer,
) -> Indices:
    if side in (ZERO, ONE):
        x0 = frozenset({(anchor, start), (anchor, stop)})
    else:
        x0 = frozenset({(start, anchor), (stop, anchor)})
    return backdrop(x0)


def _span_patch_13713586(
    shape: IntegerTuple,
    side: Integer,
    anchor: Integer,
    start: Integer,
    stop: Integer,
) -> Indices:
    x0, x1 = shape
    if side == ZERO:
        x2 = frozenset({(ONE, start), (anchor, stop)})
    elif side == ONE:
        x2 = frozenset({(anchor, start), (subtract(x0, TWO), stop)})
    elif side == TWO:
        x2 = frozenset({(start, ONE), (stop, anchor)})
    else:
        x2 = frozenset({(start, anchor), (stop, subtract(x1, TWO))})
    return backdrop(x2)


def _distance_13713586(
    shape: IntegerTuple,
    side: Integer,
    anchor: Integer,
) -> Integer:
    x0, x1 = shape
    if side == ZERO:
        return anchor
    if side == ONE:
        return subtract(decrement(x0), anchor)
    if side == TWO:
        return anchor
    return subtract(decrement(x1), anchor)


def _has_overlap_13713586(
    specs: tuple[RawSegment13713586, ...],
    shape: IntegerTuple,
    side: Integer,
) -> Boolean:
    x0 = tuple(
        _span_patch_13713586(shape, side, x1, x2, x3)
        for _, x1, x2, x3 in specs
    )
    for x1, x2 in enumerate(x0):
        for x3 in x0[x1 + ONE:]:
            if len(intersection(x2, x3)) > ZERO:
                return T
    return F


def _build_input_13713586(
    shape: IntegerTuple,
    side: Integer,
    specs: tuple[RawSegment13713586, ...],
) -> Grid:
    x0 = _base_grid_13713586(shape, side)
    for x1, x2, x3, x4 in specs:
        x5 = _segment_patch_13713586(side, x2, x3, x4)
        x0 = fill(x0, x1, x5)
    return x0


def _build_output_13713586(
    shape: IntegerTuple,
    side: Integer,
    specs: tuple[RawSegment13713586, ...],
) -> Grid:
    x0 = _base_grid_13713586(shape, side)
    x1 = tuple(
        sorted(
            specs,
            key=lambda x2: (
                -_distance_13713586(shape, side, x2[ONE]),
                x2[ONE],
                x2[TWO],
                x2[THREE],
            ),
        )
    )
    for x2, x3, x4, x5 in x1:
        x6 = _span_patch_13713586(shape, side, x3, x4, x5)
        x0 = fill(x0, x2, x6)
    return x0


def generate_13713586(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = unifint(diff_lb, diff_ub, (13, 20))
        x1 = unifint(diff_lb, diff_ub, (13, 20))
        x2 = (x0, x1)
        x3 = choice((ZERO, ONE, TWO, THREE))
        x4 = branch(x3 in (ZERO, ONE), x0, x1)
        x5 = _spaced_positions_13713586(x4, randint(THREE, FOUR))
        if x5 is None:
            continue
        x6 = branch(x3 in (ZERO, ONE), x1, x0)
        x7 = _sample_intervals_13713586(x6, len(x5))
        if len(x5) > TWO and choice((T, T, F)) and not _has_overlap_13713586(
            tuple((ZERO, x8, x9, x10) for x8, (x9, x10) in zip(x5, x7)),
            x2,
            x3,
        ):
            continue
        x8 = sample((TWO, THREE, FOUR, SIX, SEVEN, EIGHT), len(x5))
        x9 = tuple((x10, x11, x12, x13) for x10, x11, (x12, x13) in zip(x8, x5, x7))
        x10 = _build_input_13713586(x2, x3, x9)
        x11 = _build_output_13713586(x2, x3, x9)
        if x10 == x11:
            continue
        if verify_13713586(x10) != x11:
            continue
        return {"input": x10, "output": x11}
