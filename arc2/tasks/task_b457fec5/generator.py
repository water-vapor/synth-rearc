from arc2.core import *

from .helpers import diagonal_band_patch_b457fec5, recolor_band_patch_b457fec5


def _expanded_bbox_b457fec5(
    top: int,
    left: int,
    size: int,
) -> Indices:
    return frozenset(
        (i, j)
        for i in range(top - ONE, top + size + ONE)
        for j in range(left - ONE, left + size + ONE)
    )


def _place_objects_b457fec5(
    shape0: tuple[int, int],
    specs: tuple[tuple[int, int, bool], ...],
    forbidden0: Indices,
) -> tuple[Indices, ...] | None:
    h, w = shape0
    specs0 = sorted(specs, key=lambda item: item[0], reverse=True)
    forbidden = set(forbidden0)
    gray_patches: list[Indices] = []
    for size0, thickness0, mirrored0 in specs0:
        placed = False
        for _ in range(400):
            top0 = randint(ONE, h - size0 - ONE)
            left0 = randint(ONE, w - size0 - ONE)
            patch0 = shift(
                diagonal_band_patch_b457fec5(size0, thickness0, mirrored0),
                (top0, left0),
            )
            if toindices(patch0) & forbidden:
                continue
            gray_patches.append(patch0)
            forbidden |= _expanded_bbox_b457fec5(top0, left0, size0)
            placed = True
            break
        if not placed:
            return None
    return tuple(gray_patches)


def generate_b457fec5(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    x0 = remove(FIVE, interval(ONE, TEN, ONE))
    while True:
        x1 = choice((THREE, FOUR))
        x2 = tuple(sample(x0, x1))
        x3 = choice((ONE, TWO, TWO, THREE))
        x4 = []
        for _ in range(x3):
            x5 = x1 + choice((ZERO, ONE))
            x6 = x5 + unifint(diff_lb, diff_ub, (TWO, 11))
            x7 = choice((F, T))
            x4.append((x6, x5, x7))
        x5 = tuple(x4)
        x6 = maximum(apply(first, x5))
        x7 = unifint(diff_lb, diff_ub, (max(14, x6 + 3), min(30, x6 + 13)))
        x8 = unifint(diff_lb, diff_ub, (max(18, x6 + x1 + 4), min(30, x6 + x3 * 8 + 10)))
        if x7 <= x6 + TWO or x8 <= x6 + TWO:
            continue
        x9 = randint(ONE, x8 - x1 - ONE)
        x11 = frozenset(
            (i, j)
            for i in range(ZERO, THREE)
            for j in range(max(ZERO, x9 - ONE), min(x8, x9 + x1 + ONE))
        )
        x12 = _place_objects_b457fec5((x7, x8), x5, x11)
        if x12 is None:
            continue
        x13 = x12
        x14 = tuple(recolor(FIVE, patch0) for patch0 in x13)
        x15 = tuple(recolor_band_patch_b457fec5(x2, patch0) for patch0 in x13)
        x16 = frozenset((value0, (ONE, x9 + j)) for j, value0 in enumerate(x2))
        x17 = canvas(ZERO, (x7, x8))
        x18 = paint(x17, x16)
        x19 = paint(x18, merge(x14))
        x20 = paint(x18, merge(x15))
        if x19 == x20:
            continue
        return {"input": x19, "output": x20}
