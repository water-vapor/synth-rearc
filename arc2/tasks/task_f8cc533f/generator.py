from arc2.core import *

from .verifier import verify_f8cc533f


ALL_COLORS_F8CC533F = interval(ZERO, TEN, ONE)


def _symmetrize_f8cc533f(
    patch: Indices,
    side: Integer,
) -> Indices:
    x0 = set()
    x1 = subtract(side, ONE)
    for x2, x3 in patch:
        x0.add((x2, x3))
        x0.add((x2, x1 - x3))
        x0.add((x1 - x2, x3))
        x0.add((x1 - x2, x1 - x3))
    return frozenset(x0)


def _connected_f8cc533f(
    patch: Indices,
) -> Boolean:
    if len(patch) == ZERO:
        return False
    x0 = {next(iter(patch))}
    x1 = set(x0)
    while len(x0) > ZERO:
        x2 = set()
        for x3 in x0:
            for x4 in dneighbors(x3):
                if x4 in patch and x4 not in x1:
                    x1.add(x4)
                    x2.add(x4)
        x0 = x2
    return len(x1) == len(patch)


def _row_signature_count_f8cc533f(
    patch: Indices,
    side: Integer,
) -> Integer:
    x0 = set()
    for x1 in range(side):
        x2 = tuple(x3 for x3 in range(side) if (x1, x3) in patch)
        x0.add(x2)
    return len(x0)


def _build_template_f8cc533f(
    side: Integer,
) -> Indices:
    x0 = side // TWO
    x1 = frozenset((i, j) for i in range(x0 + ONE) for j in range(x0 + ONE))
    x2 = max(THREE, x0 + TWO)
    x3 = max(x2, len(x1) - ONE)
    x4 = tuple(x1)
    for _ in range(400):
        x5 = {choice(x4)}
        x6 = randint(x2, x3)
        while len(x5) < x6:
            x7 = tuple(
                x8 for x8 in x1
                if x8 not in x5 and any(x9 in x5 for x9 in dneighbors(x8))
            )
            if len(x7) == ZERO:
                break
            x5.add(choice(x7))
        if not any(x6 == ZERO for x6, _ in x5):
            continue
        if not any(x6 == ZERO for _, x6 in x5):
            continue
        x7 = _symmetrize_f8cc533f(frozenset(x5), side)
        if len(x7) == multiply(side, side):
            continue
        if len(x7) < side + side + side // TWO:
            continue
        if not _connected_f8cc533f(x7):
            continue
        if _row_signature_count_f8cc533f(x7, side) < max(THREE, side // TWO):
            continue
        return x7
    raise RuntimeError("failed to build template")


def _can_remove_f8cc533f(
    patch: Indices,
    cell: IntegerTuple,
) -> Boolean:
    x0 = patch - {cell}
    if len(x0) == ZERO:
        return False
    if not any(x1 == ZERO for x1, _ in x0):
        return False
    if not any(x1 == ZERO for _, x1 in x0):
        return False
    return _connected_f8cc533f(x0)


def _damage_copy_f8cc533f(
    template: Indices,
    side: Integer,
) -> Indices:
    x0 = set(template)
    x1 = max(ONE, min(side, len(template) // FOUR))
    if choice((T, F)):
        x2 = max(x3 for _, x3 in x0)
        x3 = frozenset(x4 for x4 in x0 if x4[1] == x2)
        if len(x3) > ZERO and all(_can_remove_f8cc533f(frozenset(x0), x4) for x4 in x3):
            x0 -= x3
    if choice((T, F)):
        x2 = max(x3 for x3, _ in x0)
        x3 = frozenset(x4 for x4 in x0 if x4[0] == x2)
        if len(x3) > ZERO and all(_can_remove_f8cc533f(frozenset(x0), x4) for x4 in x3):
            x0 -= x3
    x2 = randint(ONE, x1)
    x3 = ZERO
    while x3 < x2:
        x4 = tuple(
            x5 for x5 in x0
            if x5[0] != ZERO and x5[1] != ZERO
        )
        if len(x4) == ZERO:
            break
        x5 = tuple(
            x6
            for x6 in x4
            for _ in range(ONE + int(x6[0] == side - ONE) + int(x6[1] == side - ONE))
        )
        x6 = choice(x5)
        if not _can_remove_f8cc533f(frozenset(x0), x6):
            x4 = tuple(x7 for x7 in x4 if _can_remove_f8cc533f(frozenset(x0), x7))
            if len(x4) == ZERO:
                break
            x6 = choice(x4)
        x0.remove(x6)
        x3 = increment(x3)
    return frozenset(x0)


def _reserve_patch_f8cc533f(
    loc: IntegerTuple,
    side: Integer,
) -> Indices:
    x0, x1 = loc
    return frozenset(
        (i, j)
        for i in range(x0 - ONE, x0 + side + ONE)
        for j in range(x1 - ONE, x1 + side + ONE)
    )


def _sample_locations_f8cc533f(
    height_: Integer,
    width_: Integer,
    side: Integer,
    total: Integer,
) -> tuple[IntegerTuple, ...] | None:
    x0 = tuple()
    x1 = frozenset()
    for _ in range(400):
        if len(x0) == total:
            return x0
        x2 = tuple(
            (i, j)
            for i in range(height_ - side + ONE)
            for j in range(width_ - side + ONE)
            if len(intersection(_reserve_patch_f8cc533f((i, j), side), x1)) == ZERO
        )
        if len(x2) == ZERO:
            return None
        x3 = choice(x2)
        x0 = x0 + (x3,)
        x1 = combine(x1, _reserve_patch_f8cc533f(x3, side))
    return x0


def generate_f8cc533f(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = unifint(diff_lb, diff_ub, (FIVE, SEVEN))
        x1 = unifint(diff_lb, diff_ub, (TWO, FOUR))
        x2 = _build_template_f8cc533f(x0)
        x3 = choice(ALL_COLORS_F8CC533F)
        x4 = tuple(sample(remove(x3, ALL_COLORS_F8CC533F), x1))
        x5 = tuple(_damage_copy_f8cc533f(x2, x0) for _ in range(x1))
        x6 = frozenset(merge(x5))
        if x6 != x2:
            x7 = x2 - x6
            x8 = [set(x9) for x9 in x5]
            for x9 in x7:
                choice(x8).add(x9)
            x5 = tuple(frozenset(x9) for x9 in x8)
        if any(x9 == x2 for x9 in x5):
            continue
        if len(frozenset(merge(x5))) != len(x2):
            continue
        x7 = max(11, x0 + x0 + TWO)
        x8 = min(30, max(x7, x0 * x1 + x0 + FOUR))
        x9 = unifint(diff_lb, diff_ub, (x7, x8))
        x10 = unifint(diff_lb, diff_ub, (x7, x8))
        x11 = _sample_locations_f8cc533f(x9, x10, x0, x1)
        if x11 is None:
            continue
        x12 = canvas(x3, (x9, x10))
        x13 = canvas(x3, (x9, x10))
        for x14, x15, x16 in zip(x4, x5, x11):
            x17 = recolor(x14, shift(x15, x16))
            x18 = recolor(x14, shift(x2, x16))
            x12 = paint(x12, x17)
            x13 = paint(x13, x18)
        if x12 == x13:
            continue
        if verify_f8cc533f(x12) != x13:
            continue
        return {"input": x12, "output": x13}
