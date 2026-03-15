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
    for block_h in range(TWO, h + ONE):
        if h % block_h == ZERO and h // block_h >= THREE:
            blocks = tuple(
                crop(grid, (block_h * idx, ZERO), (block_h, w))
                for idx in range(h // block_h)
            )
            candidates.append(("vertical", blocks))
    for block_w in range(TWO, w + ONE):
        if w % block_w == ZERO and w // block_w >= THREE:
            blocks = tuple(
                crop(grid, (ZERO, block_w * idx), (h, block_w))
                for idx in range(w // block_w)
            )
            candidates.append(("horizontal", blocks))
    return candidates


def _validate_split_2ccd9fef(blocks: tuple[Grid, ...]) -> tuple[int, frozenset[int]] | None:
    palettes = tuple(_palette_2ccd9fef(block) for block in blocks)
    blank_idx = min(range(len(blocks)), key=lambda idx: (len(palettes[idx]), idx))
    blank_palette = palettes[blank_idx]
    blank = blocks[blank_idx]
    nsignal = ZERO
    for block, palette_value in zip(blocks, palettes):
        if not blank_palette.issubset(palette_value):
            return None
        if palette_value != blank_palette:
            nsignal += ONE
        for i, row in enumerate(block):
            for j, value in enumerate(row):
                if value != blank[i][j] and value in blank_palette:
                    return None
    if nsignal < TWO:
        return None
    return blank_idx, blank_palette


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
    return (max(rows) + ONE, max(cols) + ONE)


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
    best_score = NEG_ONE
    _, patch_a, box_a = sequence[-TWO]
    _, patch_b, box_b = sequence[-ONE]
    for anchor in ANCHORS_2CCD9FEF:
        anchored_a = _anchorize_patch_2ccd9fef(patch_a, box_a, anchor)
        anchored_b = _anchorize_patch_2ccd9fef(patch_b, box_b, anchor)
        score = len(anchored_a & anchored_b)
        if score > best_score:
            best_score = score
            best_anchor = anchor
    return best_anchor


def _sequence_step_2ccd9fef(indices: tuple[int, ...]) -> int:
    diffs = tuple(b - a for a, b in zip(indices, indices[ONE:]))
    step = diffs[ZERO]
    for diff in diffs[ONE:]:
        a = abs(step)
        b = abs(diff)
        while b:
            a, b = b, a % b
        step = a
    return step


def _predict_patch_2ccd9fef(
    sequence: tuple[tuple[int, frozenset[IntegerTuple], tuple[int, int, int, int]], ...],
    target_idx: int,
) -> frozenset[IntegerTuple]:
    anchor = _choose_anchor_2ccd9fef(sequence)
    idx_a, patch_a, box_a = sequence[-TWO]
    idx_b, patch_b, box_b = sequence[-ONE]
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


def verify_2ccd9fef(I: Grid) -> Grid:
    x0 = _split_candidate_blocks_2ccd9fef(I)
    x1 = []
    for x2, x3 in x0:
        x4 = _validate_split_2ccd9fef(x3)
        if x4 is None:
            continue
        x5, x6 = x4
        x7 = height(first(x3)) * width(first(x3))
        x1.append((x7, x2, x3, x5, x6))
    if not x1:
        raise ValueError("unable to split 2ccd9fef input into repeated panels")
    x2 = max(x1, key=lambda item: item[ZERO])
    x3 = x2[TWO]
    x4 = x2[THREE]
    x5 = x2[FOUR]
    x6 = sorted(value for value in _palette_2ccd9fef(I) if value not in x5)
    x7 = {}
    for x8 in x6:
        x9 = []
        for x10, x11 in enumerate(x3):
            x12 = _cells_of_color_2ccd9fef(x11, x8)
            if x12:
                x9.append((x10, x12, _bbox_2ccd9fef(x12)))
        if len(x9) >= TWO:
            x7[x8] = tuple(x9)
    x8 = x3[x4]
    x9 = x8
    for x10, x11 in x7.items():
        x12 = tuple(idx for idx, _, _ in x11)
        x13 = _sequence_step_2ccd9fef(x12)
        if x4 - x12[-ONE] != x13:
            continue
        if (x4 - x12[ZERO]) % x13 != ZERO:
            continue
        x14 = _predict_patch_2ccd9fef(x11, x4)
        x9 = fill(x9, x10, x14)
    return x9
