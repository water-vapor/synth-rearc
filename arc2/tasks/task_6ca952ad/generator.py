from arc2.core import *

from .verifier import verify_6ca952ad


BACKGROUND_6CA952AD = SEVEN
FOREGROUND_COLORS_6CA952AD = interval(ONE, SEVEN, ONE)


def _rect_patch_6ca952ad(
    height_: Integer,
    width_: Integer,
) -> Indices:
    x0 = interval(ZERO, height_, ONE)
    x1 = interval(ZERO, width_, ONE)
    return product(x0, x1)


def _grow_patch_6ca952ad(
    region: Indices,
    target_size: Integer,
) -> Indices:
    x0 = set(region)
    x1 = {choice(tuple(region))}
    while len(x1) < target_size:
        x2 = set()
        for x3 in x1:
            x2 |= set(dneighbors(x3))
        x2 &= x0
        x2 -= x1
        if len(x2) == ZERO:
            x2 = x0 - x1
        x1.add(choice(tuple(x2)))
    return normalize(frozenset(x1))


def _small_patch_6ca952ad() -> Indices:
    x0 = randint(ONE, THREE)
    while True:
        x1 = randint(ONE, THREE)
        x2 = randint(ONE, THREE)
        if multiply(x1, x2) < x0:
            continue
        x3 = _rect_patch_6ca952ad(x1, x2)
        x4 = _grow_patch_6ca952ad(x3, x0)
        return x4


def _large_patch_6ca952ad() -> Indices:
    while True:
        x0 = randint(TWO, FIVE)
        x1 = randint(ONE, FOUR)
        x2 = multiply(x0, x1)
        if x2 < FOUR:
            continue
        x3 = max(FOUR, divide(add(x2, ONE), TWO))
        x4 = randint(x3, x2)
        x5 = _rect_patch_6ca952ad(x0, x1)
        x6 = _grow_patch_6ca952ad(x5, x4)
        return x6


def generate_6ca952ad(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = unifint(diff_lb, diff_ub, (SEVEN, 18))
        x1 = unifint(diff_lb, diff_ub, (SEVEN, 18))
        x2 = choice(FOREGROUND_COLORS_6CA952AD)
        x3 = randint(ONE, THREE)
        x4 = randint(ONE, THREE)
        x5 = [(F, _small_patch_6ca952ad()) for _ in range(x3)]
        x6 = [(T, _large_patch_6ca952ad()) for _ in range(x4)]
        x7 = x5 + x6
        shuffle(x7)
        x8 = sum(width(x9) for _, x9 in x7)
        x9 = add(size(x7), ONE)
        x10 = add(x8, x9)
        if x10 > x1:
            continue
        x11 = subtract(x1, x10)
        x12 = [ONE] * add(size(x7), ONE)
        for _ in range(x11):
            x13 = randint(ZERO, len(x12) - ONE)
            x12[x13] += ONE
        x14 = []
        x15 = x12[ZERO]
        for x16, x17 in enumerate(x7):
            x18, x19 = x17
            x20 = height(x19)
            x21 = branch(x18, min(EIGHT, divide(x0, TWO)), min(FIVE, divide(x0, TWO)))
            x22 = subtract(x0, increment(x20))
            x23 = max(ONE, min(x21, x22))
            x24 = randint(ONE, x23)
            x25 = shift(x19, astuple(x24, x15))
            x26 = recolor(x2, x25)
            x14.append((x18, x26))
            x15 = add(x15, add(width(x19), x12[increment(x16)]))
        x27 = canvas(BACKGROUND_6CA952AD, (x0, x1))
        for _, x28 in x14:
            x27 = paint(x27, x28)
        x29 = x27
        for x30, x31 in x14:
            if x30:
                x32 = subtract(decrement(x0), lowermost(x31))
                x33 = move(x29, x31, toivec(x32))
                x29 = x33
        if verify_6ca952ad(x27) != x29:
            continue
        return {"input": x27, "output": x29}
