from synth_rearc.core import *


FRAME_ROWS_351D6448 = (ZERO, FOUR, EIGHT, 12)
FRAME_SHAPE_351D6448 = (THREE, 13)
INPUT_SHAPE_351D6448 = (15, 13)
CONTENT_COLORS_351D6448 = tuple(color for color in range(ONE, TEN) if color != FIVE)


def _stack_frames_351d6448(frames: tuple[Grid, ...]) -> Grid:
    gi = canvas(ZERO, INPUT_SHAPE_351D6448)
    for row in (THREE, SEVEN, 11):
        gi = fill(gi, FIVE, connect((row, ZERO), (row, INPUT_SHAPE_351D6448[ONE] - ONE)))
    for row, frame in zip(FRAME_ROWS_351D6448, frames):
        gi = paint(gi, shift(asobject(frame), (row, ZERO)))
    return gi


def _bar_frame_351d6448(
    row: Integer,
    start: Integer,
    length: Integer,
    value: Integer,
) -> Grid:
    go = canvas(ZERO, FRAME_SHAPE_351D6448)
    return fill(go, value, connect((row, start), (row, start + length - ONE)))


def _generate_bar_mode_351d6448(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    row = ONE
    step = unifint(diff_lb, diff_ub, (ONE, THREE))
    start_max = INPUT_SHAPE_351D6448[ONE] - ONE - FOUR * step
    start = unifint(diff_lb, diff_ub, (ZERO, start_max))
    max_initial = INPUT_SHAPE_351D6448[ONE] - start - FOUR * step
    initial = unifint(diff_lb, diff_ub, (ONE, max_initial))
    value = choice(CONTENT_COLORS_351D6448)
    lengths = tuple(initial + step * k for k in range(FIVE))
    frames = tuple(_bar_frame_351d6448(row, start, length, value) for length in lengths[:FOUR])
    return {"input": _stack_frames_351d6448(frames), "output": _bar_frame_351d6448(row, start, lengths[-ONE], value)}


def _motif_frame_351d6448(
    row: Integer,
    start: Integer,
    motif: tuple[Integer, ...],
) -> Grid:
    go = canvas(ZERO, FRAME_SHAPE_351D6448)
    for offset, value in enumerate(motif):
        go = fill(go, value, frozenset({(row, start + offset)}))
    return go


def _generate_shift_mode_351d6448(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    row = ONE
    step = unifint(diff_lb, diff_ub, (ONE, TWO))
    length = unifint(diff_lb, diff_ub, (TWO, FOUR))
    start_max = INPUT_SHAPE_351D6448[ONE] - length - FOUR * step
    start = unifint(diff_lb, diff_ub, (ZERO, start_max))
    colors = sample(CONTENT_COLORS_351D6448, unifint(diff_lb, diff_ub, (ONE, min(THREE, length))))
    motif = [choice(colors) for _ in range(length)]
    if size(set(motif)) == ONE:
        motif[-ONE] = choice(tuple(color for color in CONTENT_COLORS_351D6448 if color != motif[-ONE]))
    motif = tuple(motif)
    starts = tuple(start + step * k for k in range(FIVE))
    frames = tuple(_motif_frame_351d6448(row, left, motif) for left in starts[:FOUR])
    return {"input": _stack_frames_351d6448(frames), "output": _motif_frame_351d6448(row, starts[-ONE], motif)}


def _pyramid_support_351d6448(left_edge: Integer, count: Integer) -> frozenset[tuple[Integer, Integer]]:
    support = set()
    for idx in range(count):
        center = left_edge + TWO + FOUR * idx
        support.add((ZERO, center))
        support.update((ONE, center + delta) for delta in (-ONE, ZERO, ONE))
        support.update((TWO, center + delta) for delta in range(-TWO, THREE))
    return frozenset(support)


def _recolor_frame_351d6448(
    support: frozenset[tuple[Integer, Integer]],
    threshold: Integer,
    old_color: Integer,
    new_color: Integer,
) -> Grid:
    go = canvas(ZERO, FRAME_SHAPE_351D6448)
    go = fill(go, old_color, support)
    reveal = frozenset((i, j) for i, j in support if j <= threshold)
    return fill(go, new_color, reveal)


def _generate_recolor_mode_351d6448(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    count = unifint(diff_lb, diff_ub, (ONE, THREE))
    width = FOUR * (count - ONE) + FIVE
    left_edge = unifint(diff_lb, diff_ub, (ZERO, INPUT_SHAPE_351D6448[ONE] - width))
    feasible_steps = tuple(step for step in (ONE, TWO) if width - ONE >= FOUR * step)
    step = choice(feasible_steps)
    right_edge = left_edge + width - ONE
    threshold = unifint(diff_lb, diff_ub, (left_edge, right_edge - FOUR * step))
    old_color, new_color = sample(CONTENT_COLORS_351D6448, TWO)
    support = _pyramid_support_351d6448(left_edge, count)
    thresholds = tuple(threshold + step * k for k in range(FIVE))
    frames = tuple(
        _recolor_frame_351d6448(support, current, old_color, new_color)
        for current in thresholds[:FOUR]
    )
    return {
        "input": _stack_frames_351d6448(frames),
        "output": _recolor_frame_351d6448(support, thresholds[-ONE], old_color, new_color),
    }


def generate_351d6448(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    mode = choice(("bar", "shift", "recolor"))
    if mode == "bar":
        return _generate_bar_mode_351d6448(diff_lb, diff_ub)
    if mode == "shift":
        return _generate_shift_mode_351d6448(diff_lb, diff_ub)
    return _generate_recolor_mode_351d6448(diff_lb, diff_ub)
