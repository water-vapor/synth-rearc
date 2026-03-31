from __future__ import annotations

from synth_rearc.core import *

from .helpers import (
    TRANSFORMS_53FB4810,
    object_patch_53fb4810,
    full_strip_53fb4810,
    probe_strip_53fb4810,
    random_tile_53fb4810,
    strip_start_53fb4810,
)
from .verifier import verify_53fb4810


def _choose_columns_53fb4810(
    grid_width: Integer,
    object_width: Integer,
    count: Integer,
) -> tuple[Integer, ...] | None:
    x0 = tuple(range(ONE, subtract(grid_width, object_width)))
    x1 = list(x0)
    shuffle(x1)
    x2 = []
    for x3 in x1:
        if all(abs(x3 - x4) >= object_width + TWO for x4 in x2):
            x2.append(x3)
            if len(x2) == count:
                return tuple(sorted(x2))
    return None


def _paint_object_53fb4810(
    grid: Grid,
    patch: Indices,
) -> Grid:
    return fill(grid, ONE, patch)


def generate_53fb4810(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = EIGHT
        x1, x2 = choice(((ONE, TWO), (TWO, ONE), (TWO, TWO)))
        x3 = choice((THREE, THREE, FIVE))
        x4 = add(x1, TWO)
        x5 = choice((ONE, TWO))
        x6 = add(x5, ONE)
        x7 = unifint(diff_lb, diff_ub, (max(18, add(add(x3, multiply(x2, FOUR)), ONE)), 30))
        x8 = unifint(diff_lb, diff_ub, (add(multiply(x6, add(x4, TWO)), TWO), 30))
        x9 = _choose_columns_53fb4810(x8, x4, x6)
        if x9 is None:
            continue
        x10 = randint(ONE, subtract(subtract(x7, x3), multiply(x2, FOUR)))
        x13 = canvas(x0, (x7, x8))
        x14 = canvas(x0, (x7, x8))
        x15 = object_patch_53fb4810(x10, x9[ZERO], x3, x1)
        x13 = _paint_object_53fb4810(x13, x15)
        x14 = _paint_object_53fb4810(x14, x15)
        x16 = random_tile_53fb4810(x2, x1)
        x17 = strip_start_53fb4810(x10, x9[ZERO], x3, x1, x2, "down")
        x18 = full_strip_53fb4810(x16, x17, "down", x7)
        x13 = paint(x13, x18)
        x14 = paint(x14, x18)
        x19 = tuple(choice(("up", "down")) for _ in range(x5))
        x20 = []
        for x21 in x19:
            if x21 == "up":
                x22 = randint(add(x2, ONE), subtract(subtract(x7, x3), ONE))
            else:
                x22 = randint(ONE, subtract(subtract(subtract(x7, x3), x2), TWO))
            x20.append(x22)
        for x23, x24, x25 in zip(x9[ONE:], x20, x19):
            x26 = object_patch_53fb4810(x24, x23, x3, x1)
            x13 = _paint_object_53fb4810(x13, x26)
            x14 = _paint_object_53fb4810(x14, x26)
            x27 = random_tile_53fb4810(x2, x1)
            x28 = strip_start_53fb4810(x24, x23, x3, x1, x2, x25)
            x29 = probe_strip_53fb4810(x27, x28)
            x30 = full_strip_53fb4810(x27, x28, x25, x7)
            x13 = paint(x13, x29)
            x14 = paint(x14, x30)
        if equality(x13, x14):
            continue
        x31 = choice(TRANSFORMS_53FB4810)
        x32 = x31(x13)
        x33 = x31(x14)
        if verify_53fb4810(x32) != x33:
            continue
        return {"input": x32, "output": x33}
