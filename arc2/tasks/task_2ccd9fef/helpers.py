from functools import reduce
from math import gcd

from arc2.core import *


ANCHORS_2CCD9FEF = ("tl", "tr", "bl", "br")


def _palette_2ccd9fef(grid: Grid) -> frozenset[int]:
    return frozenset(value for row in grid for value in row)


def _cells_of_color_2ccd9fef(grid: Grid, value: Integer) -> frozenset[IntegerTuple]:
    return frozenset(
        (i, j)
        for i, row in enumerate(grid)
        for j, cell in enumerate(row)
        if cell == value
    )


def _bbox_2ccd9fef(patch: Patch) -> tuple[int, int, int, int]:
    rows = [i for i, _ in patch]
    cols = [j for _, j in patch]
    return (min(rows), min(cols), max(rows), max(cols))


def _split_candidate_blocks_2ccd9fef(grid: Grid) -> list[tuple[str, tuple[Grid, ...]]]:
    h, w = shape(grid)
    candidates = []
    for block_h in range(2, h + 1):
        if h % block_h == 0 and h // block_h >= 3:
            blocks = tuple(crop(grid, (block_h * idx, 0), (block_h, w)) for idx in range(h // block_h))
            candidates.append(("vertical", blocks))
    for block_w in range(2, w + 1):
        if w % block_w == 0 and w // block_w >= 3:
            blocks = tuple(crop(grid, (0, block_w * idx), (h, block_w)) for idx in range(w // block_w))
            candidates.append(("horizontal", blocks))
    return candidates


def _validate_split_2ccd9fef(
    blocks: tuple[Grid, ...],
) -> tuple[int, frozenset[int]] | None:
    palettes = tuple(_palette_2ccd9fef(block) for block in blocks)
    blank_idx = min(range(len(blocks)), key=lambda idx: (len(palettes[idx]), idx))
    blank_palette = palettes[blank_idx]
    blank = blocks[blank_idx]
    nsignal = 0
    for block, palette_value in zip(blocks, palettes):
        if not blank_palette.issubset(palette_value):
            return None
        if palette_value != blank_palette:
            nsignal += 1
        for i, row in enumerate(block):
            for j, value in enumerate(row):
                if value != blank[i][j] and value in blank_palette:
                    return None
    if nsignal < 2:
        return None
    return blank_idx, blank_palette


def split_blocks_2ccd9fef(
    grid: Grid,
) -> tuple[str, tuple[Grid, ...], int, frozenset[int]]:
    candidates = []
    for orientation, blocks in _split_candidate_blocks_2ccd9fef(grid):
        validation = _validate_split_2ccd9fef(blocks)
        if validation is None:
            continue
        blank_idx, blank_palette = validation
        block_area = height(first(blocks)) * width(first(blocks))
        candidates.append((block_area, orientation, blocks, blank_idx, blank_palette))
    if not candidates:
        raise ValueError("unable to split 2ccd9fef input into repeated panels")
    _, orientation, blocks, blank_idx, blank_palette = max(candidates, key=first)
    return orientation, blocks, blank_idx, blank_palette


def compose_blocks_2ccd9fef(blocks: tuple[Grid, ...], orientation: str) -> Grid:
    if orientation == "vertical":
        return tuple(row for block in blocks for row in block)
    return tuple(
        tuple(value for block in blocks for value in block[i])
        for i in range(len(first(blocks)))
    )


def _anchorize_patch_2ccd9fef(
    patch: Patch,
    box: tuple[int, int, int, int],
    anchor: str,
) -> frozenset[IntegerTuple]:
    top, left, bottom, right = box
    if anchor == "tl":
        return frozenset((i - top, j - left) for i, j in patch)
    if anchor == "tr":
        return frozenset((i - top, right - j) for i, j in patch)
    if anchor == "bl":
        return frozenset((bottom - i, j - left) for i, j in patch)
    return frozenset((bottom - i, right - j) for i, j in patch)


def _deanchor_patch_2ccd9fef(
    patch: Patch,
    box: tuple[int, int, int, int],
    anchor: str,
) -> frozenset[IntegerTuple]:
    top, left, bottom, right = box
    if anchor == "tl":
        return frozenset((top + i, left + j) for i, j in patch)
    if anchor == "tr":
        return frozenset((top + i, right - j) for i, j in patch)
    if anchor == "bl":
        return frozenset((bottom - i, left + j) for i, j in patch)
    return frozenset((bottom - i, right - j) for i, j in patch)


def _anchored_dims_2ccd9fef(patch: Patch) -> tuple[int, int]:
    rows = [i for i, _ in patch]
    cols = [j for _, j in patch]
    return (max(rows) + 1, max(cols) + 1)


def _choose_anchor_2ccd9fef(
    sequence: tuple[tuple[int, frozenset[IntegerTuple], tuple[int, int, int, int]], ...],
) -> str:
    for anchor in ANCHORS_2CCD9FEF:
        previous = None
        valid = True
        for _, patch, box in sequence:
            anchored = _anchorize_patch_2ccd9fef(patch, box, anchor)
            if previous is not None and not previous.issubset(anchored):
                valid = False
                break
            previous = anchored
        if valid:
            return anchor
    best_anchor = "tl"
    best_score = -1
    _, patch_a, box_a = sequence[-2]
    _, patch_b, box_b = sequence[-1]
    for anchor in ANCHORS_2CCD9FEF:
        anchored_a = _anchorize_patch_2ccd9fef(patch_a, box_a, anchor)
        anchored_b = _anchorize_patch_2ccd9fef(patch_b, box_b, anchor)
        score = len(anchored_a & anchored_b)
        if score > best_score:
            best_score = score
            best_anchor = anchor
    return best_anchor


def _sequence_step_2ccd9fef(indices: tuple[int, ...]) -> int:
    diffs = tuple(b - a for a, b in zip(indices, indices[1:]))
    return reduce(gcd, diffs)


def _predict_patch_2ccd9fef(
    sequence: tuple[tuple[int, frozenset[IntegerTuple], tuple[int, int, int, int]], ...],
    target_idx: int,
) -> frozenset[IntegerTuple]:
    anchor = _choose_anchor_2ccd9fef(sequence)
    idx_a, patch_a, box_a = sequence[-2]
    idx_b, patch_b, box_b = sequence[-1]
    step = idx_b - idx_a
    factor = (target_idx - idx_b) // step
    pred_box = tuple(b + (b - a) * factor for a, b in zip(box_a, box_b))
    anchored_a = _anchorize_patch_2ccd9fef(patch_a, box_a, anchor)
    anchored_b = _anchorize_patch_2ccd9fef(patch_b, box_b, anchor)
    if anchored_a == anchored_b:
        return _deanchor_patch_2ccd9fef(anchored_b, pred_box, anchor)
    delta = anchored_b - anchored_a
    height_a, width_a = _anchored_dims_2ccd9fef(anchored_a)
    height_b, width_b = _anchored_dims_2ccd9fef(anchored_b)
    dy = height_b - height_a
    dx = width_b - width_a
    pred = set(anchored_b)
    frontier = set(delta)
    for _ in range(factor):
        frontier = {(i + dy, j + dx) for i, j in frontier}
        pred |= frontier
    return _deanchor_patch_2ccd9fef(frozenset(pred), pred_box, anchor)


def solve_2ccd9fef(grid: Grid) -> Grid:
    _, blocks, blank_idx, blank_palette = split_blocks_2ccd9fef(grid)
    signal_colors = sorted(value for value in _palette_2ccd9fef(grid) if value not in blank_palette)
    sequences = {}
    for color_value in signal_colors:
        sequence = []
        for idx, block in enumerate(blocks):
            patch = _cells_of_color_2ccd9fef(block, color_value)
            if patch:
                sequence.append((idx, patch, _bbox_2ccd9fef(patch)))
        if len(sequence) >= 2:
            sequences[color_value] = tuple(sequence)
    output = blocks[blank_idx]
    for color_value, sequence in sequences.items():
        indices = tuple(idx for idx, _, _ in sequence)
        step = _sequence_step_2ccd9fef(indices)
        if blank_idx - last(indices) != step:
            continue
        if (blank_idx - first(indices)) % step != 0:
            continue
        patch = _predict_patch_2ccd9fef(sequence, blank_idx)
        output = fill(output, color_value, patch)
    return output
