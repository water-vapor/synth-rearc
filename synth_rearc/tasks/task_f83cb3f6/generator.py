from synth_rearc.core import *

from .verifier import verify_f83cb3f6


FG_COLORS_F83CB3F6 = remove(EIGHT, remove(ZERO, interval(ZERO, TEN, ONE)))


def _sample_frontier_positions_f83cb3f6(
    diff_lb: float,
    diff_ub: float,
    length: Integer,
) -> tuple[Integer, ...]:
    coords = tuple(range(length))
    if choice((T, F)):
        active = coords
    else:
        seg_lb = max(THREE, length // TWO)
        seg_len = unifint(diff_lb, diff_ub, (seg_lb, length))
        start = randint(ZERO, length - seg_len)
        active = tuple(range(start, start + seg_len))
    if len(active) >= FIVE and choice((T, T, F)):
        removable = active[ONE:-ONE]
        nholes = randint(ONE, min(THREE, len(removable)))
        holes = set(sample(removable, nholes))
        active = tuple(coord for coord in active if coord not in holes)
    return active if len(active) >= THREE else coords


def _choose_cells_f83cb3f6(
    candidates: tuple[IntegerTuple, ...],
    occupied: set[IntegerTuple],
    desired: Integer,
) -> tuple[IntegerTuple, ...]:
    pool = list(candidates)
    shuffle(pool)
    chosen = []
    blocked = set(occupied)
    for cell in pool:
        if cell in blocked:
            continue
        if any(abs(cell[ZERO] - other[ZERO]) + abs(cell[ONE] - other[ONE]) == ONE for other in blocked):
            continue
        chosen.append(cell)
        blocked.add(cell)
        if len(chosen) == desired:
            break
    if desired > ZERO and len(chosen) == ZERO and len(pool) > ZERO:
        chosen.append(pool[ZERO])
    return tuple(chosen)


def _paint_sources_f83cb3f6(
    gi: Grid,
    occupied: set[IntegerTuple],
    candidates: tuple[IntegerTuple, ...],
    color_value: Integer,
    desired: Integer,
) -> tuple[Grid, set[IntegerTuple]]:
    cells = _choose_cells_f83cb3f6(candidates, occupied, desired)
    if len(cells) > ZERO:
        gi = fill(gi, color_value, frozenset(cells))
        occupied.update(cells)
    return gi, occupied


def _desired_sources_f83cb3f6(
    limit: Integer,
) -> Integer:
    if limit <= ZERO:
        return ZERO
    return min(limit, choice((ONE, ONE, TWO, TWO, THREE)))


def _generate_horizontal_f83cb3f6(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    h = unifint(diff_lb, diff_ub, (TEN, 18))
    w = unifint(diff_lb, diff_ub, (TEN, 18))
    axis_row = randint(ONE, h - TWO)
    active_cols = _sample_frontier_positions_f83cb3f6(diff_lb, diff_ub, w)
    active_col_set = set(active_cols)
    color_value = choice(FG_COLORS_F83CB3F6)
    axis = frozenset((axis_row, j) for j in active_cols)
    gi = fill(canvas(ZERO, (h, w)), EIGHT, axis)
    go = fill(canvas(ZERO, (h, w)), EIGHT, axis)
    above_targets = tuple(j for j in active_cols if choice((T, T, F)))
    below_targets = tuple(j for j in active_cols if choice((T, T, F)))
    if len(above_targets) == ZERO and len(below_targets) == ZERO:
        forced = choice(active_cols)
        if choice((T, F)):
            above_targets = (forced,)
        else:
            below_targets = (forced,)
    occupied = set()
    for j in above_targets:
        candidates = tuple((i, j) for i in range(axis_row))
        gi, occupied = _paint_sources_f83cb3f6(
            gi,
            occupied,
            candidates,
            color_value,
            _desired_sources_f83cb3f6(len(candidates)),
        )
        go = fill(go, color_value, frozenset({(axis_row - ONE, j)}))
    for j in below_targets:
        candidates = tuple((i, j) for i in range(axis_row + ONE, h))
        gi, occupied = _paint_sources_f83cb3f6(
            gi,
            occupied,
            candidates,
            color_value,
            _desired_sources_f83cb3f6(len(candidates)),
        )
        go = fill(go, color_value, frozenset({(axis_row + ONE, j)}))
    inactive_cols = tuple(j for j in range(w) if j not in active_col_set)
    inactive_noise = tuple(j for j in inactive_cols if choice((T, F, F)))
    if len(inactive_noise) == ZERO and len(inactive_cols) > ZERO and choice((T, T, F)):
        inactive_noise = (choice(inactive_cols),)
    for j in inactive_noise:
        use_above = choice((T, F))
        use_below = choice((T, F))
        if not use_above and not use_below:
            use_above = T
        if use_above:
            candidates = tuple((i, j) for i in range(axis_row))
            gi, occupied = _paint_sources_f83cb3f6(
                gi,
                occupied,
                candidates,
                color_value,
                min(TWO, _desired_sources_f83cb3f6(len(candidates))),
            )
        if use_below:
            candidates = tuple((i, j) for i in range(axis_row + ONE, h))
            gi, occupied = _paint_sources_f83cb3f6(
                gi,
                occupied,
                candidates,
                color_value,
                min(TWO, _desired_sources_f83cb3f6(len(candidates))),
            )
    return {"input": gi, "output": go}


def _generate_vertical_f83cb3f6(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    h = unifint(diff_lb, diff_ub, (TEN, 18))
    w = unifint(diff_lb, diff_ub, (TEN, 18))
    axis_col = randint(ONE, w - TWO)
    active_rows = _sample_frontier_positions_f83cb3f6(diff_lb, diff_ub, h)
    active_row_set = set(active_rows)
    color_value = choice(FG_COLORS_F83CB3F6)
    axis = frozenset((i, axis_col) for i in active_rows)
    gi = fill(canvas(ZERO, (h, w)), EIGHT, axis)
    go = fill(canvas(ZERO, (h, w)), EIGHT, axis)
    left_targets = tuple(i for i in active_rows if choice((T, T, F)))
    right_targets = tuple(i for i in active_rows if choice((T, T, F)))
    if len(left_targets) == ZERO and len(right_targets) == ZERO:
        forced = choice(active_rows)
        if choice((T, F)):
            left_targets = (forced,)
        else:
            right_targets = (forced,)
    occupied = set()
    for i in left_targets:
        candidates = tuple((i, j) for j in range(axis_col))
        gi, occupied = _paint_sources_f83cb3f6(
            gi,
            occupied,
            candidates,
            color_value,
            _desired_sources_f83cb3f6(len(candidates)),
        )
        go = fill(go, color_value, frozenset({(i, axis_col - ONE)}))
    for i in right_targets:
        candidates = tuple((i, j) for j in range(axis_col + ONE, w))
        gi, occupied = _paint_sources_f83cb3f6(
            gi,
            occupied,
            candidates,
            color_value,
            _desired_sources_f83cb3f6(len(candidates)),
        )
        go = fill(go, color_value, frozenset({(i, axis_col + ONE)}))
    inactive_rows = tuple(i for i in range(h) if i not in active_row_set)
    inactive_noise = tuple(i for i in inactive_rows if choice((T, F, F)))
    if len(inactive_noise) == ZERO and len(inactive_rows) > ZERO and choice((T, T, F)):
        inactive_noise = (choice(inactive_rows),)
    for i in inactive_noise:
        use_left = choice((T, F))
        use_right = choice((T, F))
        if not use_left and not use_right:
            use_left = T
        if use_left:
            candidates = tuple((i, j) for j in range(axis_col))
            gi, occupied = _paint_sources_f83cb3f6(
                gi,
                occupied,
                candidates,
                color_value,
                min(TWO, _desired_sources_f83cb3f6(len(candidates))),
            )
        if use_right:
            candidates = tuple((i, j) for j in range(axis_col + ONE, w))
            gi, occupied = _paint_sources_f83cb3f6(
                gi,
                occupied,
                candidates,
                color_value,
                min(TWO, _desired_sources_f83cb3f6(len(candidates))),
            )
    return {"input": gi, "output": go}


def generate_f83cb3f6(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    families = (_generate_horizontal_f83cb3f6, _generate_vertical_f83cb3f6)
    while True:
        example = choice(families)(diff_lb, diff_ub)
        if example["input"] == example["output"]:
            continue
        if verify_f83cb3f6(example["input"]) != example["output"]:
            continue
        return example
