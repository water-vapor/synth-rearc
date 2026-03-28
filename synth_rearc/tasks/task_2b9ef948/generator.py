from synth_rearc.core import *
from .verifier import verify_2b9ef948


MARKER_COLORS_2B9EF948 = (ONE, THREE, SIX, SEVEN, EIGHT)
RING_FRAME_2B9EF948 = box(frozenset({ORIGIN, TWO_BY_TWO}))


def _bbox_2b9ef948(patch: Patch) -> tuple[int, int, int, int]:
    return (
        uppermost(patch),
        leftmost(patch),
        lowermost(patch),
        rightmost(patch),
    )


def _pad_bbox_2b9ef948(
    patch: Patch,
    shape_: IntegerTuple,
    pad: int,
) -> Indices:
    h, w = shape_
    top, left, bottom, right = _bbox_2b9ef948(patch)
    top = max(ZERO, top - pad)
    left = max(ZERO, left - pad)
    bottom = min(h - ONE, bottom + pad)
    right = min(w - ONE, right + pad)
    return frozenset(
        (i, j)
        for i in range(top, bottom + ONE)
        for j in range(left, right + ONE)
    )


def _ring_patch_2b9ef948(center_: IntegerTuple) -> Indices:
    return shift(RING_FRAME_2B9EF948, subtract(center_, UNITY))


def _ring_object_2b9ef948(
    center_: IntegerTuple,
    marker_color: int,
) -> Object:
    x0 = _ring_patch_2b9ef948(center_)
    x1 = recolor(FOUR, x0)
    x2 = frozenset({(marker_color, center_)})
    return x1 | x2


def _render_output_2b9ef948(
    shape_: IntegerTuple,
    center_: IntegerTuple,
    marker_color: int,
) -> Grid:
    x0 = canvas(marker_color, shape_)
    x1 = shoot(center_, UNITY)
    x2 = shoot(center_, NEG_UNITY)
    x3 = combine(x1, x2)
    x4 = shoot(center_, UP_RIGHT)
    x5 = shoot(center_, DOWN_LEFT)
    x6 = combine(x3, x4)
    x7 = combine(x6, x5)
    x8 = _ring_patch_2b9ef948(center_)
    x9 = combine(x7, x8)
    x10 = difference(x9, initset(center_))
    return fill(x0, FOUR, x10)


def _normalize_layout_2b9ef948(
    path: Indices,
    marker: IntegerTuple,
    endpoint: IntegerTuple,
) -> tuple[Indices, IntegerTuple, IntegerTuple]:
    x0 = combine(path, frozenset({marker, endpoint}))
    x1 = invert(ulcorner(x0))
    x2 = shift(path, x1)
    x3 = add(marker, x1)
    x4 = add(endpoint, x1)
    return x2, x3, x4


def _line_path_2b9ef948(endpoint: IntegerTuple) -> Indices:
    x0 = connect(ORIGIN, endpoint)
    x1 = frozenset({ORIGIN, endpoint})
    return difference(x0, x1)


def _elbow_path_2b9ef948(
    endpoint: IntegerTuple,
    horizontal_first: bool,
) -> Indices:
    di, dj = endpoint
    bend = (ZERO, dj) if horizontal_first else (di, ZERO)
    x0 = connect(ORIGIN, bend)
    x1 = connect(bend, endpoint)
    x2 = combine(x0, x1)
    x3 = frozenset({ORIGIN, endpoint})
    return difference(x2, x3)


def _u_path_2b9ef948(
    endpoint: IntegerTuple,
    extend_horizontal: bool,
    extra: int,
) -> Indices:
    di, dj = endpoint
    if extend_horizontal:
        step = ONE if dj > ZERO else NEG_ONE
        far = dj + step * extra
        bend0 = (ZERO, far)
        bend1 = (di, far)
    else:
        step = ONE if di > ZERO else NEG_ONE
        far = di + step * extra
        bend0 = (far, ZERO)
        bend1 = (far, dj)
    x0 = connect(ORIGIN, bend0)
    x1 = connect(bend0, bend1)
    x2 = connect(bend1, endpoint)
    x3 = combine(x0, x1)
    x4 = combine(x3, x2)
    x5 = frozenset({ORIGIN, endpoint})
    return difference(x4, x5)


