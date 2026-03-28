from arc2.core import *

from .verifier import verify_575b1a71


GRID_SHAPE_575B1A71 = astuple(TEN, TEN)
COLUMN_COLORS_575B1A71 = (ONE, TWO, THREE, FOUR)
COLUMN_COUNTS_575B1A71 = (ONE, ONE, TWO, TWO, THREE, THREE, FOUR)


def _sample_columns_575b1a71() -> tuple[int, ...]:
    x0 = list(range(TEN))
    if choice((True, False)):
        while True:
            x1 = randint(ZERO, subtract(TEN, TWO))
            x2 = {x1, increment(x1)}
            x3 = [x4 for x4 in x0 if x4 not in x2]
            x2.update(sample(x3, TWO))
            x4 = tuple(sorted(x2))
            x5 = sum(x7 == x6 + ONE for x6, x7 in zip(x4, x4[ONE:]))
            if x5 == ONE:
                return x4
    while True:
        x1 = tuple(sorted(sample(x0, FOUR)))
        x2 = sum(x4 == x3 + ONE for x3, x4 in zip(x1, x1[ONE:]))
        if x2 == ZERO:
            return x1


def _grow_rows_575b1a71(
    rows: set[int],
    target: Integer,
) -> tuple[int, ...]:
    while len(rows) < target:
        x0 = [x1 for x1 in range(TEN) if x1 not in rows]
        x2 = [x3 for x3 in x0 if x3 - ONE in rows or x3 + ONE in rows]
        x4 = x2 if x2 and choice((True, False, False)) else x0
        rows.add(choice(x4))
    return tuple(sorted(rows))


def _column_patch_575b1a71(
    rows: tuple[int, ...],
    column: Integer,
) -> Indices:
    return frozenset(astuple(x0, column) for x0 in rows)


def generate_575b1a71(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = _sample_columns_575b1a71()
        x1 = [choice(COLUMN_COUNTS_575B1A71) for _ in x0]
        x2 = sum(x1)
        if not 7 <= x2 <= 15:
            continue
        x3 = {x4: set() for x4 in x0}
        x4 = tuple((x5, x6) for x5, x6 in zip(x0, x0[ONE:]) if x6 == x5 + ONE)
        if x4 and choice((True, False)):
            x5 = choice(x4)
            x6 = x0.index(x5[ZERO])
            x7 = x0.index(x5[ONE])
            x8 = min(TWO, x1[x6], x1[x7])
            x9 = randint(ONE, x8)
            x10 = sample(range(TEN), x9)
            x3[x5[ZERO]].update(x10)
            x3[x5[ONE]].update(x10)
        for x11, x12 in zip(x0, x1):
            x13 = _grow_rows_575b1a71(x3[x11], x12)
            x3[x11] = set(x13)
        gi = canvas(FIVE, GRID_SHAPE_575B1A71)
        go = canvas(FIVE, GRID_SHAPE_575B1A71)
        for x14, x15 in zip(COLUMN_COLORS_575B1A71, x0):
            x16 = tuple(sorted(x3[x15]))
            x17 = _column_patch_575b1a71(x16, x15)
            gi = fill(gi, ZERO, x17)
            go = fill(go, x14, x17)
        if verify_575b1a71(gi) != go:
            continue
        return {"input": gi, "output": go}
