from arc2.core import *

from .verifier import verify_8886d717


TRANSFORMS_8886d717 = (identity, rot90, rot180, rot270)


def _grow_two_region_8886d717(
    n: Integer,
    diff_lb: float,
    diff_ub: float,
) -> Indices:
    width = n - TWO
    target_lb = max(SIX, n * width // 5)
    target_ub = min(n * width // 2, n * width - max(n, SIX))
    target = unifint(diff_lb, diff_ub, (target_lb, target_ub))
    seed_h = randint(TWO, max(TWO, n // 2 + ONE))
    seed_w = randint(TWO, max(TWO, width // 2 + ONE))
    top = randint(ZERO, n - seed_h)
    left = randint(ZERO, width - seed_w)
    cells = {
        (i, j)
        for i in range(top, top + seed_h)
        for j in range(left, left + seed_w)
    }
    target = max(target, len(cells))
    while len(cells) < target:
        patch = frozenset(cells)
        frontier = {
            loc
            for cell in patch
            for loc in dneighbors(cell)
            if 0 <= loc[0] < n and 0 <= loc[1] < width and loc not in cells
        }
        if len(frontier) == ZERO:
            break
        dense = tuple(
            loc for loc in frontier
            if len(intersection(dneighbors(loc), patch)) >= TWO
        )
        cands = dense if len(dense) > ZERO and choice((T, T, F)) else tuple(frontier)
        loc = choice(cands)
        cells.add(loc)
        if len(cells) >= target or choice((T, F, F, F)) == F:
            continue
        patch = frozenset(cells)
        extras = tuple(
            nbr for nbr in dneighbors(loc)
            if 0 <= nbr[0] < n
            and 0 <= nbr[1] < width
            and nbr not in cells
            and len(intersection(dneighbors(nbr), patch)) >= TWO
        )
        if len(extras) > ZERO:
            cells.add(choice(extras))
    return frozenset(cells)


def _active_candidates_8886d717(
    n: Integer,
    two: Indices,
) -> tuple[IntegerTuple, ...]:
    cands = []
    for i in range(n):
        for j in range(n - TWO):
            loc = (i, j)
            nxt = (i, j + ONE)
            if loc in two or nxt in two:
                continue
            if len(intersection(dneighbors(loc), two)) > ZERO:
                continue
            if len(intersection(dneighbors(nxt), two)) > ZERO:
                continue
            cands.append(loc)
    return tuple(cands)


def _sample_inactive_8886d717(
    two: Indices,
    target: Integer,
) -> Indices:
    remaining = set(two)
    selected = []
    while len(selected) < target:
        options = []
        for loc in tuple(remaining):
            new_remaining = remaining - {loc}
            if len(set(dneighbors(loc)) & new_remaining) == ZERO:
                continue
            ok = True
            for prev in selected:
                if len(set(dneighbors(prev)) & new_remaining) == ZERO:
                    ok = False
                    break
            if ok:
                options.append(loc)
        if len(options) == ZERO:
            break
        loc = choice(tuple(options))
        selected.append(loc)
        remaining.remove(loc)
    return frozenset(selected)


def generate_8886d717(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        n = unifint(diff_lb, diff_ub, (EIGHT, 14))
        two = _grow_two_region_8886d717(n, diff_lb, diff_ub)
        if len(two) < SIX:
            continue
        active_cands = _active_candidates_8886d717(n, two)
        if len(active_cands) < TWO:
            continue
        active_ub = min(len(active_cands), n + n // THREE)
        active_lb = min(active_ub, max(TWO, n // THREE))
        inactive_ub = min(max(ONE, n), max(ONE, len(two) // TWO))
        if active_lb > active_ub or inactive_ub < ONE:
            continue
        n_active = unifint(diff_lb, diff_ub, (active_lb, active_ub))
        n_inactive = unifint(diff_lb, diff_ub, (ONE, inactive_ub))
        active = frozenset(sample(active_cands, n_active))
        inactive = _sample_inactive_8886d717(two, n_inactive)
        if len(inactive) != n_inactive:
            continue
        x0 = canvas(SEVEN, (n, n))
        x1 = frozenset((i, n - ONE) for i in range(n))
        x2 = fill(x0, NINE, x1)
        x3 = fill(x2, TWO, two)
        x4 = fill(x3, EIGHT, combine(active, inactive))
        x5 = fill(x3, EIGHT, active)
        x6 = fill(x5, EIGHT, shift(active, RIGHT))
        x7 = choice(TRANSFORMS_8886d717)
        gi = x7(x4)
        go = x7(x6)
        if gi == go:
            continue
        if verify_8886d717(gi) != go:
            continue
        return {"input": gi, "output": go}
