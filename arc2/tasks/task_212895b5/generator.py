from arc2.core import *

from .helpers import (
    ARM_SPECS_212895B5,
    DIAGONAL_SPECS_212895B5,
    arm_paths_212895b5,
    block_patch_212895b5,
    diagonal_paths_212895b5,
    flatten_paths_212895b5,
)


NOISE_MOTIFS_212895B5 = (
    frozenset({(0, 0)}),
    frozenset({(0, 0)}),
    frozenset({(0, 0)}),
    frozenset({(0, 0), (0, 1)}),
    frozenset({(0, 0), (1, 0)}),
    frozenset({(0, 0), (0, 1), (0, 2)}),
    frozenset({(0, 0), (1, 0), (2, 0)}),
    frozenset({(0, 0), (0, 1), (1, 0)}),
    frozenset({(0, 0), (0, 1), (1, 1)}),
    frozenset({(0, 0), (1, 0), (1, 1)}),
    frozenset({(0, 1), (1, 0), (1, 1)}),
)


def _render_212895b5(
    I: Grid,
    origin: IntegerTuple,
) -> tuple[Grid, tuple[tuple[IntegerTuple, ...], ...], tuple[tuple[IntegerTuple, ...], ...], Indices, Indices]:
    x0 = arm_paths_212895b5(I, origin)
    x1 = diagonal_paths_212895b5(I, origin)
    x2 = flatten_paths_212895b5(x0)
    x3 = flatten_paths_212895b5(x1)
    x4 = fill(I, FOUR, x2)
    x5 = fill(x4, TWO, x3)
    return x5, x0, x1, x2, x3


def _shift_patch_212895b5(
    patch: Indices,
    offset: IntegerTuple,
) -> Indices:
    return shift(patch, offset)


def _expanded_patch_212895b5(
    patch: Indices,
) -> Indices:
    x0 = set(patch)
    for x1 in patch:
        x0.update(neighbors(x1))
    return frozenset(x0)


def _noise_patch_ok_212895b5(
    I: Grid,
    patch: Indices,
    protected: Indices,
) -> Boolean:
    if intersection(patch, protected):
        return F
    for x0 in patch:
        if index(I, x0) != ZERO:
            return F
        for x1 in insert(x0, neighbors(x0)):
            if x1 in patch:
                continue
            if index(I, x1) == FIVE:
                return F
    return T


def _scatter_noise_212895b5(
    I: Grid,
    protected: Indices,
    target_five_count: Integer,
) -> Grid:
    x0 = height(I)
    x1 = width(I)
    x2 = I
    x3 = ZERO
    while both(colorcount(x2, FIVE) < target_five_count, x3 < 800):
        x4 = choice(NOISE_MOTIFS_212895B5)
        x5 = increment(max(i for i, _ in x4))
        x6 = increment(max(j for _, j in x4))
        x7 = randint(ZERO, subtract(x0, x5))
        x8 = randint(ZERO, subtract(x1, x6))
        x9 = _shift_patch_212895b5(x4, (x7, x8))
        if not _noise_patch_ok_212895b5(x2, x9, protected):
            x3 = increment(x3)
            continue
        x2 = fill(x2, FIVE, x9)
        x3 = increment(x3)
    return x2


def _plan_arm_blockers_212895b5(
    paths: tuple[tuple[IntegerTuple, ...], ...],
) -> Indices:
    x0 = tuple(x1 for x1, x2 in enumerate(paths) if len(x2) > ONE)
    if not x0:
        return frozenset()
    x1 = choice(x0)
    x2 = tuple(x3 for x3 in x0 if x3 != x1)
    if not x2:
        return frozenset()
    x3 = choice(x2)
    x0 = set()
    for x4, x5 in enumerate(paths):
        x6 = len(x5)
        if x6 <= ONE:
            continue
        if x4 == x1:
            continue
        if both(x4 != x3, randint(ZERO, TWO) == ZERO):
            continue
        x7 = randint(ONE, decrement(x6))
        x8 = x5[x7]
        if x8 in x0:
            return frozenset()
        x0.add(x8)
    return frozenset(x0)


