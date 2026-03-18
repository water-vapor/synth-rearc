from arc2.core import *


ALL_COLORS_F9D67F8B = interval(ONE, NINE, ONE)
FULL_SIDE_F9D67F8B = 32
CROP_SIDE_F9D67F8B = 30
SEED_SIDE_F9D67F8B = 16


def _rect_f9d67f8b(
    top: Integer,
    left: Integer,
    height_: Integer,
    width_: Integer,
) -> Indices:
    return frozenset(
        (i, j)
        for i in range(top, top + height_)
        for j in range(left, left + width_)
    )


def _reserve_f9d67f8b(
    patch: Indices,
) -> Indices:
    cells = set()
    for loc in patch:
        cells.add(loc)
        for nei in dneighbors(loc):
            i, j = nei
            if 0 <= i < CROP_SIDE_F9D67F8B and 0 <= j < CROP_SIDE_F9D67F8B:
                cells.add(nei)
    return frozenset(cells)


def _orbit_f9d67f8b(
    loc: IntegerTuple,
) -> Indices:
    i, j = loc
    cells = set()
    for ii in (i, FULL_SIDE_F9D67F8B - ONE - i):
        for jj in (j, FULL_SIDE_F9D67F8B - ONE - j):
            if 0 <= ii < CROP_SIDE_F9D67F8B and 0 <= jj < CROP_SIDE_F9D67F8B:
                cells.add((ii, jj))
    return frozenset(cells)


def _mask_is_valid_f9d67f8b(
    mask: Indices,
) -> Boolean:
    seen = set()
    for i in range(CROP_SIDE_F9D67F8B):
        for j in range(CROP_SIDE_F9D67F8B):
            orbit = _orbit_f9d67f8b((i, j))
            if orbit in seen:
                continue
            seen.add(orbit)
            if len(orbit - mask) == ZERO:
                return False
    return len(mask) > ZERO


def _component_count_f9d67f8b(
    patch: Indices,
) -> Integer:
    remaining = set(patch)
    total = ZERO
    while len(remaining) > ZERO:
        frontier = {remaining.pop()}
        total += ONE
        while len(frontier) > ZERO:
            new_frontier = set()
            for loc in frontier:
                for nei in dneighbors(loc):
                    if nei in remaining:
                        remaining.remove(nei)
                        new_frontier.add(nei)
            frontier = new_frontier
    return total


def _build_component_f9d67f8b(
    forbidden: Indices,
) -> Indices | None:
    for _ in range(200):
        h1 = randint(TWO, EIGHT)
        w1 = randint(TWO, EIGHT)
        top1 = randint(ZERO, CROP_SIDE_F9D67F8B - h1)
        left1 = randint(ZERO, CROP_SIDE_F9D67F8B - w1)
        part1 = _rect_f9d67f8b(top1, left1, h1, w1)
        if len(intersection(part1, forbidden)) > ZERO:
            continue
        component = set(part1)
        if choice((True, False)):
            h2 = randint(TWO, EIGHT)
            w2 = randint(TWO, EIGHT)
            if choice((True, False)):
                top2_lo = max(ZERO, top1 - h2)
                top2_hi = min(CROP_SIDE_F9D67F8B - h2, top1 + h1 - ONE)
                left2_lo = max(ZERO, left1 - w2 + ONE)
                left2_hi = min(CROP_SIDE_F9D67F8B - w2, left1 + w1 - ONE)
            else:
                top2_lo = max(ZERO, top1 - h2 + ONE)
                top2_hi = min(CROP_SIDE_F9D67F8B - h2, top1 + h1 - ONE)
                left2_lo = max(ZERO, left1 - w2)
                left2_hi = min(CROP_SIDE_F9D67F8B - w2, left1 + w1 - ONE)
            if top2_lo <= top2_hi and left2_lo <= left2_hi:
                top2 = randint(top2_lo, top2_hi)
                left2 = randint(left2_lo, left2_hi)
                part2 = _rect_f9d67f8b(top2, left2, h2, w2)
                if len(intersection(part2, forbidden)) == ZERO:
                    component |= part2
        component = frozenset(component)
        if _component_count_f9d67f8b(component) != ONE:
            continue
        return component
    return None


