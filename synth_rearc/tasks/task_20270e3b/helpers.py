from synth_rearc.core import *


BACKGROUND_20270E3B = ONE
FOREGROUND_20270E3B = FOUR
MARKER_20270E3B = SEVEN


def normalize_parts_20270e3b(
    obj: Indices,
    anchor: Indices,
) -> tuple[Indices, Indices]:
    piece = combine(obj, anchor)
    delta = invert(ulcorner(piece))
    return shift(obj, delta), shift(anchor, delta)


def grow_connected_shape_20270e3b(
    h: Integer,
    w: Integer,
    seeds: Indices,
    blocked: Indices,
    target_cells: Integer,
) -> Indices:
    cells = set(seeds)
    tries = ZERO
    while len(cells) < target_cells and tries < 200:
        tries += ONE
        pivot = choice(tuple(cells))
        mode = choice(("h", "h", "v", "v", "dot"))
        if mode == "dot":
            direction = choice((UP, DOWN, LEFT, RIGHT))
            segment = initset(add(pivot, direction))
        elif mode == "h":
            segment = connect(pivot, (pivot[0], randint(ZERO, w - ONE)))
        else:
            segment = connect(pivot, (randint(ZERO, h - ONE), pivot[1]))
        segment = frozenset(
            loc for loc in segment
            if 0 <= loc[0] < h and 0 <= loc[1] < w and loc not in blocked
        )
        if len(segment) == ZERO:
            continue
        cells |= segment
        if min(h, w) >= 4 and uniform(0.0, 1.0) < 0.14:
            top = randint(ZERO, h - 2)
            bottom = randint(top + ONE, h - ONE)
            left = randint(ZERO, w - 2)
            right = randint(left + ONE, w - ONE)
            frame = frozenset(
                loc for loc in box(frozenset({(top, left), (bottom, right)}))
                if loc not in blocked
            )
            if len(intersection(frame, frozenset(cells))) > ZERO:
                cells |= frame
    return frozenset(cells)


def build_base_piece_20270e3b(
    diff_lb: float,
    diff_ub: float,
    marker_len: Integer,
) -> tuple[Object, Indices]:
    h = unifint(diff_lb, diff_ub, (5, 11))
    w = unifint(diff_lb, diff_ub, (max(5, marker_len + 2), 12))
    anchor_row = randint(ONE, h - ONE)
    anchor_col = randint(ZERO, w - marker_len)
    anchor = frozenset((anchor_row, anchor_col + dj) for dj in range(marker_len))
    blocked = set(anchor)
    if anchor_row + ONE < h:
        blocked |= {(anchor_row + ONE, anchor_col + dj) for dj in range(marker_len)}
    stem_col = anchor_col + randint(ZERO, marker_len - ONE)
    stem_top = randint(ZERO, anchor_row - ONE)
    seeds = set(connect((stem_top, stem_col), (anchor_row - ONE, stem_col)))
    if uniform(0.0, 1.0) < 0.8:
        row = choice((stem_top, anchor_row - ONE))
        left = randint(ZERO, stem_col)
        right = randint(stem_col, w - ONE)
        seeds |= set(connect((row, left), (row, right)))
    if uniform(0.0, 1.0) < 0.35 and anchor_row >= 2 and w >= marker_len + 4:
        top = randint(ZERO, anchor_row - 2)
        left = randint(ZERO, anchor_col)
        right = randint(anchor_col + marker_len - ONE, w - ONE)
        seeds |= set(box(frozenset({(top, left), (anchor_row - ONE, right)})))
    seeds = frozenset(loc for loc in seeds if loc not in blocked)
    max_cells = h * w - len(blocked)
    lo = min(max_cells, max(len(seeds) + 2, (h + w) // 2))
    hi = min(max_cells, max(lo, (h * w) // 2))
    target_cells = unifint(diff_lb, diff_ub, (lo, hi))
    obj = grow_connected_shape_20270e3b(h, w, seeds, frozenset(blocked), target_cells)
    obj, anchor = normalize_parts_20270e3b(obj, anchor)
    return recolor(FOREGROUND_20270E3B, obj), anchor


def build_source_piece_above_20270e3b(
    diff_lb: float,
    diff_ub: float,
    marker_len: Integer,
) -> tuple[Object, Indices]:
    h = unifint(diff_lb, diff_ub, (3, 8))
    w = unifint(diff_lb, diff_ub, (max(4, marker_len + 1), 10))
    stem_col = randint(ZERO, marker_len - ONE)
    stem_bottom = randint(ONE, h - ONE)
    seeds = set((ZERO, dj) for dj in range(marker_len))
    seeds |= set(connect((ZERO, stem_col), (stem_bottom, stem_col)))
    if uniform(0.0, 1.0) < 0.75:
        row = randint(ZERO, h - ONE)
        left = randint(ZERO, stem_col)
        right = randint(stem_col, w - ONE)
        seeds |= set(connect((row, left), (row, right)))
    max_cells = h * w
    lo = min(max_cells, max(len(seeds) + 2, (h + w) // 2))
    hi = min(max_cells, max(lo, (h * w) // 2))
    target_cells = unifint(diff_lb, diff_ub, (lo, hi))
    obj = grow_connected_shape_20270e3b(h, w, frozenset(seeds), frozenset(), target_cells)
    anchor = frozenset((NEG_ONE, dj) for dj in range(marker_len))
    obj, anchor = normalize_parts_20270e3b(obj, anchor)
    return recolor(FOREGROUND_20270E3B, obj), anchor


def build_source_piece_corner_20270e3b(
    diff_lb: float,
    diff_ub: float,
) -> tuple[Object, Indices]:
    h = unifint(diff_lb, diff_ub, (3, 8))
    w = unifint(diff_lb, diff_ub, (4, 10))
    cap_col = randint(ONE, w - ONE)
    blocked = initset((ZERO, ZERO))
    seeds = set(connect((ONE, ZERO), (ONE, cap_col)))
    seeds |= set(connect((ZERO, cap_col), (ONE, cap_col)))
    target_cells = unifint(
        diff_lb,
        diff_ub,
        (max(len(seeds) + 2, (h + w) // 2), max((h * w) // 2, len(seeds) + 2)),
    )
    obj = grow_connected_shape_20270e3b(h, w, frozenset(seeds), blocked, target_cells)
    anchor = initset((ZERO, ZERO))
    obj, anchor = normalize_parts_20270e3b(obj, anchor)
    return recolor(FOREGROUND_20270E3B, obj), anchor


def render_input_20270e3b(
    dims: IntegerTuple,
    base_obj: Object,
    base_anchor: Indices,
    source_obj: Object,
    source_anchor: Indices,
) -> Grid:
    gi = canvas(BACKGROUND_20270E3B, dims)
    gi = paint(gi, base_obj)
    gi = fill(gi, MARKER_20270E3B, base_anchor)
    gi = paint(gi, source_obj)
    gi = fill(gi, MARKER_20270E3B, source_anchor)
    return gi


def render_output_20270e3b(
    base_obj: Object,
    base_anchor: Indices,
    source_obj: Object,
    source_anchor: Indices,
) -> Grid:
    delta = add(subtract(ulcorner(base_anchor), ulcorner(source_anchor)), UP)
    moved_source = shift(source_obj, delta)
    obj = normalize(combine(base_obj, moved_source))
    go = canvas(BACKGROUND_20270E3B, shape(obj))
    return paint(go, obj)
