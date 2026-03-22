from arc2.core import *


GRID_SHAPE = (30, 30)
PALETTE = tuple(range(ONE, TEN))
BAR_COUNT_BOUNDS = (THREE, FOUR)
LINE_AXIS_BOUNDS = (THREE, 26)
BAR_CENTER_BOUNDS = (TWO, 27)
MARKER_AXIS_BOUNDS = (ONE, 28)
MIN_GAP = FOUR


def _sample_axis_positions_7e576d6e(
    count: int,
    bounds: tuple[int, int],
    min_gap: int,
) -> tuple[int, ...]:
    lo, hi = bounds
    values = tuple(range(lo, hi + ONE))
    while True:
        picks = sorted(sample(values, count))
        if all(b - a >= min_gap for a, b in zip(picks, picks[1:])):
            return tuple(picks)


def _wire_patch_7e576d6e(
    points: tuple[tuple[int, int], ...],
    vertical_bars: bool,
) -> Indices:
    patch = set()
    last_idx = len(points) - ONE
    for idx in range(last_idx):
        start = points[idx]
        end = points[idx + ONE]
        is_last_leg = idx == last_idx - ONE
        if vertical_bars:
            if is_last_leg:
                turn = (start[0], end[1])
                patch |= connect(start, turn)
                patch |= connect(turn, end)
            else:
                step = ONE if end[1] > start[1] else NEG_ONE
                turn_col = end[1] - step
                turn_a = (start[0], turn_col)
                turn_b = (end[0], turn_col)
                patch |= connect(start, turn_a)
                patch |= connect(turn_a, turn_b)
                patch |= connect(turn_b, end)
        else:
            if is_last_leg:
                turn = (end[0], start[1])
                patch |= connect(start, turn)
                patch |= connect(turn, end)
            else:
                step = ONE if end[0] > start[0] else NEG_ONE
                turn_row = end[0] - step
                turn_a = (turn_row, start[1])
                turn_b = (turn_row, end[1])
                patch |= connect(start, turn_a)
                patch |= connect(turn_a, turn_b)
                patch |= connect(turn_b, end)
    return frozenset(patch)


def _build_vertical_task_7e576d6e(
    bg: int,
    line_color: int,
    bar_color: int,
    wire_color: int,
    diff_lb: float,
    diff_ub: float,
) -> dict:
    count = unifint(diff_lb, diff_ub, BAR_COUNT_BOUNDS)
    cols = _sample_axis_positions_7e576d6e(count, LINE_AXIS_BOUNDS, MIN_GAP)
    row_values = tuple(range(BAR_CENTER_BOUNDS[0], BAR_CENTER_BOUNDS[1] + ONE))
    rows = tuple(sample(row_values, count))
    left_marker = (
        unifint(diff_lb, diff_ub, MARKER_AXIS_BOUNDS),
        randint(MARKER_AXIS_BOUNDS[0], cols[0] - TWO),
    )
    right_marker = (
        unifint(diff_lb, diff_ub, MARKER_AXIS_BOUNDS),
        randint(cols[-1] + TWO, MARKER_AXIS_BOUNDS[1]),
    )
    gi = canvas(bg, GRID_SHAPE)
    centers = []
    for col, row in zip(cols, rows):
        line = connect((ZERO, col), (GRID_SHAPE[0] - ONE, col))
        bar = connect((row - ONE, col), (row + ONE, col))
        gi = fill(gi, line_color, line)
        gi = fill(gi, bar_color, bar)
        centers.append((row, col))
    gi = fill(gi, wire_color, frozenset({left_marker, right_marker}))
    points = (left_marker,) + tuple(centers) + (right_marker,)
    patch = _wire_patch_7e576d6e(points, T)
    go = fill(gi, wire_color, patch)
    return {"input": gi, "output": go}


def _build_horizontal_task_7e576d6e(
    bg: int,
    line_color: int,
    bar_color: int,
    wire_color: int,
    diff_lb: float,
    diff_ub: float,
) -> dict:
    count = unifint(diff_lb, diff_ub, BAR_COUNT_BOUNDS)
    rows = _sample_axis_positions_7e576d6e(count, LINE_AXIS_BOUNDS, MIN_GAP)
    col_values = tuple(range(BAR_CENTER_BOUNDS[0], BAR_CENTER_BOUNDS[1] + ONE))
    cols = tuple(sample(col_values, count))
    top_marker = (
        randint(MARKER_AXIS_BOUNDS[0], rows[0] - TWO),
        unifint(diff_lb, diff_ub, MARKER_AXIS_BOUNDS),
    )
    bottom_marker = (
        randint(rows[-1] + TWO, MARKER_AXIS_BOUNDS[1]),
        unifint(diff_lb, diff_ub, MARKER_AXIS_BOUNDS),
    )
    gi = canvas(bg, GRID_SHAPE)
    centers = []
    for row, col in zip(rows, cols):
        line = connect((row, ZERO), (row, GRID_SHAPE[1] - ONE))
        bar = connect((row, col - ONE), (row, col + ONE))
        gi = fill(gi, line_color, line)
        gi = fill(gi, bar_color, bar)
        centers.append((row, col))
    gi = fill(gi, wire_color, frozenset({top_marker, bottom_marker}))
    points = (top_marker,) + tuple(centers) + (bottom_marker,)
    patch = _wire_patch_7e576d6e(points, F)
    go = fill(gi, wire_color, patch)
    return {"input": gi, "output": go}


def generate_7e576d6e(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    bg, line_color, bar_color, wire_color = sample(PALETTE, FOUR)
    if choice((T, F)):
        return _build_vertical_task_7e576d6e(
            bg,
            line_color,
            bar_color,
            wire_color,
            diff_lb,
            diff_ub,
        )
    return _build_horizontal_task_7e576d6e(
        bg,
        line_color,
        bar_color,
        wire_color,
        diff_lb,
        diff_ub,
    )