def _sample_mask_f9d67f8b(
    diff_lb: float,
    diff_ub: float,
) -> Indices:
    target = unifint(diff_lb, diff_ub, (28, 72))
    ncomponents = unifint(diff_lb, diff_ub, (TWO, THREE))
    slack = 12
    for _ in range(400):
        mask = set()
        forbidden = frozenset()
        ok = True
        for _ in range(ncomponents):
            component = _build_component_f9d67f8b(forbidden)
            if component is None:
                ok = False
                break
            mask |= component
            forbidden = frozenset(set(forbidden) | set(_reserve_f9d67f8b(component)))
        if not ok:
            continue
        mask = frozenset(mask)
        if abs(len(mask) - target) > slack:
            continue
        if _component_count_f9d67f8b(mask) != ncomponents:
            continue
        if not _mask_is_valid_f9d67f8b(mask):
            continue
        return mask
    raise RuntimeError("failed to sample mask")


def _smooth_coarse_seed_f9d67f8b(
    grid: Grid,
) -> Grid:
    rows = []
    for i in range(len(grid)):
        row = []
        for j in range(len(grid[0])):
            vals = []
            for ii in range(max(ZERO, i - ONE), min(len(grid), i + TWO)):
                for jj in range(max(ZERO, j - ONE), min(len(grid[0]), j + TWO)):
                    vals.append(grid[ii][jj])
            row.append(choice(tuple(vals)) if choice((True, False)) else mostcommon(tuple(vals)))
        rows.append(tuple(row))
    return tuple(rows)


def _build_output_f9d67f8b() -> Grid:
    for _ in range(200):
        coarse = tuple(
            tuple(choice(ALL_COLORS_F9D67F8B) for _ in range(SEED_SIDE_F9D67F8B // TWO))
            for _ in range(SEED_SIDE_F9D67F8B // TWO)
        )
        for _ in range(randint(ONE, THREE)):
            coarse = _smooth_coarse_seed_f9d67f8b(coarse)
        seed = upscale(coarse, TWO)
        for color in ALL_COLORS_F9D67F8B:
            if color not in palette(seed):
                cell = (randint(ZERO, SEED_SIDE_F9D67F8B - ONE), randint(ZERO, SEED_SIDE_F9D67F8B - ONE))
                seed = fill(seed, color, frozenset({cell}))
        for _ in range(randint(SIX, 12)):
            color = choice(ALL_COLORS_F9D67F8B)
            height_ = randint(ONE, THREE)
            width_ = randint(ONE, THREE)
            top = randint(ZERO, SEED_SIDE_F9D67F8B - height_)
            left = randint(ZERO, SEED_SIDE_F9D67F8B - width_)
            seed = fill(seed, color, _rect_f9d67f8b(top, left, height_, width_))
        for _ in range(randint(EIGHT, 20)):
            cell = (randint(ZERO, SEED_SIDE_F9D67F8B - ONE), randint(ZERO, SEED_SIDE_F9D67F8B - ONE))
            seed = fill(seed, choice(ALL_COLORS_F9D67F8B), frozenset({cell}))
        if palette(seed) != frozenset(ALL_COLORS_F9D67F8B):
            continue
        full = hconcat(seed, vmirror(seed))
        full = vconcat(full, hmirror(full))
        crop30 = crop(full, ORIGIN, (CROP_SIDE_F9D67F8B, CROP_SIDE_F9D67F8B))
        if len(frozenset(crop30)) < 10:
            continue
        if len(frozenset(dmirror(crop30))) < 10:
            continue
        return crop30
    raise RuntimeError("failed to build symmetric crop")


def generate_f9d67f8b(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        output = _build_output_f9d67f8b()
        mask = _sample_mask_f9d67f8b(diff_lb, diff_ub)
        input_ = fill(output, NINE, mask)
        if input_ == output:
            continue
        return {"input": input_, "output": output}
