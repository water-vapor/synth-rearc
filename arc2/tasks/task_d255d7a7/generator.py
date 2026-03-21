from arc2.core import *

from .helpers import build_horizontal_cap_d255d7a7
from .helpers import build_vertical_cap_d255d7a7
from .helpers import find_movable_caps_d255d7a7


def _band_starts_d255d7a7(
    size: int,
    count: int,
) -> tuple[int, ...]:
    x0 = size - (THREE * count + (count - ONE))
    x1 = [ZERO for _ in range(count + ONE)]
    for _ in range(x0):
        x2 = randint(ZERO, count)
        x1[x2] += ONE
    x3 = []
    x4 = x1[ZERO]
    for x5 in range(count):
        x3.append(x4)
        if x5 < count - ONE:
            x4 += FOUR + x1[x5 + ONE]
    return tuple(x3)


def _pattern_pair_d255d7a7() -> tuple[int, int]:
    x0 = (
        (SEVEN, SEVEN),
        (SEVEN, SEVEN),
        (SEVEN, SEVEN),
        (NINE, SEVEN),
        (SEVEN, NINE),
        (NINE, NINE),
    )
    return choice(x0)


def _paint_noise_patch_d255d7a7(
    gi: Grid,
    go: Grid,
    patch: Patch,
) -> tuple[Grid, Grid]:
    x0 = fill(gi, NINE, patch)
    x1 = fill(go, NINE, patch)
    return x0, x1


def generate_d255d7a7(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = choice(("hr", "hl", "vd", "vu"))
        x1 = x0 in ("hr", "hl")
        x2 = unifint(diff_lb, diff_ub, (ONE, FOUR))
        if x1:
            x3 = max(EIGHT, THREE * x2 + x2 - ONE)
            x4 = unifint(diff_lb, diff_ub, (x3, 22))
            x5 = unifint(diff_lb, diff_ub, (EIGHT, 26))
            x6 = _band_starts_d255d7a7(x4, x2)
        else:
            x3 = max(EIGHT, THREE * x2 + x2 - ONE)
            x4 = unifint(diff_lb, diff_ub, (EIGHT, 26))
            x5 = unifint(diff_lb, diff_ub, (x3, 22))
            x6 = _band_starts_d255d7a7(x4, x2)
        x7 = canvas(SEVEN, (x5, x4)) if not x1 else canvas(SEVEN, (x4, x5))
        x8 = x7
        x9 = []
        x10 = []
        x11 = set()
        x12 = False
        if x1:
            for x13 in x6:
                x14, x15 = _pattern_pair_d255d7a7()
                x12 = x12 or x14 == NINE or x15 == NINE
                if x0 == "hr":
                    x16 = build_horizontal_cap_d255d7a7(x13, ZERO, "right", x14, x15)
                    x17 = frozenset((x13 + ONE, x18) for x18 in range(TWO, x5))
                    x18 = shift(x16, astuple(ZERO, x5 - THREE))
                    x19 = ZERO
                else:
                    x16 = build_horizontal_cap_d255d7a7(x13, x5 - THREE, "left", x14, x15)
                    x17 = frozenset((x13 + ONE, x18) for x18 in range(x5 - TWO))
                    x18 = shift(x16, astuple(ZERO, -(x5 - THREE)))
                    x19 = x5 - TWO
                x7 = paint(x7, x16)
                x7 = fill(x7, ZERO, x17)
                x8 = paint(x8, x18)
                x9.append((x16, x18))
                x10.append(x13)
                if choice((T, F, F)):
                    x21 = [x22 for x22 in (x13 - ONE, x13 + THREE) if ZERO <= x22 < x4 and x22 not in x11]
                    if len(x21) > ZERO:
                        x23 = choice(tuple(x21))
                        x24 = choice((ONE, TWO))
                        x25 = range(x24) if x0 == "hr" else range(x5 - x24, x5)
                        x26 = frozenset((x23, x27) for x27 in x25)
                        x7, x8 = _paint_noise_patch_d255d7a7(x7, x8, x26)
                        x11.add(x23)
                        x12 = True
            x27 = [x28 for x28 in range(x4) if all(not (x29 <= x28 <= x29 + TWO) for x29 in x10) and x28 not in x11]
            shuffle(x27)
            x28 = randint(ZERO, min(TWO, len(x27)))
            for x29 in x27[:x28]:
                x30 = choice((ONE, TWO))
                x31 = choice(("left", "right"))
                x32 = range(x30) if x31 == "left" else range(x5 - x30, x5)
                x33 = frozenset((x29, x34) for x34 in x32)
                x7, x8 = _paint_noise_patch_d255d7a7(x7, x8, x33)
                x12 = True
        else:
            x35 = x6
            for x36 in x35:
                x37, x38 = _pattern_pair_d255d7a7()
                x12 = x12 or x37 == NINE or x38 == NINE
                if x0 == "vd":
                    x39 = build_vertical_cap_d255d7a7(ZERO, x36, "bottom", x37, x38)
                    x40 = frozenset((x41, x36 + ONE) for x41 in range(TWO, x5))
                    x41 = shift(x39, astuple(x5 - THREE, ZERO))
                    x42 = ZERO
                else:
                    x39 = build_vertical_cap_d255d7a7(x5 - THREE, x36, "top", x37, x38)
                    x40 = frozenset((x41, x36 + ONE) for x41 in range(x5 - TWO))
                    x41 = shift(x39, astuple(-(x5 - THREE), ZERO))
                    x42 = x5 - TWO
                x7 = paint(x7, x39)
                x7 = fill(x7, ZERO, x40)
                x8 = paint(x8, x41)
                x9.append((x39, x41))
                x10.append(x36)
                x11.update((x42, x36 + x43) for x43 in range(THREE))
            if len(x35) > ONE and choice((T, F)):
                for x44, x45 in pair(x35, x35[ONE:]):
                    x46 = x44 + THREE
                    x47 = x45 - ONE
                    if x46 > x47:
                        continue
                    x48 = choice(tuple(range(x46, x47 + ONE)))
                    x49 = ZERO if x0 == "vd" else x5 - ONE
                    x50 = frozenset({(x49, x48)})
                    x7, x8 = _paint_noise_patch_d255d7a7(x7, x8, x50)
                    x12 = True
            x51 = [x52 for x52 in range(x4) if all(not (x53 <= x52 <= x53 + TWO) for x53 in x10)]
            shuffle(x51)
            x52 = randint(ZERO, min(TWO, len(x51)))
            for x53 in x51[:x52]:
                x54 = choice((ONE, TWO))
                x55 = randint(ZERO, x5 - x54)
                x57 = frozenset((x55 + x58, x53) for x58 in range(x54))
                x7, x8 = _paint_noise_patch_d255d7a7(x7, x8, x57)
                x12 = True
        if not x12:
            if x1:
                x58 = [x59 for x59 in range(x4) if all(not (x60 <= x59 <= x60 + TWO) for x60 in x10)]
                if len(x58) == ZERO:
                    continue
                x59 = choice(tuple(x58))
                x60 = frozenset({(x59, ZERO)})
            else:
                x58 = [x59 for x59 in range(x4) if all(not (x60 <= x59 <= x60 + TWO) for x60 in x10)]
                if len(x58) == ZERO:
                    continue
                x59 = choice(tuple(x58))
                x60 = frozenset({(ZERO, x59)})
            x7, x8 = _paint_noise_patch_d255d7a7(x7, x8, x60)
        x61 = find_movable_caps_d255d7a7(x7)
        if len(x61) != x2:
            continue
        return {"input": x7, "output": x8}
