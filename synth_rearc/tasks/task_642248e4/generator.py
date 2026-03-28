from synth_rearc.core import *


COLOR_OPTIONS_642248E4 = remove(ONE, remove(ZERO, interval(ZERO, TEN, ONE)))


def _reserve_642248e4(loc: tuple[int, int], tgt: tuple[int, int]) -> frozenset[tuple[int, int]]:
    x0 = initset(loc)
    x1 = initset(tgt)
    x2 = combine(x0, x1)
    x3 = combine(neighbors(loc), neighbors(tgt))
    x4 = combine(x2, x3)
    return x4


def _place_642248e4(
    candidates: list[tuple[int, int]],
    delta: tuple[int, int],
    count: int,
    reserved: frozenset[tuple[int, int]],
) -> tuple[tuple[tuple[int, int], ...], tuple[tuple[int, int], ...], frozenset[tuple[int, int]]] | None:
    pool = candidates[:]
    shuffle(pool)
    picks = []
    targets = []
    used = reserved
    for loc in pool:
        tgt = (loc[ZERO] + delta[ZERO], loc[ONE] + delta[ONE])
        if loc in used or tgt in used:
            continue
        picks.append(loc)
        targets.append(tgt)
        used = combine(used, _reserve_642248e4(loc, tgt))
        if len(picks) == count:
            return tuple(picks), tuple(targets), used
    return None


def generate_642248e4(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        horizontal = choice((T, F))
        h = unifint(diff_lb, diff_ub, (10, 18))
        w = unifint(diff_lb, diff_ub, (10, 18))
        if horizontal:
            split = (h - ONE) // TWO
            near_rows = range(TWO, split + ONE)
            far_rows = range(split + ONE, h - TWO)
            near_candidates = [(i, j) for i in near_rows for j in range(w)]
            far_candidates = [(i, j) for i in far_rows for j in range(w)]
            near_delta = UP
            far_delta = DOWN
        else:
            split = (w - ONE) // TWO
            near_cols = range(TWO, split + ONE)
            far_cols = range(split + ONE, w - TWO)
            near_candidates = [(i, j) for i in range(h) for j in near_cols]
            far_candidates = [(i, j) for i in range(h) for j in far_cols]
            near_delta = LEFT
            far_delta = RIGHT
        if len(near_candidates) == ZERO or len(far_candidates) == ZERO:
            continue
        side_ub = min(FIVE, max(TWO, (h * w) // 35))
        near_count = unifint(diff_lb, diff_ub, (TWO, side_ub))
        far_count = unifint(diff_lb, diff_ub, (TWO, side_ub))
        placed_near = _place_642248e4(near_candidates, near_delta, near_count, frozenset())
        if placed_near is None:
            continue
        near_marks, near_targets, reserved = placed_near
        placed_far = _place_642248e4(far_candidates, far_delta, far_count, reserved)
        if placed_far is None:
            continue
        far_marks, far_targets, _ = placed_far
        near_color, far_color = sample(COLOR_OPTIONS_642248E4, TWO)
        gi = canvas(ZERO, (h, w))
        if horizontal:
            gi = fill(gi, near_color, hfrontier(ORIGIN))
            gi = fill(gi, far_color, hfrontier(toivec(h - ONE)))
        else:
            gi = fill(gi, near_color, vfrontier(ORIGIN))
            gi = fill(gi, far_color, vfrontier(tojvec(w - ONE)))
        marks = combine(near_marks, far_marks)
        gi = fill(gi, ONE, marks)
        go = fill(gi, near_color, near_targets)
        go = fill(go, far_color, far_targets)
        if mostcolor(gi) != ZERO:
            continue
        return {"input": gi, "output": go}
