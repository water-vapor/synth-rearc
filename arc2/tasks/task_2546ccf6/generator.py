from itertools import combinations

from arc2.core import *

from .helpers import (
    build_lattice_2546ccf6,
    cell_layout_2546ccf6,
    paint_cell_patch_2546ccf6,
    rot180_patch_2546ccf6,
)
from .verifier import verify_2546ccf6


CELL_HEIGHT_BOUNDS_2546ccf6 = (FOUR, FIVE)
CELL_WIDTH_BOUNDS_2546ccf6 = (FOUR, FIVE)
ROW_COUNT_CHOICES_2546ccf6 = (FOUR, FOUR, FIVE)
COL_COUNT_2546ccf6 = FOUR
SEPARATOR_COLORS_2546ccf6 = (ONE, TWO, THREE, FOUR, FIVE, SIX, SEVEN, EIGHT, NINE)
BLOCK_COUNT_BOUNDS_2546ccf6 = (ONE, THREE)
OFFSETS_2546ccf6 = (
    (ZERO, ZERO),
    (ZERO, ONE),
    (ONE, ZERO),
    (ONE, ONE),
)


def _neighbors8_2546ccf6(
    cell: tuple[Integer, Integer],
    height_value: Integer,
    width_value: Integer,
) -> tuple[tuple[Integer, Integer], ...]:
    i, j = cell
    neighbors = []
    for di in (-ONE, ZERO, ONE):
        for dj in (-ONE, ZERO, ONE):
            if di == ZERO and dj == ZERO:
                continue
            ni = add(i, di)
            nj = add(j, dj)
            if 0 <= ni < height_value and 0 <= nj < width_value:
                neighbors.append((ni, nj))
    return tuple(neighbors)


def _connected8_2546ccf6(
    patch: frozenset[tuple[Integer, Integer]],
    height_value: Integer,
    width_value: Integer,
) -> Boolean:
    if len(patch) == ZERO:
        return F
    frontier = [next(iter(patch))]
    seen = {frontier[ZERO]}
    while frontier:
        cell = frontier.pop()
        for neighbor in _neighbors8_2546ccf6(cell, height_value, width_value):
            if neighbor in patch and neighbor not in seen:
                seen.add(neighbor)
                frontier.append(neighbor)
    return len(seen) == len(patch)


def _patch_ok_2546ccf6(
    patch: frozenset[tuple[Integer, Integer]],
    height_value: Integer,
    width_value: Integer,
) -> Boolean:
    rows = {i for i, _ in patch}
    cols = {j for _, j in patch}
    area = multiply(height_value, width_value)
    x0 = rot180_patch_2546ccf6(height_value, width_value, patch)
    return (
        len(patch) >= THREE
        and len(patch) < area
        and len(rows) > ONE
        and len(cols) > ONE
        and patch != x0
        and _connected8_2546ccf6(patch, height_value, width_value)
    )


def _make_patch_2546ccf6(
    height_value: Integer,
    width_value: Integer,
) -> frozenset[tuple[Integer, Integer]]:
    x0 = max(FOUR, divide(multiply(height_value, width_value), THREE))
    while True:
        target = randint(THREE, x0)
        seed = (randint(ZERO, decrement(height_value)), randint(ZERO, decrement(width_value)))
        cells = {seed}
        while len(cells) < target:
            frontier = tuple(
                neighbor
                for cell in tuple(cells)
                for neighbor in _neighbors8_2546ccf6(cell, height_value, width_value)
                if neighbor not in cells
            )
            if len(frontier) == ZERO:
                break
            cells.add(choice(frontier))
        patch = frozenset(cells)
        if _patch_ok_2546ccf6(patch, height_value, width_value):
            return patch


def _make_block_patches_2546ccf6(
    height_value: Integer,
    width_value: Integer,
) -> tuple[frozenset[tuple[Integer, Integer]], frozenset[tuple[Integer, Integer]]]:
    while True:
        x0 = _make_patch_2546ccf6(height_value, width_value)
        x1 = _make_patch_2546ccf6(height_value, width_value)
        if x1 not in (x0, rot180_patch_2546ccf6(height_value, width_value, x0)):
            return x0, x1


def _block_cells_2546ccf6(
    row_index: Integer,
    col_index: Integer,
) -> frozenset[tuple[Integer, Integer]]:
    return frozenset(
        {
            (row_index, col_index),
            (row_index, increment(col_index)),
            (increment(row_index), col_index),
            (increment(row_index), increment(col_index)),
        }
    )


