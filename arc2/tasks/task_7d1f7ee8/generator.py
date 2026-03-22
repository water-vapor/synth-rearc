from arc2.core import *


OUTER_COUNTS_7D1F7EE8 = (ONE, TWO, TWO, THREE, THREE)
OUTER_COLORS_7D1F7EE8 = interval(ONE, TEN, ONE)


def _corners_7d1f7ee8(
    top: Integer,
    left: Integer,
    height_value: Integer,
    width_value: Integer,
) -> frozenset[tuple[Integer, Integer]]:
    return frozenset({(top, left), (top + height_value - ONE, left + width_value - ONE)})


def _bbox_7d1f7ee8(
    top: Integer,
    left: Integer,
    height_value: Integer,
    width_value: Integer,
) -> Indices:
    return backdrop(_corners_7d1f7ee8(top, left, height_value, width_value))


def _frame_7d1f7ee8(
    top: Integer,
    left: Integer,
    height_value: Integer,
    width_value: Integer,
) -> Indices:
    return box(_corners_7d1f7ee8(top, left, height_value, width_value))


def _pick_color_7d1f7ee8(forbidden: tuple[Integer, ...]) -> Integer:
    return choice(tuple(col for col in OUTER_COLORS_7D1F7EE8 if col not in forbidden))


def _sample_box_7d1f7ee8(
    region: tuple[Integer, Integer, Integer, Integer],
    reserved: Indices,
    min_h: Integer,
    max_h: Integer,
    min_w: Integer,
    max_w: Integer,
    margin: Integer,
) -> tuple[Integer, Integer, Integer, Integer, Indices] | None:
    top, left, region_h, region_w = region
    avail_h = region_h - double(margin)
    avail_w = region_w - double(margin)
    if avail_h < min_h or avail_w < min_w:
        return None
    hi_h = min(max_h, avail_h)
    hi_w = min(max_w, avail_w)
    for _ in range(80):
        box_h = unifint(0.0, 1.0, (min_h, hi_h))
        box_w = unifint(0.0, 1.0, (min_w, hi_w))
        row_start = top + margin
        row_stop = top + region_h - margin - box_h
        col_start = left + margin
        col_stop = left + region_w - margin - box_w
        if row_start > row_stop or col_start > col_stop:
            continue
        loci = choice(interval(row_start, row_stop + ONE, ONE))
        locj = choice(interval(col_start, col_stop + ONE, ONE))
        bbox = _bbox_7d1f7ee8(loci, locj, box_h, box_w)
        if bbox & reserved:
            continue
        return loci, locj, box_h, box_w, bbox
    return None


def _place_child_7d1f7ee8(
    grid: Grid,
    region: tuple[Integer, Integer, Integer, Integer],
    reserved: Indices,
    forbidden: tuple[Integer, ...],
    force_frame: Boolean,
) -> dict | None:
    _, _, region_h, region_w = region
    avail_h = region_h - FOUR
    avail_w = region_w - FOUR
    variants = []
    if avail_h >= FOUR and avail_w >= FOUR:
        variants.extend(["frame", "frame"] if force_frame else ["frame"])
    if (avail_h >= ONE and avail_w >= TWO) or (avail_h >= TWO and avail_w >= ONE):
        variants.extend(["block", "block", "block"])
    if len(variants) == 0:
        return None
    for _ in range(60):
        kind = choice(tuple(variants))
        if kind == "frame":
            min_h = SIX if force_frame and avail_h >= SIX else FOUR
            min_w = SIX if force_frame and avail_w >= SIX else FOUR
            candidate = _sample_box_7d1f7ee8(region, reserved, min_h, avail_h, min_w, avail_w, TWO)
        else:
            max_h = min(avail_h, FOUR)
            max_w = min(avail_w, FOUR)
            candidate = _sample_box_7d1f7ee8(region, reserved, ONE, max_h, ONE, max_w, TWO)
        if candidate is None:
            continue
        loci, locj, box_h, box_w, bbox = candidate
        if kind == "block" and box_h == box_w == ONE:
            continue
        patch = _frame_7d1f7ee8(loci, locj, box_h, box_w) if kind == "frame" else bbox
        color_value = _pick_color_7d1f7ee8(forbidden)
        obj = recolor(color_value, patch)
        return {
            "bbox": bbox,
            "color": color_value,
            "kind": kind,
            "object": obj,
            "region": (loci, locj, box_h, box_w),
            "reserved": reserved | bbox | (outbox(bbox) & asindices(grid)),
        }
    return None


