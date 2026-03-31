from synth_rearc.core import *

from .helpers import mirror_patch_7ed72f31
from .verifier import verify_7ed72f31


MAX_DIMS_7ED72F31 = (30, 30)
PAIR_KINDS_7ED72F31 = ("point", "point", "vline", "vline", "hline", "hline")


def _normalize_7ed72f31(
    patch: Patch,
) -> Patch:
    return shift(patch, (-uppermost(patch), -leftmost(patch)))


def _pad_patch_7ed72f31(
    patch: Patch,
    pad: int,
    dims: tuple[int, int],
) -> Indices:
    h, w = dims
    out = set()
    for i, j in toindices(patch):
        for di in range(-pad, pad + ONE):
            for dj in range(-pad, pad + ONE):
                ni = i + di
                nj = j + dj
                if ZERO <= ni < h and ZERO <= nj < w:
                    out.add((ni, nj))
    return frozenset(out)


def _connected_patch_7ed72f31(
    h: int,
    w: int,
    target: int,
    forbid_origin: bool,
) -> Indices:
    cells = tuple(
        (i, j)
        for i in range(h)
        for j in range(w)
        if (i, j) != ORIGIN or not forbid_origin
    )
    if len(cells) == ZERO:
        return frozenset()
    for _ in range(48):
        patch = {choice(cells)}
        while len(patch) < target:
            frontier = set()
            for loc in patch:
                for cand in dneighbors(loc):
                    ci, cj = cand
                    if not (ZERO <= ci < h and ZERO <= cj < w):
                        continue
                    if forbid_origin and cand == ORIGIN:
                        continue
                    if cand not in patch:
                        frontier.add(cand)
            if len(frontier) == ZERO:
                break
            patch.add(choice(tuple(frontier)))
        if len(patch) == target:
            return frozenset(patch)
    return frozenset()


def _point_shape_7ed72f31(
    diff_lb: float,
    diff_ub: float,
    gap: int,
) -> Indices:
    for _ in range(48):
        h = unifint(diff_lb, diff_ub, (TWO, SIX))
        w = unifint(diff_lb, diff_ub, (TWO, SIX))
        maxcells = h * w - (ONE if gap == ZERO else ZERO)
        if maxcells < THREE:
            continue
        mincells = max(THREE, min(maxcells, h + w - ONE))
        target = unifint(diff_lb, diff_ub, (mincells, maxcells))
        patch = _connected_patch_7ed72f31(h, w, target, gap == ZERO)
        if len(patch) == ZERO:
            continue
        if gap == ZERO and ORIGIN in patch:
            continue
        return patch
    return frozenset()


def _profile_walk_7ed72f31(
    length: int,
    depth: int,
) -> tuple[int, ...]:
    vals = [randint(ONE, depth)]
    for _ in range(length - ONE):
        prev = vals[-ONE]
        lb = max(ONE, prev - TWO)
        ub = min(depth, prev + TWO)
        vals.append(randint(lb, ub))
    if depth > ONE and len(set(vals)) == ONE and vals[ZERO] == depth:
        idx = randint(ZERO, length - ONE)
        vals[idx] = randint(max(ONE, depth - TWO), depth - ONE)
    return tuple(vals)


def _vertical_shape_7ed72f31(
    diff_lb: float,
    diff_ub: float,
) -> Indices:
    h = unifint(diff_lb, diff_ub, (THREE, SEVEN))
    w = unifint(diff_lb, diff_ub, (TWO, SIX))
    profile = _profile_walk_7ed72f31(h, w)
    return frozenset((i, j) for i, span in enumerate(profile) for j in range(w - span, w))


def _horizontal_shape_7ed72f31(
    diff_lb: float,
    diff_ub: float,
) -> Indices:
    h = unifint(diff_lb, diff_ub, (TWO, SIX))
    w = unifint(diff_lb, diff_ub, (THREE, SEVEN))
    profile = _profile_walk_7ed72f31(w, h)
    return frozenset((i, j) for j, span in enumerate(profile) for i in range(h - span, h))


def _point_pair_7ed72f31(
    diff_lb: float,
    diff_ub: float,
) -> tuple[Indices, Indices, Indices]:
    gap = choice((ZERO, ZERO, ONE))
    src0 = _point_shape_7ed72f31(diff_lb, diff_ub, gap)
    h, w = shape(src0)
    center = (h - ONE + gap, w - ONE + gap)
    offset = (h - ONE + gap + gap, w - ONE + gap + gap)
    src = shift(src0, offset)
    axis = initset(center)
    partner = mirror_patch_7ed72f31(src, axis)
    return src, axis, partner


def _vertical_pair_7ed72f31(
    diff_lb: float,
    diff_ub: float,
) -> tuple[Indices, Indices, Indices]:
    src = _vertical_shape_7ed72f31(diff_lb, diff_ub)
    axis = connect((ZERO, width(src)), (height(src) - ONE, width(src)))
    partner = mirror_patch_7ed72f31(src, axis)
    return src, axis, partner


def _horizontal_pair_7ed72f31(
    diff_lb: float,
    diff_ub: float,
) -> tuple[Indices, Indices, Indices]:
    src = _horizontal_shape_7ed72f31(diff_lb, diff_ub)
    axis = connect((height(src), ZERO), (height(src), width(src) - ONE))
    partner = mirror_patch_7ed72f31(src, axis)
    return src, axis, partner


