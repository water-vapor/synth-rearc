from synth_rearc.core import *


GRID_BOUNDS_69889D6E = (TEN, 18)


def _sample_blocked_attempts_69889d6e(
    diff_lb: float,
    diff_ub: float,
    max_attempts: Integer,
) -> tuple[Integer, ...]:
    if max_attempts <= TWO:
        return tuple()
    x0 = min(THREE, max(ONE, divide(max_attempts, FOUR)))
    x1 = unifint(diff_lb, diff_ub, (ZERO, x0))
    x2 = set()
    for _ in range(x1):
        x3 = min(FIVE, subtract(max_attempts, TWO))
        x4 = subtract(x3, len(x2))
        if x4 <= ZERO:
            break
        x5 = (ONE,) if x4 == ONE else (ONE, TWO)
        x6 = choice(x5)
        x7 = []
        for x8 in range(TWO, max_attempts):
            x9 = tuple(range(x8, x8 + x6))
            if last(x9) >= max_attempts:
                continue
            if x8 - ONE in x2:
                continue
            if last(x9) + ONE in x2:
                continue
            if any(x10 in x2 for x10 in x9):
                continue
            x7.append(x9)
        if len(x7) == ZERO:
            continue
        x11 = choice(x7)
        x2.update(x11)
    return tuple(sorted(x2))


def _make_example_69889d6e(
    dims: IntegerTuple,
    start_col: Integer,
    blocked_attempts: tuple[Integer, ...],
) -> dict:
    x0 = canvas(ZERO, dims)
    x1 = astuple(decrement(dims[0]), start_col)
    x2 = set()
    x3 = {x1}
    x4 = x1
    x5 = RIGHT
    x6 = ZERO
    x7 = set(blocked_attempts)
    while True:
        x8 = UP if equality(x5, RIGHT) else RIGHT
        x9 = add(x4, x8)
        if equality(index(x0, x9), None):
            break
        if equality(x8, UP):
            x6 = increment(x6)
            if x6 in x7:
                x2.add(x9)
                x10 = add(x4, RIGHT)
                if equality(index(x0, x10), None):
                    break
                x4 = x10
                x3.add(x4)
                x5 = RIGHT
                continue
        x4 = x9
        x3.add(x4)
        x5 = x8
    x11 = fill(x0, ONE, frozenset(x2))
    x12 = fill(x11, TWO, frozenset({x1}))
    x13 = fill(x12, TWO, frozenset(x3))
    return {"input": x12, "output": x13}


def generate_69889d6e(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = unifint(diff_lb, diff_ub, GRID_BOUNDS_69889D6E)
        x1 = unifint(diff_lb, diff_ub, GRID_BOUNDS_69889D6E)
        x2 = max(ZERO, min(subtract(x1, SIX), add(THREE, divide(x1, FOUR))))
        x3 = randint(ZERO, x2)
        x4 = min(decrement(x0), subtract(x1, x3))
        if x4 < THREE:
            continue
        x5 = _sample_blocked_attempts_69889d6e(diff_lb, diff_ub, x4)
        x6 = astuple(x0, x1)
        return _make_example_69889d6e(x6, x3, x5)
