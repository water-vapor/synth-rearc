from synth_rearc.core import *


WIDTH_CHOICES_6FFE8F07 = (18, 19, 19, 19, 19, 19)
QUADRANTS_6FFE8F07 = ("nw", "ne", "sw", "se")
OVERLAP_KINDS_6FFE8F07 = ("vertical", "horizontal")


def _rect_patch_6ffe8f07(
    top: Integer,
    left: Integer,
    height_: Integer,
    width_: Integer,
) -> Indices:
    rows = interval(top, top + height_, ONE)
    cols = interval(left, left + width_, ONE)
    return product(rows, cols)


def _buffer_patch_6ffe8f07(
    patch: Indices,
    height_: Integer,
    width_: Integer,
) -> set[tuple[int, int]]:
    out = set()
    for i, j in patch:
        for di in (-1, ZERO, ONE):
            for dj in (-1, ZERO, ONE):
                ni = i + di
                nj = j + dj
                if 0 <= ni < height_ and 0 <= nj < width_:
                    out.add((ni, nj))
    return out


def _dimension_choices_6ffe8f07(
    box_h: Integer,
    box_w: Integer,
) -> tuple[tuple[int, int], ...]:
    max_h = min(8, box_h)
    max_w = min(13, box_w)
    out = []
    for height_ in range(2, max_h + 1):
        for width_ in range(2, max_w + 1):
            area = height_ * width_
            if 4 <= area <= 40:
                out.append((height_, width_))
    return tuple(out)


def _sample_patch_in_box_6ffe8f07(
    row_lo: Integer,
    row_hi: Integer,
    col_lo: Integer,
    col_hi: Integer,
    blocked: set[tuple[int, int]],
    height_: Integer,
    width_: Integer,
    accept,
) -> Indices | None:
    box_h = row_hi - row_lo + 1
    box_w = col_hi - col_lo + 1
    if box_h < 2 or box_w < 2:
        return None
    dims = _dimension_choices_6ffe8f07(box_h, box_w)
    if len(dims) == 0:
        return None
    for _ in range(80):
        rect_h, rect_w = choice(dims)
        top = randint(row_lo, row_hi - rect_h + 1)
        left = randint(col_lo, col_hi - rect_w + 1)
        bottom = top + rect_h - 1
        right = left + rect_w - 1
        if not accept(top, bottom, left, right):
            continue
        patch = _rect_patch_6ffe8f07(top, left, rect_h, rect_w)
        if patch.isdisjoint(blocked):
            return patch
    return None


def _sample_overlap_patch_6ffe8f07(
    overlap_kind: str,
    top: Integer,
    bottom: Integer,
    left: Integer,
    right: Integer,
    height_: Integer,
    width_: Integer,
    blocked: set[tuple[int, int]],
) -> Indices | None:
    if overlap_kind == "vertical":
        side = choice(("above", "below"))
        if side == "above":
            row_lo, row_hi = ZERO, top - 1
        else:
            row_lo, row_hi = bottom + 1, height_ - 1

        def accept(
            rect_top: Integer,
            rect_bottom: Integer,
            rect_left: Integer,
            rect_right: Integer,
        ) -> Boolean:
            return rect_left <= right and rect_right >= left

        return _sample_patch_in_box_6ffe8f07(
            row_lo,
            row_hi,
            ZERO,
            width_ - 1,
            blocked,
            height_,
            width_,
            accept,
        )
    side = choice(("left", "right"))
    if side == "left":
        col_lo, col_hi = ZERO, left - 1
    else:
        col_lo, col_hi = right + 1, width_ - 1

    def accept(
        rect_top: Integer,
        rect_bottom: Integer,
        rect_left: Integer,
        rect_right: Integer,
    ) -> Boolean:
        return rect_top <= bottom and rect_bottom >= top

    return _sample_patch_in_box_6ffe8f07(
        ZERO,
        height_ - 1,
        col_lo,
        col_hi,
        blocked,
        height_,
        width_,
        accept,
    )


def _sample_quadrant_patch_6ffe8f07(
    quadrant: str,
    top: Integer,
    bottom: Integer,
    left: Integer,
    right: Integer,
    height_: Integer,
    width_: Integer,
    blocked: set[tuple[int, int]],
) -> Indices | None:
    if quadrant[ZERO] == "n":
        row_lo, row_hi = ZERO, top - 1
    else:
        row_lo, row_hi = bottom + 1, height_ - 1
    if quadrant[ONE] == "w":
        col_lo, col_hi = ZERO, left - 1
    else:
        col_lo, col_hi = right + 1, width_ - 1
    return _sample_patch_in_box_6ffe8f07(
        row_lo,
        row_hi,
        col_lo,
        col_hi,
        blocked,
        height_,
        width_,
        lambda *_: True,
    )


def _place_patch_6ffe8f07(
    grid: Grid,
    color_: Integer,
    patch: Indices,
) -> Grid:
    return fill(grid, color_, patch)


