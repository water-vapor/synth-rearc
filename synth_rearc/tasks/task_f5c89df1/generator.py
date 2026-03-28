from synth_rearc.core import *

from .verifier import verify_f5c89df1


GRID_SHAPE_F5C89DF1 = (13, 13)
ACTIVE_MARGIN_F5C89DF1 = TWO
BLUE_BBOXES_F5C89DF1 = (
    (THREE, THREE),
    (THREE, FOUR),
    (FOUR, THREE),
    (FOUR, FOUR),
    (FOUR, FIVE),
    (FIVE, FOUR),
    (FIVE, FIVE),
)


def _neighbors8_f5c89df1(
    cell: tuple[int, int],
    dims: tuple[int, int],
) -> tuple[tuple[int, int], ...]:
    i, j = cell
    h, w = dims
    out = []
    for di in (NEG_ONE, ZERO, ONE):
        for dj in (NEG_ONE, ZERO, ONE):
            if di == ZERO and dj == ZERO:
                continue
            ni = i + di
            nj = j + dj
            if 0 <= ni < h and 0 <= nj < w:
                out.append((ni, nj))
    return tuple(out)


def _connected8_f5c89df1(cells: frozenset[tuple[int, int]]) -> bool:
    if len(cells) == ZERO:
        return F
    start = next(iter(cells))
    seen = {start}
    stack = [start]
    while len(stack) > ZERO:
        cell = stack.pop()
        i, j = cell
        for di in (NEG_ONE, ZERO, ONE):
            for dj in (NEG_ONE, ZERO, ONE):
                if di == ZERO and dj == ZERO:
                    continue
                neigh = (i + di, j + dj)
                if neigh in cells and neigh not in seen:
                    seen.add(neigh)
                    stack.append(neigh)
    return len(seen) == len(cells)


def _synthesize_blue_offsets_f5c89df1(
    diff_lb: float,
    diff_ub: float,
) -> frozenset[tuple[int, int]]:
    for _ in range(300):
        box_h, box_w = choice(BLUE_BBOXES_F5C89DF1)
        anchor_candidates = tuple(
            (i, j)
            for i in range(box_h)
            for j in range(box_w)
            if 0 < j < box_w - ONE and 0 < i < box_h
        )
        anchor = choice(anchor_candidates)
        area = box_h * box_w
        target = unifint(diff_lb, diff_ub, (FIVE, min(15, area)))
        occupied = {anchor}
        while len(occupied) < target:
            frontier = set()
            for cell in occupied:
                frontier.update(
                    neigh
                    for neigh in _neighbors8_f5c89df1(cell, (box_h, box_w))
                    if neigh not in occupied
                )
            if len(frontier) == ZERO:
                break
            occupied.add(choice(tuple(frontier)))
        if len(occupied) < FIVE:
            continue
        max_cutouts = min(THREE, len(occupied) - FIVE)
        if max_cutouts > ZERO:
            ncutouts = unifint(diff_lb, diff_ub, (ZERO, max_cutouts))
            removable = [cell for cell in occupied if cell != anchor]
            shuffle(removable)
            for cell in removable:
                if ncutouts == ZERO:
                    break
                candidate = frozenset(occupied - {cell})
                if _connected8_f5c89df1(candidate):
                    occupied.remove(cell)
                    ncutouts -= ONE
        if height(occupied) < THREE or width(occupied) < THREE:
            continue
        blue = frozenset(
            (i - anchor[ZERO], j - anchor[ONE])
            for i, j in occupied
            if (i, j) != anchor
        )
        if len(blue) < FOUR:
            continue
        if not any(max(abs(i), abs(j)) > ONE for i, j in blue):
            continue
        return blue
    raise RuntimeError("failed to synthesize blue motif")


def _legal_anchor_positions_f5c89df1(
    blue_offsets: frozenset[tuple[int, int]],
) -> tuple[tuple[int, int], ...]:
    rows = (ZERO,) + tuple(i for i, _ in blue_offsets)
    cols = (ZERO,) + tuple(j for _, j in blue_offsets)
    h, w = GRID_SHAPE_F5C89DF1
    row_lo = ACTIVE_MARGIN_F5C89DF1 - minimum(rows)
    row_hi = h - ONE - ACTIVE_MARGIN_F5C89DF1 - maximum(rows)
    col_lo = ACTIVE_MARGIN_F5C89DF1 - minimum(cols)
    col_hi = w - ONE - ACTIVE_MARGIN_F5C89DF1 - maximum(cols)
    return tuple(
        (i, j)
        for i in range(row_lo, row_hi + ONE)
        for j in range(col_lo, col_hi + ONE)
    )


