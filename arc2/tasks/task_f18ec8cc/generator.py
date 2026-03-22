from arc2.core import *

from .helpers import concat_strips_f18ec8cc, split_vertical_strips_f18ec8cc
from .verifier import verify_f18ec8cc


ACTIVE_COLORS_F18EC8CC = difference(interval(ONE, TEN, ONE), frozenset({SIX}))
STRIP_COUNT_POOL_F18EC8CC = (THREE, THREE, THREE, FOUR, FOUR)


def _sample_widths_f18ec8cc(
    strip_count: Integer,
    total_width: Integer,
) -> tuple[Integer, ...]:
    x0 = [THREE] * strip_count
    x1 = total_width - strip_count * THREE
    x2 = SEVEN if equality(strip_count, THREE) else FIVE
    while x1 > ZERO:
        x3 = tuple(x4 for x4, x5 in enumerate(x0) if x5 < x2)
        if len(x3) == ZERO:
            raise ValueError("failed to distribute strip widths")
        x4 = choice(x3)
        x0[x4] += ONE
        x1 -= ONE
    shuffle(x0)
    return tuple(x0)


def _sample_colors_f18ec8cc(
    strip_count: Integer,
) -> tuple[Integer, ...]:
    x0 = tuple(sample(ACTIVE_COLORS_F18EC8CC, strip_count))
    return x0


def _noise_columns_f18ec8cc(
    width_value: Integer,
    strip_count: Integer,
) -> tuple[Integer, ...]:
    if equality(strip_count, THREE) and even(width_value):
        x0 = width_value // TWO
        return (x0 - ONE, x0)
    if equality(width_value, FIVE):
        return (choice((TWO, THREE)),)
    return ((width_value - ONE) // TWO,)


def _build_strip_f18ec8cc(
    height_value: Integer,
    width_value: Integer,
    strip_color: Integer,
    palette_values: tuple[Integer, ...],
    strip_count: Integer,
) -> Grid:
    x0 = canvas(strip_color, (height_value, width_value))
    x1 = [x2 for x2 in palette_values if not equality(x2, strip_color)]
    shuffle(x1)
    x2 = sample(tuple(range(height_value)), len(x1))
    x3 = _noise_columns_f18ec8cc(width_value, strip_count)
    for x4, x5 in enumerate(x1):
        x6 = x2[x4]
        x7 = x3[x4 % len(x3)]
        x8 = frozenset({(x6, x7)})
        x0 = fill(x0, x5, x8)
    return x0


def generate_f18ec8cc(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = choice(STRIP_COUNT_POOL_F18EC8CC)
        x1 = unifint(diff_lb, diff_ub, (SEVEN, NINE))
        x2 = branch(equality(x0, THREE), (TEN, 14), (12, 15))
        x3 = unifint(diff_lb, diff_ub, x2)
        x4 = _sample_widths_f18ec8cc(x0, x3)
        x5 = _sample_colors_f18ec8cc(x0)
        x6 = tuple(
            _build_strip_f18ec8cc(x1, x7, x8, x5, x0)
            for x7, x8 in zip(x4, x5)
        )
        x7 = concat_strips_f18ec8cc(x6)
        x8 = split_vertical_strips_f18ec8cc(x7)
        x9 = apply(first, x8)
        if x9 != x5:
            continue
        x10 = x8[1:] + x8[:1]
        x11 = apply(last, x10)
        x12 = concat_strips_f18ec8cc(x11)
        if equality(x7, x12):
            continue
        if verify_f18ec8cc(x7) != x12:
            continue
        return {"input": x7, "output": x12}
