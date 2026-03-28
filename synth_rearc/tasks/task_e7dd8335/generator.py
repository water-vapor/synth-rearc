from synth_rearc.core import *


def _lower_half_patch_e7dd8335(patch: Patch) -> Indices:
    top = uppermost(patch)
    bottom = lowermost(patch)
    split = (top + bottom) // TWO
    rows = interval(split + ONE, bottom + ONE, ONE)
    cols = interval(leftmost(patch), rightmost(patch) + ONE, ONE)
    return intersection(toindices(patch), product(rows, cols))


def _frame_patch_e7dd8335(height_: int, width_: int) -> Indices:
    patch = box(frozenset({(ZERO, ZERO), (height_ - ONE, width_ - ONE)}))
    inner_cols = interval(ONE, width_ - ONE, ONE)
    max_pillars = min(TWO, len(inner_cols))
    if max_pillars > ZERO:
        count = randint(ZERO, max_pillars)
        for col in sorted(sample(inner_cols, count)):
            patch = patch | connect((ZERO, col), (height_ - ONE, col))
    return patch


def _pillar_patch_e7dd8335(cap_width: int, pillar_height: int, inset: int, pointed: bool) -> Indices:
    center = cap_width // TWO
    left_col = center - inset
    right_col = center + inset
    top_row = ONE if pointed else ZERO
    bottom_row = top_row + pillar_height + ONE
    patch = frozenset()
    if pointed:
        patch = patch | initset((ZERO, center))
    patch = patch | connect((top_row, ZERO), (top_row, cap_width - ONE))
    patch = patch | connect((top_row + ONE, left_col), (bottom_row - ONE, left_col))
    patch = patch | connect((top_row + ONE, right_col), (bottom_row - ONE, right_col))
    patch = patch | connect((bottom_row, ZERO), (bottom_row, cap_width - ONE))
    if pointed:
        patch = patch | initset((bottom_row + ONE, center))
    return patch


def _zigzag_patch_e7dd8335(
    cap_width: int,
    depth: int,
    middle_rows: int,
    left_thick: int,
    right_thick: int,
) -> Indices:
    width_ = cap_width + depth + depth
    start = depth
    end = start + cap_width - ONE
    row = ZERO
    patch = connect((row, start), (row, end))
    row += ONE
    for step in interval(ONE, depth + ONE, ONE):
        patch = patch | initset((row, start - step))
        patch = patch | initset((row, end + step))
        row += ONE
    for _ in range(middle_rows):
        patch = patch | product((row,), interval(ZERO, left_thick, ONE))
        patch = patch | product((row,), interval(width_ - right_thick, width_, ONE))
        row += ONE
    for step in interval(depth, ZERO, NEG_ONE):
        patch = patch | initset((row, start - step))
        patch = patch | initset((row, end + step))
        row += ONE
    patch = patch | connect((row, start), (row, end))
    return patch


def _sample_patch_e7dd8335(diff_lb: float, diff_ub: float) -> Indices:
    family = choice(("frame", "frame", "pillar", "pillar", "zigzag"))
    if family == "frame":
        height_ = unifint(diff_lb, diff_ub, (FIVE, TEN))
        width_ = unifint(diff_lb, diff_ub, (FOUR, NINE))
        return _frame_patch_e7dd8335(height_, width_)
    if family == "pillar":
        cap_width = choice((FIVE, SEVEN, NINE))
        pillar_height = unifint(diff_lb, diff_ub, (TWO, SIX))
        inset = unifint(diff_lb, diff_ub, (ONE, cap_width // TWO - ONE))
        pointed = choice((T, T, F))
        return _pillar_patch_e7dd8335(cap_width, pillar_height, inset, pointed)
    cap_width = unifint(diff_lb, diff_ub, (THREE, SIX))
    depth = unifint(diff_lb, diff_ub, (ONE, THREE))
    middle_rows = unifint(diff_lb, diff_ub, (ONE, THREE))
    left_thick = unifint(diff_lb, diff_ub, (ONE, THREE))
    right_thick = unifint(diff_lb, diff_ub, (ONE, THREE))
    return _zigzag_patch_e7dd8335(cap_width, depth, middle_rows, left_thick, right_thick)


def generate_e7dd8335(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    patch = _sample_patch_e7dd8335(diff_lb, diff_ub)
    oh, ow = shape(patch)
    top_margin = unifint(diff_lb, diff_ub, (ZERO, THREE))
    bottom_margin = unifint(diff_lb, diff_ub, (ZERO, THREE))
    left_margin = unifint(diff_lb, diff_ub, (ZERO, THREE))
    right_margin = unifint(diff_lb, diff_ub, (ZERO, THREE))
    gi = canvas(ZERO, (oh + top_margin + bottom_margin, ow + left_margin + right_margin))
    placed = shift(patch, (top_margin, left_margin))
    low = _lower_half_patch_e7dd8335(placed)
    gi = fill(gi, ONE, placed)
    go = fill(gi, TWO, low)
    return {"input": gi, "output": go}
