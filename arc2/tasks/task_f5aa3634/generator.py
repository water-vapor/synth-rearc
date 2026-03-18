from arc2.core import *

from .verifier import verify_f5aa3634


FG_COLORS_F5AA3634 = remove(ZERO, interval(ZERO, TEN, ONE))
BBOX_SHAPES_F5AA3634 = (
    (THREE, THREE),
    (THREE, THREE),
    (THREE, FOUR),
    (THREE, FOUR),
    (FOUR, THREE),
    (FOUR, THREE),
    (FIVE, THREE),
    (THREE, FIVE),
)


def _neighbors_f5aa3634(
    cell: tuple[int, int],
    dims: tuple[int, int],
) -> tuple[tuple[int, int], ...]:
    i, j = cell
    h, w = dims
    candidates = ((i - ONE, j), (i + ONE, j), (i, j - ONE), (i, j + ONE))
    return tuple((a, b) for a, b in candidates if 0 <= a < h and 0 <= b < w)


def _orthogonal_path_f5aa3634(
    start: tuple[int, int],
    stop: tuple[int, int],
) -> tuple[tuple[int, int], ...]:
    i, j = start
    ti, tj = stop
    cells = [start]
    vertical_first = choice((T, F))
    if vertical_first:
        while i != ti:
            i += ONE if ti > i else NEG_ONE
            cells.append((i, j))
        while j != tj:
            j += ONE if tj > j else NEG_ONE
            cells.append((i, j))
        return tuple(cells)
    while j != tj:
        j += ONE if tj > j else NEG_ONE
        cells.append((i, j))
    while i != ti:
        i += ONE if ti > i else NEG_ONE
        cells.append((i, j))
    return tuple(cells)


