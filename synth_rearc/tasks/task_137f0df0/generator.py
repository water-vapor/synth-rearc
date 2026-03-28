from synth_rearc.core import *

from .verifier import verify_137f0df0


def _split_total_137f0df0(
    total: Integer,
    parts: Integer,
) -> tuple[Integer, ...]:
    if parts == ONE:
        return (total,)
    x0 = sorted(sample(range(total + parts - ONE), parts - ONE))
    x1 = []
    x2 = NEG_ONE
    for x3 in x0 + [total + parts - ONE]:
        x1.append(x3 - x2 - ONE)
        x2 = x3
    return tuple(x1)


def _sample_layout_137f0df0(
    length: Integer,
    count: Integer,
) -> tuple[Integer, ...]:
    x0 = length - (TWO * count + (count - ONE))
    x1 = _split_total_137f0df0(x0, count + ONE)
    x2 = []
    x3 = x1[ZERO]
    for x4 in range(count):
        x2.append(x3)
        if x4 < count - ONE:
            x3 += THREE + x1[x4 + ONE]
    return tuple(x2)


def _block_137f0df0(
    top: Integer,
    left: Integer,
) -> Indices:
    return frozenset({
        (top, left),
        (top, left + ONE),
        (top + ONE, left),
        (top + ONE, left + ONE),
    })


def _active_lines_137f0df0(
    starts: tuple[Integer, ...],
) -> frozenset[Integer]:
    return frozenset(value for start in starts for value in (start, start + ONE))


def _outside_137f0df0(
    limit: Integer,
    lower: Integer,
    upper: Integer,
) -> tuple[Integer, ...]:
    return tuple(range(lower)) + tuple(range(upper + ONE, limit))


def _build_input_137f0df0(
    shape: IntegerTuple,
    row_starts: tuple[Integer, ...],
    col_starts: tuple[Integer, ...],
) -> Grid:
    x0 = canvas(ZERO, shape)
    for x1 in row_starts:
        for x2 in col_starts:
            x0 = fill(x0, FIVE, _block_137f0df0(x1, x2))
    return x0


def _build_output_137f0df0(
    gi: Grid,
    shape: IntegerTuple,
    row_starts: tuple[Integer, ...],
    col_starts: tuple[Integer, ...],
) -> Grid:
    x0 = _active_lines_137f0df0(row_starts)
    x1 = _active_lines_137f0df0(col_starts)
    x2 = minimum(x0)
    x3 = maximum(x0)
    x4 = minimum(x1)
    x5 = maximum(x1)
    x6 = frozenset(
        (i, j)
        for i in range(x2, x3 + ONE)
        for j in range(x4, x5 + ONE)
        if i not in x0 or j not in x1
    )
    x7 = tuple(i for i in range(x2, x3 + ONE) if i not in x0)
    x8 = tuple(j for j in range(x4, x5 + ONE) if j not in x1)
    x9 = _outside_137f0df0(shape[ZERO], x2, x3)
    x10 = _outside_137f0df0(shape[ONE], x4, x5)
    x11 = frozenset((i, j) for i in x7 for j in x10)
    x12 = frozenset((i, j) for i in x9 for j in x8)
    x13 = fill(gi, TWO, x6)
    x14 = fill(x13, ONE, combine(x11, x12))
    return x14


def generate_137f0df0(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = unifint(diff_lb, diff_ub, (TEN, 14))
        x1 = unifint(diff_lb, diff_ub, (TEN, 14))
        x2 = choice((TWO, THREE, THREE))
        x3 = _sample_layout_137f0df0(x0, THREE)
        x4 = _sample_layout_137f0df0(x1, x2)
        x5 = (x0, x1)
        gi = _build_input_137f0df0(x5, x3, x4)
        go = _build_output_137f0df0(gi, x5, x3, x4)
        if verify_137f0df0(gi) != go:
            continue
        return {"input": gi, "output": go}
