from synth_rearc.core import *


ANCHORS_A57F2F04 = ("tl", "tr", "bl", "br")


def seed_patch_a57f2f04(
    block: Grid,
) -> Indices:
    x0 = tuple(x1 for x1 in palette(block) if x1 != ZERO)
    if len(x0) != ONE:
        raise ValueError("a57f2f04 expects exactly one nonzero seed color per block")
    return ofcolor(block, x0[0])


def seed_tile_bounds_a57f2f04(
    block: Grid,
) -> Tuple[IntegerTuple, IntegerTuple]:
    x0 = seed_patch_a57f2f04(block)
    x1, x2 = shape(block)
    x3 = uppermost(x0) == ZERO
    x4 = leftmost(x0) == ZERO
    x5 = lowermost(x0)
    x6 = rightmost(x0)
    x7 = ZERO if x3 else uppermost(x0)
    x8 = ZERO if x4 else leftmost(x0)
    x9 = add(x5, ONE) if x3 else subtract(x1, x7)
    x10 = add(x6, ONE) if x4 else subtract(x2, x8)
    if x9 <= ZERO or x10 <= ZERO:
        raise ValueError("a57f2f04 produced an invalid tile size")
    if not both(either(x3, x5 == decrement(x1)), either(x4, x6 == decrement(x2))):
        raise ValueError("a57f2f04 seed does not touch a block corner")
    return (x7, x8), (x9, x10)


def seed_tile_a57f2f04(
    block: Grid,
) -> Grid:
    x0, x1 = seed_tile_bounds_a57f2f04(block)
    return crop(block, x0, x1)


def repeat_tile_a57f2f04(
    tile: Grid,
    dims: IntegerTuple,
) -> Grid:
    x0, x1 = shape(tile)
    x2, x3 = dims
    return tuple(tuple(tile[i % x0][j % x1] for j in range(x3)) for i in range(x2))


def anchor_offset_a57f2f04(
    block_shape: IntegerTuple,
    tile_shape: IntegerTuple,
    anchor: str,
) -> IntegerTuple:
    x0, x1 = block_shape
    x2, x3 = tile_shape
    if anchor == "tl":
        return ORIGIN
    if anchor == "tr":
        return (ZERO, subtract(x1, x3))
    if anchor == "bl":
        return (subtract(x0, x2), ZERO)
    if anchor == "br":
        return (subtract(x0, x2), subtract(x1, x3))
    raise ValueError(f"unknown anchor {anchor}")


def render_input_block_a57f2f04(
    tile: Grid,
    block_shape: IntegerTuple,
    anchor: str,
) -> Grid:
    x0 = canvas(ZERO, block_shape)
    x1 = anchor_offset_a57f2f04(block_shape, shape(tile), anchor)
    x2 = shift(asobject(tile), x1)
    return paint(x0, x2)


def render_output_block_a57f2f04(
    block: Grid,
) -> Grid:
    x0 = seed_tile_a57f2f04(block)
    return repeat_tile_a57f2f04(x0, shape(block))
