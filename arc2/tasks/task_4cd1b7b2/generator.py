from arc2.core import *


CANONICAL_LATIN_4CD1B7B2 = (
    (ONE, TWO, THREE, FOUR),
    (THREE, FOUR, TWO, ONE),
    (TWO, ONE, FOUR, THREE),
    (FOUR, THREE, ONE, TWO),
)
LATIN_DIGITS_4CD1B7B2 = interval(ONE, FIVE, ONE)
LATIN_AXIS_4CD1B7B2 = interval(ZERO, FOUR, ONE)


def _candidates_4cd1b7b2(
    grid: Grid,
    loc: IntegerTuple,
) -> tuple[int, ...]:
    x0, x1 = loc
    x2 = remove(ZERO, frozenset(grid[x0]))
    x3 = remove(ZERO, frozenset(x4[x1] for x4 in grid))
    x4 = difference(LATIN_DIGITS_4CD1B7B2, x2)
    x5 = difference(x4, x3)
    return tuple(x5)


def _count_solutions_4cd1b7b2(
    grid: Grid,
    limit: Integer = TWO,
) -> Integer:
    x0 = grid
    while True:
        x1 = ofcolor(x0, ZERO)
        if len(x1) == ZERO:
            return ONE
        x2 = []
        x3 = F
        for x4 in x1:
            x5 = _candidates_4cd1b7b2(x0, x4)
            x6 = len(x5)
            if x6 == ZERO:
                return ZERO
            x2.append((x6, x4, x5))
            x3 = either(x3, equality(x6, ONE))
        if flip(x3):
            break
        x2.sort(key=lambda x4: (x4[ZERO], x4[ONE][ZERO], x4[ONE][ONE]))
        for _, x4, x5 in x2:
            if len(x5) != ONE:
                continue
            x0 = fill(x0, x5[ZERO], initset(x4))
    x7 = min(x2, key=lambda x4: (x4[ZERO], x4[ONE][ZERO], x4[ONE][ONE]))
    _, x8, x9 = x7
    x10 = ZERO
    for x11 in x9:
        x12 = fill(x0, x11, initset(x8))
        x13 = _count_solutions_4cd1b7b2(x12, limit)
        x10 = add(x10, x13)
        if x10 >= limit:
            return limit
    return x10


def _sample_output_4cd1b7b2() -> Grid:
    x0 = tuple(sample(LATIN_AXIS_4CD1B7B2, FOUR))
    x1 = tuple(sample(LATIN_AXIS_4CD1B7B2, FOUR))
    x2 = tuple(sample(LATIN_DIGITS_4CD1B7B2, FOUR))
    x3 = tuple(CANONICAL_LATIN_4CD1B7B2[x4] for x4 in x0)
    x4 = tuple(tuple(x5[x6] for x6 in x1) for x5 in x3)
    x5 = {x6: x7 for x6, x7 in zip(LATIN_DIGITS_4CD1B7B2, x2)}
    x6 = tuple(tuple(x5[x7] for x7 in x8) for x8 in x4)
    return x6


def _sample_zero_mask_4cd1b7b2(
    target: Integer,
) -> tuple[IntegerTuple, ...]:
    x0 = [ZERO, ZERO, ZERO, ZERO]
    x1 = []
    x2 = list(LATIN_AXIS_4CD1B7B2)
    shuffle(x2)
    for x3 in x2:
        x4 = list(LATIN_AXIS_4CD1B7B2)
        shuffle(x4)
        x5 = (x3, x4[ZERO])
        x1.append(x5)
        x0[x3] = increment(x0[x3])
    x6 = subtract(target, FOUR)
    while x6 > ZERO:
        x7 = [
            (x8, x9)
            for x8 in LATIN_AXIS_4CD1B7B2
            for x9 in LATIN_AXIS_4CD1B7B2
            if (x8, x9) not in x1 and x0[x8] < THREE
        ]
        if len(x7) == ZERO:
            break
        x8 = choice(x7)
        x1.append(x8)
        x0[x8[ZERO]] = increment(x0[x8[ZERO]])
        x6 = decrement(x6)
    x9 = [ZERO, ZERO, ZERO, ZERO]
    for _, x10 in x1:
        x9[x10] = increment(x9[x10])
    if any(equality(x10, FOUR) for x10 in x9):
        return tuple()
    return tuple(sorted(x1))


def generate_4cd1b7b2(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    from .verifier import verify_4cd1b7b2

    while True:
        x0 = _sample_output_4cd1b7b2()
        x1 = unifint(diff_lb, diff_ub, (FIVE, SIX))
        x2 = _sample_zero_mask_4cd1b7b2(x1)
        if len(x2) != x1:
            continue
        x3 = x0
        for x4 in x2:
            x3 = fill(x3, ZERO, initset(x4))
        x5 = _count_solutions_4cd1b7b2(x3)
        if x5 != ONE:
            continue
        if verify_4cd1b7b2(x3) != x0:
            continue
        return {"input": x3, "output": x0}
