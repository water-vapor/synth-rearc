from synth_rearc.core import *

from .verifier import verify_fea12743


PANEL_SHAPE_FEA12743 = (FOUR, FOUR)
GRID_SHAPE_FEA12743 = (16, 11)
PANEL_OFFSETS_FEA12743 = ((ONE, ONE), (ONE, SIX), (SIX, ONE), (SIX, SIX), (11, ONE), (11, SIX))
TRANSFORMS_FEA12743 = (identity, rot90, rot180, rot270, hmirror, vmirror, dmirror, cmirror)


def _mask_to_panel_fea12743(
    cells: Indices,
) -> Grid:
    return fill(canvas(ZERO, PANEL_SHAPE_FEA12743), TWO, cells)


def _panel_union_fea12743(
    a: Grid,
    b: Grid,
) -> Grid:
    x0 = ofcolor(a, TWO)
    x1 = ofcolor(b, TWO)
    x2 = combine(x0, x1)
    return fill(canvas(ZERO, PANEL_SHAPE_FEA12743), TWO, x2)


def _orbit_fea12743(
    panel: Grid,
) -> tuple[Grid, ...]:
    return tuple(dict.fromkeys(transform(panel) for transform in TRANSFORMS_FEA12743))


def _sample_panel_fea12743(
    diff_lb: float,
    diff_ub: float,
) -> Grid:
    universe = frozenset(product(interval(ZERO, FOUR, ONE), interval(ZERO, FOUR, ONE)))
    while True:
        ncells = unifint(diff_lb, diff_ub, (FIVE, NINE))
        cells = {choice(tuple(universe))}
        detached = choice((T, F, F))
        while len(cells) < ncells:
            taken = frozenset(cells)
            frontier = frozenset(
                loc
                for cell in taken
                for loc in dneighbors(cell)
                if 0 <= loc[0] < FOUR and 0 <= loc[1] < FOUR and loc not in taken
            )
            free = difference(universe, taken)
            remote = difference(free, frontier)
            if detached and len(remote) > ZERO and len(cells) >= THREE and choice((T, F)):
                cells.add(choice(tuple(remote)))
                detached = F
                continue
            if len(frontier) > ZERO:
                cells.add(choice(tuple(frontier)))
                continue
            cells.add(choice(tuple(free)))
        panel = _mask_to_panel_fea12743(frozenset(cells))
        orbit = _orbit_fea12743(panel)
        if len(orbit) < TWO:
            continue
        if panel == canvas(ZERO, PANEL_SHAPE_FEA12743):
            continue
        return panel


def _find_triplet_fea12743(
    panels: tuple[Grid, ...],
) -> tuple[int, int, int] | None:
    masks = tuple(ofcolor(panel, TWO) for panel in panels)
    for target in range(SIX):
        for left in range(SIX):
            for right in range(left + ONE, SIX):
                if target in (left, right):
                    continue
                left_mask = masks[left]
                right_mask = masks[right]
                target_mask = masks[target]
                if left_mask == right_mask or left_mask == target_mask or right_mask == target_mask:
                    continue
                if combine(left_mask, right_mask) == target_mask:
                    return (left, right, target)
    return None


def _compose_input_fea12743(
    panels: tuple[Grid, ...],
) -> Grid:
    grid = canvas(ZERO, GRID_SHAPE_FEA12743)
    for idx, panel in enumerate(panels):
        patch = shift(ofcolor(panel, TWO), PANEL_OFFSETS_FEA12743[idx])
        grid = fill(grid, TWO, patch)
    return grid


def generate_fea12743(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        source_panel = _sample_panel_fea12743(diff_lb, diff_ub)
        source_orbit = _orbit_fea12743(source_panel)
        if len(source_orbit) < TWO:
            continue
        left_panel, right_panel = sample(source_orbit, TWO)
        union_panel = _panel_union_fea12743(left_panel, right_panel)
        if union_panel in source_orbit:
            continue
        union_count = colorcount(union_panel, TWO)
        if union_count < SEVEN or union_count > 14:
            continue
        use_same_family = choice((T, F))
        if use_same_family:
            distractor_orbit = source_orbit
        else:
            distractor_panel = _sample_panel_fea12743(diff_lb, diff_ub)
            distractor_orbit = _orbit_fea12743(distractor_panel)
        if union_panel in distractor_orbit:
            continue
        distractors = tuple(choice(distractor_orbit) for _ in range(THREE))
        slots = sample(interval(ZERO, SIX, ONE), THREE)
        pair_slots = tuple(sorted(slots[:TWO]))
        target_slot = slots[TWO]
        panels_list = [None] * SIX
        panels_list[pair_slots[ZERO]] = left_panel
        panels_list[pair_slots[ONE]] = right_panel
        panels_list[target_slot] = union_panel
        rest = tuple(idx for idx in range(SIX) if idx not in slots)
        for idx, panel in zip(rest, distractors):
            panels_list[idx] = panel
        panels = tuple(panels_list)
        triplet = _find_triplet_fea12743(panels)
        if triplet != (pair_slots[ZERO], pair_slots[ONE], target_slot):
            continue
        gi = _compose_input_fea12743(panels)
        go = fill(gi, EIGHT, shift(ofcolor(left_panel, TWO), PANEL_OFFSETS_FEA12743[pair_slots[ZERO]]))
        go = fill(go, EIGHT, shift(ofcolor(right_panel, TWO), PANEL_OFFSETS_FEA12743[pair_slots[ONE]]))
        go = fill(go, THREE, shift(ofcolor(union_panel, TWO), PANEL_OFFSETS_FEA12743[target_slot]))
        if verify_fea12743(gi) != go:
            continue
        return {"input": gi, "output": go}
