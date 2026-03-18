from arc2.core import *

from .helpers import (
    MOTIFS_F0100645,
    halo_patch_f0100645,
    mirror_patch_f0100645,
    settle_left_objects_f0100645,
    settle_right_objects_f0100645,
    shift_patch_f0100645,
)


BG_F0100645 = SEVEN


def _dims_f0100645(
    patch: Indices,
) -> tuple[Integer, Integer]:
    return (
        ONE + max(i for i, _ in patch),
        ONE + max(j for _, j in patch),
    )


def _choose_patch_f0100645() -> Indices:
    x0 = choice(MOTIFS_F0100645)
    if choice((T, F)):
        x0 = mirror_patch_f0100645(x0)
    return x0


def _place_side_f0100645(
    grid: Grid,
    occupied: set[IntegerTuple],
    side_halo: set[IntegerTuple],
    side_color: Integer,
    side: str,
    height_value: Integer,
    width_value: Integer,
) -> tuple[Grid, set[IntegerTuple], set[IntegerTuple], Boolean]:
    x0 = grid
    x1 = occupied
    x2 = side_halo
    x3 = choice((TWO, THREE))
    for _ in range(x3):
        x4 = F
        for _ in range(120):
            x5 = _choose_patch_f0100645()
            x6, x7 = _dims_f0100645(x5)
            x8 = randint(ZERO, subtract(height_value, x6))
            if side == "left":
                x9 = max(TWO, subtract(add(divide(width_value, TWO), ONE), x7))
                x10 = randint(TWO, x9)
            else:
                x9 = max(ONE, subtract(divide(width_value, TWO), x7))
                x10 = subtract(subtract(width_value, x7), TWO)
                if x9 > x10:
                    x9 = x10
                x10 = randint(x9, x10)
            x11 = shift_patch_f0100645(x5, x8, x10)
            x12 = halo_patch_f0100645(x11)
            if len(x11 & x1) > ZERO:
                continue
            if len(x12 & x2) > ZERO:
                continue
            x0 = fill(x0, side_color, x11)
            x1 = x1 | x11
            x2 = x2 | x12
            x4 = T
            break
        if not x4:
            return x0, x1, x2, F
    return x0, x1, x2, T


def generate_f0100645(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = unifint(diff_lb, diff_ub, (EIGHT, 12))
        x1 = unifint(diff_lb, diff_ub, (NINE, 13))
        x2 = sample(remove(BG_F0100645, interval(ONE, TEN, ONE)), TWO)
        x3 = first(x2)
        x4 = last(x2)
        x5 = frozenset((i, ZERO) for i in range(x0))
        x6 = subtract(x1, ONE)
        x7 = frozenset((i, x6) for i in range(x0))
        x8 = canvas(BG_F0100645, (x0, x1))
        x9 = fill(x8, x3, x5)
        x10 = fill(x9, x4, x7)
        x11 = set(x5 | x7)
        x12 = set(x5)
        x13 = set(x7)
        x10, x11, x12, x14 = _place_side_f0100645(x10, x11, x12, x3, "left", x0, x1)
        if not x14:
            continue
        x10, x11, x13, x15 = _place_side_f0100645(x10, x11, x13, x4, "right", x0, x1)
        if not x15:
            continue
        x16 = tuple(objects(x10, T, T, F))
        x17 = tuple(obj for obj in x16 if color(obj) == x3 and leftmost(obj) > ZERO)
        x18 = tuple(obj for obj in x16 if color(obj) == x4 and rightmost(obj) < x6)
        x19 = settle_left_objects_f0100645(x17, x5, x1)
        x20 = settle_right_objects_f0100645(x18, x7, x1)
        x21 = toindices(merge(x19))
        x22 = toindices(merge(x20))
        if len(x21 & x22) > ZERO:
            continue
        x23 = canvas(BG_F0100645, (x0, x1))
        x24 = fill(x23, x3, x5)
        x25 = fill(x24, x4, x7)
        x26 = paint(x25, merge(x19))
        x27 = paint(x26, merge(x20))
        if x10 == x27:
            continue
        if size(x17) + size(x18) < FOUR:
            continue
        if size(x21) + size(x22) < SIX:
            continue
        return {"input": x10, "output": x27}
