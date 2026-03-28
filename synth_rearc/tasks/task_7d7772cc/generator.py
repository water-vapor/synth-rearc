from synth_rearc.core import *

from .verifier import verify_7d7772cc


MIN_SIDE_7D7772CC = EIGHT
MAX_SIDE_7D7772CC = 18
MIN_ACTIVE_7D7772CC = THREE
MAX_ACTIVE_7D7772CC = EIGHT


def _rect_7d7772cc(
    x0: Integer,
    x1: Integer,
    x2: Integer,
    x3: Integer,
) -> Indices:
    return frozenset((i, j) for i in range(x0, x1) for j in range(x2, x3))


def _paint_row_7d7772cc(
    x0: Grid,
    x1: Integer,
    x2: tuple[int, ...],
    x3: tuple[int, ...],
) -> Grid:
    x4 = x0
    for x5, x6 in zip(x2, x3):
        x4 = fill(x4, x6, frozenset({(x1, x5)}))
    return x4


def _paint_col_7d7772cc(
    x0: Grid,
    x1: Integer,
    x2: tuple[int, ...],
    x3: tuple[int, ...],
) -> Grid:
    x4 = x0
    for x5, x6 in zip(x2, x3):
        x4 = fill(x4, x6, frozenset({(x5, x1)}))
    return x4


def _other_color_7d7772cc(
    x0: tuple[int, ...],
    x1: Integer,
) -> Integer:
    return choice(tuple(x2 for x2 in x0 if x2 != x1))


def generate_7d7772cc(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = unifint(diff_lb, diff_ub, (MIN_SIDE_7D7772CC, MAX_SIDE_7D7772CC))
        x1 = x0
        x2 = choice((T, F))
        x3 = sample(interval(ZERO, TEN, ONE), FOUR)
        x4 = x3[ZERO]
        x5 = x3[ONE]
        x6 = x5 if randint(ZERO, TWO) == ZERO else x3[TWO]
        x7 = tuple(x8 for x8 in interval(ZERO, TEN, ONE) if x8 not in {x4, x5, x6})
        if x2:
            x8 = randint(THREE, subtract(x0, FOUR))
            x9 = randint(ONE, decrement(x8))
            x10 = interval(ONE, decrement(x1), ONE)
            x11 = randint(MIN_ACTIVE_7D7772CC, min(MAX_ACTIVE_7D7772CC, len(x10)))
            x12 = tuple(sorted(sample(x10, x11)))
            x13 = tuple(choice(x7) for _ in x12)
            x14 = sample(x12, randint(ONE, decrement(len(x12))))
            x15 = tuple(
                x13[x12.index(x16)]
                if x16 in x14
                else _other_color_7d7772cc(x7, x13[x12.index(x16)])
                for x16 in x12
            )
            x16 = increment(x8)
            x17 = canvas(x6, (x0, x1))
            x18 = fill(x17, x5, _rect_7d7772cc(x16, x0, ZERO, x1))
            x19 = fill(x18, x4, frozenset((x8, j) for j in range(x1)))
            x20 = fill(x19, x4, frozenset((i, ZERO) for i in range(x8, x0)))
            x21 = fill(x20, x4, frozenset((i, decrement(x1)) for i in range(x8, x0)))
            x22 = _paint_row_7d7772cc(x21, x16, x12, x13)
            x23 = _paint_row_7d7772cc(x22, x9, x12, x15)
            x24 = x23
            x25 = decrement(x8)
            for x26, x27, x28 in zip(x12, x13, x15):
                x24 = fill(x24, x6, frozenset({(x9, x26)}))
                x29 = x25 if x27 == x28 else ZERO
                x24 = fill(x24, x28, frozenset({(x29, x26)}))
        else:
            x8 = randint(TWO, subtract(x1, FOUR))
            x9 = randint(increment(x8), subtract(x1, TWO))
            x10 = interval(ONE, decrement(x0), ONE)
            x11 = randint(MIN_ACTIVE_7D7772CC, min(MAX_ACTIVE_7D7772CC, len(x10)))
            x12 = tuple(sorted(sample(x10, x11)))
            x13 = tuple(choice(x7) for _ in x12)
            x14 = sample(x12, randint(ONE, decrement(len(x12))))
            x15 = tuple(
                x13[x12.index(x16)]
                if x16 in x14
                else _other_color_7d7772cc(x7, x13[x12.index(x16)])
                for x16 in x12
            )
            x16 = decrement(x8)
            x17 = canvas(x6, (x0, x1))
            x18 = fill(x17, x5, _rect_7d7772cc(ZERO, x0, ZERO, x8))
            x19 = fill(x18, x4, frozenset((i, x8) for i in range(x0)))
            x20 = fill(x19, x4, frozenset((ZERO, j) for j in range(increment(x8))))
            x21 = fill(x20, x4, frozenset((decrement(x0), j) for j in range(increment(x8))))
            x22 = _paint_col_7d7772cc(x21, x16, x12, x13)
            x23 = _paint_col_7d7772cc(x22, x9, x12, x15)
            x24 = x23
            x25 = increment(x8)
            for x26, x27, x28 in zip(x12, x13, x15):
                x24 = fill(x24, x6, frozenset({(x26, x9)}))
                x29 = x25 if x27 == x28 else decrement(x1)
                x24 = fill(x24, x28, frozenset({(x26, x29)}))
        if verify_7d7772cc(x23) != x24:
            continue
        return {"input": x23, "output": x24}
