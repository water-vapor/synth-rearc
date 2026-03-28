from synth_rearc.core import *


GRID_SIZE_1D0A4B61 = 25
PERIODS_1D0A4B61 = (
    (FOUR, TWO),
    (SIX, SIX),
    (SEVEN, SEVEN),
    (NINE, NINE),
)
PALETTE_1D0A4B61 = remove(ONE, remove(ZERO, interval(ZERO, TEN, ONE)))


def _exact_vertical_period_1d0a4b61(
    grid: Grid,
) -> Integer:
    h = height(grid)
    w = width(grid)
    for period in range(ONE, h + ONE):
        if all(grid[i][j] == grid[i + period][j] for i in range(h - period) for j in range(w)):
            return period
    return h


def _exact_horizontal_period_1d0a4b61(
    grid: Grid,
) -> Integer:
    h = height(grid)
    w = width(grid)
    for period in range(ONE, w + ONE):
        if all(grid[i][j] == grid[i][j + period] for i in range(h) for j in range(w - period)):
            return period
    return w


def _repeat_tile_1d0a4b61(
    tile: Grid,
    h: Integer,
    w: Integer,
) -> Grid:
    th = height(tile)
    tw = width(tile)
    return tuple(
        tuple(tile[i % th][j % tw] for j in range(w))
        for i in range(h)
    )


def _frontier_positions_1d0a4b61(
    period: Integer,
) -> tuple[tuple[int, ...], ...]:
    if period == NINE:
        return ((ZERO,), (ZERO, THREE, SIX))
    return ((ZERO,),)


def _choose_frontiers_1d0a4b61(
    period: Integer,
) -> tuple[int, ...]:
    x0 = _frontier_positions_1d0a4b61(period)
    if len(x0) == ONE or choice((T, T, F)):
        return x0[ZERO]
    return choice(x0[ONE:])


def _state_sequence_1d0a4b61(
    length: Integer,
    nstates: Integer,
) -> tuple[int, ...]:
    if length == ZERO:
        return ()
    mode = choice(("pal", "pal", "repeat", "cycle"))
    if mode == "pal":
        half = tuple(randint(ZERO, nstates - ONE) for _ in range((length + ONE) // TWO))
        if length % TWO == ONE:
            return half + half[:-ONE][::-ONE]
        return half + half[::-ONE]
    if mode == "repeat":
        base_len = min(length, choice((ONE, TWO, THREE)))
        base = tuple(randint(ZERO, nstates - ONE) for _ in range(base_len))
        return tuple(base[i % base_len] for i in range(length))
    if nstates == ONE:
        return tuple(ZERO for _ in range(length))
    start = randint(ZERO, nstates - ONE)
    step = randint(ONE, nstates - ONE)
    return tuple((start + step * i) % nstates for i in range(length))


def _paired_state_sequences_1d0a4b61(
    nr: Integer,
    nc: Integer,
    nstates: Integer,
) -> tuple[tuple[int, ...], tuple[int, ...]]:
    x0 = _state_sequence_1d0a4b61(nr, nstates)
    if nr == nc and choice((T, F)):
        return x0, choice((x0, x0[::-ONE]))
    x1 = _state_sequence_1d0a4b61(nc, nstates)
    return x0, x1


def _build_tile_1d0a4b61(
    row_period: Integer,
    col_period: Integer,
) -> Grid:
    row_frontiers = _choose_frontiers_1d0a4b61(row_period)
    col_frontiers = _choose_frontiers_1d0a4b61(col_period)
    nonfrontier_rows = tuple(i for i in range(row_period) if i not in row_frontiers)
    nonfrontier_cols = tuple(j for j in range(col_period) if j not in col_frontiers)
    nstates = choice((TWO, THREE))
    colors = sample(PALETTE_1D0A4B61, nstates)
    row_states, col_states = _paired_state_sequences_1d0a4b61(
        len(nonfrontier_rows),
        len(nonfrontier_cols),
        nstates,
    )
    row_lookup = dict(zip(nonfrontier_rows, row_states))
    col_lookup = dict(zip(nonfrontier_cols, col_states))
    mode = choice(("add", "add", "sub"))
    special = ()
    if nstates > TWO and choice((T, F)):
        special = (randint(ZERO, nstates - ONE),)
    rows = []
    for i in range(row_period):
        row = []
        for j in range(col_period):
            if i in row_frontiers or j in col_frontiers:
                value = ONE
            else:
                a = row_lookup[i]
                b = col_lookup[j]
                residue = (a + b) % nstates if mode == "add" else (a - b) % nstates
                value = ONE if residue in special else colors[residue]
            row.append(value)
        rows.append(tuple(row))
    return tuple(rows)


def _protected_patch_1d0a4b61(
    row_period: Integer,
    col_period: Integer,
) -> Indices:
    top = choice(tuple(range(ZERO, GRID_SIZE_1D0A4B61 - row_period + ONE, row_period)))
    left = choice(tuple(range(ZERO, GRID_SIZE_1D0A4B61 - col_period + ONE, col_period)))
    return frozenset(
        (i, j)
        for i in range(top, top + row_period)
        for j in range(left, left + col_period)
    )


def _rectangle_patch_1d0a4b61(
    top: Integer,
    left: Integer,
    h: Integer,
    w: Integer,
) -> Indices:
    return frozenset(
        (i, j)
        for i in range(top, top + h)
        for j in range(left, left + w)
    )


def generate_1d0a4b61(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    h = GRID_SIZE_1D0A4B61
    w = GRID_SIZE_1D0A4B61
    while True:
        row_period, col_period = choice(PERIODS_1D0A4B61)
        x0 = _build_tile_1d0a4b61(row_period, col_period)
        if choice((T, F)):
            x0 = hmirror(x0)
        if choice((T, F)):
            x0 = vmirror(x0)
        go = _repeat_tile_1d0a4b61(x0, h, w)
        if _exact_vertical_period_1d0a4b61(go) != row_period:
            continue
        if _exact_horizontal_period_1d0a4b61(go) != col_period:
            continue
        if len(palette(go)) < THREE:
            continue
        protected = _protected_patch_1d0a4b61(row_period, col_period)
        gi = go
        nrects = unifint(diff_lb, diff_ub, (TWO, FOUR))
        rh_lb = max(TWO, row_period // TWO)
        rw_lb = max(TWO, col_period // TWO)
        rh_ub = min(EIGHT, max(rh_lb, row_period + TWO))
        rw_ub = min(TEN, max(rw_lb, col_period + THREE))
        for _ in range(nrects):
            rect_h = unifint(diff_lb, diff_ub, (rh_lb, rh_ub))
            rect_w = unifint(diff_lb, diff_ub, (rw_lb, rw_ub))
            top = randint(ZERO, h - rect_h)
            left = randint(ZERO, w - rect_w)
            patch = difference(_rectangle_patch_1d0a4b61(top, left, rect_h, rect_w), protected)
            if len(patch) == ZERO:
                continue
            gi = fill(gi, ZERO, patch)
        zeros = colorcount(gi, ZERO)
        if zeros < max(20, add(row_period, col_period)):
            continue
        if zeros > 100:
            continue
        if gi == go:
            continue
        return {"input": gi, "output": go}
