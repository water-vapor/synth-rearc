from functools import lru_cache

from synth_rearc.core import *


def _neighbors_93b4f4b3(
    loc: IntegerTuple,
    height_: Integer,
    width_: Integer,
) -> frozenset[IntegerTuple]:
    x0, x1 = loc
    x2 = set()
    if x0 > ZERO:
        x2.add((x0 - ONE, x1))
    if x0 < height_ - ONE:
        x2.add((x0 + ONE, x1))
    if x1 > ZERO:
        x2.add((x0, x1 - ONE))
    if x1 < width_ - ONE:
        x2.add((x0, x1 + ONE))
    return frozenset(x2)


def _connected_93b4f4b3(
    patch: Indices,
    height_: Integer,
    width_: Integer,
) -> Boolean:
    x0 = {next(iter(patch))}
    x1 = set()
    while len(x0) > ZERO:
        x2 = x0.pop()
        if x2 in x1:
            continue
        x1.add(x2)
        x3 = _neighbors_93b4f4b3(x2, height_, width_)
        x4 = patch.intersection(x3)
        x0 |= set(x4.difference(x1))
    return len(x1) == len(patch)


@lru_cache(maxsize=None)
def _shape_catalog_93b4f4b3(
    height_: Integer,
    width_: Integer,
) -> tuple[Indices, ...]:
    x0 = tuple((x1, x2) for x1 in range(height_) for x2 in range(width_))
    x1 = []
    x2 = set()
    x3 = height_ * width_
    x4 = height_ + ONE
    for x5 in range(ONE, ONE << x3):
        x6 = x5.bit_count()
        if x6 < x4 or x6 == x3:
            continue
        x7 = frozenset(x0[x8] for x8 in range(x3) if (x5 >> x8) & ONE)
        x9 = {x10 for x10, _ in x7}
        if len(x9) != height_:
            continue
        x10 = {x11 for _, x11 in x7}
        if len(x10) == ONE:
            continue
        if not _connected_93b4f4b3(x7, height_, width_):
            continue
        x11 = normalize(x7)
        if x11 in x2:
            continue
        x2.add(x11)
        x1.append(x11)
    return tuple(x1)


def generate_93b4f4b3(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    x0 = unifint(diff_lb, diff_ub, (TWO, THREE))
    if x0 == TWO:
        x1 = FOUR
        x2 = THREE
    else:
        x1 = unifint(diff_lb, diff_ub, (THREE, FOUR))
        x2 = unifint(diff_lb, diff_ub, (THREE, FOUR))
    x3 = _shape_catalog_93b4f4b3(x0, x1)
    x4 = tuple(sample(x3, x2))
    x5 = tuple(randint(ZERO, x1 - width(x6)) for x6 in x4)
    x6 = interval(ONE, TEN, ONE)
    x7 = choice(x6)
    x8 = tuple(sample(remove(x7, x6), x2))
    x9 = tuple(range(x2))
    x10 = x9
    while x10 == x9:
        x10 = tuple(sample(x9, x2))
    x11 = x1 + TWO
    x12 = ONE + x2 * (x0 + ONE)
    x13 = canvas(x7, (x12, x11))
    x14 = x13
    x15 = canvas(ZERO, (x12, x11))
    for x16, x17 in enumerate(x4):
        x18 = ONE + x16 * (x0 + ONE)
        x19 = shift(x17, (x18, ONE + x5[x16]))
        x13 = fill(x13, ZERO, x19)
        x14 = fill(x14, x8[x16], x19)
    for x20, x21 in enumerate(x10):
        x22 = ONE + x20 * (x0 + ONE)
        x23 = shift(x4[x21], (x22, ONE + x5[x21]))
        x24 = recolor(x8[x21], x23)
        x15 = paint(x15, x24)
    x25 = hconcat(x13, x15)
    return {"input": x25, "output": x14}
