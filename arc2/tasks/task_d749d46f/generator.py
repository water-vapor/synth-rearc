from arc2.core import *


def _rect_patch_d749d46f(height_: Integer, width_: Integer) -> Indices:
    rows = interval(ZERO, height_, ONE)
    cols = interval(ZERO, width_, ONE)
    return product(rows, cols)


def _render_input_d749d46f(
    blocks: tuple[tuple[Integer, Integer], ...],
    bgc: Integer,
    fgc: Integer,
) -> Grid:
    height_ = max(h for h, _ in blocks)
    width_ = sum(w for _, w in blocks) + len(blocks) - 1
    gi = canvas(bgc, (height_, width_))
    offset = ZERO
    for h, w in blocks:
        patch = shift(_rect_patch_d749d46f(h, w), (ZERO, offset))
        gi = fill(gi, fgc, patch)
        offset += w + 1
    return gi


def _render_output_d749d46f(
    blocks: tuple[tuple[Integer, Integer], ...],
    bgc: Integer,
    fgc: Integer,
) -> Grid:
    larges = tuple(max(h, w) for h, w in blocks)
    smalls = tuple(min(h, w) for h, w in blocks)
    width_ = sum(larges) + len(blocks) - 1
    go = canvas(bgc, (TEN, width_))
    top_offset = ZERO
    bottom_offset = ZERO
    for small, large in pair(smalls, larges):
        top_patch = shift(_rect_patch_d749d46f(small, large), (ZERO, top_offset))
        go = fill(go, fgc, top_patch)
        row_offset = subtract(TEN, large)
        bottom_patch = shift(_rect_patch_d749d46f(large, small), (row_offset, bottom_offset))
        go = fill(go, fgc, bottom_patch)
        top_offset += large + 1
        bottom_offset += small + 1
    return go


def _sample_blocks_d749d46f(
    diff_lb: float,
    diff_ub: float,
) -> tuple[tuple[Integer, Integer], ...]:
    while True:
        max_height = unifint(diff_lb, diff_ub, (THREE, SIX))
        num_blocks = unifint(diff_lb, diff_ub, (FOUR, SIX))
        anchor_width = choice((ONE, ONE, ONE, TWO))
        blocks = [(max_height, anchor_width)]
        for _ in range(num_blocks - 1):
            large = unifint(diff_lb, diff_ub, (ONE, max_height))
            small_ub = min(THREE, subtract(TEN, large))
            small = unifint(diff_lb, diff_ub, (ONE, small_ub))
            if choice((T, F)):
                block = (large, small)
            else:
                block = (small, large)
            blocks.append(block)
        shuffle(blocks)
        if not any(h > w for h, w in blocks):
            continue
        if not any(w > h for h, w in blocks):
            continue
        smalls = [min(h, w) for h, w in blocks]
        larges = [max(h, w) for h, w in blocks]
        fg_area = sum(h * w for h, w in blocks)
        input_width = sum(w for _, w in blocks) + len(blocks) - 1
        output_width = sum(larges) + len(blocks) - 1
        input_area = max_height * input_width
        if input_width < 10 or input_width > 18:
            continue
        if output_width > 25:
            continue
        if double(fg_area) >= input_area:
            continue
        if all(s == ONE for s in smalls):
            continue
        if max(h for h, _ in blocks) != max_height:
            continue
        return tuple(blocks)


def generate_d749d46f(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    bgc, fgc = sample(interval(ONE, TEN, ONE), TWO)
    blocks = _sample_blocks_d749d46f(diff_lb, diff_ub)
    gi = _render_input_d749d46f(blocks, bgc, fgc)
    go = _render_output_d749d46f(blocks, bgc, fgc)
    return {"input": gi, "output": go}