def _sample_aux_layout_2b9ef948(
    endpoint: IntegerTuple,
) -> tuple[Indices, IntegerTuple, IntegerTuple]:
    di, dj = endpoint
    if di == ZERO or dj == ZERO:
        x0 = _line_path_2b9ef948(endpoint)
        return _normalize_layout_2b9ef948(x0, ORIGIN, endpoint)
    x0 = choice(("elbow_h", "elbow_v", "elbow_h", "elbow_v", "u_h", "u_v"))
    if x0 == "elbow_h":
        x1 = _elbow_path_2b9ef948(endpoint, T)
    elif x0 == "elbow_v":
        x1 = _elbow_path_2b9ef948(endpoint, F)
    elif x0 == "u_h":
        x1 = _u_path_2b9ef948(endpoint, T, choice((ONE, ONE, TWO, TWO, THREE)))
    else:
        x1 = _u_path_2b9ef948(endpoint, F, choice((ONE, ONE, TWO, TWO, THREE)))
    return _normalize_layout_2b9ef948(x1, ORIGIN, endpoint)


def _sample_vector_2b9ef948(shape_: IntegerTuple) -> IntegerTuple:
    h, w = shape_
    maxi = min(SIX, h - THREE)
    maxj = min(SIX, w - THREE)
    for _ in range(400):
        di = randint(-maxi, maxi)
        dj = randint(-maxj, maxj)
        if (di, dj) == ORIGIN:
            continue
        if abs(di) + abs(dj) < THREE:
            continue
        if di != ZERO and dj != ZERO and abs(di) + abs(dj) < FOUR:
            continue
        return (di, dj)
    raise RuntimeError("failed to sample vector")


def _sample_ring_center_2b9ef948(
    shape_: IntegerTuple,
    offset: IntegerTuple,
) -> IntegerTuple:
    h, w = shape_
    di, dj = offset
    rows = tuple(i for i in range(ONE, h - ONE) if ONE <= i + di < h - ONE)
    cols = tuple(j for j in range(ONE, w - ONE) if ONE <= j + dj < w - ONE)
    if len(rows) == ZERO or len(cols) == ZERO:
        raise RuntimeError("no valid ring center")
    return (choice(rows), choice(cols))


def _place_aux_layout_2b9ef948(
    shape_: IntegerTuple,
    path: Indices,
    marker: IntegerTuple,
    endpoint: IntegerTuple,
    blocked: Indices,
) -> tuple[Indices, IntegerTuple, IntegerTuple] | None:
    h, w = shape_
    x0 = combine(path, frozenset({marker, endpoint}))
    rows = tuple(range(ONE, h - height(x0)))
    cols = tuple(range(ONE, w - width(x0)))
    if len(rows) == ZERO or len(cols) == ZERO:
        return None
    for _ in range(400):
        offset = (choice(rows), choice(cols))
        x1 = shift(x0, offset)
        if len(intersection(x1, blocked)) != ZERO:
            continue
        x2 = shift(path, offset)
        x3 = add(marker, offset)
        x4 = add(endpoint, offset)
        return x2, x3, x4
    return None


def _aux_object_2b9ef948(
    path: Indices,
    marker: IntegerTuple,
    endpoint: IntegerTuple,
    marker_color: int,
) -> Object:
    x0 = recolor(FIVE, path)
    x1 = frozenset({(marker_color, marker), (FOUR, endpoint)})
    return x0 | x1


def generate_2b9ef948(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        h = unifint(diff_lb, diff_ub, (12, 30))
        w = unifint(diff_lb, diff_ub, (13, 30))
        shape_ = (h, w)
        marker_color = choice(MARKER_COLORS_2B9EF948)
        offset = _sample_vector_2b9ef948(shape_)
        source_center = _sample_ring_center_2b9ef948(shape_, offset)
        target_center = add(source_center, offset)
        ring_patch = _ring_patch_2b9ef948(source_center)
        blocked = _pad_bbox_2b9ef948(ring_patch, shape_, TWO)
        layout = None
        for _ in range(200):
            path, marker, endpoint = _sample_aux_layout_2b9ef948(offset)
            layout = _place_aux_layout_2b9ef948(shape_, path, marker, endpoint, blocked)
            if layout is not None:
                break
        if layout is None:
            continue
        path, marker, endpoint = layout
        gi = canvas(ZERO, shape_)
        gi = paint(gi, _ring_object_2b9ef948(source_center, marker_color))
        gi = paint(gi, _aux_object_2b9ef948(path, marker, endpoint, marker_color))
        go = _render_output_2b9ef948(shape_, target_center, marker_color)
        if gi == go:
            continue
        try:
            valid = verify_2b9ef948(gi) == go
        except Exception:
            valid = False
        if not valid:
            continue
        return {"input": gi, "output": go}
