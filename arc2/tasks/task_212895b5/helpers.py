from arc2.core import *


BLOCK_PATCH_212895B5 = frozenset((i, j) for i in range(THREE) for j in range(THREE))

ARM_SPECS_212895B5 = (
    ((ZERO, ONE), UP, RIGHT),
    ((ONE, TWO), RIGHT, DOWN),
    ((TWO, ONE), DOWN, LEFT),
    ((ONE, ZERO), LEFT, UP),
)

DIAGONAL_SPECS_212895B5 = (
    ((ZERO, ZERO), (NEG_ONE, NEG_ONE)),
    ((ZERO, TWO), (NEG_ONE, ONE)),
    ((TWO, ZERO), (ONE, NEG_ONE)),
    ((TWO, TWO), (ONE, ONE)),
)


def block_origin_212895b5(
    I: Grid,
) -> IntegerTuple:
    return ulcorner(ofcolor(I, EIGHT))


def block_patch_212895b5(
    origin: IntegerTuple,
) -> Indices:
    return shift(BLOCK_PATCH_212895B5, origin)


def trace_stair_arm_212895b5(
    I: Grid,
    start: IntegerTuple,
    primary: IntegerTuple,
    secondary: IntegerTuple,
) -> tuple[IntegerTuple, ...]:
    x0 = []
    x1 = start
    while True:
        for x2 in (primary, secondary):
            for _ in range(TWO):
                x3 = add(x1, x2)
                if index(I, x3) != ZERO:
                    return tuple(x0)
                x0.append(x3)
                x1 = x3


def trace_diagonal_ray_212895b5(
    I: Grid,
    start: IntegerTuple,
    direction: IntegerTuple,
) -> tuple[IntegerTuple, ...]:
    x0 = []
    x1 = start
    x2 = (direction[0], ZERO)
    x3 = (ZERO, direction[1])
    while True:
        x4 = add(x1, direction)
        if index(I, x4) != ZERO:
            return tuple(x0)
        x5 = add(x1, x2)
        x6 = add(x1, x3)
        if both(index(I, x5) != ZERO, index(I, x6) != ZERO):
            return tuple(x0)
        x0.append(x4)
        x1 = x4


def arm_paths_212895b5(
    I: Grid,
    origin: IntegerTuple,
) -> tuple[tuple[IntegerTuple, ...], ...]:
    x0 = []
    for x1, x2, x3 in ARM_SPECS_212895B5:
        x4 = add(origin, x1)
        x5 = trace_stair_arm_212895b5(I, x4, x2, x3)
        x0.append(x5)
    return tuple(x0)


def diagonal_paths_212895b5(
    I: Grid,
    origin: IntegerTuple,
) -> tuple[tuple[IntegerTuple, ...], ...]:
    x0 = []
    for x1, x2 in DIAGONAL_SPECS_212895B5:
        x3 = add(origin, x1)
        x4 = trace_diagonal_ray_212895b5(I, x3, x2)
        x0.append(x4)
    return tuple(x0)


def flatten_paths_212895b5(
    paths: tuple[tuple[IntegerTuple, ...], ...],
) -> Indices:
    return frozenset(cell for path in paths for cell in path)
