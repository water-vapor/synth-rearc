from arc2.core import *

from .verifier import verify_84551f4c


Bar84551f4c = tuple[int, int, int, bool]
HEIGHT_BIAS_84551F4C = (ONE, TWO, TWO, TWO, TWO)
SHORT_HEIGHT_CUTOFF_84551F4C = THREE
TALL_HEIGHT_BOUNDS_84551F4C = (FIVE, NINE)
CHAIN_LENGTH_CAP_84551F4C = SIX


def _allowed_heights_84551f4c(grid_height: int) -> tuple[int, ...]:
    if grid_height == THREE:
        return (THREE,)
    return tuple(range(TWO, min(FOUR, grid_height) + ONE))


def _render_input_84551f4c(
    grid_height: int,
    grid_width: int,
    bars: tuple[Bar84551f4c, ...],
) -> Grid:
    x0 = canvas(ZERO, (grid_height, grid_width))
    x1 = x0
    for x2, x3, x4, _ in bars:
        x5 = frozenset((i, x2) for i in range(grid_height - x3, grid_height))
        x1 = fill(x1, x4, x5)
    return x1


def _render_output_84551f4c(
    grid_height: int,
    grid_width: int,
    bars: tuple[Bar84551f4c, ...],
) -> Grid:
    x0 = canvas(ZERO, (grid_height, grid_width))
    x1 = x0
    for x2, x3, x4, x5 in bars:
        if x5:
            continue
        x6 = frozenset((i, x2) for i in range(grid_height - x3, grid_height))
        x1 = fill(x1, x4, x6)
    x7 = decrement(grid_height)
    x8 = x1
    for x9, x10, x11, x12 in bars:
        if not x12:
            continue
        x13 = frozenset((x7, j) for j in range(x9, x9 + x10))
        x8 = fill(x8, x11, x13)
    return x8


def generate_84551f4c(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = unifint(diff_lb, diff_ub, (ZERO, FOUR))
        x1 = branch(greater(SHORT_HEIGHT_CUTOFF_84551F4C, x0), THREE, unifint(diff_lb, diff_ub, TALL_HEIGHT_BOUNDS_84551F4C))
        x2 = _allowed_heights_84551f4c(x1)
        x3 = min(x2)
        x4: list[Bar84551f4c] = []
        x5 = randint(ZERO, TWO)
        x6 = ZERO
        while x5 <= 30 - x3 and x6 < THREE:
            x7 = min(CHAIN_LENGTH_CAP_84551F4C, (30 - x5) // x3)
            if x7 < ONE:
                break
            x8 = unifint(diff_lb, diff_ub, (ONE, x7))
            x9 = x5
            x10: list[Bar84551f4c] = []
            for x11 in range(x8):
                x12 = x8 - x11 - ONE
                x13 = tuple(v for v in x2 if x9 + v + x3 * x12 <= 30)
                if len(x13) == ZERO:
                    x10 = []
                    break
                x14 = choice(x13)
                x15 = ONE if x11 == ZERO else choice(HEIGHT_BIAS_84551F4C)
                x10.append((x9, x14, x15, True))
                x9 = add(x9, x14)
            if len(x10) == ZERO:
                break
            x4.extend(x10)
            x6 = increment(x6)
            x16 = x10[-ONE][ZERO]
            x17 = x10[-ONE][ONE]
            x18 = x16
            x19 = x17
            x20 = unifint(diff_lb, diff_ub, (ZERO, TWO))
            for x21 in range(x20):
                x22 = randint(ONE, TWO) if x21 == ZERO else randint(ZERO, ONE)
                x23 = x18 + x19 + x22
                if x23 >= 30:
                    break
                x24 = choice(x2)
                x4.append((x23, x24, TWO, False))
                x18 = x23
                x19 = x24
            if len(x4) > ONE and (x6 == THREE or randint(ZERO, ONE) == ZERO):
                break
            if x18 == x16 and x19 == x17:
                x5 = x18 + x19 + randint(ONE, TWO)
            else:
                x5 = x18 + x19 + randint(ZERO, ONE)
        if len(x4) < TWO:
            continue
        x25 = max(x26 + (x27 if x29 else ONE) for x26, x27, _, x29 in x4)
        x26 = randint(ZERO, min(FOUR, 30 - x25))
        x27 = max(SEVEN, x25 + x26)
        x28 = tuple(x4)
        x29 = _render_input_84551f4c(x1, x27, x28)
        x30 = _render_output_84551f4c(x1, x27, x28)
        if verify_84551f4c(x29) != x30:
            continue
        return {"input": x29, "output": x30}