def _render_output_6ffe8f07(
    grid: Grid,
    one_cells: Indices,
    eight_patch: Indices,
) -> Grid:
    top = uppermost(eight_patch)
    bottom = lowermost(eight_patch)
    left = leftmost(eight_patch)
    right = rightmost(eight_patch)
    rows = interval(top, bottom + 1, ONE)
    cols = interval(left, right + 1, ONE)
    width_ = len(grid[0])
    height_ = len(grid)
    fill_cells = set(eight_patch)
    for row in rows:
        row_blockers = tuple(col for i, col in one_cells if i == row)
        left_blockers = tuple(col for col in row_blockers if col < left)
        right_blockers = tuple(col for col in row_blockers if col > right)
        start = ZERO if len(left_blockers) == ZERO else max(left_blockers) + 1
        stop = width_ - 1 if len(right_blockers) == ZERO else min(right_blockers) - 1
        fill_cells |= set(connect((row, start), (row, stop)))
    for col in cols:
        col_blockers = tuple(row for row, j in one_cells if j == col)
        upper_blockers = tuple(row for row in col_blockers if row < top)
        lower_blockers = tuple(row for row in col_blockers if row > bottom)
        start = ZERO if len(upper_blockers) == ZERO else max(upper_blockers) + 1
        stop = height_ - 1 if len(lower_blockers) == ZERO else min(lower_blockers) - 1
        fill_cells |= set(connect((start, col), (stop, col)))
    paint_cells = difference(frozenset(fill_cells), combine(eight_patch, one_cells))
    return fill(grid, FOUR, paint_cells)


def _place_rectangles_6ffe8f07(
    grid: Grid,
    color_: Integer,
    count: Integer,
    top: Integer,
    left: Integer,
    block_h: Integer,
    block_w: Integer,
    blocked: set[tuple[int, int]],
) -> tuple[Grid, tuple[Indices, ...], set[tuple[int, int]]] | None:
    height_ = len(grid)
    width_ = len(grid[0])
    bottom = top + block_h - 1
    right = left + block_w - 1
    patches = []
    region_choices = (
        "vertical",
        "vertical",
        "horizontal",
        "horizontal",
        "nw",
        "ne",
        "sw",
        "se",
        "nw",
        "ne",
        "sw",
        "se",
    )
    for _ in range(count):
        patch = None
        for _ in range(120):
            region = choice(region_choices)
            if region in OVERLAP_KINDS_6FFE8F07:
                patch = _sample_overlap_patch_6ffe8f07(
                    region,
                    top,
                    bottom,
                    left,
                    right,
                    height_,
                    width_,
                    blocked,
                )
            else:
                patch = _sample_quadrant_patch_6ffe8f07(
                    region,
                    top,
                    bottom,
                    left,
                    right,
                    height_,
                    width_,
                    blocked,
                )
            if patch is not None:
                break
        if patch is None:
            return None
        grid = _place_patch_6ffe8f07(grid, color_, patch)
        patches.append(patch)
        blocked |= _buffer_patch_6ffe8f07(patch, height_, width_)
    return grid, tuple(patches), blocked


def generate_6ffe8f07(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        height_ = 19
        width_ = choice(WIDTH_CHOICES_6FFE8F07)
        block_h = unifint(diff_lb, diff_ub, (4, 7))
        block_w = unifint(diff_lb, diff_ub, (4, min(7, width_ - 8)))
        top = randint(4, 7)
        left = randint(4, 6)
        if top + block_h >= height_ or left + block_w >= width_:
            continue
        eight_patch = _rect_patch_6ffe8f07(top, left, block_h, block_w)
        grid = canvas(ZERO, (height_, width_))
        grid = _place_patch_6ffe8f07(grid, EIGHT, eight_patch)
        blocked = _buffer_patch_6ffe8f07(eight_patch, height_, width_)
        mandatory_one_kind = choice(OVERLAP_KINDS_6FFE8F07)
        one_patch = _sample_overlap_patch_6ffe8f07(
            mandatory_one_kind,
            top,
            top + block_h - 1,
            left,
            left + block_w - 1,
            height_,
            width_,
            blocked,
        )
        if one_patch is None:
            continue
        grid = _place_patch_6ffe8f07(grid, ONE, one_patch)
        blocked |= _buffer_patch_6ffe8f07(one_patch, height_, width_)
        mandatory_two_kind = choice(OVERLAP_KINDS_6FFE8F07)
        two_patch = _sample_overlap_patch_6ffe8f07(
            mandatory_two_kind,
            top,
            top + block_h - 1,
            left,
            left + block_w - 1,
            height_,
            width_,
            blocked,
        )
        if two_patch is None:
            continue
        grid = _place_patch_6ffe8f07(grid, TWO, two_patch)
        blocked |= _buffer_patch_6ffe8f07(two_patch, height_, width_)
        n_one = unifint(diff_lb, diff_ub, (1, 4)) - 1
        placed_ones = _place_rectangles_6ffe8f07(
            grid,
            ONE,
            n_one,
            top,
            left,
            block_h,
            block_w,
            blocked,
        )
        if placed_ones is None:
            continue
        grid, one_patches, blocked = placed_ones
        n_two = unifint(diff_lb, diff_ub, (2, 6)) - 1
        placed_twos = _place_rectangles_6ffe8f07(
            grid,
            TWO,
            n_two,
            top,
            left,
            block_h,
            block_w,
            blocked,
        )
        if placed_twos is None:
            continue
        grid, two_patches, blocked = placed_twos
        all_one_cells = set(one_patch)
        for patch in one_patches:
            all_one_cells |= set(patch)
        output = _render_output_6ffe8f07(
            grid,
            frozenset(all_one_cells),
            eight_patch,
        )
        if grid == output:
            continue
        return {"input": grid, "output": output}
