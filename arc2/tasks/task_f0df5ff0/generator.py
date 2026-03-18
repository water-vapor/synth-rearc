from arc2.core import *


def _sample_seeds(nseeds: int) -> frozenset[tuple[int, int]]:
    candidates = [(i, j) for i in range(1, 14) for j in range(1, 14)]
    shuffle(candidates)
    seeds = []
    for loc in candidates:
        if all(max(abs(loc[0] - i), abs(loc[1] - j)) > 2 for i, j in seeds):
            seeds.append(loc)
            if len(seeds) == nseeds:
                break
    return frozenset(seeds)


def generate_f0df5ff0(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    cols = remove(ONE, remove(ZERO, interval(ZERO, TEN, ONE)))
    while True:
        ncols = unifint(diff_lb, diff_ub, (4, 7))
        nseeds = unifint(diff_lb, diff_ub, (4, 8))
        palette0 = sample(cols, ncols)
        seeds = _sample_seeds(nseeds)
        if len(seeds) != nseeds:
            continue
        halo = mapply(neighbors, seeds)
        near_space = halo - seeds
        far_space = totuple(asindices(canvas(ZERO, (15, 15))) - halo - seeds)
        if len(far_space) < ncols:
            continue
        gi = canvas(ZERO, (15, 15))
        forced = sample(far_space, ncols)
        for color_value, loc in zip(palette0, forced):
            gi = fill(gi, color_value, {loc})
        near_density = uniform(0.12, 0.28)
        far_density = uniform(0.34, 0.5)
        for loc in near_space:
            if uniform(0.0, 1.0) < near_density:
                gi = fill(gi, choice(palette0), {loc})
        for loc in far_space:
            if loc in forced:
                continue
            if uniform(0.0, 1.0) < far_density:
                gi = fill(gi, choice(palette0), {loc})
        gi = fill(gi, ONE, seeds)
        if mostcolor(gi) != ZERO:
            continue
        fgc = sum(value != ZERO for row in gi for value in row)
        if not (72 <= fgc <= 110):
            continue
        go = underfill(gi, ONE, halo)
        added = colorcount(go, ONE) - colorcount(gi, ONE)
        if not (18 <= added <= 42):
            continue
        return {"input": gi, "output": go}
