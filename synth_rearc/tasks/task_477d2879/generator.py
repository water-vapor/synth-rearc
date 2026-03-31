from synth_rearc.core import *

from .helpers import connected_components_477d2879, has_2x2_477d2879
from .helpers import in_bounds_477d2879, orth_degree_477d2879
from .helpers import orth_neighbors_477d2879, seedable_background_cells_477d2879
from .helpers import seedable_object_cells_477d2879, touches_border_477d2879
from .helpers import turn_count_477d2879, white_neighbor_count_477d2879
from .helpers import zero_regions_477d2879


GRID_SHAPE_477D2879 = (13, 13)
DIRECTIONS_477D2879 = ((-1, 0), (1, 0), (0, -1), (0, 1))
LAYOUT_TEMPLATES_477D2879 = (
    (((44, "cycle"),), 2),
    (((28, "cycle"), (24, "branch")), 4),
    (((30, "cycle"), (10, "path"), (8, "path")), 4),
    (((39, "branch"), (7, "path")), 4),
)


def _ordered_segment_477d2879(
    start: IntegerTuple,
    direction: IntegerTuple,
    length: Integer,
) -> tuple[IntegerTuple, ...]:
    di, dj = direction
    i, j = start
    cells: tuple[IntegerTuple, ...] = tuple()
    for _ in range(length):
        i += di
        j += dj
        cells = cells + ((i, j),)
    return cells


def _ordered_connect_477d2879(
    start: IntegerTuple,
    end: IntegerTuple,
) -> tuple[IntegerTuple, ...]:
    if start[0] == end[0]:
        step = ONE if end[1] > start[1] else -ONE
        return tuple((start[0], j) for j in range(start[1] + step, end[1] + step, step))
    if start[1] == end[1]:
        step = ONE if end[0] > start[0] else -ONE
        return tuple((i, start[1]) for i in range(start[0] + step, end[0] + step, step))
    return tuple()


def _weighted_choice_477d2879(
    items: tuple[tuple[Any, Integer], ...],
) -> Any:
    pool: tuple[Any, ...] = tuple()
    for value, weight in items:
        pool = pool + repeat(value, weight)
    return choice(pool)


def _valid_open_extension_477d2879(
    existing: Indices,
    occupied: Indices,
    anchor: IntegerTuple,
    segment: tuple[IntegerTuple, ...],
) -> Boolean:
    if len(segment) == ZERO:
        return F
    union = set(existing)
    prev = anchor
    for cell in segment:
        if not in_bounds_477d2879(GRID_SHAPE_477D2879, cell):
            return F
        if cell in union or cell in occupied:
            return F
        if any(nbr in occupied for nbr in orth_neighbors_477d2879(cell)):
            return F
        nbrs = {nbr for nbr in orth_neighbors_477d2879(cell) if nbr in union}
        if nbrs != {prev}:
            return F
        union.add(cell)
        prev = cell
    return not has_2x2_477d2879(frozenset(union))


def _extension_candidates_477d2879(
    path: tuple[IntegerTuple, ...],
    occupied: Indices,
    target: Integer,
) -> tuple[tuple[tuple[IntegerTuple, ...], IntegerTuple, Integer], ...]:
    if len(path) == ZERO:
        return tuple()
    current = last(path)
    existing = frozenset(path)
    remaining = target - len(path)
    maxrun = max(ONE, min(FOUR, remaining + TWO))
    previous = None if len(path) == ONE else (path[-1][0] - path[-2][0], path[-1][1] - path[-2][1])
    blocked = None if previous is None else (-previous[0], -previous[1])
    candidates: tuple[tuple[tuple[IntegerTuple, ...], IntegerTuple, Integer], ...] = tuple()
    for direction in DIRECTIONS_477D2879:
        if direction == blocked:
            continue
        for length in range(maxrun, ZERO, -ONE):
            segment = _ordered_segment_477d2879(current, direction, length)
            if not _valid_open_extension_477d2879(existing, occupied, current, segment):
                continue
            turn_weight = THREE if previous is not None and direction != previous else TWO if previous is not None else ONE
            candidates = candidates + ((segment, direction, turn_weight * (length + ONE)),)
    return candidates


