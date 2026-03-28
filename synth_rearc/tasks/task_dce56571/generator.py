from collections import Counter

from synth_rearc.core import *

from .verifier import verify_dce56571


FG_COLORS_DCE56571 = tuple(remove(EIGHT, interval(ZERO, TEN, ONE)))
HEIGHTS_DCE56571 = (FIVE, SEVEN, NINE, 11)
BACKBONE_STEPS_DCE56571 = (NEG_ONE, ZERO, ONE, ONE)


def _sample_int_dce56571(
    diff_lb: float,
    diff_ub: float,
    lower: int,
    upper: int,
) -> int:
    if upper <= lower:
        return lower
    return unifint(diff_lb, diff_ub, (lower, upper))


def _pick_value_dce56571(
    values: tuple[int, ...],
    diff_lb: float,
    diff_ub: float,
) -> int:
    x0 = _sample_int_dce56571(diff_lb, diff_ub, ZERO, len(values) - ONE)
    return values[x0]


def _shape_ok_dce56571(
    patch: Patch,
) -> bool:
    x0 = Counter(i for i, _ in patch)
    x1 = sum(count > ONE for count in x0.values())
    return x1 >= TWO


def _build_patch_dce56571(
    diff_lb: float,
    diff_ub: float,
    count: int,
    max_height: int,
    max_width: int,
) -> Indices | None:
    for _ in range(400):
        x0 = max(THREE, count // THREE)
        x1 = min(max_height, count)
        x2 = _sample_int_dce56571(diff_lb, diff_ub, x0, x1)
        x3 = ZERO
        x4 = {(ZERO, x3)}
        for x5 in range(ONE, x2):
            x3 += choice(BACKBONE_STEPS_DCE56571)
            x4.add((x5, x3))
        x6 = ZERO
        while len(x4) < count and x6 < 600:
            x7 = []
            for x8 in x4:
                for x9 in neighbors(x8):
                    if x9 in x4:
                        continue
                    x10 = len(neighbors(x9) & x4)
                    if x10 == ZERO or x10 > TWO:
                        continue
                    x11 = normalize(frozenset(x4 | {x9}))
                    if height(x11) > max_height or width(x11) > max_width:
                        continue
                    x7.append(x9)
            if len(x7) == ZERO:
                break
            x4.add(choice(tuple(set(x7))))
            x6 += ONE
        x12 = normalize(frozenset(x4))
        if len(x12) != count:
            continue
        if height(x12) < THREE or width(x12) < THREE:
            continue
        x13 = add(shape(x12), TWO_BY_TWO)
        x14 = canvas(ZERO, x13)
        x15 = shift(x12, UNITY)
        x16 = fill(x14, ONE, x15)
        x17 = objects(x16, T, T, T)
        if len(x17) != ONE:
            continue
        if not _shape_ok_dce56571(x12):
            continue
        return x12
    return None


def _place_patch_dce56571(
    diff_lb: float,
    diff_ub: float,
    height_: int,
    width_: int,
    margin: int,
    patch: Patch,
) -> Indices | None:
    x0, x1 = shape(patch)
    x2 = height_ // TWO
    x3 = min(height_ - x0 - ONE, max(ONE, x2 - ONE))
    if x3 < ONE:
        return None
    x4 = _sample_int_dce56571(diff_lb, diff_ub, ONE, x3)
    x5 = len(patch)
    x6 = max(ONE, margin)
    x7 = min(width_ - x1 - ONE, margin + x5 - x1)
    if x7 < x6:
        return None
    x8 = _sample_int_dce56571(diff_lb, diff_ub, x6, x7)
    return shift(patch, (x4, x8))


def generate_dce56571(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = _pick_value_dce56571(HEIGHTS_DCE56571, diff_lb, diff_ub)
        x1 = max(SIX, x0 - ONE)
        x2 = min(17, x0 + SIX)
        x3 = _sample_int_dce56571(diff_lb, diff_ub, x1, x2)
        x4 = max(ZERO, (TEN - x3 + ONE) // TWO)
        x5 = min(EIGHT, (30 - x3) // TWO)
        if x4 > x5:
            continue
        x6 = _sample_int_dce56571(diff_lb, diff_ub, x4, x5)
        x7 = x3 + 2 * x6
        x8 = min(x7 - TWO, max(FOUR, x3 // TWO + THREE))
        x9 = _build_patch_dce56571(diff_lb, diff_ub, x3, x0 - TWO, x8)
        if x9 is None:
            continue
        x10 = _place_patch_dce56571(diff_lb, diff_ub, x0, x7, x6, x9)
        if x10 is None:
            continue
        x11 = choice(FG_COLORS_DCE56571)
        x12 = canvas(EIGHT, (x0, x7))
        x13 = fill(x12, x11, x10)
        x14 = x0 // TWO
        x15 = astuple(x14, x6)
        x16 = astuple(x14, x7 - x6 - ONE)
        x17 = connect(x15, x16)
        x18 = fill(x12, x11, x17)
        if verify_dce56571(x13) != x18:
            continue
        return {"input": x13, "output": x18}
