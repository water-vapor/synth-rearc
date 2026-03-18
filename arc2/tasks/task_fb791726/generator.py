from arc2.core import *

from .verifier import verify_fb791726


MAX_SIDE_FB791726 = 15
BLOCK_COUNT_RANGE_FB791726 = (ONE, FIVE)
BLOCK_COLUMNS_FB791726 = (ZERO, ONE, TWO)
FOREGROUND_COLORS_FB791726 = remove(THREE, interval(ONE, TEN, ONE))


def _make_input_fb791726(
    block_offsets: tuple[Integer, ...],
    slack: Integer,
    color_value: Integer,
) -> Grid:
    x0 = len(block_offsets)
    x1 = add(multiply(THREE, x0), slack)
    x2 = canvas(ZERO, (x1, x1))
    for x3, x4 in enumerate(block_offsets):
        x5 = multiply(THREE, x3)
        x6 = add(x5, x4)
        x7 = frozenset({(x5, x6), (add(x5, TWO), x6)})
        x2 = fill(x2, color_value, x7)
    return x2


def _make_output_fb791726(
    gi: Grid,
    block_count: Integer,
) -> Grid:
    x0 = height(gi)
    x1 = shape(gi)
    x2 = canvas(ZERO, x1)
    x3 = hconcat(gi, x2)
    x4 = hconcat(x2, gi)
    x5 = vconcat(x3, x4)
    x6 = interval(ZERO, double(x0), ONE)
    for x7 in interval(ZERO, block_count, ONE):
        x8 = add(multiply(THREE, x7), ONE)
        x9 = product(initset(x8), x6)
        x10 = fill(x5, THREE, x9)
        x11 = product(initset(add(x8, x0)), x6)
        x5 = fill(x10, THREE, x11)
    return x5


def generate_fb791726(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = unifint(diff_lb, diff_ub, BLOCK_COUNT_RANGE_FB791726)
        x1 = subtract(MAX_SIDE_FB791726, multiply(THREE, x0))
        x2 = branch(greater(x1, ZERO), unifint(diff_lb, diff_ub, (ZERO, x1)), ZERO)
        x3 = tuple(choice(BLOCK_COLUMNS_FB791726) for _ in range(x0))
        x4 = choice(FOREGROUND_COLORS_FB791726)
        gi = _make_input_fb791726(x3, x2, x4)
        go = _make_output_fb791726(gi, x0)
        if gi == go:
            continue
        if verify_fb791726(gi) != go:
            continue
        return {"input": gi, "output": go}
