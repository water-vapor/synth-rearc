from synth_rearc.core import *

from .verifier import verify_f9a67cb5


def _canonical_output_f9a67cb5(
    grid: Grid,
) -> Grid:
    x0 = height(grid)
    x1 = width(grid)
    x2 = set(ofcolor(grid, TWO))
    x3 = [first(x2)]
    x4 = set()
    while len(x3) > ZERO:
        x5 = x3.pop()
        if x5 in x4:
            continue
        x4.add(x5)
        x6, x7 = x5
        x8 = None
        for x9 in range(x7 + ONE, x1):
            if grid[x6][x9] == EIGHT:
                x8 = x9
                break
        if x8 is None:
            x2 |= set(connect(x5, (x6, decrement(x1))))
            continue
        x2 |= set(connect(x5, (x6, decrement(x8))))
        x10 = tuple(i for i in range(x0) if grid[i][x8] != EIGHT)
        x11 = tuple(i for i in x10 if i < x6)
        x12 = tuple(i for i in x10 if i > x6)
        x13 = last(x11) if len(x11) > ZERO else ZERO
        x14 = first(x12) if len(x12) > ZERO else decrement(x0)
        x15 = connect((x13, decrement(x8)), (x14, decrement(x8)))
        x2 |= set(x15)
        if len(x11) > ZERO:
            x16 = (x13, x8)
            x2.add(x16)
            x3.append(x16)
        if len(x12) > ZERO:
            x17 = (x14, x8)
            x2.add(x17)
            x3.append(x17)
    return fill(grid, TWO, frozenset(x2))


def _sample_columns_f9a67cb5(
    diff_lb: float,
    diff_ub: float,
    width_value: Integer,
) -> tuple[Integer, ...] | None:
    x0 = choice((THREE, THREE, THREE, FOUR))
    if width_value < x0 * TWO + THREE:
        x0 = THREE
    if width_value < x0 * TWO + THREE:
        return None
    x1 = []
    x2 = TWO
    for x3 in range(x0):
        x4 = x0 - x3 - ONE
        x5 = width_value - TWO - x4 * TWO
        if x2 > x5:
            return None
        x6 = unifint(diff_lb, diff_ub, (x2, x5))
        x1.append(x6)
        x2 = x6 + TWO
    return tuple(x1)


def _sample_holes_f9a67cb5(
    height_value: Integer,
    blocked_row: Integer | None = None,
) -> tuple[Integer, ...]:
    while True:
        x0 = choice((ONE, ONE, TWO, TWO))
        if height_value <= FIVE:
            x0 = ONE
        x1 = list(range(height_value))
        shuffle(x1)
        x2 = []
        for x3 in x1:
            if blocked_row is not None and x3 == blocked_row:
                continue
            if any(abs(x3 - x4) <= ONE for x4 in x2):
                continue
            x2.append(x3)
            if len(x2) == x0:
                break
        if len(x2) != x0:
            continue
        return tuple(sorted(x2))


def _line_lengths_f9a67cb5(
    grid: Grid,
) -> tuple[Integer, Integer]:
    x0 = ofcolor(grid, TWO)
    x1 = tuple(sorted({j for i, j in x0}))
    x2 = tuple(sorted({i for i, j in x0}))
    return (len(x2), len(x1))


def _canonical_example_f9a67cb5(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = unifint(diff_lb, diff_ub, (TEN, 18))
        x1 = unifint(diff_lb, diff_ub, (TEN, 18))
        x2 = _sample_columns_f9a67cb5(diff_lb, diff_ub, x1)
        if x2 is None:
            continue
        x3 = randint(ZERO, decrement(x0))
        x4 = canvas(ZERO, (x0, x1))
        for x5, x6 in enumerate(x2):
            x7 = x3 if x5 == ZERO else None
            x8 = _sample_holes_f9a67cb5(x0, x7)
            x9 = difference(product(interval(ZERO, x0, ONE), initset(x6)), product(x8, initset(x6)))
            x4 = fill(x4, EIGHT, x9)
        x10 = fill(x4, TWO, frozenset({(x3, ZERO)}))
        x11 = _canonical_output_f9a67cb5(x10)
        x12 = colorcount(x11, TWO)
        x13, x14 = _line_lengths_f9a67cb5(x11)
        x15 = tuple(sorted({j for i, j in ofcolor(x11, TWO)}))
        if x12 < max(TEN, x0 + THREE):
            continue
        if x13 < THREE or x14 < THREE:
            continue
        if x15[-ONE] <= x2[ZERO]:
            continue
        if x11 == x10:
            continue
        return {"input": x10, "output": x11}


def generate_f9a67cb5(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    x0 = _canonical_example_f9a67cb5(diff_lb, diff_ub)
    x1 = choice((identity, vmirror, rot90, rot270))
    x2 = {
        "input": x1(x0["input"]),
        "output": x1(x0["output"]),
    }
    if verify_f9a67cb5(x2["input"]) != x2["output"]:
        return generate_f9a67cb5(diff_lb, diff_ub)
    return x2
