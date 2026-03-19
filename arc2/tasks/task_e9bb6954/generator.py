from arc2.core import *


def _square_halo_e9bb6954(
    top: Integer,
    left: Integer,
    h: Integer,
    w: Integer,
) -> Indices:
    return frozenset(
        (i, j)
        for i in range(max(ZERO, top - ONE), min(h, top + FOUR))
        for j in range(max(ZERO, left - ONE), min(w, left + FOUR))
    )


def _touches_same_color_e9bb6954(
    grid: Grid,
    loc: IntegerTuple,
    value: Integer,
) -> Boolean:
    return any(index(grid, ij) == value for ij in dneighbors(loc))


def _render_output_e9bb6954(
    gi: Grid,
    seeds: tuple[tuple[Integer, IntegerTuple], ...],
) -> Grid:
    go = gi
    lines = []
    for value, center_loc in seeds:
        line = combine(hfrontier(center_loc), vfrontier(center_loc))
        go = fill(go, value, line)
        lines.append((value, line))
    overlaps = frozenset()
    for k, (value, line) in enumerate(lines):
        for other_value, other_line in lines[k + ONE:]:
            if value != other_value:
                overlaps = combine(overlaps, intersection(line, other_line))
    return fill(go, ZERO, overlaps)


def generate_e9bb6954(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    cols = remove(ZERO, interval(ZERO, TEN, ONE))
    while True:
        h = unifint(diff_lb, diff_ub, (13, 20))
        w = unifint(diff_lb, diff_ub, (13, 20))
        nseeds = unifint(diff_lb, diff_ub, (ONE, THREE))
        seed_cols = sample(cols, nseeds)
        gi = canvas(ZERO, (h, w))
        seeds = []
        reserved = frozenset()
        occupied = frozenset()
        row_centers = set()
        col_centers = set()
        placed_all = T
        for value in seed_cols:
            placed = F
            for _ in range(200):
                top = randint(ZERO, h - THREE)
                left = randint(ZERO, w - THREE)
                center_loc = (top + ONE, left + ONE)
                if center_loc[ZERO] in row_centers or center_loc[ONE] in col_centers:
                    continue
                square_obj = backdrop(frozenset({(top, left), (top + TWO, left + TWO)}))
                halo = _square_halo_e9bb6954(top, left, h, w)
                if size(intersection(halo, reserved)) != ZERO:
                    continue
                gi = fill(gi, value, square_obj)
                seeds.append((value, center_loc))
                reserved = combine(reserved, halo)
                occupied = combine(occupied, square_obj)
                row_centers.add(center_loc[ZERO])
                col_centers.add(center_loc[ONE])
                placed = T
                break
            if not placed:
                placed_all = F
                break
        if not placed_all:
            continue
        area = h * w
        lo = max(8, area // 24)
        hi = min(36, max(lo, area // 7))
        nnoise = unifint(diff_lb, diff_ub, (lo, hi))
        empties = difference(asindices(gi), occupied)
        placed_noise = ZERO
        attempts = ZERO
        max_attempts = max(100, nnoise * 25)
        while placed_noise < nnoise and attempts < max_attempts:
            attempts += ONE
            loc = choice(totuple(empties))
            value = choice(cols)
            if _touches_same_color_e9bb6954(gi, loc, value):
                continue
            gi = fill(gi, value, initset(loc))
            empties = remove(loc, empties)
            placed_noise += ONE
        if placed_noise != nnoise:
            continue
        x0 = objects(gi, T, F, T)
        x1 = sizefilter(x0, NINE)
        x2 = sfilter(x1, square)
        x3 = difference(x0, x2)
        if size(x2) != nseeds:
            continue
        if any(size(x4) != ONE for x4 in x3):
            continue
        x4 = remove(ZERO, palette(gi))
        if size(x4) < FIVE:
            continue
        if mostcolor(gi) != ZERO:
            continue
        seeds = tuple(seeds)
        go = _render_output_e9bb6954(gi, seeds)
        return {"input": gi, "output": go}
