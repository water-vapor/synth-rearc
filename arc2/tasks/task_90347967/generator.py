from arc2.core import *


ACTIVE_COLORS_90347967 = tuple(remove(FIVE, remove(ZERO, interval(ZERO, TEN, ONE))))


def _sample_dims_90347967(
    diff_lb: float,
    diff_ub: float,
) -> tuple[int, int]:
    x0 = add(double(unifint(diff_lb, diff_ub, (ONE, FIVE))), ONE)
    if choice((True, False, False)):
        return x0, x0
    x1 = add(double(unifint(diff_lb, diff_ub, (ONE, FIVE))), ONE)
    return x0, x1


def _sample_offsets_90347967(
    diff_lb: float,
    diff_ub: float,
    height0: int,
    width0: int,
) -> tuple[tuple[int, int], ...]:
    while True:
        x0 = choice((THREE, THREE, FOUR))
        x1 = choice((ZERO, ZERO, ONE))
        x2 = x0 - ONE - x1
        x3 = min(FOUR, (width0 - ONE) // TWO)
        if x3 < ONE or x1 + x2 >= height0:
            continue
        x4 = unifint(diff_lb, diff_ub, (ONE, x3))
        x5 = tuple(range(-x1, x2 + ONE))
        x6 = []
        for x7 in x5:
            x8 = min(THREE, x4 + ONE)
            x9 = randint(ONE, x8)
            x10 = -ONE if x7 <= ZERO else ZERO
            x11 = -x4 + x9 - ONE
            if x11 > x10:
                break
            x12 = randint(x11, x10)
            x13 = x12 - x9 + ONE
            x6.extend((x7, x14) for x14 in range(x13, x12 + ONE))
        else:
            x15 = tuple(sorted(set(x6)))
            if not (FOUR <= len(x15) <= EIGHT):
                continue
            if not any(x16[ONE] == NEG_ONE for x16 in x15):
                continue
            return x15


def _color_offsets_90347967(
    offsets: tuple[tuple[int, int], ...],
) -> frozenset[tuple[int, tuple[int, int]]]:
    while True:
        x0 = choice((TWO, THREE, FOUR))
        x1 = min(x0, len(offsets))
        x2 = sample(ACTIVE_COLORS_90347967, x1)
        x3 = {}
        for x4, x5 in offsets:
            x6 = []
            x7 = (x4, x5 - ONE)
            x8 = (x4 - ONE, x5)
            if x7 in x3:
                x6.append(x3[x7])
            if x8 in x3:
                x6.append(x3[x8])
            if len(x6) > ZERO and randint(ZERO, 99) < 65:
                x9 = choice(tuple(x6))
            else:
                x9 = choice(x2)
            x3[(x4, x5)] = x9
        x10 = tuple(x3[x11] for x11 in offsets)
        if len(set(x10)) < TWO:
            continue
        if max(x10.count(x11) for x11 in set(x10)) == ONE:
            continue
        return frozenset((x3[x11], x11) for x11 in offsets)


def _paint_relative_object_90347967(
    grid: Grid,
    anchor: tuple[int, int],
    obj: frozenset[tuple[int, tuple[int, int]]],
) -> Grid:
    x0 = frozenset((x1, add(anchor, x2)) for x1, x2 in obj)
    return paint(grid, x0)


def _reflect_relative_object_90347967(
    anchor: tuple[int, int],
    obj: frozenset[tuple[int, tuple[int, int]]],
    dims: tuple[int, int],
) -> Grid:
    x0 = double(anchor)
    x1 = frozenset((x2, subtract(x0, add(anchor, x3))) for x2, x3 in obj)
    x2 = canvas(ZERO, dims)
    x3 = fill(x2, FIVE, initset(anchor))
    return paint(x3, x1)


def generate_90347967(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = _sample_dims_90347967(diff_lb, diff_ub)
        x1, x2 = x0
        x3 = _sample_offsets_90347967(diff_lb, diff_ub, x1, x2)
        x4 = max(abs(x5[ZERO]) for x5 in x3)
        x5 = max(abs(x5[ONE]) for x5 in x3)
        if x1 < double(x4) + ONE or x2 < double(x5) + ONE:
            continue
        x7 = randint(x4, x1 - ONE - x4)
        x8 = randint(x5, x2 - ONE - x5)
        x9 = _color_offsets_90347967(x3)
        x10 = canvas(ZERO, x0)
        x11 = fill(x10, FIVE, initset((x7, x8)))
        gi = _paint_relative_object_90347967(x11, (x7, x8), x9)
        go = _reflect_relative_object_90347967((x7, x8), x9, x0)
        if gi == go:
            continue
        return {"input": gi, "output": go}
