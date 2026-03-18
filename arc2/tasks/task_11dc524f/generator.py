from arc2.core import *


GRID_SHAPE = (13, 13)
SIDES = ("left", "right", "up", "down")
SQUARE = frozenset({(ZERO, ZERO), (ZERO, ONE), (ONE, ZERO), (ONE, ONE)})
BASE_SHAPES = (
    frozenset({(ZERO, ZERO), (ONE, ONE), (TWO, ZERO), (TWO, ONE)}),
    frozenset({(ZERO, ZERO), (ONE, ZERO), (TWO, ZERO), (TWO, ONE)}),
    frozenset({(ZERO, ONE), (ZERO, TWO), (ONE, ONE), (TWO, ZERO)}),
    frozenset({(ZERO, ONE), (ONE, ZERO), (ONE, ONE), (TWO, ZERO)}),
)


def _normalize(patch: Indices) -> Indices:
    return shift(patch, (-uppermost(patch), -leftmost(patch)))


def _shape_library() -> tuple[Indices, ...]:
    shapes = set()
    for shape in BASE_SHAPES:
        shapes.add(shape)
        shapes.add(_normalize(hmirror(shape)))
        shapes.add(_normalize(vmirror(shape)))
        shapes.add(_normalize(hmirror(vmirror(shape))))
    return tuple(shapes)


SHAPES = _shape_library()


def _in_bounds(patch: Indices) -> bool:
    return all(ZERO <= i < GRID_SHAPE[0] and ZERO <= j < GRID_SHAPE[1] for i, j in patch)


def _partner_patch(moved: Indices, side: str) -> Indices:
    if side == "left":
        return shift(vmirror(moved), (ZERO, width(moved)))
    if side == "right":
        return shift(vmirror(moved), (ZERO, -width(moved)))
    if side == "up":
        return shift(hmirror(moved), (height(moved), ZERO))
    return shift(hmirror(moved), (-height(moved), ZERO))


def _square_patch(loc: tuple[int, int]) -> Indices:
    return shift(SQUARE, loc)


def _adjacent_candidates(shape: Indices, square: Indices, side: str) -> tuple[Indices, ...]:
    si, sj = ulcorner(square)
    h = height(shape)
    w = width(shape)
    candidates = []
    if side == "left":
        mj = sj - w
        if mj < ZERO:
            return ()
        for mi in range(GRID_SHAPE[0] - h + ONE):
            moved = shift(shape, (mi, mj))
            if adjacent(moved, square) and _in_bounds(_partner_patch(moved, side)):
                candidates.append(moved)
    elif side == "right":
        mj = sj + TWO
        if mj + w > GRID_SHAPE[1]:
            return ()
        for mi in range(GRID_SHAPE[0] - h + ONE):
            moved = shift(shape, (mi, mj))
            if adjacent(moved, square) and _in_bounds(_partner_patch(moved, side)):
                candidates.append(moved)
    elif side == "up":
        mi = si - h
        if mi < ZERO:
            return ()
        for mj in range(GRID_SHAPE[1] - w + ONE):
            moved = shift(shape, (mi, mj))
            if adjacent(moved, square) and _in_bounds(_partner_patch(moved, side)):
                candidates.append(moved)
    else:
        mi = si + TWO
        if mi + h > GRID_SHAPE[0]:
            return ()
        for mj in range(GRID_SHAPE[1] - w + ONE):
            moved = shift(shape, (mi, mj))
            if adjacent(moved, square) and _in_bounds(_partner_patch(moved, side)):
                candidates.append(moved)
    return tuple(candidates)


def _max_gap(moved: Indices, side: str) -> int:
    if side == "left":
        return leftmost(moved)
    if side == "right":
        return GRID_SHAPE[1] - ONE - rightmost(moved)
    if side == "up":
        return uppermost(moved)
    return GRID_SHAPE[0] - ONE - lowermost(moved)


def _away_offset(gap: int, side: str) -> tuple[int, int]:
    if side == "left":
        return (ZERO, -gap)
    if side == "right":
        return (ZERO, gap)
    if side == "up":
        return (-gap, ZERO)
    return (gap, ZERO)


def generate_11dc524f(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        shape = choice(SHAPES)
        side = choice(SIDES)
        square_loc = (randint(TWO, EIGHT), randint(TWO, EIGHT))
        square = _square_patch(square_loc)
        moved_candidates = _adjacent_candidates(shape, square, side)
        if len(moved_candidates) == ZERO:
            continue
        moved = choice(moved_candidates)
        gapub = min(_max_gap(moved, side), SIX)
        if gapub < TWO:
            continue
        gap = unifint(diff_lb, diff_ub, (TWO, gapub))
        src = shift(moved, _away_offset(gap, side))
        partner = _partner_patch(moved, side)
        if not _in_bounds(src):
            continue
        gi = canvas(SEVEN, GRID_SHAPE)
        gi = fill(gi, TWO, src)
        gi = fill(gi, FIVE, square)
        go = canvas(SEVEN, GRID_SHAPE)
        go = fill(go, TWO, moved)
        go = fill(go, FIVE, partner)
        return {"input": gi, "output": go}
