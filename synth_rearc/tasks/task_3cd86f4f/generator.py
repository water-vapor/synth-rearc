from synth_rearc.core import *


def _positive_partition_3cd86f4f(total: int, parts: int) -> tuple[int, ...]:
    vals = [ONE] * parts
    for _ in range(total - parts):
        idx = randint(ZERO, parts - ONE)
        vals[idx] += ONE
    shuffle(vals)
    return tuple(vals)


def _diagonalize_rows_3cd86f4f(grid: Grid) -> Grid:
    h = height(grid)
    rows = []
    for i, row in enumerate(grid):
        left = tuple(ZERO for _ in range(h - i - ONE))
        right = tuple(ZERO for _ in range(i))
        rows.append(left + row + right)
    return tuple(rows)


def _left_wedge_patch_3cd86f4f(h: int, w: int, top_cut: int, bottom_cut: int) -> Indices:
    if h == ONE:
        cuts = (bottom_cut,)
    else:
        cuts = tuple(round(top_cut + (bottom_cut - top_cut) * i / (h - ONE)) for i in range(h))
    return frozenset((i, j) for i, cut in enumerate(cuts) for j in range(max(ZERO, min(w, cut))))


def _right_wedge_patch_3cd86f4f(h: int, w: int, top_cut: int, bottom_cut: int) -> Indices:
    if h == ONE:
        cuts = (bottom_cut,)
    else:
        cuts = tuple(round(top_cut + (bottom_cut - top_cut) * i / (h - ONE)) for i in range(h))
    return frozenset((i, j) for i, cut in enumerate(cuts) for j in range(max(ZERO, min(w, cut)), w))


def _diag_band_patch_3cd86f4f(h: int, w: int, anti: bool) -> Indices:
    bandw = choice((ONE, ONE, TWO))
    if anti:
        offset = randint(ZERO, h + w - TWO)
        return frozenset((i, j) for i in range(h) for j in range(w) if abs(i + j - offset) < bandw)
    offset = randint(ONE - h, w - ONE)
    return frozenset((i, j) for i in range(h) for j in range(w) if abs(j - i - offset) < bandw)


def _build_band_grid_3cd86f4f(h: int, w: int, palette0: tuple[int, ...]) -> Grid:
    gi = canvas(palette0[ZERO], (h, w))
    start = ZERO
    next_idx = ONE
    if w > ONE and len(palette0) > TWO and choice((T, T, F)):
        stripe_w = randint(ONE, min(TWO, w - ONE))
        stripe = frozenset((i, j) for i in range(h) for j in range(stripe_w))
        gi = fill(gi, palette0[next_idx], stripe)
        start = stripe_w
        next_idx += ONE
    nbands = randint(TWO, min(FOUR, h))
    heights0 = _positive_partition_3cd86f4f(h, nbands)
    avail = (palette0[ZERO],) + palette0[next_idx:]
    row = ZERO
    prev = None
    for bh in heights0:
        opts = tuple(c for c in avail if c != prev) if len(avail) > ONE else avail
        col = choice(opts)
        patch = frozenset((i, j) for i in range(row, row + bh) for j in range(start, w))
        gi = fill(gi, col, patch)
        prev = col
        row += bh
    return gi


def _build_wedge_grid_3cd86f4f(h: int, w: int, palette0: tuple[int, ...]) -> Grid:
    gi = canvas(palette0[ZERO], (h, w))
    top_cut = randint(ZERO, max(ZERO, w // THREE))
    bottom_cut = randint(max(ONE, top_cut), max(ONE, w - ONE))
    gi = fill(gi, palette0[ONE], _left_wedge_patch_3cd86f4f(h, w, top_cut, bottom_cut))
    next_idx = TWO
    if next_idx < len(palette0) and w > TWO:
        min_top = max(ONE, w - max(TWO, w // THREE + ONE))
        top_cut = randint(min_top, w - ONE)
        bottom_cut = randint(top_cut, w)
        gi = fill(gi, palette0[next_idx], _right_wedge_patch_3cd86f4f(h, w, top_cut, bottom_cut))
        next_idx += ONE
    for col in palette0[next_idx:]:
        patch = _diag_band_patch_3cd86f4f(h, w, choice((T, F)))
        if ZERO < len(patch) < h * w:
            gi = fill(gi, col, patch)
    return gi


def generate_3cd86f4f(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    cols = remove(ZERO, interval(ZERO, TEN, ONE))
    while True:
        h = unifint(diff_lb, diff_ub, (TWO, TEN))
        w = unifint(diff_lb, diff_ub, (ONE, TEN))
        if w == ONE:
            ncols = unifint(diff_lb, diff_ub, (TWO, min(FIVE, h)))
            palette0 = tuple(sample(cols, ncols))
            gi = _build_band_grid_3cd86f4f(h, w, palette0)
        else:
            mode = choice(("wedge", "wedge", "band"))
            if mode == "band":
                ncols = unifint(diff_lb, diff_ub, (TWO, FOUR))
                palette0 = tuple(sample(cols, ncols))
                gi = _build_band_grid_3cd86f4f(h, w, palette0)
            else:
                ncols = unifint(diff_lb, diff_ub, (THREE, FIVE))
                palette0 = tuple(sample(cols, ncols))
                gi = _build_wedge_grid_3cd86f4f(h, w, palette0)
        if numcolors(gi) < TWO:
            continue
        if len(set(gi)) == ONE and numcolors(gi) == ONE:
            continue
        go = _diagonalize_rows_3cd86f4f(gi)
        return {"input": gi, "output": go}
