from synth_rearc.core import *


_SINGLETON_5034A0B5 = frozenset({ORIGIN})
_DOMINO_5034A0B5 = frozenset({ORIGIN, RIGHT})
_LINE3_5034A0B5 = connect(ORIGIN, astuple(ZERO, TWO))
_LINE4_5034A0B5 = connect(ORIGIN, astuple(ZERO, THREE))
_LINE5_5034A0B5 = connect(ORIGIN, astuple(ZERO, FOUR))
_DIAG2_5034A0B5 = frozenset({ORIGIN, UNITY})
_DIAG3_5034A0B5 = frozenset({ORIGIN, UNITY, TWO_BY_TWO})
_DIAG4_5034A0B5 = frozenset({ORIGIN, UNITY, TWO_BY_TWO, THREE_BY_THREE})
_L3_5034A0B5 = frozenset({ORIGIN, DOWN, UNITY})
_L4_5034A0B5 = frozenset({ORIGIN, DOWN, TWO_BY_ZERO, astuple(TWO, ONE)})
_STEP4_5034A0B5 = frozenset({ORIGIN, RIGHT, UNITY, astuple(ONE, TWO)})
_DIAMOND4_5034A0B5 = frozenset({RIGHT, DOWN, astuple(ONE, TWO), astuple(TWO, ONE)})

_MOVING_BASES_5034A0B5 = (
    _SINGLETON_5034A0B5,
    _SINGLETON_5034A0B5,
    _DOMINO_5034A0B5,
    _DOMINO_5034A0B5,
    _LINE3_5034A0B5,
    _LINE3_5034A0B5,
    _DIAG2_5034A0B5,
    _DIAG3_5034A0B5,
    _L3_5034A0B5,
    _STEP4_5034A0B5,
)
_STATIC_BASES_5034A0B5 = (
    *_MOVING_BASES_5034A0B5,
    _LINE4_5034A0B5,
    _LINE5_5034A0B5,
    _DIAG4_5034A0B5,
    _L4_5034A0B5,
    _DIAMOND4_5034A0B5,
)


def _normalize_patch_5034a0b5(
    patch: Indices,
) -> Indices:
    x0 = uppermost(patch)
    x1 = leftmost(patch)
    return shift(patch, invert((x0, x1)))


def _variants_5034a0b5(
    patch: Indices,
) -> tuple[Indices, ...]:
    x0 = []
    for x1 in (F, T):
        for x2 in (ONE, NEG_ONE):
            for x3 in (ONE, NEG_ONE):
                x4 = set()
                for x5, x6 in patch:
                    if x1:
                        x5, x6 = x6, x5
                    x4.add((x2 * x5, x3 * x6))
                x7 = _normalize_patch_5034a0b5(frozenset(x4))
                if x7 not in x0:
                    x0.append(x7)
    return tuple(x0)


def _random_patch_5034a0b5(
    moving: Boolean,
) -> Indices:
    x0 = choice(_MOVING_BASES_5034A0B5 if moving else _STATIC_BASES_5034A0B5)
    x1 = _variants_5034a0b5(x0)
    return choice(x1)


def _inside_5034a0b5(
    loc: IntegerTuple,
    side: Integer,
) -> Boolean:
    i, j = loc
    return 0 < i < side - ONE and 0 < j < side - ONE


def _move_patch_5034a0b5(
    patch: Indices,
    direction: IntegerTuple,
    side: Integer,
) -> Indices:
    x0 = set()
    for x1 in patch:
        x2 = add(x1, direction)
        x3 = branch(_inside_5034a0b5(x2, side), x2, x1)
        x0.add(x3)
    return frozenset(x0)


def _place_static_patch_5034a0b5(
    patch: Indices,
    side: Integer,
    blocked: Indices,
) -> Indices | None:
    x0 = height(patch)
    x1 = width(patch)
    x2 = side - x0 - ONE
    x3 = side - x1 - ONE
    if x2 < ONE or x3 < ONE:
        return None
    x4 = [(i, j) for i in range(ONE, x2 + ONE) for j in range(ONE, x3 + ONE)]
    shuffle(x4)
    for x5 in x4:
        x6 = shift(patch, x5)
        if len(intersection(x6, blocked)) == ZERO:
            return x6
    return None


def _place_moving_patch_5034a0b5(
    patch: Indices,
    side: Integer,
    direction: IntegerTuple,
    blocked_in: Indices,
    blocked_out: Indices,
) -> tuple[Indices, Indices] | None:
    x0 = height(patch)
    x1 = width(patch)
    x2 = ONE
    x3 = side - x0 - ONE
    x4 = ONE
    x5 = side - x1 - ONE
    if direction == UP:
        x2 = TWO
    elif direction == DOWN:
        x3 = side - x0 - TWO
    elif direction == LEFT:
        x4 = TWO
    else:
        x5 = side - x1 - TWO
    if x2 > x3 or x4 > x5:
        return None
    x6 = [(i, j) for i in range(x2, x3 + ONE) for j in range(x4, x5 + ONE)]
    shuffle(x6)
    for x7 in x6:
        x8 = shift(patch, x7)
        x9 = _move_patch_5034a0b5(x8, direction, side)
        if size(x9) != size(x8):
            continue
        if len(intersection(x8, blocked_in)) > ZERO:
            continue
        if len(intersection(x9, blocked_out)) > ZERO:
            continue
        return x8, x9
    return None


