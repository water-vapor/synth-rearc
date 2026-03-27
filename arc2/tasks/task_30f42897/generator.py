from arc2.core import *

from .helpers import repeated_run_30f42897, run_segment_30f42897


FG_COLORS_30f42897 = remove(EIGHT, interval(ZERO, TEN, ONE))


def _cell_sides_30f42897(
    loc: IntegerTuple,
    dims: IntegerTuple,
) -> tuple[str, ...]:
    x0, x1 = dims
    x2, x3 = loc
    x4 = []
    if x2 == ZERO:
        x4.append("top")
    if x2 == x0 - ONE:
        x4.append("bottom")
    if x3 == ZERO:
        x4.append("left")
    if x3 == x1 - ONE:
        x4.append("right")
    return tuple(x4)


def _segment_kind_30f42897(
    dims: IntegerTuple,
    start: Integer,
    length: Integer,
) -> str | None:
    x0, x1 = dims
    x2 = run_segment_30f42897(dims, start, length)
    x3 = {
        (ZERO, ZERO),
        (ZERO, x1 - ONE),
        (x0 - ONE, ZERO),
        (x0 - ONE, x1 - ONE),
    }
    x4 = sum(ONE for x5 in x2 if x5 in x3)
    x5 = set()
    for x6 in x2:
        x5.update(_cell_sides_30f42897(x6, dims))
    if x4 == ZERO and len(x5) == ONE:
        return "straight"
    if x4 == ONE and len(x5) == TWO:
        return "corner"
    return None


def _candidate_starts_30f42897(
    dims: IntegerTuple,
    length: Integer,
) -> tuple[tuple[Integer, ...], tuple[Integer, ...]]:
    x0 = 2 * dims[ZERO] + 2 * dims[ONE] - FOUR
    x1 = []
    x2 = []
    for x3 in range(x0):
        x4 = _segment_kind_30f42897(dims, x3, length)
        if x4 == "straight":
            x1.append(x3)
        elif x4 == "corner":
            x2.append(x3)
    return tuple(x1), tuple(x2)


def _length_choices_30f42897(
    dims: IntegerTuple,
) -> tuple[Integer, ...]:
    x0 = dims[ZERO] + dims[ONE] - TWO
    return tuple(
        x1
        for x1 in range(TWO, SIX)
        if x0 % x1 == ZERO and THREE <= x0 // x1 <= SEVEN
    )


def _sample_dims_and_length_30f42897(
    diff_lb: float,
    diff_ub: float,
) -> tuple[IntegerTuple, Integer, tuple[Integer, ...], tuple[Integer, ...]]:
    for _ in range(200):
        x0 = unifint(diff_lb, diff_ub, (THREE, SEVEN))
        x1 = unifint(diff_lb, diff_ub, (max(NINE, x0 + TWO), 14))
        x2 = (x0, x1)
        x3 = _length_choices_30f42897(x2)
        if len(x3) == ZERO:
            continue
        x4 = choice(x3)
        x5, x6 = _candidate_starts_30f42897(x2, x4)
        if len(x5) == ZERO and len(x6) == ZERO:
            continue
        return x2, x4, x5, x6
    raise RuntimeError("failed to sample task dimensions")


def generate_30f42897(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0, x1, x2, x3 = _sample_dims_and_length_30f42897(diff_lb, diff_ub)
        x4 = bool(x3) and (not x2 or choice((T, F, F)))
        x5 = choice(x3 if x4 else x2)
        x6 = choice(FG_COLORS_30f42897)
        x7 = run_segment_30f42897(x0, x5, x1)
        x8 = repeated_run_30f42897(x0, x5, x1)
        gi = fill(canvas(EIGHT, x0), x6, x7)
        go = fill(canvas(EIGHT, x0), x6, x8)
        if gi == go:
            continue
        return {
            "input": gi,
            "output": go,
        }
