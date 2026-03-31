from synth_rearc.core import *

from .helpers import paint_progression_16de56c4
from .helpers import progression_positions_16de56c4
from .verifier import verify_16de56c4


HEIGHT_RANGE_16DE56C4 = (7, 12)
WIDTH_RANGE_16DE56C4 = (9, 21)
TRACE_COUNT_RANGE_16DE56C4 = (3, 4)
STEP_CHOICES_16DE56C4 = (1, 1, 1, 2, 2, 3, 3, 4, 5)


def _trace_specs_16de56c4(
    diff_lb: float,
    diff_ub: float,
) -> tuple[str, Integer, Integer, tuple[tuple[Integer, Integer, tuple[Integer, ...], tuple[Integer, ...], Integer | None, Integer], ...]]:
    axis = choice(("h", "v"))
    h = unifint(diff_lb, diff_ub, HEIGHT_RANGE_16DE56C4)
    w = unifint(diff_lb, diff_ub, WIDTH_RANGE_16DE56C4)
    line_limit = h if axis == "h" else w
    span_limit = w if axis == "h" else h
    trace_hi = min(TRACE_COUNT_RANGE_16DE56C4[1], line_limit)
    trace_count = unifint(diff_lb, diff_ub, (TRACE_COUNT_RANGE_16DE56C4[0], trace_hi))
    line_order = sample(range(line_limit), trace_count)
    color_order = sample(range(1, 10), 9)
    base_colors = tuple(color_order[:trace_count])
    marker_colors = list(color_order[trace_count:])
    traces = []
    for line, base_color in zip(line_order, base_colors):
        while True:
            step = choice(STEP_CHOICES_16DE56C4)
            if step >= span_limit:
                continue
            residue = randint(ZERO, step - ONE)
            full_positions = progression_positions_16de56c4(span_limit, residue, step)
            if len(full_positions) < TWO:
                continue
            side = choice(("low", "high"))
            if side == "low":
                seed_positions = full_positions[:TWO]
                marker_choices = full_positions[TWO:-ONE]
                output_positions = full_positions
            else:
                seed_positions = full_positions[-TWO:]
                marker_choices = full_positions[ONE:-TWO]
                output_positions = full_positions
            use_marker = (
                len(marker_colors) > ZERO
                and len(marker_choices) > ZERO
                and uniform(0.0, 1.0) < 0.65
            )
            if use_marker:
                marker_pos = choice(marker_choices)
                if side == "low":
                    output_positions = tuple(pos for pos in full_positions if pos <= marker_pos)
                else:
                    output_positions = tuple(pos for pos in full_positions if pos >= marker_pos)
                fill_color = marker_colors.pop(ZERO)
            else:
                marker_pos = None
                fill_color = base_color
            traces.append((line, base_color, seed_positions, output_positions, marker_pos, fill_color))
            break
    return axis, h, w, tuple(traces)


def _add_noise_16de56c4(
    gi: Grid,
    go: Grid,
    axis: str,
    lines_used: tuple[Integer, ...],
    blocked: Indices,
    colors_left: tuple[Integer, ...],
) -> tuple[Grid, Grid]:
    if len(colors_left) == ZERO:
        return gi, go
    h = len(gi)
    w = len(gi[0])
    unused_lines = [line for line in range(h if axis == "h" else w) if line not in lines_used]
    if len(unused_lines) == ZERO:
        return gi, go
    noise_count = min(len(colors_left), randint(ZERO, TWO))
    gi0 = gi
    go0 = go
    for color0 in colors_left[:noise_count]:
        for _ in range(40):
            line = choice(unused_lines)
            pos = randint(ZERO, (w if axis == "h" else h) - ONE)
            loc = (line, pos) if axis == "h" else (pos, line)
            if loc in blocked:
                continue
            gi0 = fill(gi0, color0, initset(loc))
            go0 = fill(go0, color0, initset(loc))
            blocked = insert(loc, blocked)
            break
    return gi0, go0


def generate_16de56c4(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        axis, h, w, traces = _trace_specs_16de56c4(diff_lb, diff_ub)
        gi = canvas(ZERO, (h, w))
        go = canvas(ZERO, (h, w))
        blocked = frozenset()
        for line, base_color, seed_positions, output_positions, marker_pos, fill_color in traces:
            gi = paint_progression_16de56c4(gi, axis, line, seed_positions, base_color)
            if marker_pos is not None:
                gi = paint_progression_16de56c4(gi, axis, line, (marker_pos,), fill_color)
            go = paint_progression_16de56c4(go, axis, line, output_positions, fill_color)
            blocked = combine(
                blocked,
                frozenset((line, pos) if axis == "h" else (pos, line) for pos in output_positions),
            )
        color_pool = tuple(color for color in range(1, 10) if color not in {trace[-1] for trace in traces} and color not in {trace[1] for trace in traces})
        gi, go = _add_noise_16de56c4(
            gi,
            go,
            axis,
            tuple(trace[0] for trace in traces),
            blocked,
            color_pool,
        )
        if verify_16de56c4(gi) != go:
            continue
        return {"input": gi, "output": go}
