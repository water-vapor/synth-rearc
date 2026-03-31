from __future__ import annotations

from synth_rearc.core import *


MOTIF_TEMPLATES_4E34C42C = (
    (
        (1, 1, 1),
        (1, 2, 1),
        (1, 1, 1),
    ),
    (
        (1, 0, 2),
        (1, 3, 3),
        (1, 3, 4),
        (1, 3, 3),
        (1, 0, 2),
    ),
    (
        (1, 0, 0, 0),
        (2, 2, 0, 0),
        (2, 2, 2, 2),
        (2, 2, 0, 0),
        (1, 0, 0, 0),
    ),
    (
        (1, 1, 1, 1, 1),
        (1, 2, 0, 3, 1),
        (1, 1, 1, 1, 1),
    ),
    (
        (0, 1, 1, 1, 0),
        (1, 1, 2, 1, 1),
        (0, 1, 1, 1, 0),
    ),
    (
        (1, 1, 0, 0, 4),
        (1, 2, 2, 3, 4),
        (1, 1, 0, 0, 4),
    ),
    (
        (1, 1, 1, 0),
        (1, 2, 1, 3),
        (1, 1, 1, 3),
        (0, 3, 3, 3),
    ),
)


def _bg_priority_key_4e34c42c(
    grid: Grid,
    bg: Integer,
) -> tuple[tuple[Integer, ...], ...]:
    return tuple(tuple(ZERO if value == bg else value + ONE for value in row) for row in grid)


def _build_grid_from_placements_4e34c42c(
    bg: Integer,
    pieces: tuple[Grid, ...],
    placements: dict[int, tuple[int, int]],
) -> Grid | None:
    cells: dict[tuple[int, int], Integer] = {}
    for idx, (r0, c0) in placements.items():
        piece = pieces[idx]
        for i, row in enumerate(piece):
            for j, value in enumerate(row):
                key = (r0 + i, c0 + j)
                prior = cells.get(key)
                if prior is None:
                    cells[key] = value
                    continue
                if prior != value:
                    return None
    rows = tuple(index[ZERO] for index in cells)
    cols = tuple(index[ONE] for index in cells)
    rmin = min(rows)
    rmax = max(rows)
    cmin = min(cols)
    cmax = max(cols)
    return tuple(
        tuple(cells.get((i, j), bg) for j in range(cmin, cmax + ONE))
        for i in range(rmin, rmax + ONE)
    )


def _normalize_placements_4e34c42c(
    placements: dict[int, tuple[int, int]],
) -> tuple[tuple[int, tuple[int, int]], ...]:
    rows = tuple(row for row, _ in placements.values())
    cols = tuple(col for _, col in placements.values())
    rmin = min(rows)
    cmin = min(cols)
    return tuple(
        sorted((idx, (row - rmin, col - cmin)) for idx, (row, col) in placements.items())
    )


def _informative_exact_overlap_candidates_4e34c42c(
    a: Grid,
    b: Grid,
    bg: Integer,
) -> tuple[tuple[int, int, int], ...]:
    ha = len(a)
    wa = len(a[ZERO])
    hb = len(b)
    wb = len(b[ZERO])
    candidates = set()
    for di in range(-hb + ONE, ha):
        for dj in range(-wb + ONE, wa):
            overlap = False
            informative = False
            ok = True
            for i in range(hb):
                for j in range(wb):
                    ai = i + di
                    aj = j + dj
                    if not (ZERO <= ai < ha and ZERO <= aj < wa):
                        continue
                    overlap = True
                    if a[ai][aj] != b[i][j]:
                        ok = False
                        break
                    if a[ai][aj] != bg:
                        informative = True
                if not ok:
                    break
            if not (ok and overlap and informative):
                continue
            top = min(ZERO, di)
            left = min(ZERO, dj)
            bottom = max(ha, di + hb)
            right = max(wa, dj + wb)
            area = (bottom - top) * (right - left)
            candidates.add((di, dj, area))
    return tuple(sorted(candidates, key=lambda item: (item[TWO], item[ZERO], item[ONE])))


def extract_fragments_4e34c42c(
    grid: Grid,
) -> tuple[Integer, tuple[Grid, ...]]:
    bg = mostcolor(grid)
    objs = order(objects(grid, False, False, True), ulcorner)
    pieces = tuple(subgrid(obj, grid) for obj in objs)
    return bg, pieces


