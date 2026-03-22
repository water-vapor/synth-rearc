from arc2.core import *


def _arm_patch_705a3229(
    loc: tuple[int, int],
    dims: tuple[int, int],
) -> frozenset[tuple[int, int]]:
    h, w = dims
    i = first(loc)
    j = last(loc)
    bottom = subtract(decrement(h), i)
    right = subtract(decrement(w), j)
    vdir = branch(greater(i, bottom), DOWN, UP)
    hdir = branch(greater(j, right), RIGHT, LEFT)
    return combine(shoot(loc, vdir), shoot(loc, hdir))


def _guard_705a3229(cells: frozenset[tuple[int, int]]) -> frozenset[tuple[int, int]]:
    out = set(cells)
    for cell in tuple(cells):
        out.update(neighbors(cell))
    return frozenset(out)


def generate_705a3229(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    colors = remove(ZERO, interval(ZERO, TEN, ONE))
    while True:
        n_seeds = choice((ONE, TWO, TWO, THREE, THREE, FOUR))
        min_side = max(EIGHT, add(SEVEN, n_seeds))
        h = unifint(diff_lb, diff_ub, (min_side, 16))
        w = unifint(diff_lb, diff_ub, (min_side, 16))
        rows = [i for i in range(ONE, h - ONE) if double(i) != decrement(h)]
        cols = [j for j in range(ONE, w - ONE) if double(j) != decrement(w)]
        if len(rows) == ZERO or len(cols) == ZERO:
            continue
        seed_colors = sample(colors, n_seeds)
        gi = canvas(ZERO, (h, w))
        go = gi
        seed_guard = frozenset()
        path_guard = frozenset()
        ok = T
        for color_value in seed_colors:
            candidates = [(i, j) for i in rows for j in cols]
            shuffle(candidates)
            placed = F
            for loc in candidates:
                if loc in seed_guard:
                    continue
                patch = _arm_patch_705a3229(loc, (h, w))
                if len(intersection(patch, path_guard)) != ZERO:
                    continue
                gi = fill(gi, color_value, frozenset({loc}))
                go = fill(go, color_value, patch)
                seed_guard = combine(seed_guard, _guard_705a3229(frozenset({loc})))
                path_guard = combine(path_guard, _guard_705a3229(patch))
                placed = T
                break
            if flip(placed):
                ok = F
                break
        if flip(ok):
            continue
        if gi == go:
            continue
        return {"input": gi, "output": go}
