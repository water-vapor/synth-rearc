from __future__ import annotations

from synth_rearc.core import *

from .helpers import ordered_objects_d017b73f, pack_objects_d017b73f, packed_grid_d017b73f


DOMINO_D017B73F = frozenset({(ZERO, ZERO), (ZERO, ONE)})
LINE3_D017B73F = frozenset({(ZERO, ZERO), (ZERO, ONE), (ZERO, TWO)})
ELBOW_A_D017B73F = frozenset({(ZERO, ZERO), (ZERO, ONE), (ONE, ONE)})
ELBOW_B_D017B73F = frozenset({(ZERO, ONE), (ONE, ZERO), (ONE, ONE)})
STAIR_A_D017B73F = frozenset({(ZERO, ONE), (ZERO, TWO), (ONE, ZERO), (ONE, ONE)})
J_A_D017B73F = frozenset({(ZERO, ZERO), (ZERO, ONE), (ZERO, TWO), (ONE, TWO)})
J_B_D017B73F = frozenset({(ZERO, TWO), (ONE, ZERO), (ONE, ONE), (ONE, TWO)})
HOOK_A_D017B73F = frozenset({(ZERO, ZERO), (ZERO, ONE), (ONE, ONE), (TWO, ONE)})
HOOK_B_D017B73F = frozenset({(ZERO, ONE), (ONE, ZERO), (ONE, ONE), (TWO, ZERO)})

WIDTH2_POOL_D017B73F = (
    DOMINO_D017B73F,
    DOMINO_D017B73F,
    ELBOW_A_D017B73F,
    ELBOW_A_D017B73F,
    ELBOW_B_D017B73F,
    ELBOW_B_D017B73F,
    HOOK_A_D017B73F,
    HOOK_B_D017B73F,
)

WIDTH3_POOL_D017B73F = (
    LINE3_D017B73F,
    LINE3_D017B73F,
    J_A_D017B73F,
    J_A_D017B73F,
    J_B_D017B73F,
    J_B_D017B73F,
    STAIR_A_D017B73F,
    STAIR_A_D017B73F,
)

PATTERN_POOL_D017B73F = (
    (THREE, THREE, THREE),
    (THREE, THREE, THREE),
    (THREE, TWO, THREE),
    (THREE, TWO, THREE),
    (THREE, TWO, THREE),
    (TWO, TWO, THREE),
    (TWO, TWO, THREE),
    (TWO, TWO, TWO, TWO),
    (TWO, TWO, TWO, TWO),
)


def _shape_key_d017b73f(
    patch: Patch,
) -> tuple[int, int, int, tuple[IntegerTuple, ...]]:
    x0 = frozenset(normalize(toindices(patch)))
    return (width(x0), height(x0), size(x0), tuple(sorted(x0)))


def _gap_recipe_d017b73f(
    pattern: tuple[Integer, ...],
) -> tuple[Integer, ...]:
    if pattern == (THREE, THREE, THREE):
        return (ONE, ONE, ZERO)
    if pattern == (THREE, TWO, THREE):
        return choice(((ONE, ONE, ONE), (ONE, TWO, ZERO), (TWO, ONE, ZERO)))
    if pattern == (TWO, TWO, THREE):
        return (ONE, ONE, ZERO)
    return (ONE, ONE, ONE, ZERO)


def _sample_colors_d017b73f(
    count: Integer,
) -> tuple[Integer, ...]:
    x0 = list(sample(tuple(range(ONE, TEN)), count))
    if count >= THREE and randint(ZERO, ONE) == ONE:
        x1 = randint(ONE, count - ONE)
        x2 = randint(ZERO, x1 - ONE)
        x0[x1] = x0[x2]
    return tuple(x0)


def _in_bounds_d017b73f(
    objs: tuple[Object, ...],
) -> Boolean:
    for x0 in objs:
        for _, x1 in x0:
            if not (ZERO <= x1[0] < THREE and ZERO <= x1[1]):
                return F
    return T


def _sample_shapes_d017b73f(
    pattern: tuple[Integer, ...],
) -> tuple[Indices, ...]:
    x0 = []
    for x1 in pattern:
        x2 = WIDTH2_POOL_D017B73F if x1 == TWO else WIDTH3_POOL_D017B73F
        x0.append(choice(x2))
    return tuple(x0)


def _left_positions_d017b73f(
    widths: tuple[Integer, ...],
    gaps: tuple[Integer, ...],
) -> tuple[Integer, ...]:
    x0 = [ZERO]
    for x1, x2 in zip(widths[:-1], gaps):
        x0.append(x0[-1] + x1 + x2)
    return tuple(x0)


def generate_d017b73f(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = choice(PATTERN_POOL_D017B73F)
        x1 = _sample_shapes_d017b73f(x0)
        x2 = tuple(width(x3) for x3 in x1)
        x3 = tuple(_shape_key_d017b73f(x4) for x4 in x1)
        if len(set(x3)) == ONE:
            continue
        x4 = _gap_recipe_d017b73f(x0)
        x5 = x4[:-ONE]
        x6 = last(x4)
        x7 = _left_positions_d017b73f(x2, x5)
        x8 = sum(x2) + sum(x5) + x6
        x9 = _sample_colors_d017b73f(len(x1))
        x10 = []
        for x11 in x1[ONE:]:
            x12 = randint(ZERO, THREE - height(x11))
            x10.append(x12)
        x13 = tuple(x10)
        x14 = list(range(THREE - height(first(x1)) + ONE))
        shuffle(x14)
        for x15 in x14:
            x16 = (x15,) + x13
            x17 = []
            for x18, x19, x20, x21 in zip(x1, x9, x16, x7):
                x22 = recolor(x19, x18)
                x23 = shift(x22, (x20, x21))
                x17.append(x23)
            x24 = tuple(x17)
            x25 = pack_objects_d017b73f(x24)
            if not _in_bounds_d017b73f(x25):
                continue
            x26 = canvas(ZERO, (THREE, x8))
            x27 = paint(x26, merge(x24))
            x28 = ordered_objects_d017b73f(x27)
            if len(x28) != len(x24):
                continue
            x29 = packed_grid_d017b73f(x28, THREE)
            if x29 != packed_grid_d017b73f(x24, THREE):
                continue
            return {"input": x27, "output": x29}
