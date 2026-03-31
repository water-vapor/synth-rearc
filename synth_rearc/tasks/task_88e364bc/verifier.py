from synth_rearc.core import *


def _reference_specs_88e364bc(
    I: Grid,
) -> tuple[tuple[Integer, IntegerTuple], ...]:
    x0 = objects(I, F, F, T)
    x1 = []
    for x2 in x0:
        x3 = palette(x2)
        if TWO not in x3:
            continue
        x4 = tuple(v for v, _ in x2 if v != TWO)
        x5 = mostcommon(x4)
        x6 = tuple(v for v in x4 if v != x5)
        if len(x6) == ZERO:
            continue
        x7 = mostcommon(x6)
        x8 = frozenset(loc for v, loc in x2 if v == TWO)
        x9 = frozenset(loc for v, loc in x2 if v == x7)
        x10 = []
        for x11 in x8:
            for x12 in neighbors(x11):
                if x12 in x9:
                    x10.append(subtract(x11, x12))
        if len(x10) == ZERO:
            continue
        x13 = mostcommon(tuple(x10))
        x1.append((x5, x13))
    return tuple(x1)


def _slide_88e364bc(
    I: Grid,
    start: IntegerTuple,
    value: Integer,
    direction: IntegerTuple,
) -> IntegerTuple | None:
    x0 = start
    x1 = direction if ZERO in direction else (ZERO, ONE if direction[ONE] > ZERO else NEG_ONE)
    while True:
        x2 = add(x0, x1)
        x3 = index(I, x2)
        if x3 == value:
            return x0
        x4 = add(x0, direction)
        x5 = index(I, x4)
        if x5 == ZERO:
            x0 = x4
            continue
        return None


def verify_88e364bc(
    I: Grid,
) -> Grid:
    x0 = ofcolor(I, FOUR)
    x1 = _reference_specs_88e364bc(I)
    x2 = []
    for x3 in x0:
        x4 = x3
        for x5, x6 in x1:
            x7 = _slide_88e364bc(I, x3, x5, x6)
            if x7 is not None:
                x4 = x7
                break
        x2.append(x4)
    x8 = fill(I, ZERO, x0)
    x9 = fill(x8, FOUR, frozenset(x2))
    return x9
