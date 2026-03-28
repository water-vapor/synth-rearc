from synth_rearc.core import *

from .helpers import L_PATCHES_1E5D6875, direct_halo_1e5d6875, shifted_copy_1e5d6875


GRID_SIZES_1E5D6875 = (8, 8, 10, 12, 14, 16, 16, 18)
OBJECT_COLORS_1E5D6875 = (FIVE, TWO)


def generate_1e5d6875(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = choice(GRID_SIZES_1E5D6875)
        x1 = canvas(SEVEN, (x0, x0))
        x2 = max(THREE, subtract(halve(x0), ONE))
        x3 = min(12, subtract(x0, TWO))
        x4 = unifint(diff_lb, diff_ub, (x2, x3))
        x5 = [FIVE, TWO]
        while len(x5) < x4:
            x5.append(choice(OBJECT_COLORS_1E5D6875))
        shuffle(x5)
        x6 = frozenset()
        x7 = frozenset()
        x8 = []
        x9 = x1
        x10 = ZERO
        while len(x8) < x4 and x10 < 800:
            x10 = increment(x10)
            x11 = choice(L_PATCHES_1E5D6875)
            x12 = randint(ZERO, subtract(x0, TWO))
            x13 = randint(ZERO, subtract(x0, TWO))
            x14 = shift(x11, (x12, x13))
            if size(intersection(x14, x6)) > ZERO:
                continue
            if size(intersection(x14, x7)) > ZERO:
                continue
            x15 = x5[len(x8)]
            x16 = recolor(x15, x14)
            x9 = paint(x9, x16)
            x6 = combine(x6, x14)
            x7 = combine(x7, direct_halo_1e5d6875(x14))
            x8.append(x16)
        if len(x8) < x4:
            continue
        x17 = frozenset(
            recolor(FOUR, difference(toindices(shifted_copy_1e5d6875(x18)), x6))
            for x18 in x8
            if equality(color(x18), FIVE)
        )
        x19 = paint(x9, merge(x17))
        x20 = frozenset(
            recolor(THREE, difference(toindices(shifted_copy_1e5d6875(x21)), x6))
            for x21 in x8
            if equality(color(x21), TWO)
        )
        x22 = paint(x19, merge(x20))
        if x22 == x9:
            continue
        return {"input": x9, "output": x22}
