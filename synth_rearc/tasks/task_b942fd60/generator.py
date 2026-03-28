from synth_rearc.core import *


_OBSTACLE_COLORS_B942FD60 = (THREE, SIX, SEVEN, EIGHT)


def _in_bounds_b942fd60(
    loc: IntegerTuple,
    dims: IntegerTuple,
) -> bool:
    i, j = loc
    h, w = dims
    return 0 <= i < h and 0 <= j < w


def _perpendiculars_b942fd60(
    direction: IntegerTuple,
) -> tuple[IntegerTuple, IntegerTuple]:
    if equality(direction[0], ZERO):
        return (UP, DOWN)
    return (LEFT, RIGHT)


def _free_ray_b942fd60(
    start: IntegerTuple,
    direction: IntegerTuple,
    dims: IntegerTuple,
    occupied: Indices,
) -> tuple[tuple[IntegerTuple, ...], IntegerTuple | None]:
    cells = []
    loc = add(start, direction)
    while _in_bounds_b942fd60(loc, dims) and loc not in occupied:
        cells.append(loc)
        loc = add(loc, direction)
    blocker = loc if _in_bounds_b942fd60(loc, dims) else None
    return tuple(cells), blocker


def _obstacle_options_b942fd60(
    ray: tuple[IntegerTuple, ...],
    direction: IntegerTuple,
    dims: IntegerTuple,
    occupied: Indices,
) -> tuple[tuple[tuple[IntegerTuple, ...], IntegerTuple, IntegerTuple], ...]:
    out = []
    for path_len in range(ONE, len(ray)):
        segment = ray[:path_len]
        endpoint = segment[-ONE]
        obstacle = ray[path_len]
        occupied2 = combine(occupied, combine(frozenset(segment), initset(obstacle)))
        good = T
        for turn in _perpendiculars_b942fd60(direction):
            nxt = add(endpoint, turn)
            if _in_bounds_b942fd60(nxt, dims) and nxt in occupied2:
                good = F
                break
        if good:
            out.append((segment, endpoint, obstacle))
    return tuple(out)


def _sample_cells_b942fd60(
    cells: tuple[IntegerTuple, ...],
    count: int,
) -> tuple[IntegerTuple, ...]:
    pool = list(cells)
    shuffle(pool)
    return tuple(pool[:count])


def generate_b942fd60(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        h = unifint(diff_lb, diff_ub, (FIVE, 12))
        w = unifint(diff_lb, diff_ub, (SIX, 12))
        dims = (h, w)
        seed_row = unifint(diff_lb, diff_ub, (ONE, h - TWO))
        seed = (seed_row, ZERO)
        occupied = initset(seed)
        path = frozenset()
        obstacles = {}
        active = [(seed, RIGHT, ZERO)]
        target_branches = unifint(diff_lb, diff_ub, (ONE, FOUR))
        branch_count = ZERO
        ok = T
        while len(active) > ZERO:
            loc, direction, depth = active.pop()
            ray, blocker = _free_ray_b942fd60(loc, direction, dims, occupied)
            if len(ray) == ZERO:
                if blocker is None:
                    continue
                ok = F
                break
            force_obstacle = blocker is not None
            options = _obstacle_options_b942fd60(ray, direction, dims, occupied)
            want_obstacle = F
            if len(options) > ZERO and branch_count < target_branches and depth < THREE:
                bag = ["edge", "obstacle"]
                if depth < TWO:
                    bag.append("obstacle")
                want_obstacle = choice(bag) == "obstacle"
            if force_obstacle and len(options) == ZERO:
                ok = F
                break
            if force_obstacle or want_obstacle:
                choice_idx = unifint(diff_lb, diff_ub, (ZERO, len(options) - ONE))
                segment, endpoint, obstacle = options[choice_idx]
                path = combine(path, frozenset(segment))
                occupied = combine(occupied, combine(frozenset(segment), initset(obstacle)))
                obstacle_colors = _OBSTACLE_COLORS_B942FD60
                if equality(direction, DOWN) and equality(obstacle[0], h - ONE):
                    obstacle_colors = (THREE, SIX, EIGHT)
                obstacles[obstacle] = choice(obstacle_colors)
                branch_count = increment(branch_count)
                turns = list(_perpendiculars_b942fd60(direction))
                shuffle(turns)
                for turn in turns:
                    active.append((endpoint, turn, increment(depth)))
            else:
                segment = frozenset(ray)
                path = combine(path, segment)
                occupied = combine(occupied, segment)
        if flip(ok) or branch_count == ZERO:
            continue
        free = tuple(loc for loc in asindices(canvas(ZERO, dims)) if loc not in occupied)
        if len(free) == ZERO:
            continue
        distractor_max = min(max(len(free) // 9, ONE), EIGHT)
        distractor_count = unifint(diff_lb, diff_ub, (ZERO, distractor_max))
        distractors = {}
        for loc in _sample_cells_b942fd60(free, distractor_count):
            distractors[loc] = choice(_OBSTACLE_COLORS_B942FD60)
        gi = canvas(ZERO, dims)
        gi = fill(gi, TWO, initset(seed))
        for loc, value in obstacles.items():
            gi = fill(gi, value, initset(loc))
        for loc, value in distractors.items():
            gi = fill(gi, value, initset(loc))
        go = fill(gi, TWO, path)
        if equality(gi, go):
            continue
        from .verifier import verify_b942fd60

        if verify_b942fd60(gi) != go:
            continue
        return {"input": gi, "output": go}
