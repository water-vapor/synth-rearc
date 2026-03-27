from arc2.core import *


RAY_OPTIONS = (UP, DOWN, LEFT, RIGHT)


def _in_bounds_2f767503(loc: tuple[int, int], dims: tuple[int, int]) -> bool:
    return ZERO <= loc[ZERO] < dims[ZERO] and ZERO <= loc[ONE] < dims[ONE]


def _neighbors_2f767503(loc: tuple[int, int]) -> tuple[tuple[int, int], ...]:
    i, j = loc
    return (
        (i - ONE, j),
        (i + ONE, j),
        (i, j - ONE),
        (i, j + ONE),
    )


def _ray_cells_2f767503(
    center: tuple[int, int],
    ray_dir: tuple[int, int],
    dims: tuple[int, int],
) -> tuple[tuple[int, int], ...]:
    cells = []
    loc = add(center, ray_dir)
    while _in_bounds_2f767503(loc, dims):
        cells.append(loc)
        loc = add(loc, ray_dir)
    return tuple(cells)


def _marker_parts_2f767503(
    center: tuple[int, int],
    ray_dir: tuple[int, int],
) -> tuple[frozenset[tuple[int, int]], tuple[int, int]]:
    line_dir = DOWN if ray_dir[ZERO] == ZERO else RIGHT
    arm_a = add(center, line_dir)
    arm_b = add(center, invert(line_dir))
    dot = add(center, invert(ray_dir))
    line = frozenset({center, arm_a, arm_b})
    return line, dot


def _can_add_2f767503(
    cell: tuple[int, int],
    dims: tuple[int, int],
    occupied: set[tuple[int, int]],
    forbidden: set[tuple[int, int]],
    cells: set[tuple[int, int]],
) -> bool:
    if not _in_bounds_2f767503(cell, dims):
        return False
    if cell in occupied or cell in forbidden or cell in cells:
        return False
    return all(nb not in occupied or nb in cells for nb in _neighbors_2f767503(cell))


def _grow_component_2f767503(
    anchor: tuple[int, int],
    dims: tuple[int, int],
    occupied: set[tuple[int, int]],
    forbidden: set[tuple[int, int]],
    max_size: int,
    ray_dir: tuple[int, int],
) -> frozenset[tuple[int, int]]:
    cells = {anchor}
    goal = randint(ONE, max_size)
    while len(cells) < goal:
        candidates = []
        for cell in tuple(cells):
            for nb in _neighbors_2f767503(cell):
                if not _can_add_2f767503(nb, dims, occupied, forbidden, cells):
                    continue
                weight = ONE
                if nb[ZERO] == anchor[ZERO] or nb[ONE] == anchor[ONE]:
                    weight += ONE
                forward = (
                    (nb[ZERO] - anchor[ZERO]) * ray_dir[ZERO]
                    + (nb[ONE] - anchor[ONE]) * ray_dir[ONE]
                )
                if forward >= ZERO:
                    weight += ONE
                candidates.extend([nb] * weight)
        if len(candidates) == ZERO:
            break
        cells.add(choice(candidates))
    return frozenset(cells)


def generate_2f767503(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        h = unifint(diff_lb, diff_ub, (9, 15))
        w = unifint(diff_lb, diff_ub, (9, 15))
        dims = (h, w)
        ray_dir = choice(RAY_OPTIONS)
        center = (randint(ONE, h - TWO), randint(ONE, w - TWO))
        marker, dot = _marker_parts_2f767503(center, ray_dir)
        if not _in_bounds_2f767503(dot, dims):
            continue
        if not all(_in_bounds_2f767503(cell, dims) for cell in marker):
            continue

        ray = _ray_cells_2f767503(center, ray_dir, dims)
        if len(ray) < THREE:
            continue

        ray_set = set(ray)
        guard = set(marker) | {dot, ray[ZERO]}
        target_distances = list(range(TWO, len(ray) + ONE))
        shuffle(target_distances)
        ntarget = randint(ONE, min(THREE, max(ONE, len(ray) // THREE)))
        picked = []
        for dist in target_distances:
            if all(abs(dist - prior) >= TWO for prior in picked):
                picked.append(dist)
            if len(picked) == ntarget:
                break
        if len(picked) == ZERO:
            continue
        picked.sort()

        gi = canvas(SEVEN, dims)
        gi = fill(gi, FIVE, marker)
        gi = fill(gi, NINE, {dot})

        occupied: set[tuple[int, int]] = set()
        targets = []
        failed = False
        for dist in picked:
            anchor = ray[dist - ONE]
            comp = _grow_component_2f767503(
                anchor,
                dims,
                occupied,
                guard,
                randint(ONE, 6),
                ray_dir,
            )
            if len(intersection(comp, ray_set)) == ZERO:
                failed = True
                break
            targets.append(comp)
            occupied |= set(comp)
        if failed:
            continue

        distractors = []
        ndistractors = randint(4, min(11, (h * w) // 12))
        attempts = ZERO
        while len(distractors) < ndistractors and attempts < 300:
            attempts += ONE
            anchor = (randint(ZERO, h - ONE), randint(ZERO, w - ONE))
            if anchor in occupied or anchor in guard or anchor in ray_set:
                continue
            if any(nb in occupied for nb in _neighbors_2f767503(anchor)):
                continue
            comp = _grow_component_2f767503(
                anchor,
                dims,
                occupied,
                set(ray_set) | set(marker) | {dot},
                randint(ONE, 5),
                ray_dir,
            )
            if len(comp) == ZERO or len(intersection(comp, ray_set)) != ZERO:
                continue
            distractors.append(comp)
            occupied |= set(comp)
        if len(distractors) < THREE:
            continue

        for comp in combine(tuple(targets), tuple(distractors)):
            gi = fill(gi, FOUR, comp)

        go = gi
        for comp in targets:
            go = fill(go, SEVEN, comp)

        if gi == go:
            continue
        if mostcolor(gi) != SEVEN:
            continue
        if colorcount(go, FOUR) == ZERO:
            continue
        return {"input": gi, "output": go}
