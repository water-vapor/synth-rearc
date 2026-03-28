from synth_rearc.core import *

from .helpers import (
    CANONICAL_HORIZONTAL_BARS_1190BC91,
    CANONICAL_VERTICAL_BARS_1190BC91,
    TOP_LIKE_1190BC91,
    bar_mask_1190bc91,
    paint_main_line_1190bc91,
    segment_candidates_1190bc91,
)
from .verifier import verify_1190bc91


COLORS_1190BC91 = tuple(range(ONE, TEN))


def _line_1190bc91(
    horizontal: Boolean,
    start: tuple[Integer, Integer],
    colors: tuple[Integer, ...],
) -> tuple[tuple[Integer, tuple[Integer, Integer]], ...]:
    i, j = start
    if horizontal:
        return tuple((value, (i, j + idx)) for idx, value in enumerate(colors))
    return tuple((value, (i + idx, j)) for idx, value in enumerate(colors))


def _input_grid_1190bc91(
    dims: tuple[Integer, Integer],
    line: tuple[tuple[Integer, tuple[Integer, Integer]], ...],
    bars: tuple[tuple[Integer, Indices], ...],
) -> Grid:
    gi = canvas(ZERO, dims)
    for value, loc in line:
        gi = fill(gi, value, frozenset({loc}))
    for value, patch in bars:
        gi = fill(gi, value, patch)
    return gi


def _output_grid_1190bc91(
    dims: tuple[Integer, Integer],
    line: tuple[tuple[Integer, tuple[Integer, Integer]], ...],
    bars: tuple[tuple[Integer, str], ...],
) -> Grid:
    go = paint_main_line_1190bc91(dims, line)
    for value, name in bars:
        go = fill(go, value, bar_mask_1190bc91(dims, line, name))
    return go


def generate_1190bc91(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        horizontal = choice((T, F))
        pool = CANONICAL_HORIZONTAL_BARS_1190BC91 if horizontal else CANONICAL_VERTICAL_BARS_1190BC91
        use_both = choice((T, T, F))
        bar_names = pool if use_both else (choice(pool),)
        line_len_ub = min(SEVEN, NINE - len(bar_names))
        line_len = unifint(diff_lb, diff_ub, (THREE, line_len_ub))
        side_lb = max(FOUR, line_len + ONE)
        side_ub = min(18, line_len + EIGHT)
        side = unifint(diff_lb, diff_ub, (side_lb, side_ub))
        if horizontal:
            row_lb = TWO if "top_start" in bar_names else ONE
            row_ub = side - TWO
            col_lb = TWO if "left" in bar_names else ONE
            col_ub = side - line_len
        else:
            row_lb = TWO if "top" in bar_names else ONE
            row_ub = side - line_len
            col_lb = ONE
            col_ub = side - (THREE if "right_start" in bar_names else TWO)
        if row_lb > row_ub or col_lb > col_ub:
            continue
        start = (randint(row_lb, row_ub), randint(col_lb, col_ub))
        chosen_colors = sample(COLORS_1190BC91, line_len + len(bar_names))
        line_colors = tuple(chosen_colors[:line_len])
        bar_colors = tuple(chosen_colors[line_len:])
        line = _line_1190bc91(horizontal, start, line_colors)
        dims = (side, side)
        used = frozenset({})
        input_bars = []
        output_bars = []
        failed = False
        for name, value in zip(bar_names, bar_colors):
            mask = bar_mask_1190bc91(dims, line, name)
            bar_horizontal = name in TOP_LIKE_1190BC91
            candidates = segment_candidates_1190bc91(mask, bar_horizontal)
            candidates = tuple(candidate for candidate in candidates if len(intersection(candidate, used)) == ZERO)
            if len(candidates) == ZERO:
                failed = True
                break
            patch = choice(candidates)
            used = combine(used, patch)
            input_bars.append((value, patch))
            output_bars.append((value, name))
        if failed:
            continue
        gi = _input_grid_1190bc91(dims, line, tuple(input_bars))
        go = _output_grid_1190bc91(dims, line, tuple(output_bars))
        if gi == go:
            continue
        if verify_1190bc91(gi) != go:
            continue
        return {"input": gi, "output": go}
