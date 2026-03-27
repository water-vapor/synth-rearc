from arc2.core import *

from .verifier import verify_2faf500b


def _push_rows_2faf500b(G: Grid) -> Grid:
    x0 = width(G)
    x1 = halve(x0)
    x2 = []
    for x3 in G:
        x4 = x3.index(SIX)
        x5 = subtract(subtract(x0, x4), ONE)
        x6 = combine(repeat(NINE, x4), repeat(ZERO, subtract(x1, x4)))
        x7 = combine(repeat(ZERO, subtract(x1, x5)), repeat(NINE, x5))
        x8 = combine(x6, repeat(ZERO, TWO))
        x9 = combine(x8, x7)
        x2.append(x9)
    return tuple(x2)


def _make_landscape_local_2faf500b(
    height_value: int,
    width_value: int,
    phase: int,
) -> Grid:
    x0 = halve(width_value)
    x1 = []
    for x2 in range(height_value):
        x3 = [NINE] * width_value
        x4 = x0 - ONE + ((x2 + phase) % TWO)
        x3[x4] = SIX
        x1.append(tuple(x3))
    return tuple(x1)


def _make_local_pair_2faf500b(
    height_value: int,
    width_value: int,
    is_portrait: bool,
    phase: int,
) -> tuple[Grid, Grid]:
    if is_portrait:
        x0 = _make_landscape_local_2faf500b(width_value, height_value, phase)
        x1 = _push_rows_2faf500b(x0)
        return dmirror(x0), dmirror(x1)
    x0 = _make_landscape_local_2faf500b(height_value, width_value, phase)
    x1 = _push_rows_2faf500b(x0)
    return x0, x1


def _rect_clear_2faf500b(
    rect: tuple[int, int, int, int],
    reserved: tuple[tuple[int, int, int, int], ...],
) -> bool:
    top_a, left_a, bottom_a, right_a = rect
    for top_b, left_b, bottom_b, right_b in reserved:
        if not (
            bottom_a <= top_b
            or bottom_b <= top_a
            or right_a <= left_b
            or right_b <= left_a
        ):
            return False
    return True


def generate_2faf500b(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = unifint(diff_lb, diff_ub, (EIGHT, 24))
        x1 = canvas(ZERO, (x0, x0))
        x2 = canvas(ZERO, (x0, x0))
        x3 = min(SEVEN, max(TWO, x0 // THREE))
        x4 = unifint(diff_lb, diff_ub, (ONE, x3))
        x5 = []
        x6 = ZERO
        x7 = ZERO
        while x6 < x4 and x7 < 400:
            x7 += ONE
            x8 = choice((F, T))
            x9 = unifint(diff_lb, diff_ub, (TWO, SIX))
            x10 = unifint(diff_lb, diff_ub, (TWO, SIX))
            x11 = double(x10)
            if x8:
                x12 = x11
                x13 = min(x9, subtract(x11, ONE))
            else:
                x12 = min(x9, subtract(x11, ONE))
                x13 = x11
            if not (greater(max(x12, x13), min(x12, x13))):
                continue
            x14 = branch(x8, increment(x12), x12)
            x15 = branch(x8, x13, increment(x13))
            if greater(x14, x0) or greater(x15, x0):
                continue
            x16 = randint(ZERO, subtract(x0, x14))
            x17 = randint(ZERO, subtract(x0, x15))
            x18 = (x16 - ONE, x17 - ONE, x16 + x14 + ONE, x17 + x15 + ONE)
            x19 = tuple(x5)
            if not _rect_clear_2faf500b(x18, x19):
                continue
            x20 = randint(ZERO, ONE)
            x21, x22 = _make_local_pair_2faf500b(x12, x13, x8, x20)
            x23 = branch(x8, increment(x16), x16)
            x24 = branch(x8, x17, increment(x17))
            x25 = shift(asobject(x21), astuple(x23, x24))
            x26 = shift(recolor(NINE, ofcolor(x22, NINE)), astuple(x16, x17))
            x1 = paint(x1, x25)
            x2 = paint(x2, x26)
            x5.append(x18)
            x6 += ONE
        if x6 != x4:
            continue
        x27 = add(colorcount(x1, SIX), colorcount(x1, NINE))
        if not greater(colorcount(x1, ZERO), x27):
            continue
        if verify_2faf500b(x1) != x2:
            continue
        return {"input": x1, "output": x2}
