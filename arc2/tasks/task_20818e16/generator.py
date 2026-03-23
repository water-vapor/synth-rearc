from arc2.core import *


ORIENTATIONS_20818E16 = ("ul", "ur", "ll", "lr")


def _rect_patch_20818e16(
    top: int,
    left: int,
    dims: tuple[int, int],
) -> Indices:
    h, w = dims
    return frozenset((i, j) for i in range(top, top + h) for j in range(left, left + w))


def _paint_rect_20818e16(
    grid: Grid,
    color_value: int,
    top: int,
    left: int,
    dims: tuple[int, int],
) -> Grid:
    return fill(grid, color_value, _rect_patch_20818e16(top, left, dims))


def _build_output_20818e16(
    specs: tuple[tuple[tuple[int, int], int], ...],
) -> Grid:
    ordered = tuple(sorted(specs, key=lambda item: (item[0][0] * item[0][1], item[0][0], item[0][1], item[1])))
    largest_dims, largest_color = ordered[-1]
    out = canvas(largest_color, largest_dims)
    for dims, color_value in ordered[-2::-1]:
        out = fill(out, color_value, _rect_patch_20818e16(ZERO, ZERO, dims))
    return out


def _sample_dims_20818e16(
    diff_lb: float,
    diff_ub: float,
    num_rects: int,
) -> tuple[tuple[int, int], ...]:
    while True:
        if equality(num_rects, THREE):
            dims = (
                (unifint(diff_lb, diff_ub, (ONE, THREE)), unifint(diff_lb, diff_ub, (TWO, FOUR))),
                (unifint(diff_lb, diff_ub, (FOUR, SIX)), unifint(diff_lb, diff_ub, (FOUR, SIX))),
                (unifint(diff_lb, diff_ub, (SIX, EIGHT)), unifint(diff_lb, diff_ub, (SEVEN, TEN))),
            )
        else:
            dims = (
                (unifint(diff_lb, diff_ub, (ONE, TWO)), unifint(diff_lb, diff_ub, (TWO, THREE))),
                (unifint(diff_lb, diff_ub, (TWO, FOUR)), unifint(diff_lb, diff_ub, (THREE, FIVE))),
                (unifint(diff_lb, diff_ub, (FOUR, SIX)), unifint(diff_lb, diff_ub, (FOUR, SIX))),
                (unifint(diff_lb, diff_ub, (SIX, NINE)), unifint(diff_lb, diff_ub, (SEVEN, TEN))),
            )
        dims = tuple(sorted(dims, key=lambda item: (item[0] * item[1], item[0], item[1])))
        if len({h * w for h, w in dims}) != num_rects:
            continue
        if any(h0 > h1 or w0 > w1 or equality((h0, w0), (h1, w1)) for (h0, w0), (h1, w1) in zip(dims, dims[1:])):
            continue
        return dims


def _sample_overlap_20818e16(
    diff_lb: float,
    diff_ub: float,
    dims: tuple[int, int],
) -> tuple[int, int]:
    h, w = dims
    max_overlap_h = max(ONE, min(h - ONE, max(TWO, halve(h))))
    max_overlap_w = max(ONE, min(w - ONE, max(TWO, halve(w))))
    return (
        unifint(diff_lb, diff_ub, (ONE, max_overlap_h)),
        unifint(diff_lb, diff_ub, (ONE, max_overlap_w)),
    )


def _overlap_anchor_20818e16(
    large_top: int,
    large_left: int,
    large_dims: tuple[int, int],
    dims: tuple[int, int],
    orientation: str,
    overlap_dims: tuple[int, int],
) -> tuple[int, int]:
    large_h, large_w = large_dims
    h, w = dims
    overlap_h, overlap_w = overlap_dims
    if orientation == "ul":
        return large_top - (h - overlap_h), large_left - (w - overlap_w)
    if orientation == "ur":
        return large_top - (h - overlap_h), large_left + large_w - overlap_w
    if orientation == "ll":
        return large_top + large_h - overlap_h, large_left - (w - overlap_w)
    return large_top + large_h - overlap_h, large_left + large_w - overlap_w


def _box_overlaps_20818e16(
    box_a: tuple[int, int, int, int],
    box_b: tuple[int, int, int, int],
    margin: int = ZERO,
) -> bool:
    ai, aj, ah, aw = box_a
    bi, bj, bh, bw = box_b
    ai -= margin
    aj -= margin
    bi -= margin
    bj -= margin
    ah += 2 * margin
    aw += 2 * margin
    bh += 2 * margin
    bw += 2 * margin
    return not (
        ai + ah <= bi or
        bi + bh <= ai or
        aj + aw <= bj or
        bj + bw <= aj
    )


def _find_isolated_anchor_20818e16(
    grid_dims: tuple[int, int],
    dims: tuple[int, int],
    occupied_boxes: tuple[tuple[int, int, int, int], ...],
) -> tuple[int, int] | None:
    grid_h, grid_w = grid_dims
    h, w = dims
    candidates = [
        (i, j)
        for i in range(grid_h - h + 1)
        for j in range(grid_w - w + 1)
        if all(not _box_overlaps_20818e16((i, j, h, w), box, ONE) for box in occupied_boxes)
    ]
    if len(candidates) == ZERO:
        return None
    edge_candidates = [
        (i, j)
        for i, j in candidates
        if i <= TWO or j <= TWO or i >= grid_h - h - THREE or j >= grid_w - w - THREE
    ]
    return choice(edge_candidates if len(edge_candidates) > ZERO else candidates)


