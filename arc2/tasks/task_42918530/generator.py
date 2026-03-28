from arc2.core import *


STEP_42918530 = SIX
FRAME_SIZE_42918530 = FIVE
INTERIOR_LOCS_42918530 = tuple((i, j) for i in range(ONE, FOUR) for j in range(ONE, FOUR))
FRAME_LOCS_42918530 = frozenset(
    (i, j)
    for i in range(FIVE)
    for j in range(FIVE)
    if i in (ZERO, FOUR) or j in (ZERO, FOUR)
)


def _paint_frame_42918530(
    grid: Grid,
    top: int,
    left: int,
    color: int,
    pattern: frozenset[tuple[int, int]],
) -> Grid:
    x0 = frozenset(add((top, left), x1) for x1 in FRAME_LOCS_42918530)
    x1 = frozenset(add((top, left), x2) for x2 in pattern)
    x2 = fill(grid, color, x0)
    x3 = fill(x2, color, x1)
    return x3


def generate_42918530(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    x0 = unifint(diff_lb, diff_ub, (TWO, FOUR))
    x1 = unifint(diff_lb, diff_ub, (THREE, FOUR))
    x2 = multiply(x0, x1)
    x3 = add(multiply(STEP_42918530, x0), ONE)
    x4 = add(multiply(STEP_42918530, x1), ONE)
    x5 = canvas(ZERO, (x3, x4))
    x6 = min(SIX, subtract(x2, ONE))
    x7 = unifint(diff_lb, diff_ub, (THREE, x6))
    x8 = sample(interval(ONE, TEN, ONE), x7)
    x9 = list(x8)
    x10 = subtract(x2, x7)
    for _ in range(x10):
        x9.append(choice(x8))
    shuffle(x9)
    x11 = {x12: x9.count(x12) for x12 in x8}
    x12 = tuple(x13 for x13 in x8 if greater(x11[x13], ONE))
    x13 = unifint(diff_lb, diff_ub, (ONE, len(x12)))
    x14 = sample(x12, x13)
    x15 = {
        x16: frozenset(
            add(UNITY, x17)
            for x17 in sample(
                INTERIOR_LOCS_42918530,
                unifint(diff_lb, diff_ub, (ONE, FIVE)),
            )
        )
        for x16 in x14
    }
    x16 = []
    for x17 in x8:
        x18 = x11[x17]
        if x17 in x14:
            x16.append((x17, x15[x17]))
            x16.extend((x17, frozenset()) for _ in range(decrement(x18)))
        else:
            x16.extend((x17, frozenset()) for _ in range(x18))
    shuffle(x16)
    x17 = tuple(
        (add(ONE, multiply(STEP_42918530, i)), add(ONE, multiply(STEP_42918530, j)))
        for i in range(x0)
        for j in range(x1)
    )
    x18 = x5
    x19 = x5
    for (x20, x21), (x22, x23) in zip(x16, x17):
        x18 = _paint_frame_42918530(x18, x22, x23, x20, x21)
        x24 = x21
        if len(x21) == ZERO and x20 in x15:
            x24 = x15[x20]
        x19 = _paint_frame_42918530(x19, x22, x23, x20, x24)
    return {"input": x18, "output": x19}
