from synth_rearc.core import *


def _block_cells_3b4c2228(
    x0: IntegerTuple,
) -> Indices:
    x1, x2 = x0
    return frozenset(
        {
            (x1, x2),
            (x1, x2 + ONE),
            (x1 + ONE, x2),
            (x1 + ONE, x2 + ONE),
        }
    )


def _expanded_cells_3b4c2228(
    x0: Indices,
) -> Indices:
    x1 = set()
    for x2 in x0:
        x1.add(x2)
        x1 |= neighbors(x2)
    return frozenset(x1)


def _count_green_squares_3b4c2228(
    x0: Indices,
) -> Integer:
    x1 = ZERO
    for x2, x3 in x0:
        x4 = frozenset(
            {
                (x2, x3),
                (x2, x3 + ONE),
                (x2 + ONE, x3),
                (x2 + ONE, x3 + ONE),
            }
        )
        if x4 <= x0:
            x1 += ONE
    return x1


def _singleton_candidates_3b4c2228(
    x0: Integer,
    x1: Integer,
    x2: Indices,
    x3: Indices,
) -> Tuple[IntegerTuple, ...]:
    x4 = _expanded_cells_3b4c2228(x2)
    return tuple(
        (i, j)
        for i in range(x0)
        for j in range(x1)
        if (i, j) not in x3 and (i, j) not in x4
    )


def _block_candidates_3b4c2228(
    x0: Integer,
    x1: Integer,
    x2: Indices,
    x3: Indices,
) -> Tuple[IntegerTuple, ...]:
    x4 = _expanded_cells_3b4c2228(x2)
    return tuple(
        (i, j)
        for i in range(x0 - ONE)
        for j in range(x1 - ONE)
        if len(intersection(_block_cells_3b4c2228((i, j)), x3)) == ZERO
        if len(intersection(_block_cells_3b4c2228((i, j)), x4)) == ZERO
    )


def generate_3b4c2228(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = unifint(diff_lb, diff_ub, (ONE, THREE))
        x1 = branch(
            equality(x0, THREE),
            (SEVEN, SEVEN, EIGHT),
            (FIVE, SEVEN, SEVEN, EIGHT),
        )
        x2 = choice(x1)
        x3 = choice(x1)
        x4 = unifint(diff_lb, diff_ub, (ZERO, FOUR))
        x5 = unifint(diff_lb, diff_ub, (ZERO, THREE))
        x6 = unifint(diff_lb, diff_ub, (ONE, THREE))
        x7 = frozenset()
        x8 = frozenset()
        x9 = frozenset()
        x10 = True
        for _ in range(x0):
            x11 = _block_candidates_3b4c2228(x2, x3, x7, x9)
            x12 = tuple(
                x13
                for x13 in x11
                if equality(
                    _count_green_squares_3b4c2228(combine(x7, _block_cells_3b4c2228(x13))),
                    increment(_count_green_squares_3b4c2228(x7)),
                )
            )
            if len(x12) == ZERO:
                x10 = False
                break
            x13 = choice(x12)
            x14 = _block_cells_3b4c2228(x13)
            x7 = combine(x7, x14)
            x9 = combine(x9, x14)
        if not x10:
            continue
        x15 = maximum((ZERO, minimum((x4, subtract(subtract(multiply(x2, x3), size(x9)), x6)))))
        if positive(x15):
            x16 = choice((x15, x15, maximum((ZERO, decrement(x15)))))
        else:
            x16 = ZERO
        for _ in range(x16):
            x17 = _singleton_candidates_3b4c2228(x2, x3, x7, x9)
            x18 = tuple(
                x19
                for x19 in x17
                if equality(_count_green_squares_3b4c2228(insert(x19, x7)), x0)
            )
            if len(x18) == ZERO:
                break
            x19 = choice(x18)
            x7 = insert(x19, x7)
            x9 = insert(x19, x9)
        x20 = maximum((ZERO, minimum((x5, divide(subtract(subtract(multiply(x2, x3), size(x9)), x6), FOUR)))))
        for _ in range(x20):
            x21 = _block_candidates_3b4c2228(x2, x3, x8, x9)
            if len(x21) == ZERO:
                break
            x22 = choice(x21)
            x23 = _block_cells_3b4c2228(x22)
            x8 = combine(x8, x23)
            x9 = combine(x9, x23)
        x24 = maximum((ZERO, minimum((x6, subtract(multiply(x2, x3), size(x9))))))
        for _ in range(x24):
            x25 = _singleton_candidates_3b4c2228(x2, x3, x8, x9)
            if len(x25) == ZERO:
                break
            x26 = choice(x25)
            x8 = insert(x26, x8)
            x9 = insert(x26, x9)
        if size(x8) == ZERO:
            continue
        x27 = canvas(ZERO, (x2, x3))
        x28 = fill(x27, THREE, x7)
        x29 = fill(x28, TWO, x8)
        x30 = interval(ZERO, x0, ONE)
        x31 = pair(x30, x30)
        x32 = fill(canvas(ZERO, (THREE, THREE)), ONE, x31)
        return {"input": x29, "output": x32}
