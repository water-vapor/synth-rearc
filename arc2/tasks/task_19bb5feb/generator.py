from arc2.core import *


HEIGHT_CHOICES_19BB5FEB = (FOUR, FIVE, SIX)
WIDTH_CHOICES_19BB5FEB = ((FOUR, ZERO), (FOUR, ONE), (SIX, ZERO), (SIX, ONE))
BLOCK_COUNT_CHOICES_19BB5FEB = (TWO, THREE, THREE, FOUR)
QUADRANTS_19BB5FEB = ((ZERO, ZERO), (ZERO, ONE), (ONE, ZERO), (ONE, ONE))
ACTIVE_COLORS_19BB5FEB = remove(EIGHT, interval(ONE, TEN, ONE))


def _bounds_19bb5feb(index_value: int, span: int) -> tuple[int, int]:
    if index_value == ZERO:
        return (ONE, span - TWO)
    return (ZERO, span - THREE)


def _occupied_quadrants_19bb5feb(nblocks: int) -> tuple[int, ...]:
    while True:
        x0 = tuple(sample(interval(ZERO, FOUR, ONE), nblocks))
        x1 = {x2 // TWO for x2 in x0}
        x2 = {x3 % TWO for x3 in x0}
        if len(x1) == TWO and len(x2) == TWO:
            return x0


def generate_19bb5feb(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    x0 = HEIGHT_CHOICES_19BB5FEB[unifint(diff_lb, diff_ub, (ZERO, TWO))]
    x1 = WIDTH_CHOICES_19BB5FEB[unifint(diff_lb, diff_ub, (ZERO, THREE))]
    x2, x3 = x1
    x4 = multiply(TWO, x0)
    x5 = add(multiply(TWO, x2), x3)
    x6 = randint(ONE, FOUR)
    x7 = randint(ONE, FOUR)
    x8 = randint(ONE, FOUR)
    x9 = randint(ONE, FOUR)
    x10 = add(add(x6, x4), x7)
    x11 = add(add(x8, x5), x9)
    x12 = canvas(ZERO, (x10, x11))
    x13 = product(interval(x6, add(x6, x4), ONE), interval(x8, add(x8, x5), ONE))
    x14 = fill(x12, EIGHT, x13)
    x15 = BLOCK_COUNT_CHOICES_19BB5FEB[unifint(diff_lb, diff_ub, (ZERO, THREE))]
    x16 = _occupied_quadrants_19bb5feb(x15)
    x17 = sample(ACTIVE_COLORS_19BB5FEB, x15)
    x18 = [[ZERO, ZERO], [ZERO, ZERO]]
    for x19, x20 in zip(x16, x17):
        x21, x22 = QUADRANTS_19BB5FEB[x19]
        x23, x24 = _bounds_19bb5feb(x21, x0)
        x25, x26 = _bounds_19bb5feb(x22, x2)
        x27 = randint(x23, x24)
        x28 = randint(x25, x26)
        x29 = add(x6, add(multiply(x21, x0), x27))
        x30 = add(x8, add(multiply(x22, add(x2, x3)), x28))
        x31 = product(interval(x29, add(x29, TWO), ONE), interval(x30, add(x30, TWO), ONE))
        x14 = fill(x14, x20, x31)
        x18[x21][x22] = x20
    go = tuple(tuple(row) for row in x18)
    return {"input": x14, "output": go}
