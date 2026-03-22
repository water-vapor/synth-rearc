from arc2.core import *


WIDTH_BOUNDS_72A961C9 = (SIX, 11)
BOTTOM_PAD_BOUNDS_72A961C9 = (ONE, FOUR)
SPECIAL_COLORS_72A961C9 = (TWO, EIGHT)
MAX_SPECIALS_72A961C9 = FOUR
MAX_TOP_PAD_72A961C9 = TEN


def _tower_height_72a961c9(color: int) -> int:
    return FOUR if color == TWO else THREE


def _sample_special_columns_72a961c9(width: int, count: int) -> tuple[int, ...]:
    while True:
        x0 = tuple(sorted(sample(tuple(range(width)), count)))
        x1 = tuple(x0[x2 + ONE] - x0[x2] for x2 in range(len(x0) - ONE))
        if all(x3 > ONE for x3 in x1):
            return x0


def generate_72a961c9(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    x0 = unifint(diff_lb, diff_ub, WIDTH_BOUNDS_72A961C9)
    x1 = divide(add(x0, ONE), THREE)
    x2 = unifint(diff_lb, diff_ub, (ONE, min(MAX_SPECIALS_72A961C9, x1)))
    x3 = _sample_special_columns_72a961c9(x0, x2)
    x4 = tuple(choice(SPECIAL_COLORS_72A961C9) for _ in x3)
    x5 = max(_tower_height_72a961c9(x6) for x6 in x4)
    x6 = unifint(diff_lb, diff_ub, (x5, MAX_TOP_PAD_72A961C9))
    x7 = unifint(diff_lb, diff_ub, BOTTOM_PAD_BOUNDS_72A961C9)
    x8 = add(add(x6, ONE), x7)
    x9 = frozenset((x6, j) for j in range(x0))
    x10 = canvas(ZERO, (x8, x0))
    x11 = fill(x10, ONE, x9)
    for x12, x13 in zip(x3, x4):
        x11 = fill(x11, x13, frozenset({(x6, x12)}))
    x14 = x11
    for x15, x16 in zip(x3, x4):
        x17 = _tower_height_72a961c9(x16)
        x18 = frozenset((subtract(x6, x19), x15) for x19 in range(ONE, x17))
        x19 = frozenset({(subtract(x6, x17), x15)})
        x14 = fill(x14, ONE, x18)
        x14 = fill(x14, x16, x19)
    return {"input": x11, "output": x14}