def _start_pool_477d2879(
    occupied: Indices,
    want_border: Boolean,
) -> tuple[IntegerTuple, ...]:
    h, w = GRID_SHAPE_477D2879
    cells: tuple[IntegerTuple, ...] = tuple()
    for i in range(h):
        for j in range(w):
            loc = (i, j)
            on_border = i in (ZERO, h - ONE) or j in (ZERO, w - ONE)
            if on_border != want_border:
                continue
            if loc in occupied:
                continue
            if any(nbr in occupied for nbr in orth_neighbors_477d2879(loc)):
                continue
            cells = cells + (loc,)
    return cells


def _sample_open_walk_477d2879(
    target: Integer,
    occupied: Indices,
    want_border: Boolean,
    forbid_border: Boolean,
    min_turns: Integer,
) -> tuple[IntegerTuple, ...]:
    starts = _start_pool_477d2879(occupied, want_border)
    if len(starts) == ZERO:
        return tuple()
    lower = max(THREE, target - TWO)
    upper = target + TWO
    for _ in range(240):
        path = (choice(starts),)
        while len(path) < upper:
            candidates = _extension_candidates_477d2879(path, occupied, target)
            if len(candidates) == ZERO:
                break
            segment, _, _ = _weighted_choice_477d2879(tuple((cand, cand[2]) for cand in candidates))
            path = path + segment
            patch = frozenset(path)
            ready = len(path) >= target and turn_count_477d2879(patch) >= min_turns
            if ready and (not forbid_border or not touches_border_477d2879(patch, GRID_SHAPE_477D2879)) and choice((F, T)):
                break
        patch = frozenset(path)
        if len(path) < lower or len(path) > upper:
            continue
        if turn_count_477d2879(patch) < min_turns:
            continue
        if forbid_border and touches_border_477d2879(patch, GRID_SHAPE_477D2879):
            continue
        return path
    return tuple()


def _closure_additions_477d2879(
    start: IntegerTuple,
    end: IntegerTuple,
    pivot: IntegerTuple | None,
) -> tuple[IntegerTuple, ...]:
    if pivot is None:
        segment = _ordered_connect_477d2879(end, start)
        return tuple(cell for cell in segment if cell != start)
    first_leg = _ordered_connect_477d2879(end, pivot)
    second_leg = _ordered_connect_477d2879(pivot, start)
    if (end != pivot and len(first_leg) == ZERO) or (pivot != start and len(second_leg) == ZERO):
        return tuple()
    cells = first_leg + tuple(cell for cell in second_leg if cell != pivot)
    cells = tuple(cell for cell in cells if cell not in (start, end))
    return cells if len(cells) == len(set(cells)) else tuple()


def _valid_cycle_addition_477d2879(
    component: Indices,
    occupied: Indices,
    start: IntegerTuple,
    end: IntegerTuple,
    additions: tuple[IntegerTuple, ...],
) -> Boolean:
    if len(additions) == ZERO:
        return F
    added = frozenset(additions)
    if len(added) != len(additions):
        return F
    if any(not in_bounds_477d2879(GRID_SHAPE_477D2879, cell) for cell in added):
        return F
    if len(intersection(added, component)) > ZERO or len(intersection(added, occupied)) > ZERO:
        return F
    if any(nbr in occupied for cell in added for nbr in orth_neighbors_477d2879(cell)):
        return F
    if any(sum(nbr in added for nbr in orth_neighbors_477d2879(loc)) > ZERO for loc in component if loc not in (start, end)):
        return F
    if sum(nbr in added for nbr in orth_neighbors_477d2879(start)) != ONE:
        return F
    if sum(nbr in added for nbr in orth_neighbors_477d2879(end)) != ONE:
        return F
    union = combine(component, added)
    if has_2x2_477d2879(union):
        return F
    return all(orth_degree_477d2879(union, loc) == TWO for loc in union)


def _closure_candidates_477d2879(
    component: Indices,
    occupied: Indices,
    start: IntegerTuple,
    end: IntegerTuple,
) -> tuple[tuple[tuple[IntegerTuple, ...], Integer], ...]:
    pivots: tuple[IntegerTuple | None, ...] = (None, (end[0], start[1]), (start[0], end[1]))
    candidates: tuple[tuple[tuple[IntegerTuple, ...], Integer], ...] = tuple()
    for pivot in pivots:
        additions = _closure_additions_477d2879(start, end, pivot)
        if not _valid_cycle_addition_477d2879(component, occupied, start, end, additions):
            continue
        candidates = candidates + ((additions, len(additions) + ONE),)
    return candidates


