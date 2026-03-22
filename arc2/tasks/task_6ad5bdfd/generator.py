from arc2.core import *

from .verifier import verify_6ad5bdfd


ACTIVE_COLORS_6AD5BDFD = tuple(x0 for x0 in interval(ONE, TEN, ONE) if x0 != TWO)
SIDE_OPTIONS_6AD5BDFD = ("left", "right", "top", "bottom")


def _wall_cells_6ad5bdfd(
    x0: Integer,
    x1: Integer,
    x2: str,
) -> Indices:
    if x2 == "left":
        return connect((ZERO, ZERO), (decrement(x0), ZERO))
    if x2 == "right":
        x3 = decrement(x1)
        return connect((ZERO, x3), (decrement(x0), x3))
    if x2 == "top":
        return connect((ZERO, ZERO), (ZERO, decrement(x1)))
    x4 = decrement(x0)
    return connect((x4, ZERO), (x4, decrement(x1)))


def _gravity_6ad5bdfd(
    x0: str,
) -> tuple[IntegerTuple, callable]:
    if x0 == "left":
        return LEFT, leftmost
    if x0 == "right":
        return RIGHT, lambda x1: -rightmost(x1)
    if x0 == "top":
        return UP, uppermost
    return DOWN, lambda x1: -lowermost(x1)


def _domino_patch_6ad5bdfd(
    x0: IntegerTuple,
    x1: Boolean,
) -> Indices:
    x2 = branch(x1, DOWN, RIGHT)
    x3 = add(x0, x2)
    return connect(x0, x3)


def _slide_object_6ad5bdfd(
    x0: Object,
    x1: Indices,
    x2: IntegerTuple,
) -> Object:
    x3 = x0
    while True:
        x4 = shift(x3, x2)
        x5 = toindices(x4)
        x6 = intersection(x5, x1)
        if len(x6) > ZERO:
            return x3
        x3 = x4


def _compress_objects_6ad5bdfd(
    x0: tuple[Object, ...],
    x1: Indices,
    x2: IntegerTuple,
    x3: tuple[Integer, Integer],
    x4,
) -> Grid:
    x5 = canvas(ZERO, x3)
    x6 = fill(x5, TWO, x1)
    x7 = order(x0, x4)
    x8 = x1
    x9 = x6
    for x10 in x7:
        x11 = _slide_object_6ad5bdfd(x10, x8, x2)
        x8 = combine(x8, toindices(x11))
        x9 = paint(x9, x11)
    return x9


def _can_place_6ad5bdfd(
    x0: Indices,
    x1: Indices,
    x2: Indices,
) -> Boolean:
    x3 = intersection(x0, x1)
    x4 = equality(len(x3), ZERO)
    x5 = mapply(dneighbors, x0)
    x6 = combine(x0, x5)
    x7 = intersection(x6, x2)
    x8 = equality(len(x7), ZERO)
    return both(x4, x8)


def generate_6ad5bdfd(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = choice(SIDE_OPTIONS_6AD5BDFD)
        if contained(x0, ("left", "right")):
            x1 = randint(FIVE, TEN)
            x2 = randint(EIGHT, 12)
        else:
            x1 = randint(EIGHT, 12)
            x2 = randint(SIX, TEN)
        x3 = astuple(x1, x2)
        x4 = _wall_cells_6ad5bdfd(x1, x2, x0)
        x5, x6 = _gravity_6ad5bdfd(x0)
        x7 = invert(x5)
        x8 = subtract(multiply(x1, x2), size(x4))
        x9 = max(FOUR, min(TEN, x8 // EIGHT))
        x10 = unifint(diff_lb, diff_ub, (FOUR, x9))
        x11 = sample(ACTIVE_COLORS_6AD5BDFD, randint(THREE, min(SIX, x10)))
        x12 = tuple(choice(x11) for _ in range(x10))
        x13 = tuple(choice((T, F)) for _ in range(x10))
        if size(set(x13)) == ONE:
            x14 = randint(ZERO, decrement(x10))
            x13 = tuple(flip(x15) if x16 == x14 else x15 for x16, x15 in enumerate(x13))
        x15 = tuple()
        x16 = x4
        x17 = {x18: frozenset() for x18 in ACTIVE_COLORS_6AD5BDFD}
        x18 = True
        for x19, x20 in zip(x12, x13):
            x21 = tuple()
            x22 = decrement(x1) if x20 else x1
            x23 = x2 if x20 else decrement(x2)
            for x24 in range(x22):
                for x25 in range(x23):
                    x26 = (x24, x25)
                    x27 = _domino_patch_6ad5bdfd(x26, x20)
                    if _can_place_6ad5bdfd(x27, x16, x17[x19]):
                        x21 = x21 + (x27,)
            if len(x21) == ZERO:
                x18 = False
                break
            x28 = choice(x21)
            x29 = recolor(x19, x28)
            x15 = x15 + (x29,)
            x16 = combine(x16, x28)
            x17[x19] = combine(x17[x19], x28)
        if flip(x18):
            continue
        x30 = canvas(ZERO, x3)
        x31 = fill(x30, TWO, x4)
        for x32 in x15:
            x31 = paint(x31, x32)
        x33 = _compress_objects_6ad5bdfd(x15, x4, x5, x3, x6)
        if x31 == x33:
            continue
        if size(objects(replace(x31, TWO, ZERO), T, F, T)) != x10:
            continue
        x34 = ofcolor(x31, TWO)
        if x34 != x4:
            continue
        if verify_6ad5bdfd(x31) != x33:
            continue
        x35 = tuple(shift(x36, x7) for x36 in x15)
        x36 = paint(fill(canvas(ZERO, x3), TWO, x4), merge(x35))
        if x36 == x33 and choice((T, F)):
            continue
        return {"input": x31, "output": x33}