def _place_anchored_singleton_5034a0b5(
    side: Integer,
    direction: IntegerTuple,
    blocked_in: Indices,
    blocked_out: Indices,
) -> tuple[Indices, Indices] | None:
    if direction == UP:
        x0 = tuple((ONE, j) for j in range(ONE, side - ONE))
    elif direction == DOWN:
        x0 = tuple((side - TWO, j) for j in range(ONE, side - ONE))
    elif direction == LEFT:
        x0 = tuple((i, ONE) for i in range(ONE, side - ONE))
    else:
        x0 = tuple((i, side - TWO) for i in range(ONE, side - ONE))
    x1 = list(x0)
    shuffle(x1)
    for x2 in x1:
        x3 = initset(x2)
        if len(intersection(x3, blocked_in)) > ZERO:
            continue
        if len(intersection(x3, blocked_out)) > ZERO:
            continue
        return x3, x3
    return None


def _make_frame_5034a0b5(
    side: Integer,
    bg: Integer,
    top: Integer,
    left: Integer,
    right: Integer,
    bottom: Integer,
) -> Grid:
    x0 = canvas(bg, astuple(side, side))
    x1 = fill(x0, top, connect((ZERO, ONE), (ZERO, side - TWO)))
    x2 = fill(x1, left, connect((ONE, ZERO), (side - TWO, ZERO)))
    x3 = fill(x2, right, connect((ONE, side - ONE), (side - TWO, side - ONE)))
    x4 = fill(x3, bottom, connect((side - ONE, ONE), (side - ONE, side - TWO)))
    return x4


def generate_5034a0b5(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    x0 = interval(ZERO, TEN, ONE)
    x1 = (EIGHT, NINE, TEN, 12, 13)
    while True:
        x2 = choice(x1)
        x3 = sample(x0, FIVE)
        bg, top, left, right, bottom = x3
        x4 = tuple(x5 for x5 in x0 if x5 not in x3)
        x5 = frozenset()
        x6 = frozenset()
        x7: dict[Integer, Indices] = {}
        x8 = choice((ZERO, ZERO, ONE, ONE, TWO, THREE))
        x8 = min(x8, len(x4))
        x9 = sample(x4, x8)
        x10 = T
        for x11 in x9:
            x12 = frozenset()
            for _ in range(choice((ONE, ONE, TWO))):
                x13 = _place_static_patch_5034a0b5(_random_patch_5034a0b5(F), x2, x5)
                if x13 is None:
                    x10 = F
                    break
                x12 = combine(x12, x13)
                x5 = combine(x5, x13)
                x6 = combine(x6, x13)
            if flip(x10):
                break
            x7[x11] = x12
        if flip(x10):
            continue
        x11 = {
            top: frozenset(),
            left: frozenset(),
            right: frozenset(),
            bottom: frozenset(),
        }
        x12 = {
            top: frozenset(),
            left: frozenset(),
            right: frozenset(),
            bottom: frozenset(),
        }
        x13 = (
            (top, UP),
            (left, LEFT),
            (right, RIGHT),
            (bottom, DOWN),
        )
        x14 = F
        for x15, x16 in x13:
            for _ in range(choice((ZERO, ZERO, ONE))):
                x17 = _place_anchored_singleton_5034a0b5(x2, x16, x5, x6)
                if x17 is None:
                    x10 = F
                    break
                x18, x19 = x17
                x11[x15] = combine(x11[x15], x18)
                x12[x15] = combine(x12[x15], x19)
                x5 = combine(x5, x18)
                x6 = combine(x6, x19)
            if flip(x10):
                break
            for _ in range(unifint(diff_lb, diff_ub, (ZERO, TWO))):
                x17 = _place_moving_patch_5034a0b5(
                    _random_patch_5034a0b5(T),
                    x2,
                    x16,
                    x5,
                    x6,
                )
                if x17 is None:
                    x10 = F
                    break
                x18, x19 = x17
                x11[x15] = combine(x11[x15], x18)
                x12[x15] = combine(x12[x15], x19)
                x5 = combine(x5, x18)
                x6 = combine(x6, x19)
                x14 = T
            if flip(x10):
                break
        if flip(x10):
            continue
        x15 = sum(ONE for x16 in x11.values() if positive(size(x16)))
        if x15 < TWO or flip(x14):
            continue
        gi = _make_frame_5034a0b5(x2, bg, top, left, right, bottom)
        go = _make_frame_5034a0b5(x2, bg, top, left, right, bottom)
        for x16, x17 in x7.items():
            gi = fill(gi, x16, x17)
            go = fill(go, x16, x17)
        for x16 in (top, left, right, bottom):
            gi = fill(gi, x16, x11[x16])
            go = fill(go, x16, x12[x16])
        if equality(gi, go):
            continue
        return {"input": gi, "output": go}
