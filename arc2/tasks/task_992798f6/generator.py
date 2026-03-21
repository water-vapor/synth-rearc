from arc2.core import *


def _output_992798f6(
    I: Grid,
) -> Grid:
    x0 = first(ofcolor(I, TWO))
    x1 = first(ofcolor(I, ONE))
    x2 = subtract(x1, x0)
    x3 = sign(x2)
    x4 = add(x0, x3)
    x5 = astuple(first(x1), last(x4))
    x6 = initset(x4)
    x7 = initset(x5)
    x8 = manhattan(x6, x7)
    x9 = astuple(first(x4), last(x1))
    x10 = initset(x9)
    x11 = manhattan(x6, x10)
    x12 = greater(x8, x11)
    x13 = branch(x12, subtract(x8, x11), subtract(x11, x8))
    x14 = toivec(first(x3))
    x15 = tojvec(last(x3))
    x16 = branch(x12, x14, x15)
    x17 = multiply(x13, x16)
    x18 = add(x4, x17)
    x19 = connect(x4, x18)
    x20 = connect(x18, x1)
    x21 = combine(x19, x20)
    x22 = remove(x0, x21)
    x23 = remove(x1, x22)
    x24 = fill(I, THREE, x23)
    return x24


def generate_992798f6(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = unifint(diff_lb, diff_ub, (13, 16))
        x1 = choice((12, 16))
        x2 = randint(ONE, THREE)
        x3 = randint(max(add(x2, SIX), subtract(x0, FOUR)), subtract(x0, TWO))
        x4 = randint(ONE, subtract(x1, ONE))
        x5 = randint(ONE, subtract(x1, ONE))
        x6 = abs(subtract(x5, x4))
        x7 = subtract(x3, x2)
        if x6 < TWO:
            continue
        if x7 <= x6:
            if abs(subtract(x7, x6)) < THREE:
                continue
        elif abs(subtract(x6, x7)) < THREE:
            continue
        x8 = choice((True, True, False))
        x9 = astuple(x2, x4)
        x10 = astuple(x3, x5)
        x11 = branch(x8, x9, x10)
        x12 = branch(x8, x10, x9)
        x13 = canvas(ZERO, (x0, x1))
        x14 = fill(x13, TWO, initset(x11))
        x15 = fill(x14, ONE, initset(x12))
        x16 = _output_992798f6(x15)
        x17 = size(ofcolor(x16, THREE))
        if x17 < EIGHT:
            continue
        return {"input": x15, "output": x16}
