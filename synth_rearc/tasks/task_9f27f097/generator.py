from synth_rearc.core import *

from .verifier import verify_9f27f097


GRID_SHAPE_9F27F097 = (12, 12)


def _rect_patch_9f27f097(
    start: IntegerTuple,
    dims: IntegerTuple,
) -> Indices:
    x0, x1 = start
    x2, x3 = dims
    return frozenset(
        (i, j)
        for i in range(x0, x0 + x2)
        for j in range(x1, x1 + x3)
    )


def _neighbors_9f27f097(
    cell: IntegerTuple,
    dims: IntegerTuple,
) -> tuple[IntegerTuple, ...]:
    x0, x1 = cell
    x2, x3 = dims
    x4 = []
    for x5, x6 in ((-ONE, ZERO), (ONE, ZERO), (ZERO, -ONE), (ZERO, ONE)):
        x7 = x0 + x5
        x8 = x1 + x6
        if 0 <= x7 < x2 and 0 <= x8 < x3:
            x4.append((x7, x8))
    return tuple(x4)


def _accent_patch_9f27f097(
    diff_lb: float,
    diff_ub: float,
    dims: IntegerTuple,
) -> Indices:
    x0, x1 = dims
    x2 = x0 * x1
    x3 = min(x2 - ONE, x0 + x1 + ONE)
    while True:
        x4 = unifint(diff_lb, diff_ub, (TWO, x3))
        x5 = {
            (
                unifint(diff_lb, diff_ub, (ZERO, decrement(x0))),
                unifint(diff_lb, diff_ub, (ZERO, decrement(x1))),
            )
        }
        while len(x5) < x4:
            x6 = []
            for x7 in x5:
                for x8 in _neighbors_9f27f097(x7, dims):
                    if x8 not in x5 and x8 not in x6:
                        x6.append(x8)
            x5.add(choice(tuple(x6)))
        x9 = {x10 for x10, _ in x5}
        x11 = {x12 for _, x12 in x5}
        if len(x9) < TWO or len(x11) < TWO:
            continue
        return frozenset(x5)


def _placements_9f27f097(
    diff_lb: float,
    diff_ub: float,
    dims: IntegerTuple,
) -> tuple[IntegerTuple, IntegerTuple]:
    x0, x1 = dims
    x2 = min(THREE, 11 - 2 * x0)
    x3 = unifint(diff_lb, diff_ub, (ONE, x2))
    x4 = unifint(diff_lb, diff_ub, (ONE, subtract(subtract(12, x0), add(x3, x0))))
    x5 = add(add(x3, x0), x4)
    x6 = choice((ONE, ONE, TWO))
    x7 = subtract(subtract(12, x1), x6)
    x8 = min(FOUR, subtract(x7, ONE))
    x9 = unifint(diff_lb, diff_ub, (ONE, x8))
    x10 = add(x6, x9)
    return (x3, x6), (x5, x10)


def generate_9f27f097(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = unifint(diff_lb, diff_ub, (THREE, FIVE))
        x1 = unifint(diff_lb, diff_ub, (FOUR, SIX))
        x2 = (x0, x1)
        x3 = choice(interval(ONE, TEN, ONE))
        x4 = tuple(x5 for x5 in interval(ONE, TEN, ONE) if x5 not in (ZERO, x3))
        x5, x6 = sample(x4, TWO)
        x7 = _accent_patch_9f27f097(diff_lb, diff_ub, x2)
        x8 = fill(canvas(x5, x2), x6, x7)
        if x8 == vmirror(x8):
            continue
        x9, x10 = _placements_9f27f097(diff_lb, diff_ub, x2)
        x11 = canvas(x3, GRID_SHAPE_9F27F097)
        x12 = shift(asobject(x8), x9)
        x13 = _rect_patch_9f27f097(x10, x2)
        gi = paint(x11, x12)
        gi = fill(gi, ZERO, x13)
        x14 = shift(asobject(vmirror(x8)), x10)
        go = paint(gi, x14)
        if choice((T, F)):
            gi = hmirror(gi)
            go = hmirror(go)
        if verify_9f27f097(gi) != go:
            continue
        return {"input": gi, "output": go}
