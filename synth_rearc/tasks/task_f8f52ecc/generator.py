from synth_rearc.core import *

from .helpers import route_f8f52ecc
from .verifier import verify_f8f52ecc


ACTIVE_COLORS_F8F52ECC = difference(interval(ZERO, TEN, ONE), frozenset({ONE, EIGHT}))


def _paint_bar_f8f52ecc(
    I: Grid,
    row: Integer,
    start: Integer,
    length: Integer,
) -> Grid:
    x0 = connect((row, start), (row, start + length - ONE))
    return fill(I, EIGHT, x0)


def _bar_cells_f8f52ecc(
    row: Integer,
    start: Integer,
    length: Integer,
) -> Indices:
    return connect((row, start), (row, start + length - ONE))


def _sample_bars_f8f52ecc(
    h: Integer,
    w: Integer,
) -> tuple[tuple[Integer, Integer, Integer], ...]:
    x0 = unifint(0.0, 1.0, (ONE, min(THREE, h - TWO)))
    x1 = tuple()
    x2 = tuple()
    for _ in range(200):
        x1 = tuple()
        x2 = tuple()
        x3 = tuple(sample(interval(ONE, h - ONE, ONE), x0))
        x4 = True
        for x5 in order(x3, identity):
            x6 = randint(ZERO, w - TWO)
            x7 = randint(ONE, w - x6)
            if x7 == w and choice((T, F)):
                x7 = decrement(x7)
            x8 = _bar_cells_f8f52ecc(x5, x6, x7)
            if any(len(intersection(x8, x9)) > ZERO for x9 in x2):
                x4 = False
                break
            x1 = x1 + ((x5, x6, x7),)
            x2 = x2 + (x8,)
        if x4:
            return x1
    return tuple()


def _route_union_f8f52ecc(
    points: tuple[IntegerTuple, ...],
    barriers: Indices,
) -> Indices:
    x0 = frozenset(points)
    for x1, x2 in zip(points, points[ONE:]):
        x0 = combine(x0, route_f8f52ecc(x1, x2, barriers))
    return x0


def _sample_next_point_f8f52ecc(
    prev: IntegerTuple,
    h: Integer,
    w: Integer,
) -> IntegerTuple:
    x0, x1 = prev
    x2 = randint(ZERO, FOUR)
    if x2 == ZERO and x1 < w - ONE:
        return (x0, randint(x1 + ONE, w - ONE))
    if x2 == ONE and x0 < h - ONE:
        return (randint(x0 + ONE, h - ONE), x1)
    if x0 < h - ONE:
        x3 = tuple(j for j in range(w) if j != x1)
        if len(x3) > ZERO:
            return (randint(x0 + ONE, h - ONE), choice(x3))
    if x1 < w - ONE:
        return (x0, randint(x1 + ONE, w - ONE))
    if x0 < h - ONE:
        return (randint(x0 + ONE, h - ONE), x1)
    return prev


def _sample_color_points_f8f52ecc(
    h: Integer,
    w: Integer,
    barriers: Indices,
    occupied_input: Indices,
    occupied_output: Indices,
    min_points: Integer,
    max_points: Integer,
) -> tuple[IntegerTuple, ...] | None:
    for _ in range(400):
        x0 = randint(min_points, max_points)
        x1 = set()
        x2 = tuple()
        x3 = tuple(
            (i, j)
            for i in range(h)
            for j in range(w)
            if (i, j) not in barriers and (i, j) not in occupied_input
        )
        if len(x3) == ZERO:
            return None
        x4 = choice(x3)
        x2 = (x4,)
        x1.add(x4)
        x5 = frozenset({x4})
        x6 = True
        while len(x2) < x0:
            x7 = tuple()
            x8 = x2[-ONE]
            for _ in range(60):
                x9 = _sample_next_point_f8f52ecc(x8, h, w)
                if x9 == x8 or x9 in x1 or x9 in barriers or x9 in occupied_input:
                    continue
                if x9 < x8:
                    continue
                x10 = route_f8f52ecc(x8, x9, barriers)
                if len(intersection(x10, barriers)) > ZERO:
                    continue
                if len(intersection(difference(x10, x5), occupied_output)) > ZERO:
                    continue
                x7 = x7 + (x9,)
            if len(x7) == ZERO:
                x6 = False
                break
            x11 = choice(x7)
            x12 = route_f8f52ecc(x8, x11, barriers)
            x2 = x2 + (x11,)
            x1.add(x11)
            x5 = combine(x5, x12)
        if x6 and len(x2) >= min_points:
            return x2
    return None


def _has_new_cells_f8f52ecc(
    points: tuple[IntegerTuple, ...],
    barriers: Indices,
) -> Boolean:
    x0 = _route_union_f8f52ecc(points, barriers)
    return greater(len(x0), len(points))


def generate_f8f52ecc(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = unifint(diff_lb, diff_ub, (EIGHT, 12))
        x1 = unifint(diff_lb, diff_ub, (EIGHT, 12))
        x2 = canvas(ONE, (x0, x1))
        x3 = _sample_bars_f8f52ecc(x0, x1)
        x4 = frozenset()
        for x5, x6, x7 in x3:
            x2 = _paint_bar_f8f52ecc(x2, x5, x6, x7)
            x4 = combine(x4, _bar_cells_f8f52ecc(x5, x6, x7))
        x8 = tuple(sample(ACTIVE_COLORS_F8F52ECC, randint(ONE, min(FIVE, len(ACTIVE_COLORS_F8F52ECC)))))
        x9 = x2
        x10 = x4
        x11 = x4
        x12 = False
        x13 = True
        for x14, x15 in enumerate(x8):
            x16 = branch(x14 == ZERO, TWO, randint(ONE, TWO))
            x17 = branch(x14 == ZERO, FOUR, randint(x16, THREE))
            x18 = _sample_color_points_f8f52ecc(x0, x1, x4, x10, x11, x16, x17)
            if x18 is None:
                x13 = False
                break
            for x19 in x18:
                x9 = fill(x9, x15, frozenset({x19}))
            x20 = _route_union_f8f52ecc(x18, x4)
            x10 = combine(x10, frozenset(x18))
            x11 = combine(x11, x20)
            if _has_new_cells_f8f52ecc(x18, x4):
                x12 = True
        if not x13 or not x12:
            continue
        x21 = verify_f8f52ecc(x9)
        if x21 == x9:
            continue
        if any(colorcount(x21, x22) == ZERO for x22 in palette(x9)):
            continue
        return {"input": x9, "output": x21}