def _hmirror_pair_patch_7ed72f31(
    patch: Patch,
    total_h: int,
) -> Indices:
    return frozenset((total_h - ONE - i, j) for i, j in toindices(patch))


def _vmirror_pair_patch_7ed72f31(
    patch: Patch,
    total_w: int,
) -> Indices:
    return frozenset((i, total_w - ONE - j) for i, j in toindices(patch))


def _orient_pair_7ed72f31(
    src: Indices,
    axis: Indices,
    partner: Indices,
) -> tuple[Indices, Indices, Indices]:
    footprint = combine(combine(src, axis), partner)
    total_h, total_w = shape(footprint)
    if choice((T, F)):
        src = _hmirror_pair_patch_7ed72f31(src, total_h)
        axis = _hmirror_pair_patch_7ed72f31(axis, total_h)
        partner = _hmirror_pair_patch_7ed72f31(partner, total_h)
    if choice((T, F)):
        src = _vmirror_pair_patch_7ed72f31(src, total_w)
        axis = _vmirror_pair_patch_7ed72f31(axis, total_w)
        partner = _vmirror_pair_patch_7ed72f31(partner, total_w)
    footprint = combine(combine(src, axis), partner)
    ul = ulcorner(footprint)
    offset = (-ul[ZERO], -ul[ONE])
    return shift(src, offset), shift(axis, offset), shift(partner, offset)


def _build_pair_7ed72f31(
    kind: str,
    diff_lb: float,
    diff_ub: float,
) -> tuple[Indices, Indices, Indices]:
    if kind == "point":
        return _point_pair_7ed72f31(diff_lb, diff_ub)
    if kind == "vline":
        return _vertical_pair_7ed72f31(diff_lb, diff_ub)
    return _horizontal_pair_7ed72f31(diff_lb, diff_ub)


def generate_7ed72f31(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    dims = MAX_DIMS_7ED72F31
    hmax, wmax = dims
    while True:
        bg = choice(tuple(c for c in range(TEN) if c != TWO))
        npairs = choice((TWO, THREE, THREE, THREE, FOUR))
        colors = sample(tuple(c for c in range(TEN) if c not in (bg, TWO)), npairs)
        kinds = [choice(PAIR_KINDS_7ED72F31) for _ in range(npairs)]
        if npairs >= THREE:
            kinds[ZERO] = "point"
            kinds[ONE] = choice(("vline", "hline"))
            shuffle(kinds)
        reserved = frozenset()
        placed = []
        failed = False
        for color, kind in zip(colors, kinds):
            placed_pair = None
            for _ in range(96):
                src, axis, partner = _build_pair_7ed72f31(kind, diff_lb, diff_ub)
                if len(src) == ZERO:
                    continue
                src, axis, partner = _orient_pair_7ed72f31(src, axis, partner)
                footprint = combine(combine(src, axis), partner)
                ph, pw = shape(footprint)
                if ph > hmax or pw > wmax:
                    continue
                locs = []
                for i in range(hmax - ph + ONE):
                    for j in range(wmax - pw + ONE):
                        moved = shift(footprint, (i, j))
                        padded = _pad_patch_7ed72f31(moved, ONE, dims)
                        if len(intersection(padded, reserved)) == ZERO:
                            locs.append((i, j))
                if len(locs) == ZERO:
                    continue
                offset = choice(locs)
                src = shift(src, offset)
                axis = shift(axis, offset)
                partner = shift(partner, offset)
                footprint = shift(footprint, offset)
                reserved = combine(reserved, _pad_patch_7ed72f31(footprint, ONE, dims))
                placed_pair = (color, src, axis, partner)
                break
            if placed_pair is None:
                failed = True
                break
            placed.append(placed_pair)
        if failed:
            continue
        gi = canvas(bg, dims)
        go = canvas(bg, dims)
        occ = frozenset()
        for color, src, axis, partner in placed:
            src_obj = recolor(color, src)
            axis_obj = recolor(TWO, axis)
            partner_obj = recolor(color, partner)
            gi = paint(paint(gi, axis_obj), src_obj)
            go = paint(paint(paint(go, axis_obj), src_obj), partner_obj)
            occ = combine(occ, combine(combine(src, axis), partner))
        top = uppermost(occ)
        bottom = lowermost(occ)
        left = leftmost(occ)
        right = rightmost(occ)
        mt = randint(ZERO, min(top, THREE))
        mb = randint(ZERO, min(hmax - ONE - bottom, THREE))
        ml = randint(ZERO, min(left, THREE))
        mr = randint(ZERO, min(wmax - ONE - right, THREE))
        loc = (top - mt, left - ml)
        shp = (bottom - top + ONE + mt + mb, right - left + ONE + ml + mr)
        gi = crop(gi, loc, shp)
        go = crop(go, loc, shp)
        if height(gi) < 14 or width(gi) < 14:
            continue
        if choice((T, F)):
            gi = hmirror(gi)
            go = hmirror(go)
        if choice((T, F)):
            gi = vmirror(gi)
            go = vmirror(go)
        if mostcolor(gi) != bg:
            continue
        try:
            if verify_7ed72f31(gi) != go:
                continue
        except Exception:
            continue
        return {"input": gi, "output": go}
