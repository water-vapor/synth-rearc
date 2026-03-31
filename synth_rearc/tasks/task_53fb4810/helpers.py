from __future__ import annotations

from synth_rearc.core import *


TRANSFORMS_53FB4810 = (identity, rot90, rot180, rot270)
STRIP_SIDES_53FB4810 = ("up", "down")
COLOR_POOL_53FB4810 = tuple(value for value in interval(ZERO, TEN, ONE) if value not in (ONE, EIGHT))


def tapered_object_patch_53fb4810(
    height_value: Integer,
    thickness: Integer,
) -> Indices:
    x0 = thickness + TWO
    x1 = set((ZERO, x2) for x2 in range(ONE, subtract(x0, ONE)))
    x1 |= set((subtract(height_value, ONE), x3) for x3 in range(ONE, subtract(x0, ONE)))
    for x4 in range(ONE, subtract(height_value, ONE)):
        x1 |= set((x4, x5) for x5 in range(x0))
    return frozenset(x1)


def object_patch_53fb4810(
    top: Integer,
    left: Integer,
    height_value: Integer,
    thickness: Integer,
) -> Indices:
    x0 = tapered_object_patch_53fb4810(height_value, thickness)
    return shift(x0, (top, left))


def tile_dims_53fb4810(
    period: Integer,
    thickness: Integer,
) -> IntegerTuple:
    return (period, thickness)


def random_tile_53fb4810(
    period: Integer,
    thickness: Integer,
) -> Grid:
    while True:
        x0 = tuple(
            tuple(choice(COLOR_POOL_53FB4810) for _ in range(thickness))
            for _ in range(period)
        )
        if numcolors(x0) > ONE:
            return x0


def tile_object_53fb4810(
    tile: Grid,
    top: Integer,
    left: Integer,
) -> Object:
    x0 = set()
    for x1, x2 in enumerate(tile):
        for x3, x4 in enumerate(x2):
            x0.add((x4, (top + x1, left + x3)))
    return frozenset(x0)


def strip_start_53fb4810(
    object_top: Integer,
    object_left: Integer,
    object_height: Integer,
    thickness: Integer,
    period: Integer,
    side: str,
) -> IntegerTuple:
    x0 = object_left + ONE
    if side == "up":
        return (object_top - period, x0)
    return (object_top + object_height, x0)


def full_strip_53fb4810(
    tile: Grid,
    start: IntegerTuple,
    side: str,
    grid_height: Integer,
) -> Object:
    x0 = len(tile)
    x1 = start[1]
    x2 = set()
    if side == "up":
        x3 = start[0]
        while x3 + x0 > ZERO:
            x2 |= set(tile_object_53fb4810(tile, x3, x1))
            x3 -= x0
    else:
        x4 = start[0]
        while x4 < grid_height:
            x2 |= set(tile_object_53fb4810(tile, x4, x1))
            x4 += x0
    return frozenset(x2)


def probe_strip_53fb4810(
    tile: Grid,
    start: IntegerTuple,
) -> Object:
    return tile_object_53fb4810(tile, start[0], start[1])
