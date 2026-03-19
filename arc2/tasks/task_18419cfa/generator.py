from arc2.core import *


def _frame_18419cfa(top: int, left: int, height_: int, width_: int) -> frozenset[tuple[int, int]]:
    x0 = frozenset({(top, left), (top + height_ - ONE, left + width_ - ONE)})
    return box(x0)


def _symmetry_closure_18419cfa(
    cells: frozenset[tuple[int, int]],
    dims: tuple[int, int],
) -> frozenset[tuple[int, int]]:
    height_, width_ = dims
    x0 = set()
    for i, j in cells:
        x0.add((i, j))
        x0.add((i, width_ - ONE - j))
        x0.add((height_ - ONE - i, j))
        x0.add((height_ - ONE - i, width_ - ONE - j))
    return frozenset(x0)


def _sample_full_pattern_18419cfa(
    diff_lb: float,
    diff_ub: float,
    dims: tuple[int, int],
) -> frozenset[tuple[int, int]]:
    height_, width_ = dims
    half_h = height_ // TWO
    half_w = width_ // TWO
    window_h = unifint(diff_lb, diff_ub, (ONE, min(FOUR, half_h)))
    window_w = unifint(diff_lb, diff_ub, (ONE, min(FOUR, half_w)))
    if window_h * window_w < TWO:
        if window_h == ONE:
            window_h = TWO
        else:
            window_w = TWO
    row_slack = half_h - window_h
    col_slack = half_w - window_w
    row_min = max(ZERO, row_slack - TWO)
    col_min = max(ZERO, col_slack - TWO)
    row_start = randint(row_min, row_slack)
    col_start = randint(col_min, col_slack)
    rows = tuple(range(row_start, row_start + window_h))
    cols = tuple(range(col_start, col_start + window_w))
    candidates = [(i, j) for i in rows for j in cols]
    if len(candidates) < TWO:
        return frozenset()
    n_main = unifint(diff_lb, diff_ub, (TWO, min(FIVE, len(candidates))))
    base = set(sample(candidates, n_main))
    if height_ % TWO == ONE and choice((T, F)):
        center_i = height_ // TWO
        axis_cols = sample(cols, randint(ONE, min(TWO, len(cols))))
        for j in axis_cols:
            base.add((center_i, j))
    if width_ % TWO == ONE and choice((T, F)):
        center_j = width_ // TWO
        axis_rows = sample(rows, randint(ONE, min(TWO, len(rows))))
        for i in axis_rows:
            base.add((i, center_j))
    if height_ % TWO == ONE and width_ % TWO == ONE and choice((T, F)):
        base.add((height_ // TWO, width_ // TWO))
    return _symmetry_closure_18419cfa(frozenset(base), dims)


def _input_from_full_pattern_18419cfa(
    full_pattern: frozenset[tuple[int, int]],
    dims: tuple[int, int],
    preserve_axis: str,
) -> frozenset[tuple[int, int]]:
    height_, width_ = dims
    if preserve_axis == "h":
        cutoff = (width_ + ONE) // TWO
        return frozenset((i, j) for i, j in full_pattern if j < cutoff)
    cutoff = (height_ + ONE) // TWO
    return frozenset((i, j) for i, j in full_pattern if i < cutoff)


def _shift_cells_18419cfa(
    cells: frozenset[tuple[int, int]],
    offset: tuple[int, int],
) -> frozenset[tuple[int, int]]:
    return frozenset((i + offset[0], j + offset[1]) for i, j in cells)


def _boxes_separated_18419cfa(
    candidate: tuple[int, int, int, int],
    others: list[tuple[int, int, int, int]],
) -> bool:
    top, left, height_, width_ = candidate
    bottom = top + height_ - ONE
    right = left + width_ - ONE
    for other_top, other_left, other_height, other_width in others:
        other_bottom = other_top + other_height - ONE
        other_right = other_left + other_width - ONE
        if not (
            bottom + ONE < other_top
            or other_bottom + ONE < top
            or right + ONE < other_left
            or other_right + ONE < left
        ):
            return F
    return T


def generate_18419cfa(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        n_frames = choice((ONE, ONE, TWO, TWO, THREE))
        min_side = 14 + THREE * n_frames
        height_ = unifint(diff_lb, diff_ub, (min_side, 30))
        width_ = unifint(diff_lb, diff_ub, (min_side, 30))
        gi = canvas(ZERO, (height_, width_))
        go = gi
        placed: list[tuple[int, int, int, int]] = []
        ok = T
        for _ in range(n_frames):
            frame_height = unifint(diff_lb, diff_ub, (SEVEN, min(13, height_ - TWO)))
            frame_width = unifint(diff_lb, diff_ub, (SEVEN, min(13, width_ - TWO)))
            placed_here = F
            for _ in range(100):
                top = randint(ONE, height_ - frame_height - ONE)
                left = randint(ONE, width_ - frame_width - ONE)
                rect = (top, left, frame_height, frame_width)
                if not _boxes_separated_18419cfa(rect, placed):
                    continue
                interior_shape = (frame_height - TWO, frame_width - TWO)
                full_pattern = _sample_full_pattern_18419cfa(diff_lb, diff_ub, interior_shape)
                if len(full_pattern) < EIGHT:
                    continue
                preserve_axis = choice(("h", "v"))
                input_pattern = _input_from_full_pattern_18419cfa(full_pattern, interior_shape, preserve_axis)
                if input_pattern == full_pattern or len(input_pattern) < THREE:
                    continue
                frame = _frame_18419cfa(top, left, frame_height, frame_width)
                offset = (top + ONE, left + ONE)
                input_red = _shift_cells_18419cfa(input_pattern, offset)
                output_red = _shift_cells_18419cfa(full_pattern, offset)
                gi = fill(gi, EIGHT, frame)
                gi = fill(gi, TWO, input_red)
                go = fill(go, EIGHT, frame)
                go = fill(go, TWO, output_red)
                placed.append(rect)
                placed_here = T
                break
            if not placed_here:
                ok = F
                break
        if not ok:
            continue
        if gi == go:
            continue
        return {"input": gi, "output": go}
