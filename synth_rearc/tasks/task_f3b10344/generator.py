from synth_rearc.core import *

from .verifier import verify_f3b10344


RectF3B10344 = tuple[Integer, Integer, Integer, Integer, Integer]
ACTIVE_COLORS_F3B10344 = interval(ONE, EIGHT, ONE)


def _bbox_patch_f3b10344(
    r0: Integer,
    r1: Integer,
    c0: Integer,
    c1: Integer,
) -> Indices:
    if r0 > r1 or c0 > c1:
        return frozenset({})
    return frozenset(
        (i, j)
        for i in range(r0, r1 + ONE)
        for j in range(c0, c1 + ONE)
    )


def _expanded_patch_f3b10344(
    rect: RectF3B10344,
    dims: IntegerTuple,
) -> Indices:
    _, r0, r1, c0, c1 = rect
    x0, x1 = dims
    return frozenset(
        (i, j)
        for i in range(max(ZERO, r0 - ONE), min(x0 - ONE, r1 + ONE) + ONE)
        for j in range(max(ZERO, c0 - ONE), min(x1 - ONE, c1 + ONE) + ONE)
    )


def _horizontal_corridor_f3b10344(
    left_rect: RectF3B10344,
    right_rect: RectF3B10344,
) -> Indices:
    _, r0, r1, _, c1 = left_rect
    _, r2, r3, c2, _ = right_rect
    x0 = max(r0, r2)
    x1 = min(r1, r3)
    return _bbox_patch_f3b10344(x0, x1, c1 + ONE, c2 - ONE)


def _vertical_corridor_f3b10344(
    top_rect: RectF3B10344,
    bottom_rect: RectF3B10344,
) -> Indices:
    _, r0, r1, c0, c1 = top_rect
    _, r2, r3, c2, c3 = bottom_rect
    x0 = max(c0, c2)
    x1 = min(c1, c3)
    return _bbox_patch_f3b10344(r1 + ONE, r2 - ONE, x0, x1)


def _paint_rectangles_f3b10344(
    dims: IntegerTuple,
    rects: tuple[RectF3B10344, ...],
) -> Grid:
    x0 = canvas(ZERO, dims)
    for x1, x2, x3, x4, x5 in rects:
        x6 = _bbox_patch_f3b10344(x2, x3, x4, x5)
        x0 = fill(x0, x1, x6)
    return x0


def _horizontal_bridge_f3b10344(
    I: Grid,
    bg: Integer,
    a: Object,
    b: Object,
) -> Indices:
    x0, x1 = (a, b) if leftmost(a) <= leftmost(b) else (b, a)
    x2 = max(uppermost(x0), uppermost(x1))
    x3 = min(lowermost(x0), lowermost(x1))
    x4 = rightmost(x0) + ONE
    x5 = leftmost(x1) - ONE
    x6 = _bbox_patch_f3b10344(x2, x3, x4, x5)
    if len(x6) == ZERO:
        return frozenset({})
    if palette(toobject(x6, I)) != initset(bg):
        return frozenset({})
    return _bbox_patch_f3b10344(x2 + ONE, x3 - ONE, x4, x5)


def _vertical_bridge_f3b10344(
    I: Grid,
    bg: Integer,
    a: Object,
    b: Object,
) -> Indices:
    x0, x1 = (a, b) if uppermost(a) <= uppermost(b) else (b, a)
    x2 = lowermost(x0) + ONE
    x3 = uppermost(x1) - ONE
    x4 = max(leftmost(x0), leftmost(x1))
    x5 = min(rightmost(x0), rightmost(x1))
    x6 = _bbox_patch_f3b10344(x2, x3, x4, x5)
    if len(x6) == ZERO:
        return frozenset({})
    if palette(toobject(x6, I)) != initset(bg):
        return frozenset({})
    return _bbox_patch_f3b10344(x2, x3, x4 + ONE, x5 - ONE)


