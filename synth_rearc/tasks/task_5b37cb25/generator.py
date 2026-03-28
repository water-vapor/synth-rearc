from synth_rearc.core import *

from .verifier import verify_5b37cb25


INNER_SHAPE_5B37CB25 = (28, 28)
OUTER_SHAPE_5B37CB25 = (30, 30)
TOP_EDGE_5B37CB25 = connect((ZERO, ONE), (ZERO, 28))
BOTTOM_EDGE_5B37CB25 = connect((29, ONE), (29, 28))
LEFT_EDGE_5B37CB25 = connect((ONE, ZERO), (28, ZERO))
RIGHT_EDGE_5B37CB25 = connect((ONE, 29), (28, 29))
COLORS_5B37CB25 = (ONE, TWO, THREE, FOUR, FIVE, SIX, SEVEN, EIGHT, NINE)


def _rectangle_patch_5b37cb25(
    loc: IntegerTuple,
    dims: IntegerTuple,
) -> Indices:
    i, j = loc
    h, w = dims
    return backdrop(frozenset({(i, j), (i + h - ONE, j + w - ONE)}))


def _plus_patch_5b37cb25(
    loc: IntegerTuple,
) -> Indices:
    return insert(loc, dneighbors(loc))


def _notch_zone_5b37cb25(
    loc: IntegerTuple,
) -> Indices:
    x0 = _plus_patch_5b37cb25(loc)
    x1 = add(loc, UP)
    x2 = add(loc, DOWN)
    x3 = add(loc, LEFT)
    x4 = add(loc, RIGHT)
    return x0 | initset(add(x1, UP)) | initset(add(x2, DOWN)) | initset(add(x3, LEFT)) | initset(add(x4, RIGHT))


def _frame_grid_5b37cb25(
    top: Integer,
    bottom: Integer,
    left: Integer,
    right: Integer,
) -> Grid:
    x0 = canvas(ZERO, OUTER_SHAPE_5B37CB25)
    x1 = fill(x0, top, TOP_EDGE_5B37CB25)
    x2 = fill(x1, bottom, BOTTOM_EDGE_5B37CB25)
    x3 = fill(x2, left, LEFT_EDGE_5B37CB25)
    return fill(x3, right, RIGHT_EDGE_5B37CB25)


def _embed_inner_5b37cb25(
    inner: Grid,
    frame: Grid,
) -> Grid:
    return paint(frame, shift(asobject(inner), UNITY))


def _separated_5b37cb25(
    a: tuple[int, int, int, int],
    b: tuple[int, int, int, int],
) -> Boolean:
    ai, aj, ah, aw = a
    bi, bj, bh, bw = b
    return ai + ah + ONE <= bi or bi + bh + ONE <= ai or aj + aw + ONE <= bj or bj + bw + ONE <= aj


def _sample_rectangles_5b37cb25(
    diff_lb: float,
    diff_ub: float,
) -> tuple[tuple[int, int, int, int], ...] | None:
    x0 = unifint(diff_lb, diff_ub, (THREE, SIX))
    x1 = []
    x2 = ZERO
    while len(x1) < x0 and x2 < 600:
        x2 += ONE
        x3 = unifint(diff_lb, diff_ub, (FOUR, 11))
        x4 = unifint(diff_lb, diff_ub, (FOUR, 12))
        x5 = randint(ONE, INNER_SHAPE_5B37CB25[ZERO] - x3 - ONE)
        x6 = randint(ONE, INNER_SHAPE_5B37CB25[ONE] - x4 - ONE)
        x7 = (x5, x6, x3, x4)
        if all(_separated_5b37cb25(x7, x8) for x8 in x1):
            x1.append(x7)
    if len(x1) != x0:
        return None
    x9 = sum(x3 * x4 for _, _, x3, x4 in x1)
    if not (180 <= x9 <= 360):
        return None
    return tuple(x1)


def _notch_candidates_5b37cb25(
    rects: tuple[tuple[int, int, int, int], ...],
) -> list[tuple[IntegerTuple, IntegerTuple]]:
    x0 = []
    for x1, x2, x3, x4 in rects:
        if x4 >= FIVE:
            for x5 in range(x2 + TWO, x2 + x4 - TWO):
                x0.append(((x1, x5), UP))
                x0.append(((x1 + x3 - ONE, x5), DOWN))
        if x3 >= FIVE:
            for x6 in range(x1 + TWO, x1 + x3 - TWO):
                x0.append(((x6, x2), LEFT))
                x0.append(((x6, x2 + x4 - ONE), RIGHT))
    return x0


def _sample_notches_5b37cb25(
    rects: tuple[tuple[int, int, int, int], ...],
    diff_lb: float,
    diff_ub: float,
) -> tuple[tuple[IntegerTuple, IntegerTuple], ...] | None:
    x0 = merge(tuple(_rectangle_patch_5b37cb25((x1, x2), (x3, x4)) for x1, x2, x3, x4 in rects))
    x1 = []
    for x2, x3 in _notch_candidates_5b37cb25(rects):
        x4 = add(x2, add(x3, x3))
        if contained(x4, x0):
            continue
        x1.append((x2, x3))
    shuffle(x1)
    x5 = min(SEVEN, max(TWO, len(rects) * TWO))
    x6 = unifint(diff_lb, diff_ub, (TWO, x5))
    x7 = set()
    x8 = []
    for x9, x10 in x1:
        x11 = _notch_zone_5b37cb25(x9)
        if x11 & x7:
            continue
        x8.append((x9, x10))
        x7 |= x11
        if len(x8) == x6:
            return tuple(x8)
    return None


def generate_5b37cb25(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = _sample_rectangles_5b37cb25(diff_lb, diff_ub)
        if x0 is None:
            continue
        x1 = _sample_notches_5b37cb25(x0, diff_lb, diff_ub)
        if x1 is None:
            continue
        x2 = sample(COLORS_5B37CB25, SIX)
        x3, x4, x5, x6, x7, x8 = x2
        x9 = canvas(x3, INNER_SHAPE_5B37CB25)
        for x10, x11, x12, x13 in x0:
            x14 = _rectangle_patch_5b37cb25((x10, x11), (x12, x13))
            x9 = fill(x9, x4, x14)
        for x15, _ in x1:
            x16 = _plus_patch_5b37cb25(x15)
            x9 = fill(x9, x3, x16)
        x17 = x9
        for x18, x19 in x1:
            x20 = branch(
                equality(x19, UP),
                x5,
                branch(equality(x19, DOWN), x6, branch(equality(x19, LEFT), x7, x8)),
            )
            x21 = _plus_patch_5b37cb25(x18)
            x17 = fill(x17, x20, x21)
        x22 = _frame_grid_5b37cb25(x5, x6, x7, x8)
        x23 = _embed_inner_5b37cb25(x9, x22)
        x24 = _embed_inner_5b37cb25(x17, x22)
        if verify_5b37cb25(x23) != x24:
            continue
        return {"input": x23, "output": x24}