def _valid_branch_addition_477d2879(
    component: Indices,
    occupied: Indices,
    attach: IntegerTuple,
    additions: tuple[IntegerTuple, ...],
) -> Boolean:
    if len(additions) == ZERO:
        return F
    added = frozenset(additions)
    if len(added) != len(additions):
        return F
    if any(not in_bounds_477d2879(GRID_SHAPE_477D2879, cell) for cell in added):
        return F
    if len(intersection(added, component)) > ZERO or len(intersection(added, occupied)) > ZERO:
        return F
    if any(nbr in occupied for cell in added for nbr in orth_neighbors_477d2879(cell)):
        return F
    if any(sum(nbr in added for nbr in orth_neighbors_477d2879(loc)) > ZERO for loc in component if loc != attach):
        return F
    if sum(nbr in added for nbr in orth_neighbors_477d2879(attach)) != ONE:
        return F
    union = combine(component, added)
    if has_2x2_477d2879(union):
        return F
    if orth_degree_477d2879(union, attach) != THREE:
        return F
    if sum(orth_degree_477d2879(union, loc) == THREE for loc in union) != ONE:
        return F
    return all(orth_degree_477d2879(union, loc) in (ONE, TWO) for loc in added)


def _branch_candidates_477d2879(
    component: Indices,
    occupied: Indices,
) -> tuple[tuple[tuple[IntegerTuple, ...], Integer], ...]:
    candidates: tuple[tuple[tuple[IntegerTuple, ...], Integer], ...] = tuple()
    for attach in component:
        if orth_degree_477d2879(component, attach) != TWO:
            continue
        for direction in DIRECTIONS_477D2879:
            first_step = (attach[0] + direction[0], attach[1] + direction[1])
            if first_step in component:
                continue
            for length in range(FOUR, ONE, -ONE):
                additions = _ordered_segment_477d2879(attach, direction, length)
                if not _valid_branch_addition_477d2879(component, occupied, attach, additions):
                    continue
                candidates = candidates + ((additions, len(additions) + TWO),)
    return candidates


def _sample_component_specs_477d2879() -> tuple[tuple[tuple[str, Integer], ...], Integer]:
    layout, zero_target = choice(LAYOUT_TEMPLATES_477D2879)
    specs: list[tuple[str, Integer]] = []
    for base_size, kind in layout:
        delta = choice((-TWO, -ONE, ZERO, ZERO, ONE, TWO))
        specs.append((kind, max(FIVE, base_size + delta)))
    total = sum(size0 for _, size0 in specs)
    if total < 42:
        kind0, size0 = specs[ZERO]
        specs[ZERO] = (kind0, size0 + (42 - total))
    elif total > 54:
        kind0, size0 = specs[ZERO]
        specs[ZERO] = (kind0, max(FIVE, size0 - (total - 54)))
    return tuple(sorted(specs, key=lambda item: item[1], reverse=T)), zero_target


