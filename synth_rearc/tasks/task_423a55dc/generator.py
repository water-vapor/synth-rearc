from synth_rearc.core import *

from .verifier import verify_423a55dc


_FOREGROUND_COLORS_423A55DC = (ONE, TWO, THREE, FOUR, FIVE, SIX, SEVEN, EIGHT, NINE)
_HEIGHT_RANGE_423A55DC = (TWO, SEVEN)
_WIDTH_RANGE_423A55DC = (THREE, SEVEN)
_MARGIN_RANGE_423A55DC = (ONE, FOUR)
_LEFT_OUTPUT_SLACK_RANGE_423A55DC = (ZERO, TWO)


def _monotone_path_423a55dc(
    start: Integer,
    end: Integer,
    steps: Integer,
) -> tuple[Integer, ...]:
    direction = branch(greater(end, start), ONE, NEG_ONE)
    moves = abs(subtract(end, start))
    marks = set(sample(interval(ZERO, steps, ONE), moves))
    out = [start]
    value = start
    for idx in interval(ZERO, steps, ONE):
        if idx in marks:
            value = add(value, direction)
        out.append(value)
    return tuple(out)


def _row_profile_423a55dc(
    lefts: tuple[Integer, ...],
    rights: tuple[Integer, ...],
    diff_lb: float,
    diff_ub: float,
) -> tuple[frozenset[Integer], ...]:
    h = len(lefts)
    rows = []
    for idx, (left, right) in enumerate(pair(lefts, rights)):
        span = interval(left, increment(right), ONE)
        full = frozenset(span)
        if idx == ZERO or idx == decrement(h) or right - left < TWO:
            rows.append(full)
            continue
        attempts = ZERO
        row = full
        while True:
            gap_cap = subtract(subtract(right, left), ONE)
            carve_gap = choice((T, T, F))
            if carve_gap and positive(gap_cap):
                gap_len = unifint(diff_lb, diff_ub, (ONE, gap_cap))
                gap_left = randint(increment(left), subtract(right, gap_len))
                gap = frozenset(interval(gap_left, add(gap_left, gap_len), ONE))
                row = difference(full, gap)
            else:
                row = full
            if size(intersection(row, rows[-ONE])) > ZERO or attempts > TEN:
                break
            attempts = increment(attempts)
        rows.append(row)
    return tuple(rows)


def _required_left_margin_423a55dc(
    rows: tuple[frozenset[Integer], ...],
) -> Integer:
    h = len(rows)
    min_shifted = ZERO
    for idx, cols in enumerate(rows):
        shift_j = subtract(idx, decrement(h))
        row_min = add(min(cols), shift_j)
        min_shifted = minimum((min_shifted, row_min))
    return maximum((ZERO, invert(min_shifted)))


def generate_423a55dc(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        h = unifint(diff_lb, diff_ub, _HEIGHT_RANGE_423A55DC)
        w = unifint(diff_lb, diff_ub, _WIDTH_RANGE_423A55DC)
        top_span_min = maximum((TWO, subtract(w, double(decrement(h)))))
        top_span = unifint(diff_lb, diff_ub, (top_span_min, w))
        indent = subtract(w, top_span)
        left_min = maximum((ZERO, subtract(indent, decrement(h))))
        left_max = minimum((indent, decrement(h)))
        top_left = randint(left_min, left_max)
        top_right = add(add(top_left, top_span), NEG_ONE)
        lefts = _monotone_path_423a55dc(top_left, ZERO, decrement(h))
        rights = _monotone_path_423a55dc(top_right, decrement(w), decrement(h))
        rows = _row_profile_423a55dc(lefts, rights, diff_lb, diff_ub)
        color = choice(_FOREGROUND_COLORS_423A55DC)
        compact = canvas(ZERO, (h, w))
        for idx, cols in enumerate(rows):
            compact = fill(compact, color, frozenset((idx, col) for col in cols))
        if size(colorfilter(objects(compact, T, F, F), color)) != ONE:
            continue
        top = unifint(diff_lb, diff_ub, _MARGIN_RANGE_423A55DC)
        left = add(
            _required_left_margin_423a55dc(rows),
            unifint(diff_lb, diff_ub, _LEFT_OUTPUT_SLACK_RANGE_423A55DC),
        )
        bottom = unifint(diff_lb, diff_ub, _MARGIN_RANGE_423A55DC)
        right = unifint(diff_lb, diff_ub, _MARGIN_RANGE_423A55DC)
        dims = (add(add(top, h), bottom), add(add(left, w), right))
        gi = canvas(ZERO, dims)
        go = canvas(ZERO, dims)
        for idx, cols in enumerate(rows):
            row = add(top, idx)
            gi_patch = frozenset((row, add(left, col)) for col in cols)
            shift_j = subtract(idx, decrement(h))
            go_patch = frozenset((row, add(add(left, col), shift_j)) for col in cols)
            gi = fill(gi, color, gi_patch)
            go = fill(go, color, go_patch)
        if equality(gi, go):
            continue
        if verify_423a55dc(gi) != go:
            continue
        return {"input": gi, "output": go}