def _valid_input_20818e16(
    grid: Grid,
    bgc: int,
    specs: tuple[tuple[tuple[int, int], int], ...],
) -> bool:
    if grid == canvas(bgc, shape(grid)):
        return False
    if mostcolor(grid) != bgc:
        return False
    objs = objects(grid, T, F, T)
    if len(objs) != len(specs):
        return False
    observed = {color(obj): shape(obj) for obj in objs}
    expected = {color_value: dims for dims, color_value in specs}
    return observed == expected


def generate_20818e16(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        num_rects = choice((THREE, THREE, FOUR))
        dims = _sample_dims_20818e16(diff_lb, diff_ub, num_rects)
        rect_colors = tuple(sample(interval(ONE, TEN, ONE), num_rects))
        bgc = choice(tuple(color_value for color_value in interval(ZERO, TEN, ONE) if color_value not in rect_colors))
        specs = tuple((dims[idx], rect_colors[idx]) for idx in range(num_rects))
        output = _build_output_20818e16(specs)

        large_dims, large_color = specs[-1]
        overlap_specs = specs[ONE:-ONE]
        isolated_dims, isolated_color = specs[ZERO]

        overlap_orientations = tuple(sample(ORIENTATIONS_20818E16, len(overlap_specs)))
        overlap_data = []
        top_pad = ZERO
        left_pad = ZERO
        bottom_pad = ZERO
        right_pad = ZERO
        for (rect_dims, rect_color), orientation in zip(overlap_specs, overlap_orientations):
            overlap_dims = _sample_overlap_20818e16(diff_lb, diff_ub, rect_dims)
            overlap_h, overlap_w = overlap_dims
            rect_h, rect_w = rect_dims
            if orientation == "ul":
                top_pad = max(top_pad, rect_h - overlap_h)
                left_pad = max(left_pad, rect_w - overlap_w)
            elif orientation == "ur":
                top_pad = max(top_pad, rect_h - overlap_h)
                right_pad = max(right_pad, rect_w - overlap_w)
            elif orientation == "ll":
                bottom_pad = max(bottom_pad, rect_h - overlap_h)
                left_pad = max(left_pad, rect_w - overlap_w)
            else:
                bottom_pad = max(bottom_pad, rect_h - overlap_h)
                right_pad = max(right_pad, rect_w - overlap_w)
            overlap_data.append((rect_dims, rect_color, orientation, overlap_dims))

        top_margin = unifint(diff_lb, diff_ub, (ZERO, ONE))
        left_margin = unifint(diff_lb, diff_ub, (ZERO, ONE))
        bottom_margin = unifint(diff_lb, diff_ub, (ONE, TWO))
        right_margin = unifint(diff_lb, diff_ub, (ONE, TWO))
        grid_h = top_pad + top_margin + large_dims[ZERO] + bottom_pad + bottom_margin
        grid_w = left_pad + left_margin + large_dims[ONE] + right_pad + right_margin
        grid_h = max(grid_h, unifint(diff_lb, diff_ub, (14, 17)))
        grid_w = max(grid_w, unifint(diff_lb, diff_ub, (14, 18)))
        if grid_h > 18 or grid_w > 18:
            continue
        large_top = top_pad + top_margin
        large_left = left_pad + left_margin

        placements = {large_color: (large_top, large_left, large_dims)}
        occupied_boxes = [(large_top, large_left, large_dims[ZERO], large_dims[ONE])]
        for rect_dims, rect_color, orientation, overlap_dims in overlap_data:
            rect_top, rect_left = _overlap_anchor_20818e16(
                large_top,
                large_left,
                large_dims,
                rect_dims,
                orientation,
                overlap_dims,
            )
            placements[rect_color] = (rect_top, rect_left, rect_dims)
            occupied_boxes.append((rect_top, rect_left, rect_dims[ZERO], rect_dims[ONE]))

        isolated_anchor = _find_isolated_anchor_20818e16((grid_h, grid_w), isolated_dims, tuple(occupied_boxes))
        if isolated_anchor is None:
            continue
        isolated_top, isolated_left = isolated_anchor
        placements[isolated_color] = (isolated_top, isolated_left, isolated_dims)

        after_large = []
        before_large = list(overlap_specs)
        if len(overlap_specs) == ONE:
            if choice((T, F)):
                after_large = [before_large.pop()]
        elif len(overlap_specs) > ONE:
            after_large = [before_large.pop(choice((ZERO, ONE)))]
        shuffle(before_large)

        paint_order = [color_value for _, color_value in before_large]
        paint_order.append(large_color)
        paint_order.extend(color_value for _, color_value in after_large)
        insert_at = randint(ZERO, len(paint_order))
        paint_order.insert(insert_at, isolated_color)

        grid = canvas(bgc, (grid_h, grid_w))
        for color_value in paint_order:
            top, left, rect_dims = placements[color_value]
            grid = _paint_rect_20818e16(grid, color_value, top, left, rect_dims)

        if not _valid_input_20818e16(grid, bgc, specs):
            continue
        return {"input": grid, "output": output}