def _sample_component_477d2879(
    kind: str,
    target: Integer,
    occupied: Indices,
) -> Indices:
    window = TWO if target >= TEN else ONE
    if kind == "path":
        min_turns = max(TWO, target // FOUR)
        for _ in range(160):
            path = _sample_open_walk_477d2879(target, occupied, T, F, min_turns)
            if len(path) == ZERO:
                continue
            component = frozenset(path)
            if abs(len(component) - target) > window:
                continue
            if sum(orth_degree_477d2879(component, loc) == ONE for loc in component) != TWO:
                continue
            return component
        return frozenset()
    if kind == "branch":
        min_turns = max(THREE, target // FIVE)
        for _ in range(200):
            base_target = max(SIX, target - choice((TWO, THREE, FOUR, FIVE)))
            path = _sample_open_walk_477d2879(base_target, occupied, T, F, min_turns - ONE)
            if len(path) == ZERO:
                continue
            component = frozenset(path)
            candidates = _branch_candidates_477d2879(component, occupied)
            if len(candidates) == ZERO:
                continue
            additions = _weighted_choice_477d2879(candidates)
            component = combine(component, frozenset(additions))
            if abs(len(component) - target) > window:
                continue
            if turn_count_477d2879(component) < min_turns:
                continue
            if not touches_border_477d2879(component, GRID_SHAPE_477D2879):
                continue
            return component
        return frozenset()
    min_turns = max(SIX, target // FOUR)
    for _ in range(220):
        base_target = max(EIGHT, target - choice((FOUR, FIVE, SIX, SEVEN)))
        path = _sample_open_walk_477d2879(base_target, occupied, F, T, min_turns - TWO)
        if len(path) == ZERO:
            continue
        component = frozenset(path)
        candidates = _closure_candidates_477d2879(component, occupied, first(path), last(path))
        if len(candidates) == ZERO:
            continue
        additions = _weighted_choice_477d2879(candidates)
        component = combine(component, frozenset(additions))
        if abs(len(component) - target) > window:
            continue
        if turn_count_477d2879(component) < min_turns:
            continue
        if touches_border_477d2879(component, GRID_SHAPE_477D2879):
            continue
        return component
    return frozenset()


def _paint_components_477d2879(
    shape0: IntegerTuple,
    objects0: tuple[Indices, ...],
    object_colors: tuple[Integer, ...],
    regions0: tuple[Indices, ...],
    region_colors: tuple[Integer, ...],
) -> Grid:
    x0 = canvas(ZERO, shape0)
    x1 = x0
    for x2, x3 in zip(objects0, object_colors):
        x1 = fill(x1, x3, x2)
    for x2, x3 in zip(regions0, region_colors):
        x1 = fill(x1, x3, x2)
    return x1


def _preferred_background_cells_477d2879(
    region: Indices,
    white: Indices,
) -> tuple[IntegerTuple, ...]:
    x0 = seedable_background_cells_477d2879(region, white)
    x1 = tuple(loc for loc in x0 if white_neighbor_count_477d2879(white, loc) == ZERO)
    return x1 if len(x1) > ZERO else x0


def generate_477d2879(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    x0 = GRID_SHAPE_477D2879
    x1 = interval(TWO, TEN, ONE)
    while True:
        x2, x3 = _sample_component_specs_477d2879()
        x4: tuple[Indices, ...] = tuple()
        x5 = frozenset()
        x6 = F
        for x7, x8 in x2:
            x9 = _sample_component_477d2879(x7, x8, x5)
            if len(x9) == ZERO:
                x6 = T
                break
            x4 = x4 + (x9,)
            x5 = combine(x5, x9)
        if x6:
            continue
        x10 = connected_components_477d2879(x5)
        if size(x10) != len(x4):
            continue
        if size(x5) < 42 or size(x5) > 54:
            continue
        if has_2x2_477d2879(x5):
            continue
        if max(turn_count_477d2879(obj) for obj in x10) < SIX:
            continue
        if any(orth_degree_477d2879(x5, loc) > THREE for loc in x5):
            continue
        x11 = zero_regions_477d2879(x5, x0)
        x11n = size(x11)
        if x3 == TWO and x11n not in (TWO, THREE):
            continue
        if x3 == FOUR and x11n not in (THREE, FOUR):
            continue
        x12 = tuple(seedable_object_cells_477d2879(obj, x5) for obj in x10)
        x13 = tuple(_preferred_background_cells_477d2879(region, x5) for region in x11)
        if any(len(cands) == ZERO for cands in x12):
            continue
        if any(len(cands) == ZERO for cands in x13):
            continue
        x14 = size(x10) + size(x11)
        x15 = sample(x1, x14)
        x16 = x15[:size(x10)]
        x17 = x15[size(x10):]
        x18 = _paint_components_477d2879(x0, x10, x16, x11, x17)
        x19 = fill(canvas(ZERO, x0), ONE, x5)
        x20 = x19
        for x21, x22 in zip(x12, x16):
            x23 = choice(x21)
            x20 = fill(x20, x22, frozenset({x23}))
        for x21, x22 in zip(x13, x17):
            x23 = choice(x21)
            x20 = fill(x20, x22, frozenset({x23}))
        x24 = tuple(
            (region, color0, cands, seedable_background_cells_477d2879(region, x5))
            for region, color0, cands in zip(x11, x17, x13)
            if size(region) >= 20 and len(cands) >= TWO
        )
        if len(x24) > ZERO and choice((F, F, T)):
            x25, x26, _, x27 = choice(x24)
            x28 = tuple(loc for loc in x27 if index(x20, loc) == ZERO)
            if len(x28) > ZERO:
                x20 = fill(x20, x26, frozenset({choice(x28)}))
        if mostcolor(x20) != ZERO:
            continue
        return {"input": x20, "output": x18}
