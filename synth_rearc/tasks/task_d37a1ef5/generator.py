from synth_rearc.core import *

from .verifier import verify_d37a1ef5


def _marker_df37a1ef5(
    diff_lb: float,
    diff_ub: float,
    dims: IntegerTuple,
) -> Indices:
    h, w = dims
    cells = tuple((i, j) for i in range(h) for j in range(w))
    cap = min(max(h, w), len(cells) - ONE)
    while True:
        n = unifint(diff_lb, diff_ub, (TWO, cap))
        picked = frozenset(sample(cells, n))
        rows = tuple(i for i, _ in picked)
        cols = tuple(j for _, j in picked)
        if minimum(rows) != ZERO:
            continue
        if maximum(rows) != h - ONE:
            continue
        if minimum(cols) != ZERO:
            continue
        if maximum(cols) != w - ONE:
            continue
        return picked


def generate_d37a1ef5(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        frameh = unifint(diff_lb, diff_ub, (SIX, NINE))
        framew = unifint(diff_lb, diff_ub, (EIGHT, TEN))
        innerh = frameh - TWO
        innerw = framew - TWO
        if innerh < FOUR or innerw < FOUR:
            continue
        markh = unifint(diff_lb, diff_ub, (TWO, min(FOUR, innerh - TWO)))
        markw = unifint(diff_lb, diff_ub, (TWO, min(FOUR, innerw - TWO)))
        topgap = unifint(diff_lb, diff_ub, (ONE, innerh - markh - ONE))
        leftgap = unifint(diff_lb, diff_ub, (ONE, innerw - markw - ONE))
        outer_top = ONE
        outer_left = unifint(diff_lb, diff_ub, (ONE, TWO))
        bottom_gap = unifint(diff_lb, diff_ub, (ONE, FOUR))
        right_gap = unifint(diff_lb, diff_ub, (ONE, TWO))
        shapei = (frameh + outer_top + bottom_gap, framew + outer_left + right_gap)

        x0 = (outer_top, outer_left)
        x1 = (outer_top + frameh - ONE, outer_left + framew - ONE)
        x2 = frozenset({x0, x1})
        x3 = box(x2)
        x4 = backdrop(x2)
        x5 = _marker_df37a1ef5(diff_lb, diff_ub, (markh, markw))
        x6 = shift(x5, (outer_top + topgap + ONE, outer_left + leftgap + ONE))
        x7 = backdrop(x6)
        x8 = difference(x4, x7)
        gi = canvas(ZERO, shapei)
        gi = fill(gi, TWO, x3)
        gi = fill(gi, FIVE, x6)
        go = fill(gi, TWO, x8)
        if verify_d37a1ef5(gi) != go:
            continue
        return {"input": gi, "output": go}