def _plan_diagonal_blockers_212895b5(
    origin: IntegerTuple,
    paths: tuple[tuple[IntegerTuple, ...], ...],
    protected: Indices,
) -> Indices:
    x0 = tuple(x1 for x1, x2 in enumerate(paths) if len(x2) > ZERO)
    if len(x0) < TWO:
        return frozenset()
    x1 = choice(x0)
    x2 = tuple(x3 for x3 in x0 if x3 != x1)
    x3 = choice(x2)
    x0 = set()
    for x4, ((x5, x6), x7) in enumerate(zip(DIAGONAL_SPECS_212895B5, paths)):
        x8 = len(x7)
        if x8 == ZERO:
            continue
        if x4 == x1:
            continue
        if both(x4 != x3, randint(ZERO, TWO) == ZERO):
            continue
        x9 = both(greater(x8, ONE), randint(ZERO, ONE) == ZERO)
        if x9:
            x10 = randint(ONE, decrement(x8))
            x11 = add(origin, x5) if x10 == ZERO else x7[decrement(x10)]
            x12 = add(x11, (x6[0], ZERO))
            x13 = add(x11, (ZERO, x6[1]))
            x14 = frozenset({x12, x13})
            if intersection(x14, protected) or intersection(x14, frozenset(x0)):
                x15 = x7[x10]
                if x15 in x0:
                    return frozenset()
                x0.add(x15)
                continue
            x0.update(x14)
            continue
        x10 = randint(ZERO, decrement(x8))
        x11 = x7[x10]
        if x11 in x0:
            return frozenset()
        x0.add(x11)
    return frozenset(x0)


def generate_212895b5(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = unifint(diff_lb, diff_ub, (16, 22))
        x1 = unifint(diff_lb, diff_ub, (17, 24))
        x2 = randint(FOUR, subtract(x0, SEVEN))
        x3 = randint(FOUR, subtract(x1, SEVEN))
        x4 = (x2, x3)
        x5 = canvas(ZERO, (x0, x1))
        x6 = block_patch_212895b5(x4)
        x7 = fill(x5, EIGHT, x6)
        x8, x9, x10, _, _ = _render_212895b5(x7, x4)
        x11 = _plan_arm_blockers_212895b5(x9)
        if not x11:
            continue
        x12 = x6 | flatten_paths_212895b5(x10)
        x13 = _plan_diagonal_blockers_212895b5(x4, x10, x12)
        if not x13:
            continue
        x14 = combine(x11, x13)
        x15 = fill(x7, FIVE, x14)
        x16, x17, x18, x19, x20 = _render_212895b5(x15, x4)
        x21 = tuple(len(x22) for x22 in x9)
        x23 = tuple(len(x24) for x24 in x10)
        x25 = tuple(len(x26) for x26 in x17)
        x27 = tuple(len(x28) for x28 in x18)
        x29 = sum(ONE for a, b in zip(x25, x21) if a < b)
        x30 = sum(ONE for a, b in zip(x25, x21) if a == b)
        x31 = sum(ONE for a, b in zip(x27, x23) if a < b)
        x32 = sum(ONE for a, b in zip(x27, x23) if a == b)
        if x29 == ZERO:
            continue
        if x30 == ZERO:
            continue
        if x31 == ZERO:
            continue
        if x32 == ZERO:
            continue
        if len(x19) < TEN:
            continue
        if len(x20) < EIGHT:
            continue
        if max(x25) < FOUR:
            continue
        if max(x27) < THREE:
            continue
        x33 = _expanded_patch_212895b5(x6 | x19 | x20)
        x34 = multiply(x0, x1)
        x35 = max(
            colorcount(x15, FIVE) + randint(SIX, add(TEN, TWO)),
            unifint(diff_lb, diff_ub, (x34 // 18, x34 // 10)),
        )
        x36 = _scatter_noise_212895b5(x15, x33, x35)
        x37, x38, x39, x40, x41 = _render_212895b5(x36, x4)
        x42 = colorcount(x36, FIVE)
        if x42 < x34 // 20:
            continue
        if x42 > x34 // 8:
            continue
        if colorcount(x37, ZERO) == ZERO:
            continue
        if x40 != x19:
            continue
        if x41 != x20:
            continue
        return {"input": x36, "output": x37}
