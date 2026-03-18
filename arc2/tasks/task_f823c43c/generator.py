from arc2.core import *


MASKS_BY_PERIOD_F823C43C = {
    TWO: (
        (ZERO, ONE),
    ),
    THREE: (
        (ZERO, ONE, ZERO),
        (ZERO, ONE, ONE),
    ),
}


def _tile_from_mask_f823c43c(
    bg: Integer,
    fg: Integer,
    mask: Tuple,
) -> Grid:
    period = len(mask)
    return tuple(
        tuple(
            fg if mask[i] == ONE and mask[j] == ONE else bg
            for j in range(period)
        )
        for i in range(period)
    )


def _repeat_tile_f823c43c(
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


def generate_f823c43c(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    colors = remove(SIX, interval(ZERO, TEN, ONE))
    while True:
        period = choice((TWO, THREE))
        mask = choice(MASKS_BY_PERIOD_F823C43C[period])
        bg, fg = sample(colors, TWO)
        reps_h = unifint(diff_lb, diff_ub, (FOUR, SEVEN))
        reps_w = unifint(diff_lb, diff_ub, (FOUR, SEVEN))
        h = period * reps_h + randint(ZERO, period - ONE)
        w = period * reps_w + randint(ZERO, period - ONE)
        clean_tile = _tile_from_mask_f823c43c(bg, fg, mask)
        go = _repeat_tile_f823c43c(clean_tile, h, w)
        top = period * randint(ZERO, (h - period) // period)
        left = period * randint(ZERO, (w - period) // period)
        protected = {
            (i, j)
            for i in range(top, top + period)
            for j in range(left, left + period)
        }
        candidates = tuple(
            (i, j)
            for i in range(h)
            for j in range(w)
            if (i, j) not in protected
        )
        area = h * w
        noise_lb = max(period + ONE, area // 14)
        noise_ub = min(len(candidates), max(noise_lb, area // 8))
        if noise_ub == ZERO:
            continue
        noise_count = unifint(diff_lb, diff_ub, (noise_lb, noise_ub))
        noise = sample(candidates, noise_count)
        gi = fill(go, SIX, frozenset(noise))
        if gi == go:
            continue
        return {"input": gi, "output": go}
