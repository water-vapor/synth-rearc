from arc2.core import *


LEFT_PATTERNS_BBB1B8B6 = (
    (
        (ONE, ONE, ONE, ONE),
        (ONE, ZERO, ZERO, ONE),
        (ONE, ZERO, ZERO, ONE),
        (ONE, ONE, ONE, ONE),
    ),
    (
        (ONE, ONE, ONE, ONE),
        (ONE, ZERO, ZERO, ONE),
        (ONE, ZERO, ZERO, ONE),
        (ONE, ZERO, ZERO, ONE),
    ),
    (
        (ONE, ONE, ONE, ONE),
        (ONE, ZERO, ZERO, ZERO),
        (ONE, ZERO, ONE, ONE),
        (ONE, ZERO, ONE, ZERO),
    ),
    (
        (ZERO, ZERO, ZERO, ONE),
        (ONE, ZERO, ZERO, ZERO),
        (ONE, ONE, ZERO, ZERO),
        (ONE, ONE, ONE, ZERO),
    ),
    (
        (ONE, ONE, ZERO, ZERO),
        (ONE, ZERO, ZERO, ONE),
        (ONE, ZERO, ZERO, ONE),
        (ONE, ONE, ZERO, ZERO),
    ),
    (
        (ONE, ONE, ONE, ONE),
        (ZERO, ONE, ONE, ZERO),
        (ZERO, ONE, ONE, ZERO),
        (ZERO, ZERO, ZERO, ZERO),
    ),
    (
        (ONE, ONE, ZERO, ZERO),
        (ONE, ZERO, ZERO, ONE),
        (ZERO, ZERO, ZERO, ONE),
        (ZERO, ONE, ONE, ONE),
    ),
)

TRANSFORMS_BBB1B8B6 = (
    identity,
    rot90,
    rot180,
    rot270,
    hmirror,
    vmirror,
)

FILL_COLORS_BBB1B8B6 = (TWO, TWO, TWO, THREE, THREE, SIX, SEVEN)
ALL_CELLS_BBB1B8B6 = frozenset(product(interval(ZERO, FOUR, ONE), interval(ZERO, FOUR, ONE)))


def _left_grid_bbb1b8b6() -> Grid:
    x0 = choice(LEFT_PATTERNS_BBB1B8B6)
    x1 = choice(TRANSFORMS_BBB1B8B6)
    return x1(x0)


def _mask_grid_bbb1b8b6(
    patch: Patch,
    value: Integer,
) -> Grid:
    return fill(canvas(ZERO, (FOUR, FOUR)), value, patch)


def _other_hole_mask_bbb1b8b6(
    holes: Patch,
) -> Patch:
    while True:
        x0 = _left_grid_bbb1b8b6()
        x1 = ofcolor(x0, ZERO)
        if x1 != holes:
            return x1


def _shifted_mask_bbb1b8b6(
    holes: Patch,
) -> Patch:
    x0 = (
        NEG_ONE,
        ZERO,
        ONE,
    )
    x1 = []
    for x2 in x0:
        for x3 in x0:
            if x2 == ZERO and x3 == ZERO:
                continue
            x4 = frozenset(
                (i + x2, j + x3)
                for i, j in holes
                if ZERO <= i + x2 < FOUR and ZERO <= j + x3 < FOUR
            )
            if len(x4) > ZERO and x4 != holes:
                x1.append(x4)
    if len(x1) == ZERO:
        return holes
    return choice(tuple(x1))


def _distractor_mask_bbb1b8b6(
    holes: Patch,
) -> Patch:
    x0 = tuple(holes)
    x1 = tuple(difference(ALL_CELLS_BBB1B8B6, holes))
    for _ in range(100):
        x2 = choice(("shift", "template", "subset", "superset"))
        if x2 == "shift":
            x3 = _shifted_mask_bbb1b8b6(holes)
        elif x2 == "template":
            x3 = _other_hole_mask_bbb1b8b6(holes)
        elif x2 == "subset" and len(x0) > ONE:
            x4 = randint(ONE, min(THREE, len(x0) - ONE))
            x5 = len(x0) - x4
            x3 = frozenset(sample(x0, x5))
        elif x2 == "superset" and len(x1) > ZERO:
            x4 = randint(ONE, min(THREE, len(x1)))
            x5 = frozenset(sample(x1, x4))
            x3 = combine(holes, x5)
        else:
            x6 = randint(ONE, len(ALL_CELLS_BBB1B8B6) - ONE)
            x3 = frozenset(sample(tuple(ALL_CELLS_BBB1B8B6), x6))
        if len(x3) > ZERO and x3 != holes:
            return x3
    return frozenset({choice(x1)})


def generate_bbb1b8b6(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = _left_grid_bbb1b8b6()
        x1 = ofcolor(x0, ZERO)
        x2 = choice(FILL_COLORS_BBB1B8B6)
        x3 = choice((T, T, T, F, F))
        x4 = x1 if x3 else _distractor_mask_bbb1b8b6(x1)
        x5 = _mask_grid_bbb1b8b6(x4, x2)
        x6 = canvas(FIVE, (FOUR, ONE))
        x7 = hconcat(x0, x6)
        x8 = hconcat(x7, x5)
        x9 = fill(x0, x2, x1)
        x10 = branch(x3, x9, x0)
        return {"input": x8, "output": x10}