def _corner_targets_f5c89df1(
    source_anchor: tuple[int, int],
    usable: frozenset[tuple[int, int]],
) -> tuple[tuple[int, int], ...]:
    si, sj = source_anchor
    options = []
    for di in range(ONE, FIVE):
        for dj in range(ONE, FIVE):
            upper = ((si - di, sj - dj), (si - di, sj + dj))
            lower = ((si + di, sj - dj), (si + di, sj + dj))
            full = upper + lower
            if all(pos in usable for pos in full):
                options.append(full)
            if all(pos in usable for pos in upper):
                options.append(upper)
            if all(pos in usable for pos in lower):
                options.append(lower)
    if len(options) == ZERO:
        return ()
    four_sets = tuple(option for option in options if len(option) == FOUR)
    if len(four_sets) > ZERO and choice((T, T, F)):
        return choice(four_sets)
    return choice(tuple(options))


def _axis_targets_f5c89df1(
    source_anchor: tuple[int, int],
    usable: frozenset[tuple[int, int]],
) -> tuple[tuple[int, int], ...]:
    si, sj = source_anchor
    horizontal = tuple(sorted(pos for pos in usable if pos[ZERO] == si))
    vertical = tuple(sorted(pos for pos in usable if pos[ONE] == sj))
    modes = []
    if len(horizontal) > ZERO:
        modes.append(horizontal)
    if len(vertical) > ZERO:
        modes.append(vertical)
    if len(modes) == ZERO:
        return ()
    candidates = choice(tuple(modes))
    if candidates[ZERO][ZERO] == si:
        before = tuple(pos for pos in candidates if pos[ONE] < sj)
        after = tuple(pos for pos in candidates if pos[ONE] > sj)
    else:
        before = tuple(pos for pos in candidates if pos[ZERO] < si)
        after = tuple(pos for pos in candidates if pos[ZERO] > si)
    if len(before) > ZERO and len(after) > ZERO and choice((T, T, F)):
        picked = {choice(before), choice(after)}
        if len(candidates) >= THREE and choice((T, F, F)):
            extras = tuple(pos for pos in candidates if pos not in picked)
            if len(extras) > ZERO:
                picked.add(choice(extras))
        return tuple(sorted(picked))
    ntargets = min(len(candidates), choice((ONE, TWO, TWO, THREE)))
    return tuple(sorted(sample(candidates, ntargets)))


def _free_targets_f5c89df1(
    usable: frozenset[tuple[int, int]],
    diff_lb: float,
    diff_ub: float,
) -> tuple[tuple[int, int], ...]:
    candidates = tuple(sorted(usable))
    ntargets = unifint(diff_lb, diff_ub, (ONE, min(FOUR, len(candidates))))
    return tuple(sorted(sample(candidates, ntargets)))


def _choose_targets_f5c89df1(
    source_anchor: tuple[int, int],
    source_blue: frozenset[tuple[int, int]],
    legal_anchors: tuple[tuple[int, int], ...],
    diff_lb: float,
    diff_ub: float,
) -> tuple[tuple[int, int], ...]:
    blocked = set(source_blue)
    blocked.add(source_anchor)
    usable = frozenset(pos for pos in legal_anchors if pos not in blocked)
    if len(usable) == ZERO:
        return ()
    modes = [
        lambda: _axis_targets_f5c89df1(source_anchor, usable),
        lambda: _corner_targets_f5c89df1(source_anchor, usable),
        lambda: _free_targets_f5c89df1(usable, diff_lb, diff_ub),
    ]
    shuffle(modes)
    for mode in modes:
        targets = mode()
        if len(targets) > ZERO:
            return targets
    return ()


def generate_f5c89df1(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        blue_offsets = _synthesize_blue_offsets_f5c89df1(diff_lb, diff_ub)
        legal_anchors = _legal_anchor_positions_f5c89df1(blue_offsets)
        if len(legal_anchors) < TWO:
            continue
        source_anchor = choice(legal_anchors)
        source_blue = shift(blue_offsets, source_anchor)
        targets = _choose_targets_f5c89df1(
            source_anchor,
            source_blue,
            legal_anchors,
            diff_lb,
            diff_ub,
        )
        if len(targets) == ZERO:
            continue
        target_sets = apply(lbind(shift, blue_offsets), frozenset(targets))
        output_blue = merge(target_sets)
        gi = canvas(ZERO, GRID_SHAPE_F5C89DF1)
        gi = fill(gi, EIGHT, source_blue)
        gi = fill(gi, TWO, frozenset(targets))
        gi = fill(gi, THREE, initset(source_anchor))
        go = canvas(ZERO, GRID_SHAPE_F5C89DF1)
        go = fill(go, EIGHT, output_blue)
        if verify_f5c89df1(gi) != go:
            continue
        return {"input": gi, "output": go}
