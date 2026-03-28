from synth_rearc.core import *

from .helpers import (
    GRID_SHAPE_B20F7C8B,
    LEGEND_SHAPES_B20F7C8B,
    dihedral_variants_b20f7c8b,
    paint_pattern_at_b20f7c8b,
    paint_solid_at_b20f7c8b,
)
from .verifier import verify_b20f7c8b


LEGEND_COLORS_B20F7C8B = (ONE, TWO, THREE, FOUR, FIVE, SIX, SEVEN)
LEGEND_ROW_SETS_B20F7C8B = (
    (ONE, FIVE, TEN, 15),
    (ONE, SIX, TEN, 15),
    (TWO, SIX, 11, 15),
    (TWO, SEVEN, 11, 15),
)


def _legend_panel_b20f7c8b(
    side: str,
) -> Indices:
    x0 = interval(ZERO, GRID_SHAPE_B20F7C8B[0], ONE)
    x1 = interval(16, GRID_SHAPE_B20F7C8B[1], ONE) if side == "right" else interval(ZERO, SIX, ONE)
    return product(x0, x1)


def _legend_origin_b20f7c8b(
    side: str,
    row_start: int,
    patch: Patch,
) -> tuple[int, int]:
    x0 = width(patch)
    x1 = randint(ONE, SIX - x0 - ONE)
    x2 = 16 if side == "right" else ZERO
    return (row_start, x2 + x1)


def generate_b20f7c8b(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = choice(("left", "right"))
        x1 = canvas(ZERO, GRID_SHAPE_B20F7C8B)
        x2 = fill(x1, EIGHT, _legend_panel_b20f7c8b(x0))
        x3 = sample(LEGEND_COLORS_B20F7C8B, FOUR)
        x4 = sample(LEGEND_SHAPES_B20F7C8B, FOUR)
        x5 = list(zip(x3, x4))
        x6 = sample(x5, FOUR)
        x7 = choice(LEGEND_ROW_SETS_B20F7C8B)
        x8 = x2
        for x9, x10 in zip(x6, x7):
            x11, x12 = x9
            x13 = _legend_origin_b20f7c8b(x0, x10, x12)
            x14 = shift(x12, x13)
            x8 = fill(x8, x11, x14)
        x15 = choice(((ONE, EIGHT), (TWO, NINE)))
        x16 = (ONE, EIGHT) if x0 == "right" else (EIGHT, 15)
        x17 = ((x15[0], x16[0]), (x15[0], x16[1]), (x15[1], x16[0]), (x15[1], x16[1]))
        x18 = sample(x5, FOUR)
        x19 = tuple(x20 for x20, x21 in enumerate(x18) if x21[0] != TWO)
        x20 = min(choice((ZERO, ZERO, ONE, ONE, TWO)), len(x19))
        x21 = frozenset(sample(x19, x20))
        x22 = x8
        x23 = x8
        for x24, x25 in enumerate(zip(x17, x18)):
            x26, x27 = x25
            x28, x29 = x27
            if x24 in x21:
                x22 = paint_solid_at_b20f7c8b(x22, x26, x28)
                x23 = paint_pattern_at_b20f7c8b(x23, x26, x29)
            else:
                x30 = choice(dihedral_variants_b20f7c8b(x29))
                x22 = paint_pattern_at_b20f7c8b(x22, x26, x30)
                x23 = paint_solid_at_b20f7c8b(x23, x26, x28)
        if x22 == x23:
            continue
        if verify_b20f7c8b(x22) != x23:
            continue
        return {"input": x22, "output": x23}
