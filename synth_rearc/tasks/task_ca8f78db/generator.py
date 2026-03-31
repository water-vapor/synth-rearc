from synth_rearc.core import *

from .helpers import (
    is_pattern_row_ca8f78db,
    recover_cycle_ca8f78db,
    render_wallpaper_ca8f78db,
)


GRID_SIZE_CA8F78DB = 30
PERIOD_CHOICES_CA8F78DB = (TWO, THREE, FOUR, FIVE, SIX, SEVEN, EIGHT)
ACCENT_COLORS_CA8F78DB = (TWO, THREE, FOUR, FIVE, SIX, SEVEN, EIGHT, NINE)
PATTERN_PARITY_CA8F78DB = ONE


def _rectangle_patch_ca8f78db(
    top: Integer,
    left: Integer,
    height_value: Integer,
    width_value: Integer,
) -> Indices:
    return frozenset(
        (x0, x1)
        for x0 in range(top, top + height_value)
        for x1 in range(left, left + width_value)
    )


def _sample_rectangle_ca8f78db(
    diff_lb: float,
    diff_ub: float,
) -> tuple[Integer, Integer, Integer, Integer]:
    x0 = unifint(diff_lb, diff_ub, (TWO, EIGHT))
    x1 = unifint(diff_lb, diff_ub, (TWO, SIX))
    x2 = randint(ZERO, GRID_SIZE_CA8F78DB - x0)
    x3 = randint(ZERO, GRID_SIZE_CA8F78DB - x1)
    x4 = choice(("free", "free", "free", "top", "bottom", "left", "right"))
    if x4 == "top":
        x2 = ZERO
    elif x4 == "bottom":
        x2 = GRID_SIZE_CA8F78DB - x0
    elif x4 == "left":
        x3 = ZERO
    elif x4 == "right":
        x3 = GRID_SIZE_CA8F78DB - x1
    return x2, x3, x0, x1


def generate_ca8f78db(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = choice(PERIOD_CHOICES_CA8F78DB)
        x1 = (ONE,) + tuple(sample(ACCENT_COLORS_CA8F78DB, x0 - ONE))
        x2 = render_wallpaper_ca8f78db(
            x1,
            GRID_SIZE_CA8F78DB,
            GRID_SIZE_CA8F78DB,
            PATTERN_PARITY_CA8F78DB,
        )
        x3 = frozenset()
        x4 = unifint(diff_lb, diff_ub, (THREE, SIX))
        for _ in range(x4):
            x5, x6, x7, x8 = _sample_rectangle_ca8f78db(diff_lb, diff_ub)
            x9 = _rectangle_patch_ca8f78db(x5, x6, x7, x8)
            x3 = combine(x3, x9)
        x10 = fill(x2, ZERO, x3)
        x11 = colorcount(x10, ZERO)
        if x11 < 40 or x11 > 95:
            continue
        x12 = tuple(
            x13
            for x13 in range(GRID_SIZE_CA8F78DB)
            if is_pattern_row_ca8f78db(x10[x13])
        )
        if len(x12) != GRID_SIZE_CA8F78DB // TWO:
            continue
        x13 = x12[ZERO] % TWO
        if x13 != PATTERN_PARITY_CA8F78DB:
            continue
        x14 = recover_cycle_ca8f78db(x10, x12)
        if x14 != x1:
            continue
        x15 = render_wallpaper_ca8f78db(
            x14,
            GRID_SIZE_CA8F78DB,
            GRID_SIZE_CA8F78DB,
            x13,
        )
        if x15 != x2:
            continue
        return {"input": x10, "output": x2}
