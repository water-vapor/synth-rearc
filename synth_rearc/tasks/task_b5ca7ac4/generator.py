from __future__ import annotations

from synth_rearc.core import *

from .helpers import (
    BOARD_SHAPE_B5CA7AC4,
    LEFT_BORDER_B5CA7AC4,
    RIGHT_BORDER_B5CA7AC4,
    TILE_SIDE_B5CA7AC4,
    TileSpecB5CA7AC4,
    pack_tiles_b5ca7ac4,
    render_tiles_b5ca7ac4,
)
from .verifier import verify_b5ca7ac4


BACKGROUND_POOL_B5CA7AC4 = tuple(x0 for x0 in range(TEN) if x0 not in (LEFT_BORDER_B5CA7AC4, RIGHT_BORDER_B5CA7AC4))
LEFT_OUTPUT_COLS_B5CA7AC4 = (ZERO, TILE_SIDE_B5CA7AC4)
RIGHT_OUTPUT_COLS_B5CA7AC4 = (
    subtract(BOARD_SHAPE_B5CA7AC4[ONE], double(TILE_SIDE_B5CA7AC4)),
    subtract(BOARD_SHAPE_B5CA7AC4[ONE], TILE_SIDE_B5CA7AC4),
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


def _placeable_b5ca7ac4(
    tile: TileSpecB5CA7AC4,
    placed: tuple[TileSpecB5CA7AC4, ...],
) -> Boolean:
    return all(not _boxes_overlap_b5ca7ac4(tile, other) for other in placed)


def _pick_inner_colors_b5ca7ac4(
    bg: Integer,
    border: Integer,
    count: Integer,
) -> tuple[Integer, ...]:
    x0 = tuple(x1 for x1 in range(TEN) if x1 not in (bg, border))
    return tuple(sample(x0, count))


def _layout_ok_b5ca7ac4(
    input_tiles: tuple[TileSpecB5CA7AC4, ...],
    output_tiles: tuple[TileSpecB5CA7AC4, ...],
) -> Boolean:
    x0 = {x1.left for x1 in output_tiles if x1.border == LEFT_BORDER_B5CA7AC4}
    x1 = {x2.left for x2 in output_tiles if x2.border == RIGHT_BORDER_B5CA7AC4}
    if x0 != set(LEFT_OUTPUT_COLS_B5CA7AC4):
        return False
    if x1 != set(RIGHT_OUTPUT_COLS_B5CA7AC4):
        return False
    x2 = {(x3.border, x3.inner): x3.left for x3 in input_tiles}
    x3 = {(x4.border, x4.inner): x4.left for x4 in output_tiles}
    x4 = any(x2[x5] != x3[x5] for x5 in x2 if x5[ZERO] == LEFT_BORDER_B5CA7AC4)
    x5 = any(x2[x6] != x3[x6] for x6 in x2 if x6[ZERO] == RIGHT_BORDER_B5CA7AC4)
    x6 = sum(abs(x2[x7] - x3[x7]) for x7 in x2)
    return both(both(x4, x5), x6 >= 20)


def generate_b5ca7ac4(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    x0, x1 = BOARD_SHAPE_B5CA7AC4
    x2 = subtract(x0, TILE_SIDE_B5CA7AC4)
    x3 = subtract(x1, TILE_SIDE_B5CA7AC4)
    for _ in range(400):
        x4 = choice(BACKGROUND_POOL_B5CA7AC4)
        x5 = choice((THREE, FOUR))
        x6 = choice((THREE, FOUR, FIVE))
        x7 = _pick_inner_colors_b5ca7ac4(x4, LEFT_BORDER_B5CA7AC4, x5)
        x8 = _pick_inner_colors_b5ca7ac4(x4, RIGHT_BORDER_B5CA7AC4, x6)
        x9 = [(LEFT_BORDER_B5CA7AC4, x10) for x10 in x7] + [(RIGHT_BORDER_B5CA7AC4, x11) for x11 in x8]
        shuffle(x9)
        x10 = ()
        x11 = True
        for x12, x13 in x9:
            x14 = False
            for _ in range(120):
                x15 = TileSpecB5CA7AC4(
                    top=randint(ZERO, x2),
                    left=randint(ZERO, x3),
                    border=x12,
                    inner=x13,
                )
                if _placeable_b5ca7ac4(x15, x10):
                    x10 = x10 + (x15,)
                    x14 = True
                    break
            if not x14:
                x11 = False
                break
        if not x11:
            continue
        x16 = tuple(sorted(x10, key=lambda x17: (x17.top, x17.left, x17.border, x17.inner)))
        x17 = pack_tiles_b5ca7ac4(x16, x1)
        if not _layout_ok_b5ca7ac4(x16, x17):
            continue
        x18 = render_tiles_b5ca7ac4(x4, x16, BOARD_SHAPE_B5CA7AC4)
        x19 = render_tiles_b5ca7ac4(x4, x17, BOARD_SHAPE_B5CA7AC4)
        if x18 == x19:
            continue
        if verify_b5ca7ac4(x18) != x19:
            continue
        return {"input": x18, "output": x19}
    raise RuntimeError("failed to generate a valid b5ca7ac4 example")
