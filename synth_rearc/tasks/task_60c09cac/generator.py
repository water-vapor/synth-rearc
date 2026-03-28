from synth_rearc.core import *


NCOLORS_60C09CAC = (ONE, TWO, TWO, THREE)
PATCH_SIZES_60C09CAC = (ONE, ONE, TWO, TWO, THREE, THREE, FOUR)
STEPS_60C09CAC = (UP, DOWN, LEFT, RIGHT)


def _grow_patch_60c09cac(
    ncells: Integer,
) -> Indices:
    x0 = {ORIGIN}
    while len(x0) < ncells:
        x1 = []
        for x2 in tuple(x0):
            for x3 in STEPS_60C09CAC:
                x4 = add(x2, x3)
                if x4 in x0:
                    continue
                x5 = normalize(frozenset((*x0, x4)))
                if height(x5) > FOUR or width(x5) > FOUR:
                    continue
                x1.append(x4)
        if len(x1) == ZERO:
            break
        x0.add(choice(tuple(x1)))
    x6 = normalize(frozenset(x0))
    return x6


def _placements_60c09cac(
    h: Integer,
    w: Integer,
    patch: Indices,
    occupied: Indices,
) -> Tuple[IntegerTuple]:
    x0, x1 = shape(patch)
    x2 = []
    for x3 in range(add(subtract(h, x0), ONE)):
        for x4 in range(add(subtract(w, x1), ONE)):
            x5 = shift(patch, (x3, x4))
            if len(x5 & occupied) != ZERO:
                continue
            x2.append((x3, x4))
    return tuple(x2)


def generate_60c09cac(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    x0 = remove(ZERO, interval(ZERO, TEN, ONE))
    while True:
        x1 = unifint(diff_lb, diff_ub, (THREE, NINE))
        x2 = unifint(diff_lb, diff_ub, (THREE, NINE))
        x3 = choice(NCOLORS_60C09CAC)
        x4 = sample(x0, x3)
        x5 = unifint(diff_lb, diff_ub, (x3, min(FOUR, add(x3, ONE))))
        x6 = list(x4)
        x6.extend(choice(x4) for _ in range(subtract(x5, x3)))
        x7 = canvas(ZERO, (x1, x2))
        x8 = frozenset()
        x9 = ZERO
        x10 = ZERO
        while x9 < x5 and x10 < multiply(x5, TEN):
            x10 = add(x10, ONE)
            x11 = choice(PATCH_SIZES_60C09CAC)
            x12 = _grow_patch_60c09cac(x11)
            x13 = _placements_60c09cac(x1, x2, x12, x8)
            if len(x13) == ZERO:
                continue
            x14 = shift(x12, choice(x13))
            x15 = x6[x9]
            x7 = fill(x7, x15, x14)
            x8 = x8 | x14
            x9 = add(x9, ONE)
        x16 = size(x8)
        x17 = multiply(x1, x2)
        x18 = max(FIVE, divide(x17, THREE))
        if x9 != x5:
            continue
        if x16 < TWO:
            continue
        if x16 > x18:
            continue
        if colorcount(x7, ZERO) == ZERO:
            continue
        x19 = upscale(x7, TWO)
        return {"input": x7, "output": x19}
