from arc2.core import *

from .helpers import (
    INPUT_COLORS_6165EA8F,
    render_table_6165ea8f,
    shape_signature_6165ea8f,
    transform_patch_6165ea8f,
)
from .verifier import verify_6165ea8f


def _free_neighbors_6165ea8f(
    loc: IntegerTuple,
    occupied: set[IntegerTuple],
    h: Integer,
    w: Integer,
) -> tuple[IntegerTuple, ...]:
    return tuple(
        (i, j)
        for i, j in dneighbors(loc)
        if 0 <= i < h and 0 <= j < w and (i, j) not in occupied
    )


def _random_sparse_shape_6165ea8f(
    diff_lb: float,
    diff_ub: float,
) -> tuple[Indices, tuple[IntegerTuple, ...]]:
    for _ in range(200):
        h = randint(3, 6)
        w = randint(3, 6)
        max_cells = min(h * w - ONE, 12)
        min_cells = max(5, min(h + w - ONE, max_cells))
        if min_cells > max_cells:
            continue
        ncells = unifint(diff_lb, diff_ub, (min_cells, max_cells))
        start = (randint(ZERO, h - ONE), randint(ZERO, w - ONE))
        path = [start]
        occupied = {start}
        spine_goal = randint(max(4, ncells - 3), ncells)
        while len(path) < spine_goal:
            cands = _free_neighbors_6165ea8f(path[-ONE], occupied, h, w)
            if len(cands) == ZERO:
                break
            nxt = choice(cands)
            path.append(nxt)
            occupied.add(nxt)
        if len(occupied) < max(4, ncells - 4):
            continue
        while len(occupied) < ncells:
            branch_sources = [cell for cell in occupied if _free_neighbors_6165ea8f(cell, occupied, h, w)]
            if len(branch_sources) == ZERO:
                break
            src = choice(branch_sources)
            nxt = choice(_free_neighbors_6165ea8f(src, occupied, h, w))
            occupied.add(nxt)
        patch = frozenset(normalize(frozenset(occupied)))
        if len(patch) != ncells:
            continue
        if height(patch) < THREE or width(patch) < THREE:
            continue
        area = height(patch) * width(patch)
        if area == len(patch) or area > len(patch) * THREE:
            continue
        if hline(patch) or vline(patch):
            continue
        sig = shape_signature_6165ea8f(patch)
        return patch, sig
    raise ValueError("unable to sample a sparse connected shape for 6165ea8f")


def _class_sizes_6165ea8f(
    ncolors: Integer,
) -> tuple[Integer, ...]:
    nclasses = randint(max(2, ncolors - 3), min(4, ncolors - ONE))
    sizes = [ONE] * nclasses
    remaining = ncolors - nclasses
    while remaining > ZERO:
        cands = [idx for idx, size_value in enumerate(sizes) if size_value < THREE]
        idx = choice(cands)
        sizes[idx] += ONE
        remaining -= ONE
    shuffle(sizes)
    return tuple(sizes)


def _dilate_patch_6165ea8f(
    patch: Patch,
) -> frozenset[IntegerTuple]:
    return frozenset(
        (i + di, j + dj)
        for i, j in toindices(patch)
        for di in (-ONE, ZERO, ONE)
        for dj in (-ONE, ZERO, ONE)
    )


def _place_shapes_6165ea8f(
    items: tuple[tuple[Integer, Indices], ...],
    h: Integer,
    w: Integer,
) -> dict[Integer, Indices] | None:
    usable_w = w - TWO
    ordered = sorted(
        items,
        key=lambda item: (height(item[ONE]) * width(item[ONE]), len(item[ONE])),
        reverse=True,
    )
    placed = {}
    forbidden = set()
    for value, patch in ordered:
        ph = height(patch)
        pw = width(patch)
        cands = [
            (top, left)
            for top in range(h - ph + ONE)
            for left in range(usable_w - pw + ONE)
        ]
        shuffle(cands)
        success = False
        for top, left in cands:
            shifted = shift(patch, (top, left))
            cells = toindices(shifted)
            if any(cell in forbidden for cell in cells):
                continue
            placed[value] = shifted
            forbidden |= _dilate_patch_6165ea8f(shifted)
            success = True
            break
        if not success:
            return None
    return placed


def _compose_input_6165ea8f(
    order: tuple[Integer, ...],
    placed: dict[Integer, Indices],
    h: Integer,
    w: Integer,
) -> Grid:
    grid = canvas(ZERO, (h, w))
    for value, patch in placed.items():
        grid = fill(grid, value, patch)
    for idx, value in enumerate(order):
        grid = fill(grid, value, frozenset({(idx, w - ONE)}))
    return grid


def generate_6165ea8f(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        ncolors = unifint(diff_lb, diff_ub, (4, 7))
        colors = list(sample(INPUT_COLORS_6165EA8F, ncolors))
        class_sizes = _class_sizes_6165ea8f(ncolors)
        bases = []
        seen = set()
        while len(bases) < len(class_sizes):
            patch, sig = _random_sparse_shape_6165ea8f(diff_lb, diff_ub)
            if sig in seen:
                continue
            seen.add(sig)
            bases.append((patch, sig))
        members = []
        color_idx = ZERO
        for class_size, (base_patch, sig) in zip(class_sizes, bases):
            for _ in range(class_size):
                value = colors[color_idx]
                color_idx += ONE
                turns = randint(ZERO, THREE)
                mirrored = bool(randint(ZERO, ONE))
                patch = transform_patch_6165ea8f(base_patch, turns, mirrored)
                members.append((value, patch, sig))
        shuffle(members)
        h = unifint(diff_lb, diff_ub, (20, 28))
        w = unifint(diff_lb, diff_ub, (20, 29))
        placed = _place_shapes_6165ea8f(
            tuple((value, patch) for value, patch, _ in members),
            h,
            w,
        )
        if placed is None:
            continue
        order = tuple(value for value, _, _ in members)
        signatures = tuple(sig for _, _, sig in members)
        gi = _compose_input_6165ea8f(order, placed, h, w)
        go = render_table_6165ea8f(order, signatures)
        if verify_6165ea8f(gi) != go:
            continue
        return {"input": gi, "output": go}
