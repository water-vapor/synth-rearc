from arc2.core import *


TOP = "top"
BOTTOM = "bottom"
LEFT_SIDE = "left"
RIGHT_SIDE = "right"

SIDES = (TOP, BOTTOM, LEFT_SIDE, RIGHT_SIDE)
COLORS = (TWO, THREE, FOUR, FIVE, SIX, SEVEN, EIGHT, NINE)
GUIDE_COUNTS = (ONE, TWO, TWO, TWO, THREE, THREE)
BASE_FRAME = box(frozenset({ORIGIN, THREE_BY_THREE}))


def _clip_patch_c62e2108(
    patch: Indices,
    dims: IntegerTuple,
) -> Indices:
    h, w = dims
    return frozenset((i, j) for i, j in patch if 0 <= i < h and 0 <= j < w)


def _frame_patch_c62e2108(
    loc: IntegerTuple,
) -> Indices:
    return shift(BASE_FRAME, loc)


def _guide_patch_c62e2108(
    loc: IntegerTuple,
    dims: IntegerTuple,
    guides: frozenset[str],
) -> Indices:
    h, w = dims
    i, j = loc
    patch = set()
    if TOP in guides:
        patch |= connect((ZERO, j), (ZERO, j + THREE))
    if BOTTOM in guides:
        patch |= connect((h - ONE, j), (h - ONE, j + THREE))
    if LEFT_SIDE in guides:
        patch |= connect((i, ZERO), (i + THREE, ZERO))
    if RIGHT_SIDE in guides:
        patch |= connect((i, w - ONE), (i + THREE, w - ONE))
    return frozenset(patch)


def _axis_offsets_c62e2108(
    start: int,
    stop: int,
    limit: int,
    backward: bool,
    forward: bool,
) -> tuple[int, ...]:
    offsets = []
    if backward:
        offset = -FOUR
        while stop + offset >= ZERO:
            offsets.append(offset)
            offset -= FOUR
    if forward:
        offset = FOUR
        while start + offset < limit:
            offsets.append(offset)
            offset += FOUR
    return tuple(offsets)


def _output_patch_c62e2108(
    loc: IntegerTuple,
    dims: IntegerTuple,
    guides: frozenset[str],
) -> Indices:
    h, w = dims
    i, j = loc
    frame = _frame_patch_c62e2108(loc)
    patch = set(frame)
    row_offsets = _axis_offsets_c62e2108(i, i + THREE, h, TOP in guides, BOTTOM in guides)
    col_offsets = _axis_offsets_c62e2108(j, j + THREE, w, LEFT_SIDE in guides, RIGHT_SIDE in guides)
    for offset in row_offsets:
        patch |= _clip_patch_c62e2108(shift(frame, (offset, ZERO)), dims)
    for offset in col_offsets:
        patch |= _clip_patch_c62e2108(shift(frame, (ZERO, offset)), dims)
    return frozenset(patch)


def _halo_c62e2108(
    patch: Indices,
    dims: IntegerTuple,
) -> Indices:
    h, w = dims
    halo = set()
    for loc in patch:
        i, j = loc
        if 0 <= i < h and 0 <= j < w:
            halo.add(loc)
        for nloc in dneighbors(loc):
            ni, nj = nloc
            if 0 <= ni < h and 0 <= nj < w:
                halo.add(nloc)
    return frozenset(halo)


def generate_c62e2108(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        h = unifint(diff_lb, diff_ub, (17, 24))
        w = unifint(diff_lb, diff_ub, (17, 24))
        dims = (h, w)
        color = choice(COLORS)
        if min(h, w) < 20:
            frame_count = choice((ONE, ONE, TWO))
        else:
            frame_count = choice((ONE, TWO, TWO))
        blocked = frozenset()
        placed = []
        used_rows = set()
        used_cols = set()
        success = T
        for _ in range(frame_count):
            guide_count = choice(GUIDE_COUNTS)
            guides = frozenset(sample(SIDES, guide_count))
            locs = [(i, j) for i in range(TWO, h - FIVE) for j in range(TWO, w - FIVE)]
            shuffle(locs)
            found = None
            for loc in locs:
                if loc[0] in used_rows or loc[1] in used_cols:
                    continue
                frame = _frame_patch_c62e2108(loc)
                guide_patch = _guide_patch_c62e2108(loc, dims, guides)
                output_patch = _output_patch_c62e2108(loc, dims, guides)
                input_patch = combine(frame, guide_patch)
                input_halo = _halo_c62e2108(input_patch, dims)
                output_halo = _halo_c62e2108(output_patch, dims)
                if positive(size(intersection(blocked, input_halo))):
                    continue
                if positive(size(intersection(blocked, output_halo))):
                    continue
                found = {
                    "frame": frame,
                    "guides": guide_patch,
                    "output": output_patch,
                }
                blocked = combine(blocked, combine(input_halo, output_halo))
                used_rows.add(loc[0])
                used_cols.add(loc[1])
                placed.append(found)
                break
            if found is None:
                success = F
                break
        if flip(success):
            continue
        gi = canvas(ZERO, dims)
        go = canvas(ZERO, dims)
        for item in placed:
            gi = paint(gi, recolor(color, item["frame"]))
            gi = fill(gi, ONE, item["guides"])
            go = paint(go, recolor(color, item["output"]))
        if equality(gi, go):
            continue
        return {"input": gi, "output": go}
