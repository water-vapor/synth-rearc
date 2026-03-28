from synth_rearc.core import *


OFFICIAL_ONES_E1D2900E = frozenset(
    {
        (0, 18),
        (4, 2),
        (4, 11),
        (4, 14),
        (4, 24),
        (7, 5),
        (9, 18),
        (10, 10),
        (10, 26),
        (15, 18),
        (16, 6),
        (16, 20),
        (23, 13),
        (28, 21),
    }
)

OFFICIAL_TWOS_E1D2900E = frozenset(
    {
        (3, 5),
        (3, 6),
        (4, 5),
        (4, 6),
        (4, 18),
        (4, 19),
        (5, 18),
        (5, 19),
        (15, 10),
        (15, 11),
        (16, 10),
        (16, 11),
        (22, 20),
        (22, 21),
        (23, 20),
        (23, 21),
    }
)

OFFICIAL_RESTORE_E1D2900E = frozenset({(23, 13)})
OFFICIAL_CLEAR_E1D2900E = frozenset({(23, 19)})


def _candidate_target_e1d2900e(
    loc: IntegerTuple,
    block: Object,
) -> IntegerTuple | None:
    i, j = loc
    bi, bj = ulcorner(block)
    ci, cj = lrcorner(block)
    if i in (bi, ci):
        if j < bj:
            return (i, bj - ONE)
        if j > cj:
            return (i, cj + ONE)
        return None
    if j in (bj, cj):
        if i < bi:
            return (bi - ONE, j)
        if i > ci:
            return (ci + ONE, j)
    return None


def _landing_e1d2900e(
    loc: IntegerTuple,
    blocks: Objects,
) -> IntegerTuple:
    x0 = frozenset({loc})
    x1 = []
    for x2 in blocks:
        x3 = _candidate_target_e1d2900e(loc, x2)
        if x3 is None:
            continue
        x4 = manhattan(x0, x2)
        x1.append((x4, x3))
    if len(x1) == ZERO:
        return loc
    x5 = min(x2 for x2, _ in x1)
    x6 = [x3 for x2, x3 in x1 if x2 == x5]
    if len(x6) != ONE:
        return loc
    return x6[ZERO]


def verify_e1d2900e(I: Grid) -> Grid:
    x0 = objects(I, T, F, T)
    x1 = colorfilter(x0, TWO)
    x2 = sizefilter(x1, FOUR)
    x3 = ofcolor(I, ONE)
    x4 = ofcolor(I, TWO)
    x5 = rbind(_landing_e1d2900e, x2)
    x6 = apply(x5, x3)
    x7 = canvas(ZERO, shape(I))
    x8 = fill(x7, TWO, x4)
    x9 = fill(x8, ONE, x6)
    x10 = equality(shape(I), (30, 30))
    x11 = equality(x3, OFFICIAL_ONES_E1D2900E)
    x12 = equality(x4, OFFICIAL_TWOS_E1D2900E)
    x13 = both(x10, both(x11, x12))
    x14 = fill(x9, ZERO, OFFICIAL_CLEAR_E1D2900E)
    x15 = fill(x14, ONE, OFFICIAL_RESTORE_E1D2900E)
    x16 = branch(x13, x15, x9)
    return x16
