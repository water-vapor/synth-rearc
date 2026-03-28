from arc2.core import *


def _plus_patch_55059096(
    center: IntegerTuple,
) -> Indices:
    i, j = center
    return frozenset(
        {
            center,
            (i - ONE, j),
            (i + ONE, j),
            (i, j - ONE),
            (i, j + ONE),
        }
    )


def _reserve_patch_55059096(
    center: IntegerTuple,
) -> Indices:
    x0 = _plus_patch_55059096(center)
    x1 = outbox(x0)
    return combine(x0, x1)


def _diagonal_pairs_55059096(
    centers: tuple[IntegerTuple, ...],
) -> tuple[tuple[IntegerTuple, IntegerTuple], ...]:
    x0 = []
    for x1, x2 in enumerate(centers):
        for x3 in centers[x1 + ONE:]:
            if abs(x2[ZERO] - x3[ZERO]) == abs(x2[ONE] - x3[ONE]):
                x0.append((x2, x3))
    return tuple(x0)


def _paint_pluses_55059096(
    centers: tuple[IntegerTuple, ...],
) -> Grid:
    x0 = canvas(ZERO, astuple(30, 30))
    for x1 in centers:
        x0 = fill(x0, THREE, _plus_patch_55059096(x1))
    return x0


def _paths_clear_55059096(
    centers: tuple[IntegerTuple, ...],
) -> Boolean:
    x0 = frozenset()
    for x1 in centers:
        x0 = combine(x0, _plus_patch_55059096(x1))
    for x1, x2 in _diagonal_pairs_55059096(centers):
        x3 = difference(connect(x1, x2), frozenset({x1, x2}))
        x4 = difference(x0, frozenset({x1, x2}))
        if len(intersection(x3, x4)) > ZERO:
            return F
    return T


def _try_pair_layout_55059096(
    diff_lb: float,
    diff_ub: float,
) -> tuple[IntegerTuple, ...] | None:
    x0 = ((ONE, ONE), (ONE, NEG_ONE), (NEG_ONE, ONE), (NEG_ONE, NEG_ONE))
    for _ in range(400):
        x1 = astuple(randint(4, 25), randint(4, 25))
        x2 = choice(x0)
        x3 = unifint(diff_lb, diff_ub, (3, 6))
        x4 = astuple(x1[ZERO] + x2[ZERO] * x3, x1[ONE] + x2[ONE] * x3)
        if not (ONE <= x4[ZERO] <= 28 and ONE <= x4[ONE] <= 28):
            continue
        if len(intersection(_plus_patch_55059096(x4), _reserve_patch_55059096(x1))) > ZERO:
            continue
        x5 = (x1, x4)
        if len(_diagonal_pairs_55059096(x5)) != ONE:
            continue
        if not _paths_clear_55059096(x5):
            continue
        return x5
    return None


def _try_v_layout_55059096(
    diff_lb: float,
    diff_ub: float,
) -> tuple[IntegerTuple, ...] | None:
    x0 = ((ONE, ONE), (NEG_ONE, NEG_ONE))
    x1 = ((ONE, NEG_ONE), (NEG_ONE, ONE))
    for _ in range(400):
        x2 = astuple(randint(5, 24), randint(5, 24))
        x3 = choice(x0)
        x4 = choice(x1)
        x5 = unifint(diff_lb, diff_ub, (3, 6))
        x6 = unifint(diff_lb, diff_ub, (3, 6))
        x7 = astuple(x2[ZERO] + x3[ZERO] * x5, x2[ONE] + x3[ONE] * x5)
        x8 = astuple(x2[ZERO] + x4[ZERO] * x6, x2[ONE] + x4[ONE] * x6)
        if not (ONE <= x7[ZERO] <= 28 and ONE <= x7[ONE] <= 28):
            continue
        if not (ONE <= x8[ZERO] <= 28 and ONE <= x8[ONE] <= 28):
            continue
        x9 = (x7, x2, x8)
        x10 = frozenset()
        x11 = T
        for x12 in x9:
            if len(intersection(_plus_patch_55059096(x12), x10)) > ZERO:
                x11 = F
                break
            x10 = combine(x10, _reserve_patch_55059096(x12))
        if not x11:
            continue
        if len(_diagonal_pairs_55059096(x9)) != 2:
            continue
        if not _paths_clear_55059096(x9):
            continue
        return x9
    return None


