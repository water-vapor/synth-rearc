from synth_rearc.core import *

from .helpers import seed_patch_0becf7df, swap_key_pairs_0becf7df


def _split_total_0becf7df(
    total: Integer,
    parts: Integer,
    minimum: Integer,
) -> tuple[Integer, ...]:
    slack = total - parts * minimum
    if slack == ZERO:
        return tuple(minimum for _ in range(parts))
    cuts = sorted(sample(range(slack + parts - ONE), parts - ONE))
    values = []
    prev = NEG_ONE
    for cut in cuts + [slack + parts - ONE]:
        values.append(cut - prev - ONE + minimum)
        prev = cut
    return tuple(values)


def _candidate_cells_0becf7df(
    region: set[IntegerTuple],
    area: set[IntegerTuple],
    occupied: set[IntegerTuple],
) -> tuple[IntegerTuple, ...]:
    candidates = set()
    for cell in region:
        for neighbor in dneighbors(cell):
            if neighbor in area and neighbor not in occupied:
                candidates.add(neighbor)
    return tuple(candidates)


def _pick_cell_0becf7df(
    candidates: tuple[IntegerTuple, ...],
    region: set[IntegerTuple],
    occupied: set[IntegerTuple],
    center: tuple[float, float],
) -> IntegerTuple:
    best = []
    best_score = None
    for cell in candidates:
        own = sum(neighbor in region for neighbor in dneighbors(cell))
        touch = sum(neighbor in occupied and neighbor not in region for neighbor in dneighbors(cell))
        dist = abs(cell[ZERO] - center[ZERO]) + abs(cell[ONE] - center[ONE])
        score = (touch > ZERO, own, -dist)
        if best_score is None or score > best_score:
            best = [cell]
            best_score = score
        elif score == best_score:
            best.append(cell)
    return choice(best)


def generate_0becf7df(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    cols = interval(ONE, TEN, ONE)
    while True:
        keycols = sample(cols, FOUR)
        boxh = unifint(diff_lb, diff_ub, (FIVE, SEVEN))
        boxw = unifint(diff_lb, diff_ub, (FOUR, SIX))
        top = randint(ONE, TEN - boxh)
        left = randint(THREE, TEN - boxw)
        seeds0 = seed_patch_0becf7df()
        maxi = max(i for i, _ in seeds0)
        maxj = max(j for _, j in seeds0)
        offi = randint(ZERO, boxh - maxi - ONE)
        offj = randint(ZERO, boxw - maxj - ONE)
        seeds = list(shift(seeds0, (top + offi, left + offj)))
        shuffle(seeds)
        area = {(i, j) for i in range(top, top + boxh) for j in range(left, left + boxw)}
        total = unifint(diff_lb, diff_ub, (12, min(len(area), 20)))
        targets = list(_split_total_0becf7df(total, FOUR, TWO))
        if max(targets) < FOUR:
            targets[ZERO] += TWO
            targets[ONE] -= ONE
            targets[TWO] -= ONE
        regions = {idx: {seeds[idx]} for idx in range(FOUR)}
        occupied = set(seeds)
        center = (top + boxh / TWO, left + boxw / TWO)
        failed = F
        while any(len(regions[idx]) < targets[idx] for idx in range(FOUR)):
            choices = []
            for idx in range(FOUR):
                if len(regions[idx]) >= targets[idx]:
                    continue
                candidates = _candidate_cells_0becf7df(regions[idx], area, occupied)
                if len(candidates) != ZERO:
                    choices.append((idx, candidates))
            if len(choices) == ZERO:
                failed = T
                break
            idx, candidates = choice(choices)
            cell = _pick_cell_0becf7df(candidates, regions[idx], occupied, center)
            regions[idx].add(cell)
            occupied.add(cell)
        if failed:
            continue
        rows = {i for i, _ in occupied}
        cols0 = {j for _, j in occupied}
        if len(rows) < THREE or len(cols0) < THREE:
            continue
        gi = canvas(ZERO, (TEN, TEN))
        keyobj = frozenset({
            (keycols[ZERO], ORIGIN),
            (keycols[ONE], RIGHT),
            (keycols[TWO], DOWN),
            (keycols[THREE], UNITY),
        })
        gi = paint(gi, keyobj)
        obj = frozenset(
            (keycols[idx], cell)
            for idx in range(FOUR)
            for cell in regions[idx]
        )
        gi = paint(gi, obj)
        go = swap_key_pairs_0becf7df(gi)
        return {"input": gi, "output": go}
