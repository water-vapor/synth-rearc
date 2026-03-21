from collections import deque

from arc2.core import *


TRANSFORMS_CC9053AA = (
    identity,
    rot90,
    rot180,
    rot270,
    hmirror,
    vmirror,
    lambda x: hmirror(rot90(x)),
    lambda x: vmirror(rot90(x)),
)


def _random_sparse_cols_cc9053aa(
    width: int,
    limit: int = TWO,
):
    x0 = tuple(x1 for x1 in range(TWO, width - TWO) if x1 % TWO == ZERO)
    if len(x0) == ZERO:
        return set()
    x2 = randint(ZERO, min(limit, len(x0)))
    if x2 == ZERO:
        return set()
    return set(sample(x0, x2))


def _striped_canvas_cc9053aa(
    height: int,
    width: int,
    extras: dict,
):
    x0 = canvas(ZERO, (height + TWO, width + TWO))
    for x1 in range(height):
        if x1 % TWO == ZERO:
            x2 = frozenset((x1 + ONE, x3 + ONE) for x3 in range(width))
        else:
            x3 = set(extras.get(x1, set()))
            x3 |= {ZERO, width - ONE}
            x2 = frozenset((x1 + ONE, x4 + ONE) for x4 in x3)
        x0 = fill(x0, EIGHT, x2)
    return x0


def _safe_cells_and_entries_cc9053aa(
    I: Grid,
):
    x0 = ofcolor(I, EIGHT)
    x1 = ofcolor(I, SEVEN)
    x2 = ofcolor(I, NINE)
    x3 = frozenset(x4 for x4 in x0 if len(dneighbors(x4) & x1) > ZERO)
    x4 = difference(x0, x3)
    x5 = tuple(sorted({x7 for x6 in x2 for x7 in dneighbors(x6) if x7 in x0}))
    return x4, x5


def _trace_path_cc9053aa(
    I: Grid,
):
    x0, x1 = _safe_cells_and_entries_cc9053aa(I)
    if len(x1) != TWO:
        return None, ZERO
    x2 = x1[ZERO]
    x3 = x1[ONE]
    x4 = deque((x2,))
    x5 = {x2: ZERO}
    x6 = {x2: ONE}
    x7 = {x2: None}
    while len(x4) > ZERO:
        x8 = x4.popleft()
        for x9 in sorted(dneighbors(x8)):
            if x9 not in x0:
                continue
            x10 = x5[x8] + ONE
            if x9 not in x5:
                x5[x9] = x10
                x6[x9] = x6[x8]
                x7[x9] = x8
                x4.append(x9)
            elif x5[x9] == x10:
                x6[x9] += x6[x8]
    if x3 not in x5:
        return None, ZERO
    x11 = []
    x12 = x3
    while x12 is not None:
        x11.append(x12)
        x12 = x7[x12]
    return frozenset(x11), x6[x3]


def _make_left_right_cc9053aa(
    diff_lb: float,
    diff_ub: float,
):
    x0 = subtract(double(unifint(diff_lb, diff_ub, (THREE, FIVE))), ONE)
    x1 = subtract(double(unifint(diff_lb, diff_ub, (FOUR, SEVEN))), ONE)
    x2 = {x3: _random_sparse_cols_cc9053aa(x1) for x3 in range(ONE, x0, TWO)}
    x3 = tuple(range(TWO, x0 - ONE, TWO))
    x4 = choice(x3)
    x5 = choice((True, False))
    x6 = subtract(x4, ONE) if x5 else add(x4, ONE)
    x7 = _striped_canvas_cc9053aa(x0, x1, x2)
    x8 = x1 // TWO
    x7 = fill(x7, SEVEN, {(x6 + ONE, x8 + ONE)})
    x7 = fill(x7, NINE, {(x4 + ONE, ZERO), (x4 + ONE, x1 + ONE)})
    return x7


def _make_same_side_cc9053aa(
    diff_lb: float,
    diff_ub: float,
):
    x0 = subtract(double(unifint(diff_lb, diff_ub, (FOUR, SIX))), ONE)
    x1 = subtract(double(unifint(diff_lb, diff_ub, (FOUR, SEVEN))), ONE)
    x2 = randint(ONE, (x0 - THREE) // TWO)
    x3 = {}
    for x4 in range(ONE, x0, TWO):
        x5 = x4 < double(x2) + ONE
        x3[x4] = set() if x5 else _random_sparse_cols_cc9053aa(x1)
    x6 = _striped_canvas_cc9053aa(x0, x1, x3)
    x7 = x1 // TWO
    for x8 in range(ONE, double(x2), TWO):
        x6 = fill(x6, SEVEN, {(x8 + ONE, x7 + ONE)})
    x6 = fill(x6, NINE, {(ZERO, ONE), (ZERO, x1)})
    return x6


def _make_split_vertical_cc9053aa(
    diff_lb: float,
    diff_ub: float,
):
    x0 = subtract(double(unifint(diff_lb, diff_ub, (FOUR, SIX))), ONE)
    x1 = subtract(double(unifint(diff_lb, diff_ub, (FOUR, SEVEN))), ONE)
    x2 = x0 // TWO
    x3 = x1 // TWO
    x4 = {}
    for x5 in range(ONE, x0, TWO):
        if x5 == x2:
            x4[x5] = {x3}
        elif x5 in {ONE, x0 - TWO}:
            x4[x5] = set()
        else:
            x4[x5] = _random_sparse_cols_cc9053aa(x1, ONE)
    x6 = _striped_canvas_cc9053aa(x0, x1, x4)
    x7 = max(TWO, subtract(x3, ONE))
    x8 = min(x1 - THREE, add(x3, ONE))
    x6 = fill(x6, SEVEN, {(TWO, x7 + ONE), (x0 - ONE, x8 + ONE)})
    x6 = fill(x6, NINE, {(ZERO, x3 + ONE), (x0 + ONE, x3 + ONE)})
    return x6


def generate_cc9053aa(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    x0 = (
        _make_left_right_cc9053aa,
        _make_same_side_cc9053aa,
        _make_split_vertical_cc9053aa,
    )
    while True:
        x1 = choice(x0)
        x2 = x1(diff_lb, diff_ub)
        x3, x4 = _trace_path_cc9053aa(x2)
        if x3 is None or x4 != ONE:
            continue
        if mostcolor(x2) != ZERO:
            continue
        x5 = fill(x2, NINE, x3)
        x6 = choice(TRANSFORMS_CC9053AA)
        x7 = x6(x2)
        x8 = x6(x5)
        return {"input": x7, "output": x8}
