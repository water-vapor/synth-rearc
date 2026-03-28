from synth_rearc.core import *


DIAMOND_TEMPLATE_652646ff = frozenset(
    {
        (ZERO, TWO),
        (ZERO, THREE),
        (ONE, ONE),
        (ONE, FOUR),
        (TWO, ZERO),
        (TWO, FIVE),
        (THREE, ZERO),
        (THREE, FIVE),
        (FOUR, ONE),
        (FOUR, FOUR),
        (FIVE, TWO),
        (FIVE, THREE),
    }
)

ABOVE_STEPS_652646ff = (
    (ZERO, -FIVE),
    (ZERO, -THREE),
    (-ONE, -FOUR),
    (-ONE, -ONE),
    (-TWO, TWO),
    (THREE, THREE),
)


def diamond_patch_652646ff(
    origin: IntegerTuple,
) -> Indices:
    return shift(DIAMOND_TEMPLATE_652646ff, origin)


def clipped_diamond_patch_652646ff(
    origin: IntegerTuple,
    dims: IntegerTuple,
) -> Indices:
    x0 = dims[ZERO]
    x1 = dims[ONE]
    x2 = diamond_patch_652646ff(origin)
    return frozenset((x3, x4) for x3, x4 in x2 if 0 <= x3 < x0 and 0 <= x4 < x1)


def diamond_block_652646ff(
    bg: Integer,
    fg: Integer,
) -> Grid:
    x0 = canvas(bg, (SIX, SIX))
    return fill(x0, fg, DIAMOND_TEMPLATE_652646ff)