def _decorate_frame_7d1f7ee8(
    grid: Grid,
    region: tuple[Integer, Integer, Integer, Integer],
    forbidden: tuple[Integer, ...],
    require_child: Boolean,
    depth: Integer,
) -> tuple[Grid, list[dict]]:
    children = []
    reserved = frozenset()
    lower = ONE if require_child else ZERO
    upper = TWO if depth == ZERO else ONE
    target = choice(interval(lower, upper + ONE, ONE))
    for child_idx in range(target):
        force_frame = child_idx == ZERO and depth == ZERO
        child = _place_child_7d1f7ee8(grid, region, reserved, forbidden, force_frame)
        if child is None:
            continue
        grid = paint(grid, child["object"])
        children.append(child)
        reserved = child["reserved"]
        if child["kind"] == "frame" and depth < ONE and choice((T, T, F)):
            grid, grandchildren = _decorate_frame_7d1f7ee8(
                grid,
                child["region"],
                (child["color"],) + forbidden,
                choice((T, F)),
                increment(depth),
            )
            children.extend(grandchildren)
    return grid, children


def generate_7d1f7ee8(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        num_outer = choice(OUTER_COUNTS_7D1F7EE8)
        grid_h = unifint(diff_lb, diff_ub, (max(12, add(8, multiply(3, num_outer))), 30))
        grid_w = unifint(diff_lb, diff_ub, (max(12, add(9, multiply(4, num_outer))), 30))
        gi = canvas(ZERO, (grid_h, grid_w))
        fullinds = asindices(gi)
        outer_colors = sample(OUTER_COLORS_7D1F7EE8, num_outer)
        decorated = sample(interval(ZERO, num_outer, ONE), choice((ONE, ONE, min(TWO, num_outer))))
        reserved = frozenset()
        outer_specs = []
        success = T
        changed = F

        for idx, outer_color in enumerate(outer_colors):
            must_decorate = idx in decorated
            min_h = NINE if must_decorate else FIVE
            min_w = NINE if must_decorate else FIVE
            max_h = min(grid_h, 16 if must_decorate else 13)
            max_w = min(grid_w, 19 if must_decorate else 15)
            candidate = _sample_box_7d1f7ee8(
                (ZERO, ZERO, grid_h, grid_w),
                reserved,
                min_h,
                max_h,
                min_w,
                max_w,
                ZERO,
            )
            if candidate is None:
                success = F
                break
            loci, locj, box_h, box_w, bbox = candidate
            outer_patch = _frame_7d1f7ee8(loci, locj, box_h, box_w)
            gi = fill(gi, outer_color, outer_patch)
            reserved = reserved | bbox | (outbox(bbox) & fullinds)
            outer_specs.append((outer_color, bbox))
            gi, children = _decorate_frame_7d1f7ee8(
                gi,
                (loci, locj, box_h, box_w),
                (outer_color,),
                must_decorate,
                ZERO,
            )
            if must_decorate and len(children) == 0:
                success = F
                break
            changed = changed or len(children) > 0

        if not success or not changed:
            continue

        occupied = toindices(merge(objects(gi, T, F, T)))
        go = gi
        for outer_color, bbox in outer_specs:
            go = fill(go, outer_color, bbox & occupied)
        if gi == go:
            continue
        return {"input": gi, "output": go}
