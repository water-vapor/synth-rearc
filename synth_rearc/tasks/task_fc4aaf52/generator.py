from synth_rearc.core import *


OUTER_PATTERNS_FC4AAF52 = {
    THREE: (
        (ONE, THREE, THREE),
        (ONE, THREE, FIVE),
        (THREE, FIVE, FIVE),
        (THREE, FIVE, SEVEN),
    ),
    FOUR: (
        (ONE, THREE, FIVE, THREE),
        (ONE, THREE, THREE, FIVE),
        (ONE, ONE, THREE, FIVE),
        (ONE, THREE, FIVE, FIVE),
        (THREE, FIVE, SEVEN, FIVE),
        (THREE, FIVE, FIVE, SEVEN),
    ),
}


def _rows_overlap_fc4aaf52(
    left_a: int,
    width_a: int,
    left_b: int,
    width_b: int,
) -> bool:
    right_a = left_a + width_a - ONE
    right_b = left_b + width_b - ONE
    return max(left_a, left_b) <= min(right_a, right_b)


def _make_outer_rows_fc4aaf52(
    widths: tuple[int, ...],
) -> tuple[tuple[int, int], ...]:
    while True:
        lefts = [ZERO]
        valid = True
        for prev_width, width in zip(widths, widths[ONE:]):
            if width > prev_width:
                deltas = (-ONE, ZERO)
            elif width < prev_width:
                deltas = (ZERO, ONE)
            else:
                deltas = (-ONE, ZERO, ONE)
            options = tuple(
                delta
                for delta in deltas
                if _rows_overlap_fc4aaf52(lefts[-ONE], prev_width, lefts[-ONE] + delta, width)
            )
            if len(options) == ZERO:
                valid = False
                break
            lefts.append(lefts[-ONE] + choice(options))
        if valid:
            offset = min(lefts)
            return tuple((left - offset, width) for left, width in zip(lefts, widths))


def _sample_inner_widths_fc4aaf52(
    outer_rows: tuple[tuple[int, int], ...],
) -> tuple[int, ...]:
    while True:
        widths = []
        prev_width = ZERO
        for idx, (_, outer_width) in enumerate(outer_rows):
            max_inner_width = outer_width - TWO
            if max_inner_width <= ZERO:
                widths.append(ZERO)
                prev_width = ZERO
                continue
            lower = max(ZERO, prev_width - TWO)
            upper = min(max_inner_width, prev_width + THREE)
            options = list(range(lower, upper + ONE))
            if idx == ZERO and ZERO in options and randint(ZERO, THREE) != ZERO:
                width = ZERO
            else:
                if idx == len(outer_rows) - ONE and ZERO in options:
                    options.remove(ZERO)
                width = choice(tuple(options))
            widths.append(width)
            prev_width = width
        if max(widths) > ZERO:
            return tuple(widths)


def _row_segment_fc4aaf52(
    row: int,
    left: int,
    width: int,
):
    return connect((row, left), (row, left + width - ONE))


def generate_fc4aaf52(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    h = 16
    w = 16
    bgc = EIGHT
    cols = remove(bgc, interval(ZERO, TEN, ONE))
    while True:
        gi = canvas(bgc, (h, w))
        go = canvas(bgc, (h, w))
        outer_color, inner_color = sample(cols, TWO)
        half_height = unifint(diff_lb, diff_ub, (THREE, FOUR))
        width_pattern = choice(OUTER_PATTERNS_FC4AAF52[half_height])
        outer_top_rows = _make_outer_rows_fc4aaf52(width_pattern)
        inner_top_widths = _sample_inner_widths_fc4aaf52(outer_top_rows)
        seam_width = outer_top_rows[-ONE][ONE]
        full_outer_rows = outer_top_rows + tuple(reversed(outer_top_rows))
        full_inner_widths = inner_top_widths + tuple(reversed(inner_top_widths))
        full_height = len(full_outer_rows)
        obj_width = max(left + width for left, width in full_outer_rows)
        top_hi = h - full_height - TWO
        top = unifint(diff_lb, diff_ub, (TWO, top_hi))
        left_max = w - obj_width - seam_width
        left_hi = min(FOUR, left_max)
        left_lo = ONE if left_hi >= ONE else ZERO
        left = unifint(diff_lb, diff_ub, (left_lo, left_hi))
        for ridx, ((row_left, row_width), inner_width) in enumerate(zip(full_outer_rows, full_inner_widths)):
            row = top + ridx
            shift_j = seam_width if ridx < half_height else ZERO
            outer_seg = _row_segment_fc4aaf52(row, left + row_left, row_width)
            gi = fill(gi, outer_color, outer_seg)
            go = fill(go, inner_color, shift(outer_seg, (ZERO, shift_j)))
            if inner_width > ZERO:
                inner_seg = _row_segment_fc4aaf52(row, left + row_left + ONE, inner_width)
                gi = fill(gi, inner_color, inner_seg)
                go = fill(go, outer_color, shift(inner_seg, (ZERO, shift_j)))
        if size(objects(gi, F, F, T)) != ONE:
            continue
        return {"input": gi, "output": go}
