from arc2.core import *

from .verifier import verify_320afe60


GRID_HEIGHT_320AFE60 = 22
GRID_WIDTH_BOUNDS_320AFE60 = (18, 28)
BACKGROUND_320AFE60 = FOUR
INPUT_COLOR_320AFE60 = ONE
LEFT_COLOR_320AFE60 = TWO
RIGHT_COLOR_320AFE60 = THREE
SIDE_ORDER_320AFE60 = ("top", "bottom", "left", "right")
SINGLE_SIDES_320AFE60 = ("top", "bottom", "left", "right")
CORNERS_320AFE60 = ("tl", "tr", "bl", "br")
TRIPLE_SIDES_320AFE60 = ("left", "right")
SHAPE_ATTEMPTS_320AFE60 = 64


def _full_rect_320afe60(
    h: Integer,
    w: Integer,
) -> Indices:
    return frozenset((i, j) for i in range(h) for j in range(w))


def _side_patch_320afe60(
    h: Integer,
    w: Integer,
    side: str,
) -> Indices:
    if equality(side, "top"):
        return frozenset((ZERO, j) for j in range(w))
    if equality(side, "bottom"):
        return frozenset((decrement(h), j) for j in range(w))
    if equality(side, "left"):
        return frozenset((i, ZERO) for i in range(h))
    return frozenset((i, decrement(w)) for i in range(h))


def _open_sides_320afe60(
    patch: Indices,
) -> tuple[str, ...]:
    h, w = shape(patch)
    x0 = []
    for side in SIDE_ORDER_320AFE60:
        if not _side_patch_320afe60(h, w, side) <= patch:
            x0.append(side)
    return tuple(x0)


def _touches_all_sides_320afe60(
    patch: Indices,
) -> Boolean:
    h, w = shape(patch)
    return all(len(patch & _side_patch_320afe60(h, w, side)) > ZERO for side in SIDE_ORDER_320AFE60)


def _connected_320afe60(
    patch: Indices,
) -> Boolean:
    x0 = next(iter(patch))
    x1 = {x0}
    x2 = [x0]
    while len(x2) > ZERO:
        x3 = x2.pop()
        for x4 in dneighbors(x3):
            if x4 in patch and x4 not in x1:
                x1.add(x4)
                x2.append(x4)
    return equality(len(x1), len(patch))


def _valid_shape_320afe60(
    patch: Indices,
    target: tuple[str, ...],
) -> Boolean:
    if len(patch) < TWO:
        return F
    if flip(_connected_320afe60(patch)):
        return F
    if flip(_touches_all_sides_320afe60(patch)):
        return F
    return equality(_open_sides_320afe60(patch), target)


def _maybe_interior_hole_320afe60(
    patch: Indices,
    target: tuple[str, ...],
) -> Indices:
    h, w = shape(patch)
    if h < FOUR or w < FOUR:
        return patch
    if choice((T, F, F)) is F:
        return patch
    for _ in range(16):
        hh = randint(ONE, subtract(h, TWO))
        ww = randint(ONE, subtract(w, TWO))
        if hh >= h or ww >= w:
            continue
        top = randint(ONE, subtract(subtract(h, hh), ONE))
        left = randint(ONE, subtract(subtract(w, ww), ONE))
        hole = frozenset((i, j) for i in range(top, add(top, hh)) for j in range(left, add(left, ww)))
        cand = difference(patch, hole)
        if _valid_shape_320afe60(cand, target):
            return cand
    return patch


def _sample_closed_shape_320afe60(
    max_width: Integer,
) -> Indices:
    for _ in range(SHAPE_ATTEMPTS_320AFE60):
        h = choice((TWO, TWO, THREE, THREE, THREE, FOUR, FOUR, FIVE))
        w = choice(tuple(v for v in (TWO, TWO, THREE, THREE, FOUR, FOUR, FIVE, SIX) if v <= max_width))
        x0 = _full_rect_320afe60(h, w)
        x1 = _maybe_interior_hole_320afe60(x0, ())
        if _valid_shape_320afe60(x1, ()):
            return x1
    return frozenset({(ZERO, ZERO), (ZERO, ONE), (ONE, ZERO), (ONE, ONE)})


def _side_notch_320afe60(
    h: Integer,
    w: Integer,
    side: str,
) -> Indices | None:
    if side in ("top", "bottom"):
        if w < THREE:
            return None
        span = randint(ONE, subtract(w, TWO))
        start = randint(ONE, subtract(subtract(w, span), ONE))
        depth = randint(ONE, subtract(h, ONE))
        rows = range(depth) if equality(side, "top") else range(subtract(h, depth), h)
        cols = range(start, add(start, span))
        return frozenset((i, j) for i in rows for j in cols)
    if h < THREE:
        return None
    span = randint(ONE, subtract(h, TWO))
    start = randint(ONE, subtract(subtract(h, span), ONE))
    depth = randint(ONE, subtract(w, ONE))
    rows = range(start, add(start, span))
    cols = range(depth) if equality(side, "left") else range(subtract(w, depth), w)
    return frozenset((i, j) for i in rows for j in cols)