def assemble_fragments_4e34c42c(
    bg: Integer,
    pieces: tuple[Grid, ...],
) -> Grid:
    if len(pieces) == ONE:
        return pieces[ZERO]
    n = len(pieces)
    pair_candidates = tuple(
        tuple(
            tuple()
            if i == j
            else _informative_exact_overlap_candidates_4e34c42c(pieces[i], pieces[j], bg)
            for j in range(n)
        )
        for i in range(n)
    )
    best_grid = None
    best_area = 10 ** 9
    seen = set()

    def better(grid: Grid, area: Integer) -> bool:
        nonlocal best_grid, best_area
        if area < best_area:
            return True
        if area > best_area or best_grid is None:
            return False
        return _bg_priority_key_4e34c42c(grid, bg) < _bg_priority_key_4e34c42c(best_grid, bg)

    def rec(
        placements: dict[int, tuple[int, int]],
        remaining: tuple[int, ...],
    ) -> None:
        nonlocal best_grid, best_area
        state = (_normalize_placements_4e34c42c(placements), tuple(sorted(remaining)))
        if state in seen:
            return
        seen.add(state)
        grid = _build_grid_from_placements_4e34c42c(bg, pieces, placements)
        if grid is None:
            return
        area = len(grid) * len(grid[ZERO])
        if area > best_area:
            return
        if len(remaining) == ZERO:
            if better(grid, area):
                best_area = area
                best_grid = grid
            return
        option_sets = []
        for j in remaining:
            pos_to_area: dict[tuple[int, int], tuple[int, tuple[tuple[int, ...], ...], int, int]] = {}
            for i, (ri, ci) in placements.items():
                for di, dj, _ in pair_candidates[i][j]:
                    pos = (ri + di, ci + dj)
                    placements[j] = pos
                    merged = _build_grid_from_placements_4e34c42c(bg, pieces, placements)
                    del placements[j]
                    if merged is None:
                        continue
                    metric = (
                        len(merged) * len(merged[ZERO]),
                        _bg_priority_key_4e34c42c(merged, bg),
                        len(merged),
                        len(merged[ZERO]),
                    )
                    prior = pos_to_area.get(pos)
                    if prior is None or metric < prior:
                        pos_to_area[pos] = metric
            if len(pos_to_area) == ZERO:
                continue
            candidates = tuple(
                sorted(
                    (metric + (pos[ZERO], pos[ONE]) for pos, metric in pos_to_area.items()),
                )
            )
            option_sets.append((len(candidates), j, candidates))
        if len(option_sets) == ZERO:
            return
        option_sets.sort()
        _, chosen, candidates = option_sets[ZERO]
        next_remaining = tuple(idx for idx in remaining if idx != chosen)
        for _, _, _, _, row, col in candidates:
            placements[chosen] = (row, col)
            rec(placements, next_remaining)
            del placements[chosen]

    for start in range(n):
        rec({start: (ZERO, ZERO)}, tuple(idx for idx in range(n) if idx != start))
    if best_grid is None:
        raise ValueError("unable to assemble fragments")
    return best_grid


def _rotations_4e34c42c(
    grid: Grid,
) -> tuple[Grid, ...]:
    out = [grid]
    for _ in range(THREE):
        out.append(rot90(out[-ONE]))
    return tuple(out)


def _instantiate_motif_4e34c42c(
    template: Grid,
    bg: Integer,
) -> Grid:
    labels = tuple(sorted({value for row in template for value in row if value != ZERO}))
    colors = sample(tuple(color for color in range(ONE, TEN) if color != bg), len(labels))
    mapping = {ZERO: bg}
    for label, color in zip(labels, colors):
        mapping[label] = color
    return tuple(tuple(mapping[value] for value in row) for row in template)


def _non_bg_indices_4e34c42c(
    grid: Grid,
    bg: Integer,
) -> tuple[tuple[int, int], ...]:
    return tuple(
        (i, j)
        for i, row in enumerate(grid)
        for j, value in enumerate(row)
        if value != bg
    )


def _connected_non_bg_4e34c42c(
    grid: Grid,
    bg: Integer,
) -> bool:
    cells = set(_non_bg_indices_4e34c42c(grid, bg))
    if len(cells) == ZERO:
        return False
    stack = [next(iter(cells))]
    seen = set()
    while len(stack) > ZERO:
        cell = stack.pop()
        if cell in seen:
            continue
        seen.add(cell)
        i, j = cell
        for nei in ((i - ONE, j), (i + ONE, j), (i, j - ONE), (i, j + ONE)):
            if nei in cells and nei not in seen:
                stack.append(nei)
    return seen == cells


