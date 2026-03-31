from __future__ import annotations

from dataclasses import dataclass

from synth_rearc.core import *


BOARD_SHAPE_B5CA7AC4 = (22, 22)
TILE_SIDE_B5CA7AC4 = FIVE
INNER_SIDE_B5CA7AC4 = THREE
LEFT_BORDER_B5CA7AC4 = EIGHT
RIGHT_BORDER_B5CA7AC4 = TWO


@dataclass(frozen=True)
class TileSpecB5CA7AC4:
    top: Integer
    left: Integer
    border: Integer
    inner: Integer


def _tile_patch_b5ca7ac4(
    top: Integer,
    left: Integer,
) -> Indices:
    return frozenset(
        (i, j)
        for i in range(top, add(top, TILE_SIDE_B5CA7AC4))
        for j in range(left, add(left, TILE_SIDE_B5CA7AC4))
    )


def _inner_patch_b5ca7ac4(
    top: Integer,
    left: Integer,
) -> Indices:
    x0 = add(top, ONE)
    x1 = add(left, ONE)
    return frozenset(
        (i, j)
        for i in range(x0, add(x0, INNER_SIDE_B5CA7AC4))
        for j in range(x1, add(x1, INNER_SIDE_B5CA7AC4))
    )


def _boxes_overlap_b5ca7ac4(
    first: TileSpecB5CA7AC4,
    second: TileSpecB5CA7AC4,
) -> Boolean:
    x0 = add(first.top, decrement(TILE_SIDE_B5CA7AC4))
    x1 = add(second.top, decrement(TILE_SIDE_B5CA7AC4))
    x2 = add(first.left, decrement(TILE_SIDE_B5CA7AC4))
    x3 = add(second.left, decrement(TILE_SIDE_B5CA7AC4))
    x4 = x0 < second.top or x1 < first.top
    x5 = x2 < second.left or x3 < first.left
    return not (x4 or x5)


def extract_tiles_b5ca7ac4(
    grid: Grid,
) -> tuple[TileSpecB5CA7AC4, ...]:
    x0 = objects(grid, T, F, T)
    x1 = sizefilter(x0, NINE)
    x2 = tuple(sorted((x3 for x3 in x1 if square(x3)), key=lambda x4: (uppermost(x4), leftmost(x4), color(x4))))
    x3 = []
    for x4 in x2:
        x5 = outbox(x4)
        x6 = toobject(x5, grid)
        if len(x6) != 16:
            continue
        if numcolors(x6) != ONE:
            continue
        x7 = color(x6)
        if x7 not in (LEFT_BORDER_B5CA7AC4, RIGHT_BORDER_B5CA7AC4):
            continue
        x8 = TileSpecB5CA7AC4(
            top=subtract(uppermost(x4), ONE),
            left=subtract(leftmost(x4), ONE),
            border=x7,
            inner=color(x4),
        )
        x3.append(x8)
    return tuple(x3)


def _pack_left_b5ca7ac4(
    tiles: tuple[TileSpecB5CA7AC4, ...],
) -> tuple[TileSpecB5CA7AC4, ...]:
    x0 = []
    x1 = sorted(tiles, key=lambda x2: (x2.left, x2.top, x2.inner))
    for x2 in x1:
        x3 = ZERO
        x4 = TileSpecB5CA7AC4(x2.top, x3, x2.border, x2.inner)
        while any(_boxes_overlap_b5ca7ac4(x4, x5) for x5 in x0):
            x3 = increment(x3)
            x4 = TileSpecB5CA7AC4(x2.top, x3, x2.border, x2.inner)
        x0.append(x4)
    return tuple(x0)


def _pack_right_b5ca7ac4(
    tiles: tuple[TileSpecB5CA7AC4, ...],
    width_value: Integer,
) -> tuple[TileSpecB5CA7AC4, ...]:
    x0 = []
    x1 = sorted(tiles, key=lambda x2: (-x2.left, x2.top, x2.inner))
    for x2 in x1:
        x3 = subtract(width_value, TILE_SIDE_B5CA7AC4)
        x4 = TileSpecB5CA7AC4(x2.top, x3, x2.border, x2.inner)
        while any(_boxes_overlap_b5ca7ac4(x4, x5) for x5 in x0):
            x3 = decrement(x3)
            x4 = TileSpecB5CA7AC4(x2.top, x3, x2.border, x2.inner)
        x0.append(x4)
    return tuple(x0)


def pack_tiles_b5ca7ac4(
    tiles: tuple[TileSpecB5CA7AC4, ...],
    width_value: Integer,
) -> tuple[TileSpecB5CA7AC4, ...]:
    x0 = tuple(x1 for x1 in tiles if x1.border == LEFT_BORDER_B5CA7AC4)
    x1 = tuple(x2 for x2 in tiles if x2.border == RIGHT_BORDER_B5CA7AC4)
    x2 = _pack_left_b5ca7ac4(x0)
    x3 = _pack_right_b5ca7ac4(x1, width_value)
    x4 = x2 + x3
    return tuple(sorted(x4, key=lambda x5: (x5.top, x5.left, x5.border, x5.inner)))


def render_tiles_b5ca7ac4(
    bg: Integer,
    tiles: tuple[TileSpecB5CA7AC4, ...],
    dims: IntegerTuple = BOARD_SHAPE_B5CA7AC4,
) -> Grid:
    x0 = canvas(bg, dims)
    for x1 in tiles:
        x2 = _tile_patch_b5ca7ac4(x1.top, x1.left)
        x3 = _inner_patch_b5ca7ac4(x1.top, x1.left)
        x0 = fill(x0, x1.border, x2)
        x0 = fill(x0, x1.inner, x3)
    return x0