def _sample_single_open_shape_320afe60(
    max_width: Integer,
) -> Indices:
    side = choice(SINGLE_SIDES_320AFE60)
    target = (side,)
    for _ in range(SHAPE_ATTEMPTS_320AFE60):
        if side in ("top", "bottom"):
            h = choice((TWO, THREE, THREE, FOUR, FOUR, FIVE, SIX))
            w = choice(tuple(v for v in (THREE, FOUR, FOUR, FIVE, FIVE, SIX, SEVEN, EIGHT) if v <= max_width))
        else:
            h = choice((THREE, THREE, FOUR, FOUR, FIVE, FIVE, SIX))
            w = choice(tuple(v for v in (TWO, THREE, THREE, FOUR, FIVE, SIX, SEVEN) if v <= max_width))
        x0 = _side_notch_320afe60(h, w, side)
        if x0 is None:
            continue
        x1 = difference(_full_rect_320afe60(h, w), x0)
        x2 = _maybe_interior_hole_320afe60(x1, target)
        if _valid_shape_320afe60(x2, target):
            return x2
    return frozenset({(ZERO, ZERO), (ONE, ZERO), (ONE, ONE), (ZERO, TWO), (ONE, TWO)})


def _corner_notch_320afe60(
    h: Integer,
    w: Integer,
    corner: str,
) -> Indices:
    dh = randint(ONE, subtract(h, ONE))
    dw = randint(ONE, subtract(w, ONE))
    if equality(corner, "tl"):
        rows = range(dh)
        cols = range(dw)
    elif equality(corner, "tr"):
        rows = range(dh)
        cols = range(subtract(w, dw), w)
    elif equality(corner, "bl"):
        rows = range(subtract(h, dh), h)
        cols = range(dw)
    else:
        rows = range(subtract(h, dh), h)
        cols = range(subtract(w, dw), w)
    return frozenset((i, j) for i in rows for j in cols)


def _sample_double_open_shape_320afe60(
    max_width: Integer,
) -> Indices:
    corner = choice(CORNERS_320AFE60)
    target_map = {
        "tl": ("top", "left"),
        "tr": ("top", "right"),
        "bl": ("bottom", "left"),
        "br": ("bottom", "right"),
    }
    target = target_map[corner]
    for _ in range(SHAPE_ATTEMPTS_320AFE60):
        h = choice((THREE, THREE, FOUR, FOUR, FIVE, SIX))
        w = choice(tuple(v for v in (THREE, FOUR, FIVE, FIVE, SIX, SEVEN, EIGHT, NINE) if v <= max_width))
        x0 = difference(_full_rect_320afe60(h, w), _corner_notch_320afe60(h, w, corner))
        x1 = _maybe_interior_hole_320afe60(x0, target)
        if _valid_shape_320afe60(x1, target):
            return x1
    return frozenset({(ZERO, ONE), (ZERO, TWO), (ONE, ZERO), (ONE, ONE), (ONE, TWO), (TWO, ZERO), (TWO, ONE), (TWO, TWO)})


