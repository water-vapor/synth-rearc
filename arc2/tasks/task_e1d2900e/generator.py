from arc2.core import *


def _block_cells_e1d2900e(
    loc: IntegerTuple,
) -> Indices:
    i, j = loc
    return frozenset({(i, j), (i, j + ONE), (i + ONE, j), (i + ONE, j + ONE)})


def _reserve_block_e1d2900e(
    loc: IntegerTuple,
) -> Indices:
    i, j = loc
    cells = set()
    for ii in range(i - ONE, i + THREE):
        for jj in range(j - ONE, j + THREE):
            cells.add((ii, jj))
    return frozenset(cells)


def _slots_e1d2900e(
    loc: IntegerTuple,
) -> tuple[tuple[IntegerTuple, IntegerTuple], ...]:
    i, j = loc
    return (
        ((i - ONE, j), UP),
        ((i - ONE, j + ONE), UP),
        ((i, j - ONE), LEFT),
        ((i + ONE, j - ONE), LEFT),
        ((i, j + TWO), RIGHT),
        ((i + ONE, j + TWO), RIGHT),
        ((i + TWO, j), DOWN),
        ((i + TWO, j + ONE), DOWN),
    )


def _candidate_target_e1d2900e(
    loc: IntegerTuple,
    block: IntegerTuple,
) -> IntegerTuple | None:
    i, j = loc
    bi, bj = block
    if i in (bi, bi + ONE):
        if j < bj:
            return (i, bj - ONE)
        if j > bj + ONE:
            return (i, bj + TWO)
        return None
    if j in (bj, bj + ONE):
        if i < bi:
            return (bi - ONE, j)
        if i > bi + ONE:
            return (bi + TWO, j)
    return None


def _landing_e1d2900e(
    loc: IntegerTuple,
    blocks: tuple[IntegerTuple, ...],
) -> IntegerTuple:
    candidates = []
    for block in blocks:
        target = _candidate_target_e1d2900e(loc, block)
        if target is None:
            continue
        bi, bj = block
        di = ZERO if bi <= loc[0] <= bi + ONE else min(abs(loc[0] - bi), abs(loc[0] - (bi + ONE)))
        dj = ZERO if bj <= loc[1] <= bj + ONE else min(abs(loc[1] - bj), abs(loc[1] - (bj + ONE)))
        candidates.append((di + dj, target))
    if len(candidates) == ZERO:
        return loc
    best_dist = min(dist for dist, _ in candidates)
    best_targets = [target for dist, target in candidates if dist == best_dist]
    if len(best_targets) != ONE:
        return loc
    return best_targets[ZERO]


def _place_blocks_e1d2900e(
    h: Integer,
    w: Integer,
    nblocks: Integer,
) -> tuple[IntegerTuple, ...] | None:
    candidates = [(i, j) for i in range(ONE, h - TWO) for j in range(ONE, w - TWO)]
    shuffle(candidates)
    blocks = []
    reserved = set()
    for loc in candidates:
        reserve = _reserve_block_e1d2900e(loc)
        if any(i < ZERO or i >= h or j < ZERO or j >= w for i, j in reserve):
            continue
        if len(intersection(reserve, reserved)) > ZERO:
            continue
        blocks.append(loc)
        reserved |= set(reserve)
        if len(blocks) == nblocks:
            return tuple(blocks)
    return None


def _ray_cells_e1d2900e(
    slot: IntegerTuple,
    direction: IntegerTuple,
    h: Integer,
    w: Integer,
) -> tuple[IntegerTuple, ...]:
    i, j = slot
    if direction == UP:
        return tuple((ii, j) for ii in range(ZERO, i))
    if direction == DOWN:
        return tuple((ii, j) for ii in range(i + ONE, h))
    if direction == LEFT:
        return tuple((i, jj) for jj in range(ZERO, j))
    return tuple((i, jj) for jj in range(j + ONE, w))


def _sample_source_e1d2900e(
    slot: IntegerTuple,
    direction: IntegerTuple,
    blocks: tuple[IntegerTuple, ...],
    occupied: Indices,
    h: Integer,
    w: Integer,
) -> IntegerTuple | None:
    candidates = list(_ray_cells_e1d2900e(slot, direction, h, w))
    shuffle(candidates)
    for loc in candidates:
        if contained(loc, occupied):
            continue
        if _landing_e1d2900e(loc, blocks) != slot:
            continue
        return loc
    return None


def generate_e1d2900e(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        large = choice((T, T, F))
        if large:
            h = 30
            w = 30
            nblocks = unifint(diff_lb, diff_ub, (TWO, FOUR))
        else:
            h = unifint(diff_lb, diff_ub, (10, 18))
            w = unifint(diff_lb, diff_ub, (12, 22))
            nblocks = TWO if h * w < 220 else unifint(diff_lb, diff_ub, (TWO, THREE))
        blocks = _place_blocks_e1d2900e(h, w, nblocks)
        if blocks is None:
            continue
        selected = []
        for block in blocks:
            slots = list(_slots_e1d2900e(block))
            shuffle(slots)
            keep = choice((ONE, TWO, TWO, THREE, THREE, FOUR))
            selected.extend(slots[:keep])
        target_cells = tuple(loc for loc, _ in selected)
        if len(frozenset(target_cells)) != len(target_cells):
            continue
        occupied = set()
        for block in blocks:
            occupied |= set(_block_cells_e1d2900e(block))
        occupied |= set(target_cells)
        sources = []
        ok = True
        for slot, direction in selected:
            source = _sample_source_e1d2900e(slot, direction, blocks, frozenset(occupied), h, w)
            if source is None:
                ok = False
                break
            sources.append(source)
            occupied.add(source)
        if not ok:
            continue
        distractor_candidates = [
            (i, j)
            for i in range(h)
            for j in range(w)
            if (i, j) not in occupied and _landing_e1d2900e((i, j), blocks) == (i, j)
        ]
        ndistractors = unifint(diff_lb, diff_ub, (ONE, nblocks + THREE))
        if len(distractor_candidates) < ndistractors:
            continue
        distractors = sample(distractor_candidates, ndistractors)
        gi = canvas(ZERO, (h, w))
        go = canvas(ZERO, (h, w))
        for block in blocks:
            cells = _block_cells_e1d2900e(block)
            gi = fill(gi, TWO, cells)
            go = fill(go, TWO, cells)
        gi = fill(gi, ONE, frozenset(sources) | frozenset(distractors))
        go = fill(go, ONE, frozenset(target_cells) | frozenset(distractors))
        return {"input": gi, "output": go}
