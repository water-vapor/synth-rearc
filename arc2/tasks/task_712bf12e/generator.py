from arc2.core import *


MOTIFS_712BF12E = (
    frozenset({(0, 0)}),
    frozenset({(0, 0), (0, 1)}),
    frozenset({(0, 0), (1, 0)}),
    frozenset({(0, 0), (0, 1), (0, 2)}),
    frozenset({(0, 0), (1, 0), (2, 0)}),
    frozenset({(0, 0), (0, 1), (1, 0)}),
    frozenset({(0, 0), (0, 1), (1, 1)}),
    frozenset({(0, 0), (1, 0), (1, 1)}),
    frozenset({(0, 1), (1, 0), (1, 1)}),
    frozenset({(0, 0), (0, 1), (1, 1), (1, 2)}),
    frozenset({(0, 0), (1, 0), (1, 1), (2, 1)}),
    frozenset({(0, 0), (0, 1), (1, 0), (1, 1)}),
    frozenset({(0, 0), (0, 1), (0, 2), (0, 3)}),
    frozenset({(0, 0), (1, 0), (2, 0), (3, 0)}),
)


def _trace_seed_712bf12e(
    I: Grid,
    seed: IntegerTuple,
) -> tuple[IntegerTuple, ...]:
    x0 = height(I)
    x1 = width(I)
    x2, x3 = seed
    x4 = [seed]
    while x2 > ZERO:
        x5 = decrement(x2)
        x6 = (x5, x3)
        x7 = index(I, x6)
        if x7 == ZERO:
            x2 = x5
            x4.append((x2, x3))
            continue
        x8 = increment(x3)
        if both(x8 < x1, equality(index(I, (x2, x8)), ZERO)):
            x3 = x8
            x4.append((x2, x3))
            continue
        break
    return tuple(x4)


def _solve_712bf12e(
    I: Grid,
) -> tuple[Grid, tuple[tuple[IntegerTuple, ...], ...], Indices]:
    x0 = tuple(sorted(ofcolor(I, TWO), key=lambda x: x[1]))
    x1 = tuple(_trace_seed_712bf12e(I, x2) for x2 in x0)
    x2 = frozenset(cell for path in x1 for cell in path)
    x3 = fill(I, TWO, x2)
    return x3, x1, x2


def _sample_seed_columns_712bf12e(
    width_: Integer,
) -> tuple[Integer, Integer, Integer]:
    while True:
        x0 = sorted(sample(tuple(range(ONE, width_ - ONE)), THREE))
        x1 = tuple(b - a for a, b in zip(x0, x0[1:]))
        if minimum(x1) < TWO:
            continue
        if x0[-1] > subtract(width_, THREE):
            continue
        return tuple(x0)


def _plan_blockers_712bf12e(
    height_: Integer,
    width_: Integer,
    seed_col: Integer,
    allow_stop: Boolean,
) -> Indices:
    x0 = subtract(height_, ONE)
    x1 = seed_col
    x2 = set()
    x3 = randint(ZERO, min(THREE, subtract(subtract(width_, ONE), x1)))
    x4 = ZERO
    while x0 > ZERO:
        x5 = both(allow_stop, greater(x4, THREE))
        x6 = both(x5, greater(x0, TWO))
        x7 = randint(ZERO, SIX) == ZERO
        if both(x6, x7):
            x2.add((decrement(x0), x1))
            if increment(x1) < width_:
                x2.add((x0, increment(x1)))
            break
        x8 = greater(x3, ZERO)
        x9 = increment(x1) < width_
        x10 = randint(ZERO, FOUR) == ZERO
        if both(both(x8, x9), x10):
            x2.add((decrement(x0), x1))
            x1 = increment(x1)
            x3 = decrement(x3)
            x4 = increment(x4)
            continue
        x0 = decrement(x0)
        x4 = increment(x4)
    return frozenset(x2)


def _shift_patch_712bf12e(
    patch: Indices,
    offset: IntegerTuple,
) -> Indices:
    x0, x1 = offset
    return frozenset((i + x0, j + x1) for i, j in patch)


def _scatter_noise_712bf12e(
    I: Grid,
    protected: Indices,
    target_five_count: Integer,
) -> Grid:
    x0 = height(I)
    x1 = width(I)
    x2 = I
    x3 = ZERO
    while both(colorcount(x2, FIVE) < target_five_count, x3 < 400):
        x4 = choice(MOTIFS_712BF12E)
        x5 = increment(max(i for i, _ in x4))
        x6 = increment(max(j for _, j in x4))
        x7 = randint(ZERO, subtract(x0, x5))
        x8 = randint(ZERO, subtract(x1, x6))
        x9 = _shift_patch_712bf12e(x4, (x7, x8))
        x10 = intersection(x9, protected)
        if x10:
            x3 = increment(x3)
            continue
        x11 = any(index(x2, x12) != ZERO for x12 in x9)
        if x11:
            x3 = increment(x3)
            continue
        x2 = fill(x2, FIVE, x9)
        x3 = increment(x3)
    return x2


def generate_712bf12e(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = unifint(diff_lb, diff_ub, (12, 13))
        x1 = unifint(diff_lb, diff_ub, (13, 15))
        x2 = _sample_seed_columns_712bf12e(x1)
        x3 = branch(randint(ZERO, TWO) == ZERO, randint(ZERO, TWO), NEG_ONE)
        x4 = frozenset()
        for x5, x6 in enumerate(x2):
            x7 = x5 == x3
            x8 = _plan_blockers_712bf12e(x0, x1, x6, x7)
            x4 = combine(x4, x8)
        x9 = canvas(ZERO, (x0, x1))
        x10 = fill(x9, FIVE, x4)
        x11 = frozenset((subtract(x0, ONE), x12) for x12 in x2)
        x13 = fill(x10, TWO, x11)
        x14, x15, x16 = _solve_712bf12e(x13)
        x17 = tuple(len(x18) for x18 in x15)
        x18 = tuple(sum(ONE for a, b in zip(x19, x19[1:]) if b[1] != a[1]) for x19 in x15)
        x19 = sum(x18)
        x20 = sum(ONE for x21 in x15 if x21[-ONE][0] == ZERO)
        x21 = size(x16) - THREE
        if x20 < TWO:
            continue
        if x19 < TWO:
            continue
        if x19 > EIGHT:
            continue
        if minimum(x17) < FIVE:
            continue
        if x21 < add(x0, SIX):
            continue
        x22 = multiply(x0, x1)
        x23 = maximum((colorcount(x13, FIVE), unifint(diff_lb, diff_ub, (x22 // SIX, x22 // FOUR))))
        x24 = _scatter_noise_712bf12e(x13, x16, x23)
        x25, x26, x27 = _solve_712bf12e(x24)
        x28 = tuple(len(x29) for x29 in x26)
        x29 = tuple(sum(ONE for a, b in zip(x30, x30[1:]) if b[1] != a[1]) for x30 in x26)
        x30 = sum(x29)
        x31 = sum(ONE for x32 in x26 if x32[-ONE][0] == ZERO)
        x32 = size(x27) - THREE
        x33 = colorcount(x24, FIVE)
        if x31 < TWO:
            continue
        if x30 < TWO:
            continue
        if x30 > EIGHT:
            continue
        if minimum(x28) < FIVE:
            continue
        if x32 < add(x0, SIX):
            continue
        if x33 < x22 // SEVEN:
            continue
        if x33 > x22 // THREE:
            continue
        if colorcount(x25, ZERO) == ZERO:
            continue
        return {"input": x24, "output": x25}