def _candidate_bridges_f3b10344(
    I: Grid,
    rects: tuple[Object, ...],
) -> tuple[tuple[Integer, Integer, Integer, Integer, Integer, Indices], ...]:
    x0 = mostcolor(I)
    x1 = []
    for x2, x3 in enumerate(rects):
        for x4 in range(x2 + ONE, len(rects)):
            x5 = rects[x4]
            x6 = color(x3)
            if x6 != color(x5):
                continue
            if hmatching(x3, x5):
                x7 = _horizontal_bridge_f3b10344(I, x0, x3, x5)
                if len(x7) == ZERO:
                    continue
                x8, x9 = (x3, x5) if leftmost(x3) <= leftmost(x5) else (x5, x3)
                x10 = leftmost(x9) - rightmost(x8) - ONE
                x1.append((x6, x10, invert(size(x7)), x2, x4, x7))
                continue
            if vmatching(x3, x5):
                x7 = _vertical_bridge_f3b10344(I, x0, x3, x5)
                if len(x7) == ZERO:
                    continue
                x8, x9 = (x3, x5) if uppermost(x3) <= uppermost(x5) else (x5, x3)
                x10 = uppermost(x9) - lowermost(x8) - ONE
                x1.append((x6, x10, invert(size(x7)), x2, x4, x7))
    return tuple(sorted(x1))


def _build_output_f3b10344(
    I: Grid,
) -> Grid:
    x0 = objects(I, T, F, T)
    x1 = sfilter(x0, lambda x2: equality(size(x2), size(backdrop(x2))))
    x2 = tuple(
        sorted(
            x1,
            key=lambda x3: (
                color(x3),
                uppermost(x3),
                leftmost(x3),
                lowermost(x3),
                rightmost(x3),
            ),
        )
    )
    x3 = _candidate_bridges_f3b10344(I, x2)
    x4 = {x5: x5 for x5 in range(len(x2))}

    def x5(n: Integer) -> Integer:
        while x4[n] != n:
            x4[n] = x4[x4[n]]
            n = x4[n]
        return n

    x6 = I
    for _, _, _, x7, x8, x9 in x3:
        x10 = x5(x7)
        x11 = x5(x8)
        if x10 == x11:
            continue
        x4[x11] = x10
        x6 = fill(x6, EIGHT, x9)
    return x6


def _sample_horizontal_group_f3b10344(
    dims: IntegerTuple,
    color: Integer,
    length: Integer,
    blocked: Indices,
) -> tuple[tuple[RectF3B10344, ...], Indices] | None:
    x0, x1 = dims
    for _ in range(300):
        x2 = randint(ONE, min(SIX, x0 - TWO))
        x3 = tuple(randint(THREE, min(NINE, x1 - ONE)) for _ in range(length))
        x4 = tuple((randint(ZERO, TWO), randint(ZERO, TWO)) for _ in range(length))
        x5 = tuple(randint(ONE, min(TEN, x1 - TWO)) for _ in range(length - ONE))
        x6 = max(x7 for x7, _ in x4) + ONE
        x7 = max(x8 for _, x8 in x4) + ONE
        if x6 + x2 + x7 > x0:
            continue
        x8 = sum(x3) + sum(x5)
        if x8 > x1:
            continue
        x9 = randint(x6, x0 - x2 - x7)
        x10 = randint(ZERO, x1 - x8)
        x11 = tuple()
        x12 = tuple()
        x13 = x10
        for x14, (x15, x16) in zip(x3, x4):
            x17 = x9 - ONE - x15
            x18 = x9 + x2 + x16
            x19 = (color, x17, x18, x13, x13 + x14 - ONE)
            x11 = x11 + (x19,)
            x12 = x12 + (_expanded_patch_f3b10344(x19, dims),)
            x13 += x14
            if len(x11) < length:
                x13 += x5[len(x11) - ONE]
        x20 = tuple(_horizontal_corridor_f3b10344(x21, x22) for x21, x22 in zip(x11, x11[ONE:]))
        if any(len(x21) == ZERO for x21 in x20):
            continue
        x21 = merge(frozenset(x12 + x20))
        if len(intersection(x21, blocked)) > ZERO:
            continue
        return x11, x21
    return None