def _paint_motif_4e34c42c(
    canvas_grid: list[list[int]],
    motif: Grid,
    top: Integer,
    left: Integer,
    bg: Integer,
) -> bool:
    h = len(motif)
    w = len(motif[ZERO])
    for i in range(h):
        for j in range(w):
            value = motif[i][j]
            if value == bg:
                continue
            if canvas_grid[top + i][left + j] != bg:
                return False
    for i in range(h):
        for j in range(w):
            value = motif[i][j]
            if value != bg:
                canvas_grid[top + i][left + j] = value
    return True


def _touches_previous_4e34c42c(
    prev_cells: tuple[tuple[int, int], ...],
    motif: Grid,
    top: Integer,
    left: Integer,
    bg: Integer,
) -> bool:
    placed = {(top + i, left + j) for i, j in _non_bg_indices_4e34c42c(motif, bg)}
    prev = set(prev_cells)
    for i, j in placed:
        if (i - ONE, j) in prev or (i + ONE, j) in prev or (i, j - ONE) in prev or (i, j + ONE) in prev:
            return True
    return False


def _crop_grid_4e34c42c(
    grid: Grid,
    top: Integer,
    left: Integer,
    height0: Integer,
    width0: Integer,
) -> Grid:
    return tuple(tuple(row[left:left + width0]) for row in grid[top:top + height0])


def _place_motif_chain_4e34c42c(
    diff_lb: float,
    diff_ub: float,
) -> tuple[Integer, Grid, tuple[tuple[int, int, int, int], ...]]:
    bg = choice(tuple(range(TEN)))
    motif_count = unifint(diff_lb, diff_ub, (FOUR, FIVE))
    work_h = 30
    work_w = 30
    canvas_grid = [[bg for _ in range(work_w)] for _ in range(work_h)]
    motif_boxes = []
    prev_cells: tuple[tuple[int, int], ...] | None = None
    for idx in range(motif_count):
        for _ in range(200):
            motif = _instantiate_motif_4e34c42c(choice(MOTIF_TEMPLATES_4E34C42C), bg)
            motif = choice(_rotations_4e34c42c(motif))
            h = len(motif)
            w = len(motif[ZERO])
            if idx == ZERO:
                top = randint(EIGHT, 12)
                left = randint(EIGHT, 12)
            else:
                prev_box = motif_boxes[-ONE]
                min_top = max(ZERO, prev_box[ZERO] - h - TWO)
                max_top = min(work_h - h, prev_box[TWO] + TWO)
                min_left = max(ZERO, prev_box[ONE] - w - TWO)
                max_left = min(work_w - w, prev_box[THREE] + TWO)
                if min_top > max_top or min_left > max_left:
                    continue
                top = randint(min_top, max_top)
                left = randint(min_left, max_left)
            if not _touches_previous_4e34c42c(prev_cells or tuple(), motif, top, left, bg) and idx != ZERO:
                continue
            snapshot = [row[:] for row in canvas_grid]
            if not _paint_motif_4e34c42c(canvas_grid, motif, top, left, bg):
                canvas_grid = snapshot
                continue
            box = (top, left, top + h - ONE, left + w - ONE)
            motif_boxes.append(box)
            prev_cells = tuple((top + i, left + j) for i, j in _non_bg_indices_4e34c42c(motif, bg))
            break
        else:
            raise ValueError("failed to place motif chain")
    rows = tuple(i for i, row in enumerate(canvas_grid) for value in row if value != bg)
    cols = tuple(j for row in canvas_grid for j, value in enumerate(row) if value != bg)
    top_margin = randint(ZERO, ONE)
    left_margin = randint(ZERO, ONE)
    bottom_margin = randint(ZERO, ONE)
    right_margin = randint(ZERO, ONE)
    r0 = max(ZERO, min(rows) - top_margin)
    c0 = max(ZERO, min(cols) - left_margin)
    r1 = min(work_h - ONE, max(rows) + bottom_margin)
    c1 = min(work_w - ONE, max(cols) + right_margin)
    go = _crop_grid_4e34c42c(tuple(tuple(row) for row in canvas_grid), r0, c0, r1 - r0 + ONE, c1 - c0 + ONE)
    shifted_boxes = tuple((top - r0, left - c0, bottom - r0, right - c0) for top, left, bottom, right in motif_boxes)
    return bg, go, shifted_boxes


