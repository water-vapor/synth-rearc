from synth_rearc.core import *

from .helpers import blue_patch_c97c0139


def _line_patch_c97c0139(
    start: IntegerTuple,
    horizontal: Boolean,
    length: Integer,
) -> Indices:
    x0 = subtract(length, ONE)
    if horizontal:
        x1 = astuple(start[ZERO], add(start[ONE], x0))
    else:
        x1 = astuple(add(start[ZERO], x0), start[ONE])
    return connect(start, x1)


def _reserve_patch_c97c0139(
    patch: Patch,
) -> Indices:
    x0 = max(ZERO, subtract(uppermost(patch), ONE))
    x1 = max(ZERO, subtract(leftmost(patch), ONE))
    x2 = min(29, add(lowermost(patch), ONE))
    x3 = min(29, add(rightmost(patch), ONE))
    return frozenset(
        (x4, x5)
        for x4 in range(x0, x2 + ONE)
        for x5 in range(x1, x3 + ONE)
    )


def generate_c97c0139(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    x0 = astuple(30, 30)
    while True:
        x1 = unifint(diff_lb, diff_ub, (ONE, THREE))
        x2 = tuple()
        x3 = frozenset()
        x4 = ZERO
        x5 = 14 if x1 < THREE else 12
        while len(x2) < x1 and x4 < 300:
            x4 = increment(x4)
            x6 = choice((T, F))
            x7 = unifint(diff_lb, diff_ub, (FIVE, x5))
            x8 = divide(subtract(x7, ONE), TWO)
            if x6:
                x9 = randint(x8, subtract(29, x8))
                x10 = randint(ZERO, subtract(30, x7))
                x11 = _line_patch_c97c0139(astuple(x9, x10), T, x7)
            else:
                x9 = randint(ZERO, subtract(30, x7))
                x10 = randint(x8, subtract(29, x8))
                x11 = _line_patch_c97c0139(astuple(x9, x10), F, x7)
            x12 = blue_patch_c97c0139(x11)
            x13 = combine(x11, x12)
            x14 = _reserve_patch_c97c0139(x13)
            if len(intersection(x14, x3)) > ZERO:
                continue
            x2 = x2 + (x11,)
            x3 = combine(x3, x14)
        if len(x2) != x1:
            continue
        x15 = canvas(ZERO, x0)
        x16 = canvas(ZERO, x0)
        x17 = frozenset()
        for x18 in x2:
            x19 = blue_patch_c97c0139(x18)
            x20 = combine(x18, x19)
            x15 = fill(x15, TWO, x18)
            x16 = fill(x16, EIGHT, x19)
            x16 = fill(x16, TWO, x18)
            x17 = combine(x17, x20)
        x21 = uppermost(x17)
        x22 = lowermost(x17)
        x23 = leftmost(x17)
        x24 = rightmost(x17)
        x25 = add(subtract(x22, x21), ONE)
        x26 = add(subtract(x24, x23), ONE)
        x27 = min(30, max(15, add(x25, TWO)))
        x28 = min(30, add(x25, 8))
        x29 = min(30, max(15, add(x26, TWO)))
        x30 = min(30, add(x26, 8))
        if x27 > x28 or x29 > x30:
            continue
        x31 = unifint(diff_lb, diff_ub, (x27, x28))
        x32 = unifint(diff_lb, diff_ub, (x29, x30))
        x33 = max(ZERO, subtract(x22, subtract(x31, ONE)))
        x34 = min(x21, subtract(30, x31))
        x35 = max(ZERO, subtract(x24, subtract(x32, ONE)))
        x36 = min(x23, subtract(30, x32))
        if x33 > x34 or x35 > x36:
            continue
        x37 = randint(x33, x34)
        x38 = randint(x35, x36)
        x39 = astuple(x37, x38)
        x40 = astuple(x31, x32)
        x41 = crop(x15, x39, x40)
        x42 = crop(x16, x39, x40)
        if x41 == x42:
            continue
        return {"input": x41, "output": x42}
