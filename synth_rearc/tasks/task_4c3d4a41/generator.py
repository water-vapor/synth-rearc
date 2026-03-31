from synth_rearc.core import *

from .verifier import verify_4c3d4a41


LEFT_COLUMNS_4C3D4A41 = (ONE, THREE, FIVE, SEVEN)
RIGHT_COLUMNS_4C3D4A41 = tuple(j + TEN for j in LEFT_COLUMNS_4C3D4A41)
HEIGHT_CHOICES_4C3D4A41 = (TWO, THREE, FOUR)
BAR_COLORS_4C3D4A41 = (ONE, TWO, THREE, FOUR, SIX, SEVEN, EIGHT, NINE)


def _left_patch_4c3d4a41(
    heights: tuple[Integer, Integer, Integer, Integer],
) -> Indices:
    x0 = frozenset((FIVE, j) for j in range(ONE, EIGHT))
    x1 = frozenset(
        (i, j)
        for j, h in zip(LEFT_COLUMNS_4C3D4A41, heights)
        for i in range(SIX - h, SIX)
    )
    return combine(x0, x1)


def _scaffold_patch_4c3d4a41() -> Indices:
    x0 = frozenset((ZERO, j) for j in range(NINE, 20))
    x1 = frozenset((SEVEN, j) for j in range(NINE, 20))
    x2 = frozenset((i, 19) for i in range(8))
    x3 = frozenset((i, NINE) for i in combine(interval(ZERO, FOUR, ONE), interval(SIX, 8, ONE)))
    return merge((x0, x1, x2, x3))


def generate_4c3d4a41(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = tuple(choice(HEIGHT_CHOICES_4C3D4A41) for _ in LEFT_COLUMNS_4C3D4A41)
        x1 = tuple(unifint(diff_lb, diff_ub, (ONE, FOUR)) for _ in RIGHT_COLUMNS_4C3D4A41)
        x2 = tuple(unifint(diff_lb, diff_ub, (maximum((TWO, x3)), FOUR)) for x3 in x1)
        x4 = sample(BAR_COLORS_4C3D4A41, FOUR)
        x5 = canvas(ZERO, (8, 20))
        x6 = fill(x5, FIVE, _scaffold_patch_4c3d4a41())
        x7 = fill(x6, FIVE, _left_patch_4c3d4a41(x0))
        x8 = x7
        for x9, x10, x11, x12 in zip(RIGHT_COLUMNS_4C3D4A41, x4, x1, x2):
            x13 = subtract(x12, x11)
            if positive(x13):
                x14 = frozenset((i, x9) for i in range(ONE, x13 + ONE))
                x8 = fill(x8, FIVE, x14)
            x15 = frozenset((i, x9) for i in range(x13 + ONE, x12 + ONE))
            x8 = fill(x8, x10, x15)
        x16 = verify_4c3d4a41(x8)
        if equality(x8, x16):
            continue
        return {"input": x8, "output": x16}