def _synthesize_patch_f5aa3634(
    diff_lb: float,
    diff_ub: float,
    dims: tuple[int, int],
) -> frozenset[tuple[int, int]]:
    h, w = dims
    area = h * w
    min_cells = max(FIVE, (area + ONE) // TWO)
    max_cells = min(area - ONE, max(min_cells, (TWO * area + THREE) // THREE))
    for _ in range(100):
        anchor = (randint(ZERO, h - ONE), randint(ZERO, w - ONE))
        edge_cells = (
            (ZERO, randint(ZERO, w - ONE)),
            (h - ONE, randint(ZERO, w - ONE)),
            (randint(ZERO, h - ONE), ZERO),
            (randint(ZERO, h - ONE), w - ONE),
        )
        cells = {anchor}
        for edge_cell in edge_cells:
            cells.update(_orthogonal_path_f5aa3634(anchor, edge_cell))
        if len(cells) > max_cells:
            continue
        target = unifint(diff_lb, diff_ub, (max(len(cells), min_cells), max_cells))
        while len(cells) < target:
            frontier = set()
            for cell in cells:
                frontier.update(
                    neighbor
                    for neighbor in _neighbors_f5aa3634(cell, dims)
                    if neighbor not in cells
                )
            if len(frontier) == ZERO:
                break
            cells.add(choice(tuple(frontier)))
        if len(cells) < min_cells or len(cells) >= area:
            continue
        return frozenset(cells)
    raise RuntimeError("failed to synthesize connected motif")


def _colorize_patch_f5aa3634(
    patch: frozenset[tuple[int, int]],
    dims: tuple[int, int],
) -> Grid:
    cells = tuple(sorted(patch))
    color_choices = [TWO, THREE, THREE]
    if len(cells) >= NINE and choice((T, F, F)):
        color_choices.append(FOUR)
    ncolors = min(len(cells), choice(tuple(color_choices)))
    palette = tuple(sample(FG_COLORS_F5AA3634, ncolors))
    seeds = tuple(sample(cells, ncolors))
    assignment = {cell: palette[idx] for idx, cell in enumerate(seeds)}
    pending = set(cells) - set(seeds)
    while len(pending) > ZERO:
        frontier = [
            cell
            for cell in pending
            if any(neighbor in assignment for neighbor in _neighbors_f5aa3634(cell, dims))
        ]
        cell = choice(frontier)
        neighboring_colors = tuple(
            assignment[neighbor]
            for neighbor in _neighbors_f5aa3634(cell, dims)
            if neighbor in assignment
        )
        fill_color = branch(
            choice((T, T, F)),
            mostcommon(neighboring_colors),
            choice(neighboring_colors),
        )
        assignment[cell] = fill_color
        pending.remove(cell)
    h, w = dims
    rows = []
    for i in range(h):
        row = []
        for j in range(w):
            row.append(assignment.get((i, j), ZERO))
        rows.append(tuple(row))
    return tuple(rows)


def _make_crop_f5aa3634(
    diff_lb: float,
    diff_ub: float,
    seen: set[Grid],
) -> Grid:
    for _ in range(200):
        dims = choice(BBOX_SHAPES_F5AA3634)
        patch = _synthesize_patch_f5aa3634(diff_lb, diff_ub, dims)
        crop = _colorize_patch_f5aa3634(patch, dims)
        if crop not in seen:
            return crop
    raise RuntimeError("failed to create unique crop")


def _object_from_crop_f5aa3634(
    crop: Grid,
    top: int,
    left: int,
) -> Object:
    cells = set()
    for i, row in enumerate(crop):
        for j, value in enumerate(row):
            if value != ZERO:
                cells.add((value, (top + i, left + j)))
    return frozenset(cells)


def _expanded_bbox_f5aa3634(
    top: int,
    left: int,
    box_h: int,
    box_w: int,
    dims: tuple[int, int],
) -> frozenset[tuple[int, int]]:
    h, w = dims
    rows = range(max(ZERO, top - ONE), min(h, top + box_h + ONE))
    cols = range(max(ZERO, left - ONE), min(w, left + box_w + ONE))
    return frozenset((i, j) for i in rows for j in cols)


def _place_crops_f5aa3634(
    crops: tuple[Grid, ...],
    dims: tuple[int, int],
) -> tuple[tuple[int, int], ...] | None:
    h, w = dims
    blocked = set()
    placements = [None] * len(crops)
    order = sorted(
        range(len(crops)),
        key=lambda idx: shape(crops[idx])[ZERO] * shape(crops[idx])[ONE],
        reverse=True,
    )
    for idx in order:
        box_h, box_w = shape(crops[idx])
        candidates = []
        for top in range(h - box_h + ONE):
            for left in range(w - box_w + ONE):
                expanded = _expanded_bbox_f5aa3634(top, left, box_h, box_w, dims)
                if blocked.isdisjoint(expanded):
                    candidates.append((top, left))
        if len(candidates) == ZERO:
            return None
        placements[idx] = choice(candidates)
        top, left = placements[idx]
        blocked.update(_expanded_bbox_f5aa3634(top, left, box_h, box_w, dims))
    return tuple(placements)


def generate_f5aa3634(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        seen = set()
        target = _make_crop_f5aa3634(diff_lb, diff_ub, seen)
        seen.add(target)
        ndistractors = choice((TWO, THREE))
        distractors = []
        for _ in range(ndistractors):
            crop = _make_crop_f5aa3634(diff_lb, diff_ub, seen)
            seen.add(crop)
            distractors.append(crop)
        crops = [target, target] + distractors
        shuffle(crops)
        max_h = max(shape(crop)[ZERO] for crop in crops)
        max_w = max(shape(crop)[ONE] for crop in crops)
        grid_h = unifint(diff_lb, diff_ub, (max(TEN, max_h + FOUR), 18))
        grid_w = unifint(diff_lb, diff_ub, (max(13, max_w + FIVE), 18))
        placements = _place_crops_f5aa3634(tuple(crops), (grid_h, grid_w))
        if placements is None:
            continue
        gi = canvas(ZERO, (grid_h, grid_w))
        for crop, (top, left) in zip(crops, placements):
            gi = paint(gi, _object_from_crop_f5aa3634(crop, top, left))
        if len(objects(gi, F, F, T)) != len(crops):
            continue
        if verify_f5aa3634(gi) != target:
            continue
        return {"input": gi, "output": target}
