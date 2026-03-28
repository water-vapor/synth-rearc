from synth_rearc.core import *


def make_rectangle_8cb8642d(
    top: Integer,
    left: Integer,
    height_: Integer,
    width_: Integer,
) -> Indices:
    x0 = interval(top, top + height_, ONE)
    x1 = interval(left, left + width_, ONE)
    x2 = product(x0, x1)
    return x2


def pattern_indices_8cb8642d(
    patch: Patch,
) -> Indices:
    x0 = increment(uppermost(patch))
    x1 = decrement(lowermost(patch))
    x2 = increment(leftmost(patch))
    x3 = decrement(rightmost(patch))
    x4 = set()
    while x0 <= x1 and x2 <= x3:
        x5 = x1 - x0 + ONE
        x6 = x3 - x2 + ONE
        x7 = make_rectangle_8cb8642d(x0, x2, x5, x6)
        if x5 <= TWO or x6 <= TWO:
            x4 |= x7
            break
        x4 |= corners(x7)
        x0 += ONE
        x1 -= ONE
        x2 += ONE
        x3 -= ONE
    return frozenset(x4)


def transform_rectangle_8cb8642d(
    grid: Grid,
    patch: Patch,
    fill_color: Integer,
    pattern_color: Integer,
) -> Grid:
    x0 = box(patch)
    x1 = delta(x0)
    x2 = fill(grid, ZERO, x1)
    x3 = fill(x2, fill_color, x0)
    x4 = pattern_indices_8cb8642d(patch)
    x5 = fill(x3, pattern_color, x4)
    return x5
