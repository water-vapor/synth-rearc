from arc2.core import *


MOTIFS_5FFB2104 = (
    frozenset({(0, 0)}),
    frozenset({(0, 0)}),
    frozenset({(0, 0), (0, 1)}),
    frozenset({(0, 0), (0, 1)}),
    frozenset({(0, 0), (1, 0)}),
    frozenset({(0, 0), (1, 0)}),
    frozenset({(0, 0), (0, 1), (0, 2)}),
    frozenset({(0, 0), (0, 1), (1, 0)}),
    frozenset({(0, 0), (0, 1), (1, 1)}),
    frozenset({(0, 0), (1, 0), (1, 1)}),
    frozenset({(0, 1), (1, 0), (1, 1)}),
    frozenset({(0, 0), (0, 1), (1, 0), (1, 1)}),
    frozenset({(0, 0), (0, 1), (1, 0), (1, 1)}),
)

LANE_ORDERS_5FFB2104 = (
    (2, 2, 1),
    (2, 1, 2),
)


def _rows_5ffb2104(
    patch: Patch,
    top: Integer,
) -> frozenset[int]:
    return frozenset(top + i for i, _ in patch)


def _make_pair_lane_5ffb2104() -> tuple[int, tuple[tuple[Patch, int], tuple[Patch, int]]]:
    for _ in range(200):
        x0 = choice(MOTIFS_5FFB2104)
        x1 = choice(MOTIFS_5FFB2104)
        x2 = max(height(x0), height(x1))
        x3 = x2 + choice((ZERO, ZERO, ONE))
        x4 = randint(ZERO, x3 - height(x0))
        x5 = randint(ZERO, x3 - height(x1))
        x6 = _rows_5ffb2104(x0, x4)
        x7 = _rows_5ffb2104(x1, x5)
        if size(intersection(x6, x7)) == ZERO:
            continue
        return (x3, ((x0, x4), (x1, x5)))
    raise RuntimeError("unable to build overlapping lane for 5ffb2104")


def _make_single_lane_5ffb2104() -> tuple[int, tuple[tuple[Patch, int], ...]]:
    x0 = choice(MOTIFS_5FFB2104)
    x1 = height(x0) + choice((ZERO, ZERO, ONE))
    x2 = randint(ZERO, x1 - height(x0))
    return (x1, ((x0, x2),))


def _lane_span_5ffb2104(
    lane: tuple[tuple[Patch, int], ...],
) -> int:
    return sum(width(patch) for patch, _ in lane)


def _pack_objects_right_5ffb2104(
    objs: tuple[Object, ...],
    dims: IntegerTuple,
) -> tuple[Object, ...]:
    x0 = list(objs)
    x1 = T
    x2 = astuple(ZERO, ONE)
    x3 = decrement(dims[ONE])
    while x1:
        x1 = F
        x4 = frozenset()
        for x5 in x0:
            x4 = combine(x4, toindices(x5))
        x6 = []
        for x7 in x0:
            x8 = toindices(x7)
            x9 = difference(x4, x8)
            x10 = shift(x7, x2)
            x11 = toindices(x10)
            x12 = rightmost(x7) < x3
            x13 = intersection(difference(x11, x8), x9)
            x14 = both(x12, equality(size(x13), ZERO))
            if x14:
                x6.append(x10)
                x1 = T
            else:
                x6.append(x7)
        x0 = x6
    return tuple(x0)


def _paint_objects_5ffb2104(
    objs: tuple[Object, ...],
    dims: IntegerTuple,
) -> Grid:
    x0 = canvas(ZERO, dims)
    for x1 in objs:
        x0 = paint(x0, x1)
    return x0


def _object_5ffb2104(
    patch: Patch,
    top: Integer,
    left: Integer,
    value: Integer,
) -> Object:
    return shift(recolor(value, patch), (top, left))


def generate_5ffb2104(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    cols = tuple(remove(ZERO, interval(ZERO, TEN, ONE)))
    while True:
        x0 = choice(LANE_ORDERS_5FFB2104)
        x1 = []
        for x2 in x0:
            if x2 == 2:
                x1.append(_make_pair_lane_5ffb2104())
            else:
                x1.append(_make_single_lane_5ffb2104())
        x2 = randint(ZERO, ONE)
        x3 = randint(ZERO, TWO)
        x4 = (randint(ZERO, TWO), randint(ZERO, TWO))
        x5 = x2 + x3 + x4[ZERO] + x4[ONE] + sum(x6 for x6, _ in x1)
        if x5 < 6 or x5 > 12:
            continue
        x6 = max(_lane_span_5ffb2104(x7) for _, x7 in x1)
        x7 = max(6, x6 + 3)
        x8 = min(14, x7 + 5)
        if x7 > x8:
            continue
        x9 = unifint(diff_lb, diff_ub, (x7, x8))
        x10 = choice((FOUR, FOUR, FIVE))
        x11 = list(sample(cols, x10))
        while len(x11) < FIVE:
            x11.append(choice(x11))
        shuffle(x11)
        x12 = []
        x13 = x2
        x14 = ZERO
        x15 = T
        for x16, (x17, x18) in enumerate(x1):
            if len(x18) == TWO:
                (x19, x20), (x21, x22) = x18
                x23 = width(x19)
                x24 = width(x21)
                x25 = x23 + ONE
                x26 = x9 - x24
                if choice((ZERO, ONE, ONE)) != ZERO:
                    x26 = max(x25, decrement(x26))
                if x25 > x26:
                    x15 = F
                    break
                x27 = randint(x25, x26)
                x28 = randint(ZERO, x27 - x23 - ONE)
                x29 = _object_5ffb2104(x19, x13 + x20, x28, x11[x14])
                x30 = _object_5ffb2104(x21, x13 + x22, x27, x11[x14 + ONE])
                x12.extend((x29, x30))
                x14 += TWO
            else:
                x19, x20 = x18[ZERO]
                x21 = width(x19)
                x22 = x9 - x21
                if x22 > ZERO and choice((ZERO, ONE, ONE)) != ZERO:
                    x22 = decrement(x22)
                if x22 < ZERO:
                    x15 = F
                    break
                x23 = randint(ZERO, x22)
                x24 = _object_5ffb2104(x19, x13 + x20, x23, x11[x14])
                x12.append(x24)
                x14 += ONE
            x13 += x17
            if x16 < TWO:
                x13 += x4[x16]
        if not x15:
            continue
        x25 = tuple(x12)
        x26 = _paint_objects_5ffb2104(x25, (x5, x9))
        if mostcolor(x26) != ZERO:
            continue
        if size(objects(x26, T, F, T)) != FIVE:
            continue
        x27 = _pack_objects_right_5ffb2104(x25, (x5, x9))
        x28 = _paint_objects_5ffb2104(x27, (x5, x9))
        if x26 == x28:
            continue
        if any(leftmost(x29) == leftmost(x30) for x29, x30 in zip(x25, x27)):
            continue
        if size(remove(ZERO, palette(x26))) < FOUR:
            continue
        return {"input": x26, "output": x28}
