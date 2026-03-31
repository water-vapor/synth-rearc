from itertools import combinations

from synth_rearc.core import *

from .verifier import verify_e12f9a14


RING_COORDS_E12F9A14 = (
    (-1, -1),
    (-1, 0),
    (-1, 1),
    (-1, 2),
    (0, -1),
    (0, 2),
    (1, -1),
    (1, 2),
    (2, -1),
    (2, 0),
    (2, 1),
    (2, 2),
)

RAY_SPECS_E12F9A14 = {
    (-1, -1): (ORIGIN, NEG_UNITY),
    (-1, 0): (ORIGIN, UP),
    (-1, 1): (RIGHT, UP),
    (-1, 2): (RIGHT, UP_RIGHT),
    (0, -1): (ORIGIN, LEFT),
    (0, 2): (RIGHT, RIGHT),
    (1, -1): (DOWN, LEFT),
    (1, 2): (UNITY, RIGHT),
    (2, -1): (DOWN, DOWN_LEFT),
    (2, 0): (DOWN, DOWN),
    (2, 1): (UNITY, DOWN),
    (2, 2): (UNITY, UNITY),
}

HOLE_COUNT_CHOICES_E12F9A14 = (ONE, TWO, TWO, THREE, THREE, FOUR)


def _frame_connected_e12f9a14(
    missing: tuple[IntegerTuple, ...],
) -> Boolean:
    x0 = frozenset(RING_COORDS_E12F9A14) - frozenset(missing)
    x1 = {x2: set() for x2 in x0}
    for x2 in x0:
        for x3 in x0:
            if x2 != x3 and manhattan(frozenset({x2}), frozenset({x3})) == ONE:
                x1[x2].add(x3)
    x4 = {first(x0)}
    x5 = set()
    while x4:
        x6 = x4.pop()
        if x6 in x5:
            continue
        x5.add(x6)
        x4.update(x1[x6] - x5)
    return equality(size(x5), size(x0))


PATTERN_LIBRARY_E12F9A14 = tuple(
    tuple(x0)
    for x1 in range(ONE, FIVE)
    for x0 in combinations(RING_COORDS_E12F9A14, x1)
    if _frame_connected_e12f9a14(tuple(x0))
)

PATTERNS_BY_COUNT_E12F9A14 = {
    x0: tuple(x1 for x1 in PATTERN_LIBRARY_E12F9A14 if equality(len(x1), x0))
    for x0 in range(ONE, FIVE)
}


def _clip_indices_e12f9a14(
    patch: Patch,
    dims: IntegerTuple,
) -> Indices:
    x0, x1 = dims
    return frozenset((x2, x3) for x2, x3 in toindices(patch) if 0 <= x2 < x0 and 0 <= x3 < x1)


def _input_parts_e12f9a14(
    top_left: IntegerTuple,
    frame_color: Integer,
    core_color: Integer,
    missing: tuple[IntegerTuple, ...],
) -> tuple[Object, Object]:
    x0, x1 = top_left
    x2 = frozenset(
        {
            (core_color, (x0, x1)),
            (core_color, (x0, increment(x1))),
            (core_color, (increment(x0), x1)),
            (core_color, (increment(x0), increment(x1))),
        }
    )
    x3 = frozenset(
        (
            frame_color,
            add(top_left, x4),
        )
        for x4 in RING_COORDS_E12F9A14
        if x4 not in missing
    )
    return x2, x3


def _ray_cells_e12f9a14(
    top_left: IntegerTuple,
    missing: tuple[IntegerTuple, ...],
    dims: IntegerTuple,
) -> Indices:
    x0 = frozenset()
    for x1 in missing:
        x2, x3 = RAY_SPECS_E12F9A14[x1]
        x4 = add(top_left, x2)
        x5 = shoot(add(x4, x3), x3)
        x0 = combine(x0, _clip_indices_e12f9a14(x5, dims))
    return x0


def _halo_e12f9a14(
    patch: Patch,
    dims: IntegerTuple,
) -> Indices:
    x0, x1 = dims
    x2 = set()
    for x3, x4 in toindices(patch):
        for x5 in (-1, 0, 1):
            for x6 in (-1, 0, 1):
                x7 = add((x3, x4), (x5, x6))
                if 0 <= x7[0] < x0 and 0 <= x7[1] < x1:
                    x2.add(x7)
    return frozenset(x2)


def generate_e12f9a14(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = unifint(diff_lb, diff_ub, (EIGHT, 30))
        x1 = astuple(x0, x0)
        x2 = tuple(range(TEN))
        x3 = choice(x2)
        x4 = choice(tuple(x5 for x5 in x2 if x5 != x3))
        x5 = tuple(x6 for x6 in x2 if x6 not in (x3, x4))
        x6 = min(FIVE, max(ONE, x0 // SIX))
        x7 = randint(max(ONE, decrement(x6)), x6)
        x8 = tuple(sample(x5, x7))
        x9 = canvas(x3, x1)
        x10 = set()
        x11 = set()
        x12 = []
        x13 = True
        for x14 in x8:
            x15 = False
            for _ in range(200):
                x16 = choice(HOLE_COUNT_CHOICES_E12F9A14)
                x17 = choice(PATTERNS_BY_COUNT_E12F9A14[x16])
                x18 = randint(ONE, subtract(x0, THREE))
                x19 = randint(ONE, subtract(x0, THREE))
                x20 = astuple(x18, x19)
                x21, x22 = _input_parts_e12f9a14(x20, x4, x14, x17)
                x23 = toindices(combine(x21, x22))
                x24 = _ray_cells_e12f9a14(x20, x17, x1)
                x25 = combine(x23, x24)
                if any(x26 in x10 for x26 in x23):
                    continue
                if any(x27 in x11 for x27 in x25):
                    continue
                x9 = paint(paint(x9, x22), x21)
                x10.update(_halo_e12f9a14(x23, x1))
                x11.update(x25)
                x12.append((x14, x24))
                x15 = True
                break
            if not x15:
                x13 = False
                break
        if not x13:
            continue
        x28 = x9
        for x29, x30 in x12:
            x28 = underfill(x28, x29, x30)
        if verify_e12f9a14(x9) != x28:
            continue
        return {"input": x9, "output": x28}