def _double_corner_notch_320afe60(
    h: Integer,
    w: Integer,
    side: str,
) -> Indices | None:
    if equality(side, "left"):
        if h < FOUR:
            return None
        dh0 = randint(ONE, max(ONE, h // TWO))
        dh1 = randint(ONE, max(ONE, h // TWO))
        if add(dh0, dh1) >= h:
            return None
        dw0 = randint(ONE, subtract(w, ONE))
        dw1 = randint(ONE, subtract(w, ONE))
        x0 = frozenset((i, j) for i in range(dh0) for j in range(dw0))
        x1 = frozenset((i, j) for i in range(subtract(h, dh1), h) for j in range(dw1))
        return combine(x0, x1)
    if equality(side, "right"):
        if h < FOUR:
            return None
        dh0 = randint(ONE, max(ONE, h // TWO))
        dh1 = randint(ONE, max(ONE, h // TWO))
        if add(dh0, dh1) >= h:
            return None
        dw0 = randint(ONE, subtract(w, ONE))
        dw1 = randint(ONE, subtract(w, ONE))
        x0 = frozenset((i, j) for i in range(dh0) for j in range(subtract(w, dw0), w))
        x1 = frozenset((i, j) for i in range(subtract(h, dh1), h) for j in range(subtract(w, dw1), w))
        return combine(x0, x1)
    return None


def _sample_triple_open_shape_320afe60(
    max_width: Integer,
) -> Indices:
    side = choice(TRIPLE_SIDES_320AFE60)
    target = ("top", "bottom", side)
    for _ in range(SHAPE_ATTEMPTS_320AFE60):
        h = choice((FOUR, FIVE, FIVE, SIX))
        w = choice(tuple(v for v in (FOUR, FIVE, SIX, SIX, SEVEN, EIGHT) if v <= max_width))
        x0 = _double_corner_notch_320afe60(h, w, side)
        if x0 is None:
            continue
        x1 = difference(_full_rect_320afe60(h, w), x0)
        x2 = _maybe_interior_hole_320afe60(x1, target)
        if _valid_shape_320afe60(x2, target):
            return x2
    return frozenset(
        {
            (ZERO, ONE),
            (ZERO, TWO),
            (ZERO, THREE),
            (ONE, ZERO),
            (ONE, ONE),
            (ONE, TWO),
            (ONE, THREE),
            (TWO, ZERO),
            (TWO, ONE),
            (TWO, TWO),
            (TWO, THREE),
            (THREE, ONE),
            (THREE, TWO),
            (THREE, THREE),
        }
    )


def _sample_shape_320afe60(
    kind: str,
    max_width: Integer,
) -> tuple[Indices, Boolean]:
    if equality(kind, "single"):
        return _sample_single_open_shape_320afe60(max_width), T
    if equality(kind, "multi"):
        if choice((T, T, F)):
            return _sample_double_open_shape_320afe60(max_width), F
        return _sample_triple_open_shape_320afe60(max_width), F
    return _sample_closed_shape_320afe60(max_width), F


def _kind_vector_320afe60(
    nobj: Integer,
) -> tuple[str, ...]:
    nmovers = randint(ONE, subtract(nobj, ONE))
    x0 = ["single"] * nmovers
    while len(x0) < nobj:
        x0.append(choice(("closed", "closed", "multi")))
    shuffle(x0)
    return tuple(x0)


def _row_starts_320afe60(
    heights: tuple[Integer, ...],
) -> tuple[Integer, ...] | None:
    slack = subtract(GRID_HEIGHT_320AFE60, add(sum(heights), decrement(len(heights))))
    if slack < ZERO:
        return None
    extras = [ZERO] * add(len(heights), ONE)
    for _ in range(slack):
        extras[randint(ZERO, len(heights))] += ONE
    x0 = []
    cursor = extras[ZERO]
    for idx, h in enumerate(heights):
        x0.append(cursor)
        cursor += h
        if idx < decrement(len(heights)):
            cursor += ONE + extras[add(idx, ONE)]
    return tuple(x0)


def _input_col_320afe60(
    grid_w: Integer,
    obj_w: Integer,
) -> Integer:
    slack = subtract(grid_w, obj_w)
    if slack <= FOUR:
        return randint(ZERO, slack)
    return randint(TWO, subtract(slack, TWO))


def _render_input_320afe60(
    grid_w: Integer,
    patches: tuple[Indices, ...],
) -> Grid:
    x0 = canvas(BACKGROUND_320AFE60, (GRID_HEIGHT_320AFE60, grid_w))
    for patch in patches:
        x0 = paint(x0, recolor(INPUT_COLOR_320AFE60, patch))
    return x0


def _render_output_320afe60(
    grid_w: Integer,
    patches: tuple[Indices, ...],
    movers: tuple[Boolean, ...],
) -> Grid:
    x0 = canvas(BACKGROUND_320AFE60, (GRID_HEIGHT_320AFE60, grid_w))
    for patch, mover in zip(patches, movers):
        if mover:
            x1 = shift(patch, (ZERO, subtract(decrement(grid_w), rightmost(patch))))
            x0 = paint(x0, recolor(RIGHT_COLOR_320AFE60, x1))
        else:
            x2 = shift(patch, (ZERO, invert(leftmost(patch))))
            x0 = paint(x0, recolor(LEFT_COLOR_320AFE60, x2))
    return x0


def generate_320afe60(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        grid_w = unifint(diff_lb, diff_ub, GRID_WIDTH_BOUNDS_320AFE60)
        nobj = choice((THREE, THREE, FOUR, FOUR, FIVE))
        kinds = _kind_vector_320afe60(nobj)
        specs = []
        max_width = min(NINE, subtract(grid_w, TWO))
        for kind in kinds:
            patch, mover = _sample_shape_320afe60(kind, max_width)
            specs.append((patch, mover))
        heights = tuple(height(patch) for patch, _ in specs)
        starts = _row_starts_320afe60(heights)
        if starts is None:
            continue
        placed = []
        movers = []
        for start, (patch, mover) in zip(starts, specs):
            col = _input_col_320afe60(grid_w, width(patch))
            placed.append(shift(patch, (start, col)))
            movers.append(mover)
        if all(movers) or flip(any(movers)):
            continue
        gi = _render_input_320afe60(grid_w, tuple(placed))
        go = _render_output_320afe60(grid_w, tuple(placed), tuple(movers))
        if verify_320afe60(gi) != go:
            continue
        return {"input": gi, "output": go}
