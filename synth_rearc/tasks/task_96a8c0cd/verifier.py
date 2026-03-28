from synth_rearc.core import *


def _turn_96a8c0cd(
    direction: IntegerTuple,
    value: Integer,
) -> IntegerTuple:
    if equality(direction, DOWN):
        return branch(equality(value, ONE), RIGHT, LEFT)
    if equality(direction, UP):
        return branch(equality(value, ONE), LEFT, RIGHT)
    if equality(direction, RIGHT):
        return branch(equality(value, ONE), UP, DOWN)
    return branch(equality(value, ONE), DOWN, UP)


def _tail_96a8c0cd(
    loc: IntegerTuple,
    direction: IntegerTuple,
    dims: IntegerTuple,
) -> IntegerTuple:
    h, w = dims
    if equality(direction, DOWN):
        return astuple(decrement(h), loc[ONE])
    if equality(direction, UP):
        return astuple(ZERO, loc[ONE])
    if equality(direction, RIGHT):
        return astuple(loc[ZERO], decrement(w))
    return astuple(loc[ZERO], ZERO)


def verify_96a8c0cd(I: Grid) -> Grid:
    x0 = objects(I, T, F, T)
    x1 = first(totuple(colorfilter(x0, TWO)))
    x2 = combine(colorfilter(x0, ONE), colorfilter(x0, THREE))
    x3 = first(totuple(x2))
    x4 = ulcorner(x1)
    x5 = branch(
        equality(x4[ZERO], ZERO),
        DOWN,
        branch(equality(x4[ZERO], decrement(height(I))), UP, branch(equality(x4[ONE], ZERO), RIGHT, LEFT)),
    )
    x6 = initset(x4)
    x7 = {}
    for x8 in x2:
        for x9 in toindices(x8):
            x7[x9] = x8
    x10 = x4
    x11 = shape(I)
    while True:
        x12 = None
        x13 = add(x10, x5)
        while contained(x13[ZERO], interval(ZERO, x11[ZERO], ONE)) and contained(x13[ONE], interval(ZERO, x11[ONE], ONE)):
            if contained(x13, x7):
                x12 = x13
                break
            x13 = add(x13, x5)
        if equality(x12, None):
            x14 = _tail_96a8c0cd(x10, x5, x11)
            x6 = combine(x6, connect(x10, x14))
            break
        x15 = x7[x12]
        x16 = subtract(x12, x5)
        x17 = _turn_96a8c0cd(x5, color(x15))
        if equality(x5[ZERO], ZERO):
            x18 = branch(equality(x17, UP), decrement(uppermost(x15)), increment(lowermost(x15)))
            x19 = astuple(x18, x16[ONE])
            x20 = branch(equality(x5, RIGHT), increment(rightmost(x15)), decrement(leftmost(x15)))
            x21 = astuple(x18, x20)
        else:
            x18 = branch(equality(x17, RIGHT), increment(rightmost(x15)), decrement(leftmost(x15)))
            x19 = astuple(x16[ZERO], x18)
            x20 = branch(equality(x5, DOWN), increment(lowermost(x15)), decrement(uppermost(x15)))
            x21 = astuple(x20, x18)
        x6 = combine(x6, connect(x10, x16))
        x6 = combine(x6, connect(x16, x19))
        x6 = combine(x6, connect(x19, x21))
        x10 = x21
    return fill(I, TWO, x6)
