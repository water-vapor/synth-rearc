from synth_rearc.core import *


GRID_SIZE_1478ab18 = EIGHT
SPAN_BAG_1478ab18 = (
    THREE,
    THREE,
    FOUR,
    FOUR,
    FIVE,
    FIVE,
    SIX,
    SEVEN,
)


def _diag_length_1478ab18(
    pair: tuple[IntegerTuple, IntegerTuple],
) -> Integer:
    a, b = pair
    return abs(a[0] - b[0])


def _longest_diagonal_pair_1478ab18(
    points: tuple[IntegerTuple, ...],
) -> tuple[IntegerTuple, IntegerTuple] | None:
    pairs = []
    for a in points:
        for b in points:
            if not (a < b):
                continue
            if abs(a[0] - b[0]) != abs(a[1] - b[1]):
                continue
            pairs.append((a, b))
    if len(pairs) == ZERO:
        return None
    best = max(pairs, key=_diag_length_1478ab18)
    bestlen = _diag_length_1478ab18(best)
    if sum(_diag_length_1478ab18(pair) == bestlen for pair in pairs) != ONE:
        return None
    return best


def _triangle_1478ab18(
    a: IntegerTuple,
    b: IntegerTuple,
    c: IntegerTuple,
) -> Indices:
    x0 = connect(a, b)
    x1 = connect(a, c)
    x2 = connect(b, c)
    x3 = combine(x0, x1)
    return combine(x2, x3)


def generate_1478ab18(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    del diff_lb, diff_ub
    while True:
        span = choice(SPAN_BAG_1478ab18)
        limit = GRID_SIZE_1478ab18 - span - ONE
        top = randint(ZERO, limit)
        left = randint(ZERO, limit)
        tl = (top, left)
        tr = (top, left + span)
        bl = (top + span, left)
        br = (top + span, left + span)
        corners = (tl, tr, bl, br)
        missing = choice(corners)
        present = tuple(corner for corner in corners if corner != missing)
        pair = _longest_diagonal_pair_1478ab18(present)
        if pair is None:
            continue
        extra_corner = next(corner for corner in present if corner not in pair)
        triangle = _triangle_1478ab18(first(pair), last(pair), missing)
        inactive_diagonal = tuple(cell for cell in connect(missing, extra_corner) if cell not in corners)
        box = tuple(
            (i, j)
            for i in range(top, top + span + ONE)
            for j in range(left, left + span + ONE)
        )
        candidates = tuple(cell for cell in box if cell not in triangle and cell not in corners)
        if len(candidates) == ZERO:
            continue
        preferred = tuple(cell for cell in inactive_diagonal if cell in candidates)
        pool = preferred * FOUR + tuple(cell for cell in candidates if cell not in preferred)
        distractor = choice(pool)
        markers = present + (distractor,)
        best = _longest_diagonal_pair_1478ab18(markers)
        if best is None or set(best) != set(pair):
            continue
        gi = canvas(SEVEN, (GRID_SIZE_1478ab18, GRID_SIZE_1478ab18))
        gi = fill(gi, FIVE, frozenset(markers))
        go = fill(gi, EIGHT, triangle)
        go = fill(go, FIVE, frozenset(markers))
        return {"input": gi, "output": go}
