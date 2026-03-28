from synth_rearc.core import *


def generate_73c3b0d8(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    h = unifint(diff_lb, diff_ub, (SIX, 12))
    w = unifint(diff_lb, diff_ub, (THREE, EIGHT))
    bar = unifint(diff_lb, diff_ub, (TWO, h - ONE))
    row = hfrontier(toivec(bar))
    gi = fill(canvas(ZERO, (h, w)), TWO, row)

    rows_above = interval(ZERO, bar - TWO, ONE)
    rows_below = interval(bar + ONE, h - ONE, ONE)
    cols = interval(ZERO, w, ONE)
    above_cands = totuple(product(rows_above, cols))
    below_cands = totuple(product(rows_below, cols))

    has_tip = choice((T, T, T, F))
    tip = frozenset()
    if has_tip:
        tip = frozenset({(bar - TWO, choice(cols))})

    max_above = min(THREE, len(above_cands))
    max_below = min(TWO, len(below_cands))
    num_above = unifint(diff_lb, diff_ub, (ZERO, max_above))
    num_below = unifint(diff_lb, diff_ub, (ZERO, max_below))
    if not has_tip and num_above + num_below == ZERO:
        if max_above > ZERO:
            num_above = ONE
        else:
            num_below = ONE

    blocked = set(tip)
    for loc in tip:
        blocked.update(neighbors(loc))

    above = []
    for loc in sample(above_cands, len(above_cands)):
        if loc in blocked:
            continue
        above.append(loc)
        blocked.add(loc)
        blocked.update(neighbors(loc))
        if len(above) == num_above:
            break

    below = []
    for loc in sample(below_cands, len(below_cands)):
        if loc in blocked:
            continue
        below.append(loc)
        blocked.add(loc)
        blocked.update(neighbors(loc))
        if len(below) == num_below:
            break

    above = frozenset(above)
    below = frozenset(below)
    dots = combine(tip, combine(above, below))
    gi = fill(gi, FOUR, dots)

    fallen = shift(dots, DOWN)
    tips = shift(tip, DOWN)
    left = mapply(rbind(shoot, NEG_UNITY), tips)
    right = mapply(rbind(shoot, UP_RIGHT), tips)
    rays = combine(left, right)

    go = fill(canvas(ZERO, (h, w)), TWO, row)
    go = fill(go, FOUR, fallen)
    go = fill(go, FOUR, rays)
    return {"input": gi, "output": go}