def _disjoint_blocks_2546ccf6(
    blocks: tuple[tuple[Integer, Integer], ...],
) -> Boolean:
    occupied = frozenset({})
    for row_index, col_index in blocks:
        cells = _block_cells_2546ccf6(row_index, col_index)
        if len(intersection(occupied, cells)) > ZERO:
            return F
        occupied = combine(occupied, cells)
    return T


def _sample_blocks_2546ccf6(
    diff_lb: float,
    diff_ub: float,
    usable_rows: Integer,
    usable_cols: Integer,
) -> tuple[tuple[Integer, Integer], ...]:
    candidates = tuple(
        (row_index, col_index)
        for row_index in range(subtract(usable_rows, ONE))
        for col_index in range(subtract(usable_cols, ONE))
    )
    x0 = min(BLOCK_COUNT_BOUNDS_2546ccf6[ONE], len(candidates))
    for size_value in range(x0, ZERO, NEG_ONE):
        valid = tuple(combo for combo in combinations(candidates, size_value) if _disjoint_blocks_2546ccf6(combo))
        if len(valid) == ZERO:
            continue
        target = unifint(diff_lb, diff_ub, (ONE, size_value))
        x1 = tuple(combo for combo in combinations(candidates, target) if _disjoint_blocks_2546ccf6(combo))
        return choice(x1)
    return (choice(candidates),)


def _row_heights_2546ccf6(
    diff_lb: float,
    diff_ub: float,
) -> tuple[Integer, ...]:
    x0 = unifint(diff_lb, diff_ub, CELL_HEIGHT_BOUNDS_2546ccf6)
    x1 = choice(ROW_COUNT_CHOICES_2546ccf6)
    if x1 == FIVE:
        x2 = randint(TWO, decrement(x0))
    else:
        x2 = x0 if choice((T, F)) else randint(TWO, decrement(x0))
    return tuple([x0] * subtract(x1, ONE) + [x2])


def _col_widths_2546ccf6(
    diff_lb: float,
    diff_ub: float,
) -> tuple[Integer, ...]:
    x0 = unifint(diff_lb, diff_ub, CELL_WIDTH_BOUNDS_2546ccf6)
    x1 = x0 if choice((T, T, F)) else randint(TWO, decrement(x0))
    return (x0, x0, x0, x1)


def _usable_count_2546ccf6(
    lengths: tuple[Integer, ...],
) -> Integer:
    return len(lengths) if equality(last(lengths), first(lengths)) else subtract(len(lengths), ONE)


def generate_2546ccf6(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        row_heights = _row_heights_2546ccf6(diff_lb, diff_ub)
        col_widths = _col_widths_2546ccf6(diff_lb, diff_ub)
        usable_rows = _usable_count_2546ccf6(row_heights)
        usable_cols = _usable_count_2546ccf6(col_widths)
        if usable_rows < THREE or usable_cols < THREE:
            continue
        separator_color = choice(SEPARATOR_COLORS_2546ccf6)
        gi = build_lattice_2546ccf6(row_heights, col_widths, separator_color)
        go = gi
        row_spans, col_spans, _ = cell_layout_2546ccf6(gi)
        blocks = _sample_blocks_2546ccf6(diff_lb, diff_ub, usable_rows, usable_cols)
        block_colors = sample(tuple(value for value in SEPARATOR_COLORS_2546ccf6 if value != separator_color), len(blocks))
        for (row_index, col_index), color_value in zip(blocks, block_colors):
            height_value = subtract(row_spans[row_index][ONE], row_spans[row_index][ZERO])
            width_value = subtract(col_spans[col_index][ONE], col_spans[col_index][ZERO])
            x0, x1 = _make_block_patches_2546ccf6(height_value, width_value)
            x2 = rot180_patch_2546ccf6(height_value, width_value, x1)
            x3 = rot180_patch_2546ccf6(height_value, width_value, x0)
            x4 = (x0, x1, x2, x3)
            x5 = randint(ZERO, THREE)
            for patch_index, patch in enumerate(x4):
                di, dj = OFFSETS_2546ccf6[patch_index]
                go = paint_cell_patch_2546ccf6(go, row_spans, col_spans, add(row_index, di), add(col_index, dj), color_value, patch)
                if patch_index != x5:
                    gi = paint_cell_patch_2546ccf6(gi, row_spans, col_spans, add(row_index, di), add(col_index, dj), color_value, patch)
        if gi == go:
            continue
        if verify_2546ccf6(gi) != go:
            continue
        return {"input": gi, "output": go}