def _sample_vertical_group_f3b10344(
    dims: IntegerTuple,
    color: Integer,
    length: Integer,
    blocked: Indices,
) -> tuple[tuple[RectF3B10344, ...], Indices] | None:
    x0, x1 = dims
    for _ in range(300):
        x2 = randint(ONE, min(SIX, x1 - TWO))
        x3 = tuple(randint(THREE, min(NINE, x0 - ONE)) for _ in range(length))
        x4 = tuple((randint(ZERO, TWO), randint(ZERO, TWO)) for _ in range(length))
        x5 = tuple(randint(ONE, min(TEN, x0 - TWO)) for _ in range(length - ONE))
        x6 = max(x7 for x7, _ in x4) + ONE
        x7 = max(x8 for _, x8 in x4) + ONE
        if x6 + x2 + x7 > x1:
            continue
        x8 = sum(x3) + sum(x5)
        if x8 > x0:
            continue
        x9 = randint(x6, x1 - x2 - x7)
        x10 = randint(ZERO, x0 - x8)
        x11 = tuple()
        x12 = tuple()
        x13 = x10
        for x14, (x15, x16) in zip(x3, x4):
            x17 = x9 - ONE - x15
            x18 = x9 + x2 + x16
            x19 = (color, x13, x13 + x14 - ONE, x17, x18)
            x11 = x11 + (x19,)
            x12 = x12 + (_expanded_patch_f3b10344(x19, dims),)
            x13 += x14
            if len(x11) < length:
                x13 += x5[len(x11) - ONE]
        x20 = tuple(_vertical_corridor_f3b10344(x21, x22) for x21, x22 in zip(x11, x11[ONE:]))
        if any(len(x21) == ZERO for x21 in x20):
            continue
        x21 = merge(frozenset(x12 + x20))
        if len(intersection(x21, blocked)) > ZERO:
            continue
        return x11, x21
    return None


def _sample_single_rect_f3b10344(
    dims: IntegerTuple,
    color: Integer,
    blocked: Indices,
) -> tuple[RectF3B10344, Indices] | None:
    x0, x1 = dims
    for _ in range(200):
        x2 = randint(THREE, min(EIGHT, x0))
        x3 = randint(THREE, min(NINE, x1))
        x4 = randint(ZERO, x0 - x2)
        x5 = randint(ZERO, x1 - x3)
        x6 = (color, x4, x4 + x2 - ONE, x5, x5 + x3 - ONE)
        x7 = _expanded_patch_f3b10344(x6, dims)
        if len(intersection(x7, blocked)) > ZERO:
            continue
        return x6, x7
    return None


def generate_f3b10344(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = unifint(diff_lb, diff_ub, (25, 30))
        x1 = unifint(diff_lb, diff_ub, (28, 30))
        x2 = (x0, x1)
        x3 = choice((TWO, TWO, THREE))
        x4 = tuple(sample(ACTIVE_COLORS_F3B10344, x3))
        x5 = choice((TWO, TWO, THREE, THREE, FOUR))
        x6 = [TWO for _ in range(x5)]
        x7 = randint(ZERO, x5)
        for x8 in sample(tuple(range(x5)), x7):
            x6[x8] = THREE
        x9 = randint(ZERO, TWO)
        x10 = sum(x6) + x9
        if x10 < FIVE or x10 > 11:
            continue
        x11 = ["h", "v"] + [choice(("h", "v")) for _ in range(x5 - TWO)]
        x12 = tuple()
        x13 = frozenset({})
        x14 = True
        for x15, x16 in zip(x11, x6):
            x17 = choice(x4)
            if x15 == "h":
                x18 = _sample_horizontal_group_f3b10344(x2, x17, x16, x13)
            else:
                x18 = _sample_vertical_group_f3b10344(x2, x17, x16, x13)
            if x18 is None:
                x14 = False
                break
            x19, x20 = x18
            x12 = x12 + x19
            x13 = combine(x13, x20)
        if not x14:
            continue
        for _ in range(x9):
            x15 = _sample_single_rect_f3b10344(x2, choice(x4), x13)
            if x15 is None:
                x14 = False
                break
            x16, x17 = x15
            x12 = x12 + (x16,)
            x13 = combine(x13, x17)
        if not x14:
            continue
        x15 = _paint_rectangles_f3b10344(x2, x12)
        x16 = _build_output_f3b10344(x15)
        if x15 == x16:
            continue
        if verify_f3b10344(x15) != x16:
            continue
        return {"input": x15, "output": x16}
