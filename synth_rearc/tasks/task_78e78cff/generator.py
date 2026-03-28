from synth_rearc.core import *

from .verifier import verify_78e78cff


WIDTH_BOUNDS_78E78CFF = (10, 14)
BLOCK_BOUNDS_78E78CFF = (2, 3)
GAP_BOUNDS_78E78CFF = (1, 2)
MARGIN_BOUNDS_78E78CFF = (2, 4)
INPUT_COLORS_78E78CFF = interval(ZERO, TEN, ONE)


def _segment_length_78e78cff(limit: int) -> int:
    if limit <= ONE:
        return ONE
    return choice((ONE, ONE, TWO))


def _boundary_gap_78e78cff(marker_col: int, width: int) -> tuple[int, int]:
    left_lb = max(ONE, marker_col - THREE)
    left_ub = marker_col
    gap_left = randint(left_lb, left_ub)
    right_lb = max(gap_left, marker_col - ONE)
    right_ub = min(width - TWO, marker_col + TWO)
    gap_right = randint(right_lb, right_ub)
    return (gap_left, gap_right)


def _grow_block_from_boundary_78e78cff(
    marker_col: int,
    width: int,
    length: int,
    boundary_gap: tuple[int, int],
) -> list[tuple[int, int]]:
    gaps = [boundary_gap]
    left_only_last = length > ONE and choice((ZERO, ONE, TWO, THREE)) == ZERO
    gap_left, gap_right = boundary_gap
    for step in range(ONE, length):
        gap_left = max(ONE, gap_left - randint(ZERO, ONE))
        if left_only_last and step == length - ONE:
            gap_right = width - ONE
        else:
            gap_right = min(width - TWO, gap_right + randint(ZERO, ONE))
        if gap_left > marker_col:
            gap_left = marker_col
        if gap_right < marker_col - ONE:
            gap_right = marker_col - ONE
        gaps.append((gap_left, gap_right))
    return gaps


def _shape_patch_for_gap_78e78cff(
    row: int,
    gap: tuple[int, int],
    width: int,
) -> Indices:
    gap_left, gap_right = gap
    cells = set()
    if gap_left > ZERO:
        left_len = _segment_length_78e78cff(gap_left)
        cells |= {(row, col) for col in range(gap_left - left_len, gap_left)}
    if gap_right < width - ONE:
        right_cap = width - ONE - gap_right
        right_len = _segment_length_78e78cff(right_cap)
        cells |= {(row, col) for col in range(gap_right + ONE, gap_right + right_len + ONE)}
    return frozenset(cells)


def _paint_output_gap_78e78cff(
    grid: Grid,
    row: int,
    gap: tuple[int, int],
    fill_color: int,
) -> Grid:
    gap_left, gap_right = gap
    patch = frozenset((row, col) for col in range(gap_left, gap_right + ONE))
    return underfill(grid, fill_color, patch)


def generate_78e78cff(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        width = unifint(diff_lb, diff_ub, WIDTH_BOUNDS_78E78CFF)
        top_margin = unifint(diff_lb, diff_ub, MARGIN_BOUNDS_78E78CFF)
        bottom_margin = unifint(diff_lb, diff_ub, MARGIN_BOUNDS_78E78CFF)
        top_block = unifint(diff_lb, diff_ub, BLOCK_BOUNDS_78E78CFF)
        bottom_block = unifint(diff_lb, diff_ub, BLOCK_BOUNDS_78E78CFF)
        middle_gap = unifint(diff_lb, diff_ub, GAP_BOUNDS_78E78CFF)
        height = top_margin + top_block + middle_gap + bottom_block + bottom_margin
        marker_col = randint(TWO, width - THREE)
        top_boundary = _boundary_gap_78e78cff(marker_col, width)
        bottom_boundary = _boundary_gap_78e78cff(marker_col, width)
        top_gaps = _grow_block_from_boundary_78e78cff(marker_col, width, top_block, top_boundary)
        bottom_boundary_to_gap = _grow_block_from_boundary_78e78cff(marker_col, width, bottom_block, bottom_boundary)
        bottom_gaps = list(reversed(bottom_boundary_to_gap))
        full_gap = (ZERO, width - ONE)
        output_gaps = (
            [top_gaps[ZERO]] * top_margin
            + top_gaps
            + [full_gap] * middle_gap
            + bottom_gaps
            + [bottom_gaps[-ONE]] * bottom_margin
        )
        top_start = top_margin
        gap_start = top_start + top_block
        bottom_start = gap_start + middle_gap
        bottom_end = bottom_start + bottom_block
        colors = sample(INPUT_COLORS_78E78CFF, THREE)
        bg_color, shape_color, fill_color = colors
        gi = canvas(bg_color, (height, width))
        for row, gap in zip(range(top_start, top_start + top_block), top_gaps):
            gi = fill(gi, shape_color, _shape_patch_for_gap_78e78cff(row, gap, width))
        for row, gap in zip(range(bottom_start, bottom_end), bottom_gaps):
            gi = fill(gi, shape_color, _shape_patch_for_gap_78e78cff(row, gap, width))
        candidate_rows = tuple(
            row
            for row in range(gap_start, bottom_end)
            if output_gaps[row][ZERO] <= marker_col <= output_gaps[row][ONE]
        )
        if len(candidate_rows) == ZERO:
            continue
        marker_row = choice(candidate_rows)
        if index(gi, (marker_row, marker_col)) != bg_color:
            continue
        gi = fill(gi, fill_color, initset((marker_row, marker_col)))
        go = gi
        for row, gap in enumerate(output_gaps):
            go = _paint_output_gap_78e78cff(go, row, gap, fill_color)
        if verify_78e78cff(gi) != go:
            continue
        return {"input": gi, "output": go}
