from synth_rearc.core import *


TOP_D6E50E54 = "top"
BOTTOM_D6E50E54 = "bottom"
LEFT_D6E50E54 = "left"
RIGHT_D6E50E54 = "right"


def _project_marker_d6e50e54(
    side: str,
    line: int,
    distance: int,
    top: int,
    bottom: int,
    left: int,
    right: int,
    size_: int,
) -> tuple[tuple[int, int], tuple[int, int]]:
    if side == TOP_D6E50E54:
        source = (top - distance, line)
        target_row = top if distance < size_ else decrement(top)
        target = (target_row, line)
    elif side == BOTTOM_D6E50E54:
        source = (bottom + distance, line)
        target_row = bottom if distance < size_ else increment(bottom)
        target = (target_row, line)
    elif side == LEFT_D6E50E54:
        source = (line, left - distance)
        target_col = left if distance < size_ else decrement(left)
        target = (line, target_col)
    else:
        source = (line, right + distance)
        target_col = right if distance < size_ else increment(right)
        target = (line, target_col)
    return source, target


def generate_d6e50e54(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = unifint(diff_lb, diff_ub, (THREE, SIX))
        x1 = randint(ZERO, x0 + THREE)
        x2 = randint(ZERO, x0 + THREE)
        x3 = randint(ZERO, x0 + THREE)
        x4 = randint(ZERO, x0 + THREE)
        x5 = interval(x1, x1 + x0, ONE)
        x6 = interval(x3, x3 + x0, ONE)
        x7 = product(x5, x6)
        x8 = tuple()
        if x1 > ZERO:
            x8 = x8 + tuple((TOP_D6E50E54, x9) for x9 in x6)
        if x2 > ZERO:
            x8 = x8 + tuple((BOTTOM_D6E50E54, x9) for x9 in x6)
        if x3 > ZERO:
            x8 = x8 + tuple((LEFT_D6E50E54, x9) for x9 in x5)
        if x4 > ZERO:
            x8 = x8 + tuple((RIGHT_D6E50E54, x9) for x9 in x5)
        x9 = len(x8)
        if x9 < TWO:
            continue
        x10 = x1 + x0 + x2
        x11 = x3 + x0 + x4
        x12 = canvas(SEVEN, (x10, x11))
        x13 = fill(x12, ONE, x7)
        x14 = fill(x12, TWO, x7)
        x15 = tuple(sample(x8, unifint(diff_lb, diff_ub, (TWO, min(SEVEN, x9)))))
        x16 = frozenset()
        x17 = x13
        x18 = x14
        x19 = True
        for x20, x21 in x15:
            if x20 == TOP_D6E50E54:
                x22 = randint(ONE, x1)
            elif x20 == BOTTOM_D6E50E54:
                x22 = randint(ONE, x2)
            elif x20 == LEFT_D6E50E54:
                x22 = randint(ONE, x3)
            else:
                x22 = randint(ONE, x4)
            x23, x24 = _project_marker_d6e50e54(
                x20,
                x21,
                x22,
                x1,
                x1 + x0 - ONE,
                x3,
                x3 + x0 - ONE,
                x0,
            )
            if contained(x24, x16):
                x19 = False
                break
            x16 = insert(x24, x16)
            x17 = fill(x17, NINE, initset(x23))
            x18 = fill(x18, NINE, initset(x24))
        if x19:
            return {"input": x17, "output": x18}