def _window_from_boxes_4e34c42c(
    grid: Grid,
    boxes: tuple[tuple[int, int, int, int], ...],
    indices: tuple[int, ...],
) -> Grid:
    tops = tuple(boxes[idx][ZERO] for idx in indices)
    lefts = tuple(boxes[idx][ONE] for idx in indices)
    bottoms = tuple(boxes[idx][TWO] for idx in indices)
    rights = tuple(boxes[idx][THREE] for idx in indices)
    top = max(ZERO, min(tops) - randint(ZERO, ONE))
    left = max(ZERO, min(lefts) - randint(ZERO, ONE))
    bottom = min(len(grid) - ONE, max(bottoms) + randint(ZERO, ONE))
    right = min(len(grid[ZERO]) - ONE, max(rights) + randint(ZERO, ONE))
    return _crop_grid_4e34c42c(grid, top, left, bottom - top + ONE, right - left + ONE)


def _fragment_windows_4e34c42c(
    bg: Integer,
    output_grid: Grid,
    motif_boxes: tuple[tuple[int, int, int, int], ...],
) -> tuple[Grid, ...]:
    motifs = len(motif_boxes)
    windows = []
    for idx in range(motifs - ONE):
        windows.append(_window_from_boxes_4e34c42c(output_grid, motif_boxes, (idx, idx + ONE)))
    if motifs >= FOUR and uniform(0.0, 1.0) < 0.7:
        pick = randint(ONE, motifs - TWO)
        windows.append(_window_from_boxes_4e34c42c(output_grid, motif_boxes, (pick,)))
    if motifs >= FIVE and uniform(0.0, 1.0) < 0.5:
        pick = randint(ZERO, motifs - THREE)
        windows.append(_window_from_boxes_4e34c42c(output_grid, motif_boxes, (pick, pick + ONE, pick + TWO)))
    deduped = []
    seen = set()
    for window in windows:
        if window in seen:
            continue
        if not _connected_non_bg_4e34c42c(window, bg):
            continue
        seen.add(window)
        deduped.append(window)
    return tuple(deduped)


def _scatter_fragments_4e34c42c(
    bg: Integer,
    fragments: tuple[Grid, ...],
    diff_lb: float,
    diff_ub: float,
) -> Grid:
    max_h = max(len(fragment) for fragment in fragments)
    max_w = max(len(fragment[ZERO]) for fragment in fragments)
    h = unifint(diff_lb, diff_ub, (max(26, max_h + 16), 30))
    w = unifint(diff_lb, diff_ub, (max(26, max_w + 16), 30))
    ordered = order(fragments, lambda piece: (-len(piece) * len(piece[ZERO]), -len(piece), -len(piece[ZERO])))
    for _ in range(12):
        canvas_grid = [[bg for _ in range(w)] for _ in range(h)]
        rectangles = []
        failed = False
        for fragment in ordered:
            fh = len(fragment)
            fw = len(fragment[ZERO])
            placed = False
            for _ in range(600):
                top = randint(ZERO, h - fh)
                left = randint(ZERO, w - fw)
                rect = (top - ONE, left - ONE, top + fh, left + fw)
                if any(
                    not (
                        rect[TWO] < other[ZERO]
                        or rect[ZERO] > other[TWO]
                        or rect[THREE] < other[ONE]
                        or rect[ONE] > other[THREE]
                    )
                    for other in rectangles
                ):
                    continue
                for i in range(fh):
                    for j in range(fw):
                        canvas_grid[top + i][left + j] = fragment[i][j]
                rectangles.append((top, left, top + fh - ONE, left + fw - ONE))
                placed = True
                break
            if not placed:
                failed = True
                break
        if not failed:
            return tuple(tuple(row) for row in canvas_grid)
    raise ValueError("failed to scatter fragments")


TWENTY = 20
TWENTY_FIVE = 25


def build_example_4e34c42c(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        try:
            bg, output_grid, motif_boxes = _place_motif_chain_4e34c42c(diff_lb, diff_ub)
            fragments = _fragment_windows_4e34c42c(bg, output_grid, motif_boxes)
            input_grid = _scatter_fragments_4e34c42c(bg, fragments, diff_lb, diff_ub)
        except ValueError:
            continue
        if len(fragments) < THREE:
            continue
        if extract_fragments_4e34c42c(input_grid)[ONE] == (output_grid,):
            continue
        try:
            assembled = assemble_fragments_4e34c42c(bg, fragments)
        except ValueError:
            continue
        if assembled != output_grid:
            continue
        return {"input": input_grid, "output": output_grid}