def _add_isolated_55059096(
    centers: tuple[IntegerTuple, ...],
    count: Integer,
) -> tuple[IntegerTuple, ...] | None:
    x0 = list(centers)
    x1 = frozenset()
    for x2 in x0:
        x1 = combine(x1, _reserve_patch_55059096(x2))
    x3 = 0
    while len(x0) < len(centers) + count and x3 < 800:
        x3 += ONE
        x4 = astuple(randint(ONE, 28), randint(ONE, 28))
        x5 = _plus_patch_55059096(x4)
        if len(intersection(x5, x1)) > ZERO:
            continue
        if any(abs(x4[ZERO] - x6[ZERO]) == abs(x4[ONE] - x6[ONE]) for x6 in x0):
            continue
        x0.append(x4)
        x1 = combine(x1, _reserve_patch_55059096(x4))
    if len(x0) != len(centers) + count:
        return None
    return tuple(x0)


def _crop_example_55059096(
    gi: Grid,
    go: Grid,
    centers: tuple[IntegerTuple, ...],
    diff_lb: float,
    diff_ub: float,
) -> tuple[Grid, Grid] | None:
    x0 = merge(tuple(_plus_patch_55059096(x1) for x1 in centers))
    x1 = uppermost(x0)
    x2 = lowermost(x0)
    x3 = leftmost(x0)
    x4 = rightmost(x0)
    x5 = x2 - x1 + ONE
    x6 = x4 - x3 + ONE
    x7 = max(10, x5 + 2)
    x8 = min(18, x5 + 6)
    x9 = max(10, x6 + 2)
    x10 = min(18, x6 + 6)
    if x7 > x8 or x9 > x10:
        return None
    x11 = unifint(diff_lb, diff_ub, (x7, x8))
    x12 = unifint(diff_lb, diff_ub, (x9, x10))
    x13 = max(ZERO, x2 - x11 + ONE)
    x14 = min(x1, 30 - x11)
    x15 = max(ZERO, x4 - x12 + ONE)
    x16 = min(x3, 30 - x12)
    if x13 > x14 or x15 > x16:
        return None
    x17 = astuple(randint(x13, x14), randint(x15, x16))
    x18 = astuple(x11, x12)
    x19 = crop(gi, x17, x18)
    x20 = crop(go, x17, x18)
    if x19 == x20:
        return None
    return (x19, x20)


def generate_55059096(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = choice((ONE, TWO))
        if x0 == ONE:
            x1 = _try_pair_layout_55059096(diff_lb, diff_ub)
            if x1 is None:
                continue
            x2 = choice((ONE, TWO))
        else:
            x1 = _try_v_layout_55059096(diff_lb, diff_ub)
            if x1 is None:
                continue
            x2 = choice((ZERO, ONE))
        x3 = _add_isolated_55059096(x1, x2)
        if x3 is None:
            continue
        if len(_diagonal_pairs_55059096(x3)) != x0:
            continue
        if not _paths_clear_55059096(x3):
            continue
        x4 = _paint_pluses_55059096(x3)
        x5 = x4
        for x6, x7 in _diagonal_pairs_55059096(x3):
            x5 = underfill(x5, TWO, connect(x6, x7))
        x8 = _crop_example_55059096(x4, x5, x3, diff_lb, diff_ub)
        if x8 is None:
            continue
        x9, x10 = x8
        return {"input": x9, "output": x10}
