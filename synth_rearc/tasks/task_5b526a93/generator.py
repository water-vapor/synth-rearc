from synth_rearc.core import *

from .verifier import verify_5b526a93


RING_PATCH_5B526A93 = frozenset(
    {
        (ZERO, ZERO),
        (ZERO, ONE),
        (ZERO, TWO),
        (ONE, ZERO),
        (ONE, TWO),
        (TWO, ZERO),
        (TWO, ONE),
        (TWO, TWO),
    }
)

INCOMPLETE_ROW_COUNT_RANGE_5B526A93 = (TWO, THREE)
COLUMN_COUNT_RANGE_5B526A93 = (THREE, FIVE)
ROW_GAP_RANGE_5B526A93 = (ONE, FOUR)
COLUMN_GAP_RANGE_5B526A93 = (ONE, THREE)
TOP_MARGIN_RANGE_5B526A93 = (ONE, THREE)
BOTTOM_MARGIN_RANGE_5B526A93 = (ONE, THREE)
LEFT_MARGIN_RANGE_5B526A93 = (ONE, TWO)
RIGHT_MARGIN_RANGE_5B526A93 = (ONE, SIX)


def _sample_starts_5b526a93(
    diff_lb: float,
    diff_ub: float,
    count: Integer,
    lead_bounds: tuple[Integer, Integer],
    gap_bounds: tuple[Integer, Integer],
    tail_bounds: tuple[Integer, Integer],
) -> tuple[tuple[Integer, ...], Integer]:
    x0 = unifint(diff_lb, diff_ub, lead_bounds)
    x1 = [x0]
    for _ in range(count - ONE):
        x2 = unifint(diff_lb, diff_ub, gap_bounds)
        x1.append(x1[-1] + THREE + x2)
    x3 = unifint(diff_lb, diff_ub, tail_bounds)
    x4 = x1[-1] + THREE + x3
    return tuple(x1), x4


def _paint_rings_5b526a93(
    grid: Grid,
    anchors: Container,
    color_value: Integer,
) -> Grid:
    x0 = grid
    for x1 in anchors:
        x2 = shift(RING_PATCH_5B526A93, x1)
        x0 = fill(x0, color_value, x2)
    return x0


def generate_5b526a93(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = increment(unifint(diff_lb, diff_ub, INCOMPLETE_ROW_COUNT_RANGE_5B526A93))
        x1 = unifint(diff_lb, diff_ub, COLUMN_COUNT_RANGE_5B526A93)
        x2, x3 = _sample_starts_5b526a93(
            diff_lb,
            diff_ub,
            x0,
            TOP_MARGIN_RANGE_5B526A93,
            ROW_GAP_RANGE_5B526A93,
            BOTTOM_MARGIN_RANGE_5B526A93,
        )
        x4, x5 = _sample_starts_5b526a93(
            diff_lb,
            diff_ub,
            x1,
            LEFT_MARGIN_RANGE_5B526A93,
            COLUMN_GAP_RANGE_5B526A93,
            RIGHT_MARGIN_RANGE_5B526A93,
        )
        if x3 > 30 or x5 > 30:
            continue
        x6 = choice((first(x2), last(x2)))
        x7 = first(x4)
        x8 = product(initset(x6), x4)
        x9 = remove(x6, x2)
        x10 = product(x9, initset(x7))
        x11 = combine(x8, x10)
        x12 = product(x2, x4)
        gi = canvas(ZERO, (x3, x5))
        gi = _paint_rings_5b526a93(gi, x11, ONE)
        go = canvas(ZERO, (x3, x5))
        go = _paint_rings_5b526a93(go, x12, EIGHT)
        go = _paint_rings_5b526a93(go, x11, ONE)
        if verify_5b526a93(gi) != go:
            continue
        return {"input": gi, "output": go}
