from synth_rearc.core import *


SLASH_REFLECTIONS_6BCDB01E = {
    RIGHT: UP,
    UP: RIGHT,
    LEFT: DOWN,
    DOWN: LEFT,
}

BACKSLASH_REFLECTIONS_6BCDB01E = {
    RIGHT: DOWN,
    DOWN: RIGHT,
    LEFT: UP,
    UP: LEFT,
}


def _bounce_6bcdb01e(
    I: Grid,
    loc: IntegerTuple,
    direction: IntegerTuple,
) -> IntegerTuple | None:
    x0 = add(loc, direction)
    x1 = equality(index(I, add(x0, UP_RIGHT)), EIGHT)
    x2 = equality(index(I, add(x0, DOWN_LEFT)), EIGHT)
    x3 = either(x1, x2)
    x4 = equality(index(I, add(x0, NEG_UNITY)), EIGHT)
    x5 = equality(index(I, add(x0, UNITY)), EIGHT)
    x6 = either(x4, x5)
    if x3 == x6:
        return None
    if x3:
        return SLASH_REFLECTIONS_6BCDB01E[direction]
    return BACKSLASH_REFLECTIONS_6BCDB01E[direction]


def verify_6bcdb01e(I: Grid) -> Grid:
    x0 = objects(I, T, F, T)
    x1 = colorfilter(x0, THREE)
    x2 = first(totuple(x1))
    x3 = hline(x2)
    x4 = uppermost(x2)
    x5 = leftmost(x2)
    x6 = rightmost(x2)
    x7 = lowermost(x2)
    if x3:
        if x5 == ZERO:
            x8 = astuple(x4, x6)
            x9 = RIGHT
        else:
            x8 = astuple(x4, x5)
            x9 = LEFT
    else:
        if x4 == ZERO:
            x8 = astuple(x7, x5)
            x9 = DOWN
        else:
            x8 = astuple(x4, x5)
            x9 = UP
    x10 = I
    while True:
        x11 = add(x8, x9)
        x12 = index(I, x11)
        if x12 is None:
            break
        if x12 == EIGHT:
            x13 = _bounce_6bcdb01e(I, x8, x9)
            if x13 is None:
                break
            x9 = x13
            x11 = add(x8, x9)
            x12 = index(I, x11)
            if x12 is None or x12 == EIGHT:
                break
        x8 = x11
        x10 = fill(x10, THREE, initset(x8))
    return x10
