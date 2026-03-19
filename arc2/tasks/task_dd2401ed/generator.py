from arc2.core import *


def _bar_indices_dd2401ed(height: int, col: int) -> Indices:
    return frozenset((i, col) for i in range(height))


def _sample_blue_positions_dd2401ed(
    bar_col: int,
    height: int,
    diff_lb: float,
    diff_ub: float,
) -> tuple[Indices, tuple[int, ...], frozenset[int]]:
    num_active_cols = unifint(diff_lb, diff_ub, (ONE, bar_col))
    active_cols = {ZERO}
    if num_active_cols > ONE:
        active_cols.update(sample(range(ONE, bar_col), num_active_cols - ONE))
    active_cols_tuple = tuple(sorted(active_cols))
    blue_positions = {(choice(range(height)), col) for col in active_cols_tuple}
    max_extra = min(TWO, height * len(active_cols_tuple) - len(blue_positions))
    if max_extra > ZERO:
        extra_count = unifint(diff_lb, diff_ub, (ZERO, max_extra))
        if extra_count > ZERO:
            extra_pool = [
                (i, j)
                for i in range(height)
                for j in active_cols_tuple
                if (i, j) not in blue_positions
            ]
            blue_positions.update(sample(extra_pool, extra_count))
    offsets = frozenset(bar_col - col for col in active_cols_tuple)
    return frozenset(blue_positions), active_cols_tuple, offsets


def _sample_gap_reds_dd2401ed(
    bar_col: int,
    new_col: int,
    blue_offsets: frozenset[int],
    height: int,
    diff_lb: float,
    diff_ub: float,
    matched: bool,
) -> Indices:
    gap_cols = tuple(range(bar_col + ONE, new_col))
    required_cols = frozenset(bar_col + offset for offset in blue_offsets)
    gap_reds = set()
    if matched:
        for col in sorted(required_cols):
            gap_reds.add((choice(range(height)), col))
        extra_pool = [
            (i, j)
            for i in range(height)
            for j in gap_cols
            if (i, j) not in gap_reds
        ]
        max_extra = min(THREE, len(extra_pool))
        if max_extra > ZERO:
            extra_count = unifint(diff_lb, diff_ub, (ZERO, max_extra))
            if extra_count > ZERO:
                gap_reds.update(sample(extra_pool, extra_count))
        return frozenset(gap_reds)
    missing_col = choice(tuple(required_cols))
    available_cols = tuple(j for j in gap_cols if j != missing_col)
    available_pool = [(i, j) for i in range(height) for j in available_cols]
    if len(available_pool) == ZERO:
        return frozenset()
    max_gap = min(FOUR, len(available_pool))
    min_gap = ZERO if choice((T, F)) else ONE
    gap_count = unifint(diff_lb, diff_ub, (min_gap, max_gap))
    if gap_count == ZERO:
        return frozenset()
    return frozenset(sample(available_pool, gap_count))


def generate_dd2401ed(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    height = SEVEN
    width = add(TEN, FIVE)
    bar_col = unifint(diff_lb, diff_ub, (ONE, FIVE))
    bar = _bar_indices_dd2401ed(height, bar_col)
    blue_positions, _, blue_offsets = _sample_blue_positions_dd2401ed(
        bar_col,
        height,
        diff_lb,
        diff_ub,
    )
    max_offset = maximum(blue_offsets)
    new_col = bar_col + max_offset + ONE
    matched = choice((T, F))
    gap_reds = _sample_gap_reds_dd2401ed(
        bar_col,
        new_col,
        blue_offsets,
        height,
        diff_lb,
        diff_ub,
        matched,
    )
    outside_cols = tuple(range(new_col + ONE, width))
    outside_pool = [(i, j) for i in range(height) for j in outside_cols]
    outside_count = unifint(diff_lb, diff_ub, (ONE, min(FOUR, len(outside_pool))))
    outside_reds = frozenset(sample(outside_pool, outside_count))
    red_positions = gap_reds | outside_reds
    gi = canvas(ZERO, (height, width))
    gi = fill(gi, ONE, blue_positions)
    gi = fill(gi, TWO, red_positions)
    gi = fill(gi, FIVE, bar)
    go = cover(gi, bar)
    if matched:
        go = fill(go, ONE, gap_reds)
    go = fill(go, FIVE, _bar_indices_dd2401ed(height, new_col))
    return {"input": gi, "output": go}
