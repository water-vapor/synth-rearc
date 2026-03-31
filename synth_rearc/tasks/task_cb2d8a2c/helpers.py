from __future__ import annotations

from synth_rearc.core import *


BAR_PALETTE_CB2D8A2C = frozenset((ONE, TWO))


def bar_objects_cb2d8a2c(
    I: Grid,
) -> tuple[Object, ...]:
    x0 = objects(I, F, F, T)
    return tuple(
        x1 for x1 in x0
        if palette(x1).issubset(BAR_PALETTE_CB2D8A2C) and size(x1) > ONE
    )


def bar_patch_cb2d8a2c(
    I: Grid,
) -> Indices:
    x0 = bar_objects_cb2d8a2c(I)
    if len(x0) == ZERO:
        return frozenset()
    return merge(tuple(toindices(x1) for x1 in x0))


def trace_path_cb2d8a2c(
    I: Grid,
) -> Indices:
    x0 = bar_objects_cb2d8a2c(I)
    x1 = first(totuple(ofcolor(I, THREE)))
    x2 = equality(height(first(x0)), ONE)
    if x2:
        x3 = DOWN if x1[ZERO] == ZERO else UP
        x4 = tuple(sorted(x0, key=uppermost, reverse=x3 == UP))
    else:
        x3 = RIGHT if x1[ONE] == ZERO else LEFT
        x4 = tuple(sorted(x0, key=leftmost, reverse=x3 == LEFT))
    x5 = initset(x1)
    x6 = x1
    for x7 in x4:
        x8 = colorcount(x7, ONE)
        if x2:
            x9 = uppermost(x7) - x8 - ONE if x3 == DOWN else lowermost(x7) + x8 + ONE
            x10 = rightmost(x7) + x8 + ONE if leftmost(x7) == ZERO else leftmost(x7) - x8 - ONE
            x11 = astuple(x9, x6[ONE])
            x12 = astuple(x9, x10)
        else:
            x9 = leftmost(x7) - x8 - ONE if x3 == RIGHT else rightmost(x7) + x8 + ONE
            x10 = lowermost(x7) + x8 + ONE if uppermost(x7) == ZERO else uppermost(x7) - x8 - ONE
            x11 = astuple(x6[ZERO], x9)
            x12 = astuple(x10, x9)
        x5 = combine(x5, connect(x6, x11))
        x5 = combine(x5, connect(x11, x12))
        x6 = x12
    if x3 == DOWN:
        x13 = astuple(decrement(height(I)), x6[ONE])
    elif x3 == UP:
        x13 = astuple(ZERO, x6[ONE])
    elif x3 == RIGHT:
        x13 = astuple(x6[ZERO], decrement(width(I)))
    else:
        x13 = astuple(x6[ZERO], ZERO)
    return combine(x5, connect(x6, x13))
