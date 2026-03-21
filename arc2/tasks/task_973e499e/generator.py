from arc2.core import *


def _neighbors_973e499e(loc: IntegerTuple, n: Integer) -> tuple[IntegerTuple, ...]:
    i, j = loc
    out = []
    for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        a, b = i + di, j + dj
        if 0 <= a < n and 0 <= b < n:
            out.append((a, b))
    return tuple(out)


def _grow_regions_973e499e(n: Integer, nregions: Integer) -> tuple[frozenset[IntegerTuple], ...]:
    cells = tuple((i, j) for i in range(n) for j in range(n))
    seeds = sample(cells, nregions)
    regions = [set((seed,)) for seed in seeds]
    frontiers = [set(_neighbors_973e499e(seed, n)) - set(seeds) for seed in seeds]
    assigned = set(seeds)
    while len(assigned) < n * n:
        active = [k for k, frontier in enumerate(frontiers) if frontier]
        if not active:
            break
        k = choice(active)
        loc = choice(tuple(frontiers[k]))
        regions[k].add(loc)
        assigned.add(loc)
        for frontier in frontiers:
            frontier.discard(loc)
        for nbr in _neighbors_973e499e(loc, n):
            if nbr not in assigned:
                frontiers[k].add(nbr)
    return tuple(frozenset(region) for region in regions)


def _paint_regions_973e499e(
    n: Integer,
    regions: tuple[frozenset[IntegerTuple], ...],
    colors: tuple[Integer, ...],
) -> Grid:
    gi = canvas(ZERO, (n, n))
    ordered = tuple(sorted(regions, key=len, reverse=True))
    color_usage = {color: 0 for color in colors}
    for color, region in zip(colors, ordered[: len(colors)]):
        gi = fill(gi, color, region)
        color_usage[color] += len(region)
    for region in ordered[len(colors) :]:
        color_order = tuple(sorted(colors, key=lambda color: (color_usage[color], randint(0, 99))))
        color = choice(color_order[: max(1, min(2, len(color_order)))])
        gi = fill(gi, color, region)
        color_usage[color] += len(region)
    return gi


def _valid_input_973e499e(gi: Grid) -> bool:
    if colorcount(gi, ZERO) != ZERO:
        return False
    cols = tuple(remove(ZERO, palette(gi)))
    if len(cols) < 2:
        return False
    counts = tuple(len(ofcolor(gi, color)) for color in cols)
    if min(counts) < 3:
        return False
    if max(counts) == len(gi) * len(gi[0]):
        return False
    if not any(len(objects(fill(canvas(ZERO, shape(gi)), color, ofcolor(gi, color)), T, F, T)) > 1 for color in cols):
        return False
    return True


def _render_973e499e(gi: Grid) -> Grid:
    shp = shape(gi)
    go = canvas(ZERO, multiply(shp, shp))
    for color in remove(ZERO, palette(gi)):
        cells = ofcolor(gi, color)
        mover = lbind(shift, cells)
        offsets = apply(rbind(multiply, shp), cells)
        go = fill(go, color, mapply(mover, offsets))
    return go


def _transform_973e499e(gi: Grid) -> Grid:
    rotf = choice((identity, rot90, rot180, rot270))
    gi = rotf(gi)
    if choice((True, False)):
        gi = hmirror(gi)
    if choice((True, False)):
        gi = vmirror(gi)
    return gi


def generate_973e499e(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    cols = remove(ZERO, interval(ZERO, TEN, ONE))
    while True:
        n = unifint(diff_lb, diff_ub, (3, 5))
        max_colors = 3 if n <= 4 else 4
        ncolors = unifint(diff_lb, diff_ub, (2, max_colors))
        nregions = unifint(diff_lb, diff_ub, (ncolors + 1, min(ncolors + 2, n + 1)))
        colors = tuple(sample(cols, ncolors))
        regions = _grow_regions_973e499e(n, nregions)
        gi = _paint_regions_973e499e(n, regions, colors)
        gi = _transform_973e499e(gi)
        if not _valid_input_973e499e(gi):
            continue
        go = _render_973e499e(gi)
        return {"input": gi, "output": go}
