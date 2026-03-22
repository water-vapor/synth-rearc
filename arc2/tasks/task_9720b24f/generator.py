from arc2.core import *

from .helpers import hook_outline_9720b24f
from .helpers import interior_patch_9720b24f
from .helpers import kite_outline_9720b24f
from .helpers import wedge_outline_9720b24f


GRID_BOUNDS_9720B24F = (10, 22)
TRANSFORMS_9720B24F = (identity, hmirror, vmirror, dmirror, cmirror)


def _bbox_with_padding_9720b24f(
    patch: Patch,
    dims: IntegerTuple,
    pad: Integer,
) -> Indices:
    x0, x1 = dims
    x2 = max(ZERO, uppermost(patch) - pad)
    x3 = min(x0 - ONE, lowermost(patch) + pad)
    x4 = max(ZERO, leftmost(patch) - pad)
    x5 = min(x1 - ONE, rightmost(patch) + pad)
    return frozenset((i, j) for i in range(x2, x3 + ONE) for j in range(x4, x5 + ONE))


def _sample_component_patch_9720b24f(
    diff_lb: float,
    diff_ub: float,
) -> Indices:
    x0 = randint(ZERO, TWO)
    if x0 == ZERO:
        x1 = max(FIVE, unifint(diff_lb, diff_ub, (FIVE, NINE)))
        x2 = max(FOUR, unifint(diff_lb, diff_ub, (FOUR, SEVEN)))
        x3 = randint(ONE, max(ONE, min(THREE, x1 - THREE)))
        x4 = hook_outline_9720b24f(x2, x1, x3)
    elif x0 == ONE:
        x5 = randint(TWO, FOUR)
        x4 = wedge_outline_9720b24f(x5)
    else:
        x6 = randint(TWO, FOUR)
        x4 = kite_outline_9720b24f(x6)
    x7 = choice(TRANSFORMS_9720B24F)
    x8 = normalize(x7(x4))
    return x8


def _sample_intruder_patch_9720b24f(
    interior: Indices,
) -> Indices:
    x0 = tuple(sorted(interior))
    x1 = set(interior)
    x2 = []
    for x3 in x0:
        x2.append(initset(x3))
        for x4 in ((ZERO, ONE), (ONE, ZERO), (ONE, ONE), (ONE, NEG_ONE)):
            x5 = add(x3, x4)
            if x5 in x1:
                x2.append(frozenset({x3, x5}))
                x6 = add(x5, x4)
                if x6 in x1:
                    x2.append(frozenset({x3, x5, x6}))
        x7 = add(x3, RIGHT)
        x8 = add(x3, DOWN)
        x9 = add(x8, RIGHT)
        if x7 in x1 and x8 in x1 and x9 in x1:
            x2.append(frozenset({x3, x7, x8, x9}))
    x10 = tuple(sorted({tuple(sorted(x11)) for x11 in x2}, key=len))
    x11 = [frozenset(x12) for x12 in x10 if len(x12) > ZERO]
    if len(x11) == ZERO:
        return frozenset()
    x12 = [x13 for x13 in x11 if len(x13) > ONE]
    return choice(x12 if len(x12) > ZERO and randint(ZERO, ONE) == ONE else x11)


def _sample_noise_patch_9720b24f(
    available: Indices,
) -> Indices:
    x0 = tuple(sorted(available))
    if len(x0) == ZERO:
        return frozenset()
    x1 = set(available)
    x2 = choice(x0)
    x3 = randint(ZERO, THREE)
    if x3 == ZERO:
        return initset(x2)
    if x3 == ONE:
        x4 = choice((UP, DOWN, LEFT, RIGHT))
        x5 = add(x2, x4)
        if x5 in x1:
            return frozenset({x2, x5})
        return initset(x2)
    x6 = choice((UP_RIGHT, UNITY, DOWN_LEFT, NEG_UNITY))
    x7 = add(x2, x6)
    if x7 not in x1:
        return initset(x2)
    if x3 == TWO:
        return frozenset({x2, x7})
    x8 = add(x7, x6)
    if x8 in x1:
        return frozenset({x2, x7, x8})
    return frozenset({x2, x7})


def generate_9720b24f(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    x0 = tuple(remove(ZERO, interval(ZERO, TEN, ONE)))
    while True:
        x1 = unifint(diff_lb, diff_ub, GRID_BOUNDS_9720B24F)
        x2 = unifint(diff_lb, diff_ub, GRID_BOUNDS_9720B24F)
        x3 = canvas(ZERO, (x1, x2))
        x4 = x3
        x5 = randint(ONE, THREE)
        x6 = list(sample(x0, min(len(x0), x5 + FOUR)))
        x7 = set()
        x8 = set()
        x9 = ZERO
        x10 = T
        for _ in range(x5):
            x11 = None
            x12 = None
            for _ in range(120):
                x13 = _sample_component_patch_9720b24f(diff_lb, diff_ub)
                x14, x15 = shape(x13)
                if x14 > x1 or x15 > x2:
                    continue
                x16 = randint(ZERO, x1 - x14)
                x17 = randint(ZERO, x2 - x15)
                x18 = shift(x13, (x16, x17))
                x19 = _bbox_with_padding_9720b24f(x18, (x1, x2), ONE)
                if len(intersection(x19, x7)) > ZERO:
                    continue
                x20 = x6.pop()
                x21 = recolor(x20, x18)
                x22 = interior_patch_9720b24f(x21, (x1, x2))
                if len(x22) < ONE:
                    x6.insert(ZERO, x20)
                    continue
                x23 = _sample_intruder_patch_9720b24f(x22)
                if len(x23) < ONE:
                    x6.insert(ZERO, x20)
                    continue
                x24 = tuple(remove(x20, x0))
                x25 = choice(x24)
                x11 = (x20, x18, x19, x22, x23, x25)
                x12 = x21
                break
            if x11 is None or x12 is None:
                x10 = F
                break
            x26, x27, x28, x29, x30, x31 = x11
            x3 = fill(x3, x26, x27)
            x4 = fill(x4, x26, x27)
            x4 = fill(x4, x31, x30)
            x7 |= set(x28)
            x8 |= set(x29)
            x9 += len(x30)
        if not x10:
            continue
        x32 = randint(ZERO, THREE)
        x33 = x7 | x8
        x34 = set()
        for _ in range(x32):
            x35 = {
                (i, j)
                for i in range(x1)
                for j in range(x2)
                if (i, j) not in x33 and (i, j) not in x34
            }
            x36 = {
                x37
                for x37 in x35
                if len(intersection(neighbors(x37), x34)) == ZERO and len(intersection(neighbors(x37), x8)) == ZERO
            }
            x38 = _sample_noise_patch_9720b24f(frozenset(x36))
            if len(x38) == ZERO:
                continue
            x39 = choice(x0)
            x3 = fill(x3, x39, x38)
            x4 = fill(x4, x39, x38)
            x34 |= set(x38)
        if x9 < ONE:
            continue
        if x3 == x4:
            continue
        return {"input": x4, "output": x3}
