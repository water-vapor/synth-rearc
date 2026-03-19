from arc2.core import *


PALETTE_17B80AD2 = (ONE, TWO, THREE, FOUR, SIX, SEVEN, EIGHT, NINE)


def _fill_marked_columns_17b80ad2(grid: Grid) -> Grid:
    rows = [list(row) for row in grid]
    height_value = len(rows)
    width_value = len(rows[ZERO])
    for j in range(width_value):
        if rows[-ONE][j] != FIVE:
            continue
        color_value = FIVE
        for i in range(height_value - ONE, -ONE, -ONE):
            if rows[i][j] != ZERO:
                color_value = rows[i][j]
            rows[i][j] = color_value
    return tuple(tuple(row) for row in rows)


def _choose_target_columns_17b80ad2(side: int, count: int) -> tuple[int, ...]:
    pool = list(range(ONE, side - ONE))
    if len(pool) <= count:
        return tuple(pool)
    best = sorted(sample(pool, count))
    best_gap = min((b - a) for a, b in zip(best, best[ONE:])) if count > ONE else side
    for _ in range(24):
        cols = sorted(sample(pool, count))
        gap = min((b - a) for a, b in zip(cols, cols[ONE:])) if count > ONE else side
        if gap > best_gap:
            best = cols
            best_gap = gap
        if gap >= THREE:
            return tuple(cols)
    return tuple(best)


def _anchor_colors_17b80ad2(count: int) -> tuple[int, ...]:
    colors = []
    prev = None
    for _ in range(count):
        if prev is not None and choice((T, F, F)):
            color_value = prev
        else:
            cands = [value for value in PALETTE_17B80AD2 if value != prev]
            color_value = choice(cands)
        colors.append(color_value)
        prev = color_value
    return tuple(colors)


def generate_17b80ad2(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    side = unifint(diff_lb, diff_ub, (SEVEN, 19))
    max_targets = ONE if side <= EIGHT else TWO if side <= 14 else THREE
    ntargets = unifint(diff_lb, diff_ub, (ONE, max_targets))
    target_cols = _choose_target_columns_17b80ad2(side, ntargets)
    gi = canvas(ZERO, (side, side))

    for col in target_cols:
        max_anchors = min(FOUR, side - TWO)
        nanchors = unifint(diff_lb, diff_ub, (ONE, max_anchors))
        rows = sorted(sample(range(ONE, side - ONE), nanchors))
        colors = _anchor_colors_17b80ad2(nanchors)
        for row, color_value in zip(rows, colors):
            gi = fill(gi, color_value, frozenset({(row, col)}))
        gi = fill(gi, FIVE, frozenset({(side - ONE, col)}))

    for col in range(side):
        if col in target_cols:
            continue
        if side <= EIGHT:
            counts = (ZERO, ZERO, ZERO, ZERO, ONE)
        elif side <= 13:
            counts = (ZERO, ZERO, ONE, ONE, TWO)
        else:
            counts = (ZERO, ONE, ONE, TWO, TWO)
        nnoise = choice(counts)
        if nnoise == ZERO:
            continue
        rows = sample(range(side - ONE), min(nnoise, side - ONE))
        for row in rows:
            color_value = choice(PALETTE_17B80AD2)
            gi = fill(gi, color_value, frozenset({(row, col)}))

    go = _fill_marked_columns_17b80ad2(gi)
    if choice((T, F)):
        gi = vmirror(gi)
        go = vmirror(go)
    return {"input": gi, "output": go}
