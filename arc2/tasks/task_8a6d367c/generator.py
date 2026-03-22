from itertools import combinations

from arc2.core import *


GRID_SHAPE_8A6D367C = (27, 21)
BACKGROUND_8A6D367C = EIGHT
HINT_TOP_OPTIONS_8A6D367C = (ONE, ONE, TWO)
FRAME_GAP_OPTIONS_8A6D367C = (THREE, FOUR, FIVE, SIX)
FAMILY_OPTIONS_8A6D367C = (
    ((THREE, THREE), FOUR, (FOUR, FIVE)),
    ((FOUR, THREE), THREE, (FOUR, FIVE)),
    ((THREE, FOUR), TWO, (TWO, FOUR)),
)
MAX_SHAPE_ATTEMPTS_8A6D367C = 256


def _connected_8a6d367c(
    patch: Indices,
) -> bool:
    x0 = {next(iter(patch))}
    x1 = [next(iter(patch))]
    while len(x1) > ZERO:
        x2 = x1.pop()
        for x3 in neighbors(x2):
            if x3 not in patch or x3 in x0:
                continue
            x0.add(x3)
            x1.append(x3)
    return len(x0) == len(patch)


def _shape_cells_8a6d367c(
    dims: tuple[Integer, Integer],
    diff_lb: float,
    diff_ub: float,
) -> Indices:
    x0 = tuple(asindices(canvas(ZERO, dims)))
    x1 = dims[ZERO] * dims[ONE]
    x2 = max(THREE, (x1 + ONE) // TWO)
    x3 = x1 - ONE
    x4 = asindices(canvas(ZERO, dims))
    for _ in range(MAX_SHAPE_ATTEMPTS_8A6D367C):
        x5 = unifint(diff_lb, diff_ub, (x2, x3))
        x6 = frozenset(sample(x0, x5))
        if len({x7 for x7, _ in x6}) != dims[ZERO]:
            continue
        if len({x8 for _, x8 in x6}) != dims[ONE]:
            continue
        if x6 == box(x6):
            continue
        if x6 == x4:
            continue
        if not _connected_8a6d367c(x6):
            continue
        return x6
    return frozenset({})


def _unique_seed_8a6d367c(
    target: Indices,
    distractors: tuple[Indices, ...],
) -> Indices:
    x0 = tuple(target)
    for x1 in range(ONE, len(x0)):
        x2 = []
        for x3 in combinations(x0, x1):
            x4 = frozenset(x3)
            if any(x4.issubset(x5) for x5 in distractors):
                continue
            x2.append(x4)
        if len(x2) > ZERO:
            return choice(x2)
    return frozenset({})


def _sample_shapes_8a6d367c(
    dims: tuple[Integer, Integer],
    nhints: Integer,
    diff_lb: float,
    diff_ub: float,
) -> tuple[Indices, tuple[Indices, ...], Indices]:
    while True:
        x0 = _shape_cells_8a6d367c(dims, diff_lb, diff_ub)
        if len(x0) == ZERO:
            continue
        x1 = []
        while len(x1) < nhints - ONE:
            x2 = _shape_cells_8a6d367c(dims, diff_lb, diff_ub)
            if len(x2) == ZERO or x2 == x0 or x2 in x1:
                continue
            x1.append(x2)
        x3 = tuple(x1)
        x4 = _unique_seed_8a6d367c(x0, x3)
        if len(x4) == ZERO:
            continue
        return x0, x3, x4


def _frame_patch_8a6d367c(
    dims: tuple[Integer, Integer],
    color_value: Integer,
) -> Object:
    x0 = asindices(canvas(ZERO, dims))
    return recolor(color_value, box(x0))


def _scaled_patch_8a6d367c(
    patch: Indices,
    dims: tuple[Integer, Integer],
    scale: Integer,
    color_value: Integer,
) -> Object:
    x0 = paint(canvas(ZERO, dims), recolor(ONE, patch))
    x1 = upscale(x0, scale)
    x2 = ofcolor(x1, ONE)
    return recolor(color_value, x2)


def generate_8a6d367c(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0, x1, x2 = choice(FAMILY_OPTIONS_8A6D367C)
        x3 = unifint(diff_lb, diff_ub, x2)
        x4 = (x0[ZERO] * x1 + TWO, x0[ONE] * x1 + TWO)
        x5 = x0[ONE] * x3 + decrement(x3)
        if x5 > GRID_SHAPE_8A6D367C[ONE]:
            continue

        x6 = choice(HINT_TOP_OPTIONS_8A6D367C)
        x7 = choice(FRAME_GAP_OPTIONS_8A6D367C)
        x8 = add(add(x6, x0[ZERO]), x7)
        x9 = subtract(GRID_SHAPE_8A6D367C[ZERO], x4[ZERO])
        if x8 > x9:
            continue

        x10 = max(ZERO, subtract(subtract(GRID_SHAPE_8A6D367C[ONE], x4[ONE]), TWO))
        x11 = randint(TWO if x10 >= TWO else ZERO, add(x10, TWO) if x10 >= TWO else x10)
        x12 = max(ZERO, subtract(GRID_SHAPE_8A6D367C[ONE], x5))
        x13 = max(ZERO, decrement(x12))
        x14 = randint(ONE if x13 >= ONE else ZERO, x13)
        x15 = tuple(add(x14, multiply(x16, add(x0[ONE], ONE))) for x16 in interval(ZERO, x3, ONE))

        x17 = tuple(x18 for x18 in interval(ZERO, 10, ONE) if x18 != BACKGROUND_8A6D367C)
        x18 = sample(x17, x3 + TWO)
        x19 = x18[ZERO]
        x20 = x18[ONE]
        x21 = tuple(x18[TWO:])

        x22, x23, x24 = _sample_shapes_8a6d367c(x0, x3, diff_lb, diff_ub)
        x25 = list(x23) + [x22]
        shuffle(x25)

        x26 = canvas(BACKGROUND_8A6D367C, GRID_SHAPE_8A6D367C)
        for x27, x28, x29 in zip(x15, x25, x21):
            x30 = shift(recolor(x29, x28), (x6, x27))
            x26 = paint(x26, x30)

        x31 = randint(x8, x9)
        x32 = shift(_frame_patch_8a6d367c(x4, x19), (x31, x11))
        x26 = paint(x26, x32)
        x33 = shift(_scaled_patch_8a6d367c(x24, x0, x1, x20), add((x31, x11), UNITY))
        x26 = paint(x26, x33)

        x34 = canvas(BACKGROUND_8A6D367C, x4)
        x34 = paint(x34, _frame_patch_8a6d367c(x4, x19))
        x35 = shift(_scaled_patch_8a6d367c(x22, x0, x1, x20), UNITY)
        x34 = paint(x34, x35)

        if x26 == x34:
            continue
        return {"input": x26, "output": x34}
