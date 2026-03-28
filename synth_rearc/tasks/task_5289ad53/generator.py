from synth_rearc.core import *


BACKGROUND_COLORS_5289AD53 = (ZERO, ONE, FIVE, EIGHT)
COUNT_PAIRS_5289AD53 = (
    (TWO, TWO),
    (THREE, TWO),
    (TWO, FOUR),
    (FOUR, ONE),
    (THREE, THREE),
)


def _overlaps_5289ad53(a0: int, a1: int, b0: int, b1: int) -> bool:
    return not (a1 < b0 or b1 < a0)


def _touches_same_row_5289ad53(a0: int, a1: int, b0: int, b1: int) -> bool:
    return not (a1 + ONE < b0 or b1 + ONE < a0)


def _can_place_bar_5289ad53(
    bars: list[tuple[int, int, int, int]],
    color_value: int,
    row_value: int,
    left_value: int,
    length_value: int,
) -> bool:
    right_value = left_value + length_value - ONE
    for other_color, other_row, other_left, other_length in bars:
        other_right = other_left + other_length - ONE
        if row_value == other_row and _touches_same_row_5289ad53(
            left_value,
            right_value,
            other_left,
            other_right,
        ):
            return False
        if abs(row_value - other_row) == ONE and _overlaps_5289ad53(
            left_value,
            right_value,
            other_left,
            other_right,
        ):
            return False
    return True


def _paint_bar_5289ad53(
    grid: Grid,
    color_value: int,
    row_value: int,
    left_value: int,
    length_value: int,
) -> Grid:
    patch = frozenset((row_value, j) for j in range(left_value, left_value + length_value))
    return fill(grid, color_value, patch)


def _make_output_5289ad53(count3_value: int, count2_value: int) -> Grid:
    x0 = combine(repeat(THREE, count3_value), repeat(TWO, count2_value))
    x1 = combine(x0, repeat(ZERO, subtract(SIX, add(count3_value, count2_value))))
    return (x1[:THREE], x1[THREE:SIX])


def generate_5289ad53(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        count3_value, count2_value = choice(COUNT_PAIRS_5289AD53)
        height_value = unifint(diff_lb, diff_ub, (TEN, 15))
        width_value = unifint(diff_lb, diff_ub, (TEN, 19))
        background_value = choice(BACKGROUND_COLORS_5289AD53)
        color_values = list(combine(repeat(THREE, count3_value), repeat(TWO, count2_value)))
        shuffle(color_values)
        bars: list[tuple[int, int, int, int]] = []
        attempts = ZERO
        max_bar_length = max(TWO, min(NINE, width_value - TWO))
        while len(bars) < len(color_values) and attempts < 400:
            attempts += ONE
            color_value = color_values[len(bars)]
            row_value = choice(interval(ONE, height_value - ONE, ONE))
            length_value = unifint(diff_lb, diff_ub, (TWO, max_bar_length))
            left_value = choice(interval(ZERO, width_value - length_value + ONE, ONE))
            if not _can_place_bar_5289ad53(
                bars,
                color_value,
                row_value,
                left_value,
                length_value,
            ):
                continue
            bars.append((color_value, row_value, left_value, length_value))
        if len(bars) != len(color_values):
            continue
        gi = canvas(background_value, (height_value, width_value))
        for color_value, row_value, left_value, length_value in bars:
            gi = _paint_bar_5289ad53(gi, color_value, row_value, left_value, length_value)
        go = _make_output_5289ad53(count3_value, count2_value)
        if gi == go:
            continue
        return {"input": gi, "output": go}
