from arc2.core import *

from .verifier import verify_84db8fc4


DIMS_84DB8FC4 = (TEN, TEN)
NONZERO_COLORS_84DB8FC4 = (ONE, THREE)
SYMMETRIES_84DB8FC4 = (identity, rot90, rot180, rot270, hmirror, vmirror, dmirror, cmirror)


def _neighbors_84db8fc4(
    cell,
):
    i, j = cell
    h, w = DIMS_84DB8FC4
    out = []
    for ni, nj in ((i - ONE, j), (i + ONE, j), (i, j - ONE), (i, j + ONE)):
        if ZERO <= ni < h and ZERO <= nj < w:
            out.append((ni, nj))
    return tuple(out)


def _is_border_84db8fc4(
    cell,
) -> Boolean:
    i, j = cell
    h, w = DIMS_84DB8FC4
    return i in (ZERO, h - ONE) or j in (ZERO, w - ONE)


def _can_add_84db8fc4(
    cell,
    component,
    occupied,
    interior_only: Boolean,
) -> Boolean:
    if cell in component:
        return False
    if cell in occupied:
        return False
    if interior_only and _is_border_84db8fc4(cell):
        return False
    for neighbor in _neighbors_84db8fc4(cell):
        if neighbor in occupied and neighbor not in component:
            return False
    return True


def _seed_candidates_84db8fc4(
    occupied,
    interior_only: Boolean,
):
    h, w = DIMS_84DB8FC4
    return tuple(
        (i, j)
        for i in range(h)
        for j in range(w)
        if _can_add_84db8fc4((i, j), frozenset(), occupied, interior_only)
    )


def _grow_component_84db8fc4(
    seed,
    occupied,
    target_size: Integer,
    interior_only: Boolean,
):
    if not _can_add_84db8fc4(seed, frozenset(), occupied, interior_only):
        return frozenset()
    component = {seed}
    frontier = {
        neighbor
        for neighbor in _neighbors_84db8fc4(seed)
        if _can_add_84db8fc4(neighbor, component, occupied, interior_only)
    }
    while len(component) < target_size and len(frontier) > ZERO:
        cell = choice(tuple(frontier))
        frontier.remove(cell)
        if not _can_add_84db8fc4(cell, component, occupied, interior_only):
            continue
        component.add(cell)
        for neighbor in _neighbors_84db8fc4(cell):
            if _can_add_84db8fc4(neighbor, component, occupied, interior_only):
                frontier.add(neighbor)
    return frozenset(component)


def _paint_example_84db8fc4(
    base_grid,
    border_components,
    enclosed_components,
) -> dict:
    gi = [row[:] for row in base_grid]
    go = [row[:] for row in base_grid]
    for component in border_components:
        for i, j in component:
            gi[i][j] = ZERO
            go[i][j] = TWO
    for component in enclosed_components:
        for i, j in component:
            gi[i][j] = ZERO
            go[i][j] = FIVE
    return {
        "input": format_grid(gi),
        "output": format_grid(go),
    }


def _random_example_84db8fc4(
    diff_lb: float,
    diff_ub: float,
) -> dict | None:
    base_grid = [
        [choice(NONZERO_COLORS_84DB8FC4) for _ in range(DIMS_84DB8FC4[ONE])]
        for _ in range(DIMS_84DB8FC4[ZERO])
    ]
    occupied = set()
    border_components = []
    enclosed_components = []
    border_sizes = (
        unifint(diff_lb, diff_ub, (FIVE, TEN)),
        unifint(diff_lb, diff_ub, (TWO, SIX)),
        unifint(diff_lb, diff_ub, (TWO, SIX)),
    )
    enclosed_sizes = (
        unifint(diff_lb, diff_ub, (FOUR, EIGHT)),
        unifint(diff_lb, diff_ub, (TWO, FIVE)),
    )
    for target_size in border_sizes:
        seeds = tuple(
            cell
            for cell in _seed_candidates_84db8fc4(occupied, False)
            if _is_border_84db8fc4(cell)
        )
        if len(seeds) == ZERO:
            return None
        seed = choice(seeds)
        component = _grow_component_84db8fc4(seed, occupied, target_size, False)
        if len(component) == ZERO:
            return None
        border_components.append(component)
        occupied |= component
    for target_size in enclosed_sizes:
        seeds = _seed_candidates_84db8fc4(occupied, True)
        if len(seeds) == ZERO:
            return None
        seed = choice(seeds)
        component = _grow_component_84db8fc4(seed, occupied, target_size, True)
        if len(component) == ZERO:
            return None
        enclosed_components.append(component)
        occupied |= component
    example = _paint_example_84db8fc4(base_grid, border_components, enclosed_components)
    zero_count = colorcount(example["input"], ZERO)
    if zero_count < 15 or zero_count > 35:
        return None
    if verify_84db8fc4(example["input"]) != example["output"]:
        return None
    return example


def _fallback_example_84db8fc4() -> dict:
    base_grid = [
        [choice(NONZERO_COLORS_84DB8FC4) for _ in range(DIMS_84DB8FC4[ONE])]
        for _ in range(DIMS_84DB8FC4[ZERO])
    ]
    border_components = (
        frozenset({(ZERO, ZERO), (ZERO, ONE), (ONE, ZERO), (TWO, ZERO), (TWO, ONE)}),
        frozenset({(ZERO, EIGHT), (ONE, EIGHT), (TWO, EIGHT), (TWO, NINE)}),
        frozenset({(SEVEN, ZERO), (EIGHT, ZERO), (EIGHT, ONE), (NINE, ONE), (NINE, TWO)}),
    )
    enclosed_components = (
        frozenset({(THREE, FOUR), (THREE, FIVE), (FOUR, FIVE), (FIVE, FOUR), (FIVE, FIVE)}),
        frozenset({(SIX, SIX), (SIX, SEVEN), (SEVEN, SIX)}),
    )
    example = _paint_example_84db8fc4(base_grid, border_components, enclosed_components)
    transform = choice(SYMMETRIES_84DB8FC4)
    example = {
        "input": transform(example["input"]),
        "output": transform(example["output"]),
    }
    return example


def generate_84db8fc4(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    for _ in range(8):
        example = _random_example_84db8fc4(diff_lb, diff_ub)
        if example is not None:
            return example
    example = _fallback_example_84db8fc4()
    if verify_84db8fc4(example["input"]) != example["output"]:
        raise RuntimeError("fallback example for 84db8fc4 is invalid")
    return example
