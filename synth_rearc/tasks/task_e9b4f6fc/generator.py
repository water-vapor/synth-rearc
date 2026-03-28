from synth_rearc.core import *

from .verifier import verify_e9b4f6fc


GRID_SIZE_E9B4F6FC = 13
FG_COLORS_E9B4F6FC = remove(ZERO, interval(ZERO, TEN, ONE))


def _rectangle_patch_e9b4f6fc(
    top: Integer,
    left: Integer,
    height_: Integer,
    width_: Integer,
) -> Patch:
    x0 = interval(top, top + height_, ONE)
    x1 = interval(left, left + width_, ONE)
    return product(x0, x1)


def _grow_patch_e9b4f6fc(
    height_: Integer,
    width_: Integer,
    occupied: set[IntegerTuple],
    anchors: tuple[Patch, ...],
    target_size: Integer,
) -> Patch | None:
    x0 = tuple(
        (i, j)
        for i in range(height_)
        for j in range(width_)
        if (i, j) not in occupied
    )
    if len(x0) == ZERO:
        return None
    x1 = set()
    for x2 in anchors:
        x1.update(x2)
    x3 = tuple(
        x4 for x4 in x0
        if any(x5 in x1 for x5 in dneighbors(x4))
    )
    x6 = x3 if len(x3) > ZERO and choice((T, T, F)) else x0
    x7 = {choice(x6)}
    while len(x7) < target_size:
        x8 = set()
        for x9 in tuple(x7):
            for x10 in dneighbors(x9):
                a, b = x10
                if not (ZERO <= a < height_ and ZERO <= b < width_):
                    continue
                if x10 in occupied or x10 in x7:
                    continue
                x8.add(x10)
        if len(x8) == ZERO:
            return None
        x11 = {x12: sum(x13 in x7 for x13 in dneighbors(x12)) for x12 in x8}
        x14 = maximum(x11.values())
        x15 = tuple(x16 for x16 in x8 if x11[x16] == x14)
        x17 = x15 if choice((T, T, F)) else tuple(x8)
        x7.add(choice(x17))
    return frozenset(x7)


def _pair_start_valid_e9b4f6fc(
    start: IntegerTuple,
    rect_patch: Patch,
    occupied: set[IntegerTuple],
    used_rows: set[Integer],
) -> Boolean:
    x0, x1 = start
    if x0 in used_rows:
        return F
    if x1 >= GRID_SIZE_E9B4F6FC - ONE:
        return F
    x2 = {(x0, x1), (x0, x1 + ONE)}
    if any(x3 in rect_patch or x3 in occupied for x3 in x2):
        return F
    for x4 in x2:
        for x5 in dneighbors(x4):
            if x5 in rect_patch:
                return F
            if x5 in occupied and x5 not in x2:
                return F
    return T


def _pair_starts_e9b4f6fc(
    rect_patch: Patch,
    npairs: Integer,
) -> tuple[IntegerTuple, ...] | None:
    x0 = []
    x1 = set()
    x2 = set()
    for _ in range(npairs):
        x3 = tuple(
            (i, j)
            for i in range(GRID_SIZE_E9B4F6FC)
            for j in range(GRID_SIZE_E9B4F6FC - ONE)
            if _pair_start_valid_e9b4f6fc((i, j), rect_patch, x1, x2)
        )
        if len(x3) == ZERO:
            return None
        x4 = choice(x3)
        x0.append(x4)
        x2.add(x4[ZERO])
        x1.update({x4, (x4[ZERO], x4[ONE] + ONE)})
    return tuple(x0)


def generate_e9b4f6fc(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = unifint(diff_lb, diff_ub, (FOUR, SEVEN))
        x1 = unifint(diff_lb, diff_ub, (FOUR, SEVEN))
        x2 = multiply(x0, x1)
        x3 = choice((TWO, THREE, THREE)) if x2 >= 30 else TWO
        x4 = sample(FG_COLORS_E9B4F6FC, ONE + x3 + x3)
        x5 = x4[ZERO]
        x6 = x4[ONE:ONE + x3]
        x7 = x4[ONE + x3:]
        x8 = []
        x9 = set()
        x10 = F
        for x11 in range(x3):
            x12 = x3 - x11 - ONE
            x13 = min(SIX, x2 - len(x9) - THREE * x12)
            if x13 < THREE:
                x10 = T
                break
            x14 = unifint(diff_lb, diff_ub, (THREE, x13))
            x15 = _grow_patch_e9b4f6fc(x0, x1, x9, tuple(x8), x14)
            if x15 is None:
                x10 = T
                break
            x8.append(x15)
            x9.update(x15)
        if x10:
            continue
        x16 = canvas(x5, (x0, x1))
        x17 = canvas(x5, (x0, x1))
        for x18, x19, x20 in zip(x8, x6, x7):
            x16 = fill(x16, x19, x18)
            x17 = fill(x17, x20, x18)
        x21 = randint(ZERO, GRID_SIZE_E9B4F6FC - x0)
        x22 = randint(ZERO, GRID_SIZE_E9B4F6FC - x1)
        x23 = _rectangle_patch_e9b4f6fc(x21, x22, x0, x1)
        x24 = _pair_starts_e9b4f6fc(x23, x3)
        if x24 is None:
            continue
        x25 = canvas(ZERO, (GRID_SIZE_E9B4F6FC, GRID_SIZE_E9B4F6FC))
        x25 = fill(x25, x5, x23)
        for x26, x27 in zip(x8, x6):
            x28 = shift(x26, (x21, x22))
            x25 = fill(x25, x27, x28)
        for x29, x30, x31 in zip(x24, x7, x6):
            x32, x33 = x29
            x25 = fill(x25, x30, initset((x32, x33)))
            x25 = fill(x25, x31, initset((x32, x33 + ONE)))
        if verify_e9b4f6fc(x25) != x17:
            continue
        return {"input": x25, "output": x17}
