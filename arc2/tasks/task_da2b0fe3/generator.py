from arc2.core import *


COLORS_DA2B0FE3 = (ONE, TWO, FOUR, FIVE, SIX, SEVEN, EIGHT, NINE)
GRID_SHAPE_DA2B0FE3 = (TEN, TEN)
PATTERN_MODES_DA2B0FE3 = ("constant", "alternate", "mirror", "random")


def _make_lengths_da2b0fe3(height: int, width: int, diff_lb: float, diff_ub: float) -> tuple[int, ...]:
    if width == ONE:
        return tuple(ONE for _ in range(height))
    mode = choice(PATTERN_MODES_DA2B0FE3)
    if mode == "constant":
        value = unifint(diff_lb, diff_ub, (ONE, width))
        return tuple(value for _ in range(height))
    if mode == "alternate":
        a = unifint(diff_lb, diff_ub, (ONE, width))
        b = unifint(diff_lb, diff_ub, (ONE, width))
        if a == b:
            b = branch(equality(a, ONE), width, ONE)
        phase = randint(ZERO, ONE)
        return tuple(a if (k + phase) % TWO == ZERO else b for k in range(height))
    if mode == "mirror":
        half = [unifint(diff_lb, diff_ub, (ONE, width)) for _ in range((height + ONE) // TWO)]
        tail = half[:-ONE] if height % TWO == ONE else half
        return tuple(half + list(reversed(tail)))
    seq = [unifint(diff_lb, diff_ub, (ONE, width)) for _ in range(height)]
    if width > ONE and len(set(seq)) == ONE:
        idx = randint(ZERO, height - ONE)
        step = choice((-ONE, ONE))
        seq[idx] = min(width, max(ONE, seq[idx] + step))
    return tuple(seq)


def _sample_intervals_da2b0fe3(span: int) -> tuple[tuple[int, int], tuple[int, int]]:
    while True:
        start_a = randint(ZERO, span - ONE)
        end_a = randint(start_a, span - ONE)
        start_b = randint(ZERO, span - ONE)
        end_b = randint(start_b, span - ONE)
        if min(start_a, start_b) != ZERO:
            continue
        if max(end_a, end_b) != span - ONE:
            continue
        if max(start_a, start_b) > min(end_a, end_b):
            continue
        return (start_a, end_a), (start_b, end_b)


def _make_component_da2b0fe3(
    top: int,
    left: int,
    width: int,
    interval: tuple[int, int],
    align_right: bool,
    diff_lb: float,
    diff_ub: float,
) -> frozenset[tuple[int, int]]:
    start, end = interval
    seq = _make_lengths_da2b0fe3(end - start + ONE, width, diff_lb, diff_ub)
    cells = set()
    for offset, length in enumerate(seq):
        row = top + start + offset
        shift = width - length if align_right else ZERO
        for col in range(length):
            cells.add((row, left + shift + col))
    return frozenset(cells)


def generate_da2b0fe3(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        color = choice(COLORS_DA2B0FE3)
        span_h = unifint(diff_lb, diff_ub, (FOUR, SEVEN))
        left_w = unifint(diff_lb, diff_ub, (ONE, FOUR))
        right_w = unifint(diff_lb, diff_ub, (ONE, FOUR))
        if left_w + right_w + ONE > SEVEN:
            continue
        max_top = min(THREE, TEN - span_h - ONE)
        max_left = min(THREE, TEN - left_w - right_w - TWO)
        top = randint(ONE, max_top)
        left = randint(ONE, max_left)
        gap_col = left + left_w
        interval_a, interval_b = _sample_intervals_da2b0fe3(span_h)
        left_cells = _make_component_da2b0fe3(
            top,
            left,
            left_w,
            interval_a,
            choice((T, F)),
            diff_lb,
            diff_ub,
        )
        right_cells = _make_component_da2b0fe3(
            top,
            gap_col + ONE,
            right_w,
            interval_b,
            choice((T, F)),
            diff_lb,
            diff_ub,
        )
        if size(left_cells) < FOUR or size(right_cells) < FOUR:
            continue
        if rightmost(left_cells) != gap_col - ONE:
            continue
        if leftmost(right_cells) != gap_col + ONE:
            continue
        grid = fill(canvas(ZERO, GRID_SHAPE_DA2B0FE3), color, combine(left_cells, right_cells))
        line = connect((ZERO, gap_col), (NINE, gap_col))
        out = fill(grid, THREE, line)
        if choice((T, F)):
            grid = dmirror(grid)
            out = dmirror(out)
        comps = objects(grid, T, F, T)
        if size(comps) != TWO:
            continue
        return {"input": grid, "output": out}
