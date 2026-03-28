from synth_rearc.core import *


def _expand_row_b0f4d537(
    x0: tuple[Integer, ...],
    x1: tuple[Integer, ...],
    x2: Integer,
) -> tuple[Integer, ...]:
    x3 = (NEG_ONE,) + x1 + (x2,)
    x4 = tuple(subtract(subtract(x3[x5 + ONE], x3[x5]), ONE) for x5 in range(len(x3) - ONE))
    x5 = tuple()
    for x6, x7 in enumerate(x0):
        if even(x6):
            x5 = x5 + repeat(x7, x4[x6 // TWO])
        else:
            x5 = x5 + (x7,)
    return x5


def _active_rows_b0f4d537(
    x0: Grid,
) -> tuple[tuple[Integer, ...], ...]:
    x1 = tuple(first(x2) for x2 in vsplit(x0, height(x0)))
    return tuple(x2 for x2 in x1 if any(x3 != FIVE for x3 in x2))


def _marker_columns_b0f4d537(
    x0: Grid,
) -> tuple[Integer, ...]:
    x1 = tuple(first(x2) for x2 in vsplit(x0, height(x0)))
    x2 = tuple(x3 for x3 in x1 if contained(FOUR, x3))
    x3 = min(x2, key=lambda x4: x4.count(FOUR))
    return tuple(x4 for x4, x5 in enumerate(x3) if x5 == FOUR)


def _special_positions_b0f4d537(
    x0: Grid,
) -> tuple[Integer, ...]:
    x1 = tuple(first(x2) for x2 in vsplit(x0, height(x0)))
    return tuple(x2 for x2, x3 in enumerate(x1) if x3[ZERO] == FOUR and x3[NEG_ONE] == FOUR)


def verify_b0f4d537(I: Grid) -> Grid:
    x0 = frontiers(I)
    x1 = colorfilter(x0, FIVE)
    x2 = extract(x1, vline)
    x3 = leftmost(x2)
    x4 = height(I)
    x5 = width(I)
    x6 = crop(I, ORIGIN, astuple(x4, x3))
    x7 = increment(x3)
    x8 = crop(I, astuple(ZERO, x7), astuple(x4, subtract(x5, x7)))
    x9 = contained(FOUR, palette(x6))
    x10 = branch(x9, x6, x8)
    x11 = branch(x9, x8, x6)
    x12 = _marker_columns_b0f4d537(x10)
    x13 = _active_rows_b0f4d537(x11)
    x14 = mostcommon(x13)
    x15 = tuple(x16 for x16 in x13 if x16 != x14)
    x16 = _special_positions_b0f4d537(x10)
    x17 = width(x10)
    x18 = _expand_row_b0f4d537(x14, x12, x17)
    x19 = tuple(_expand_row_b0f4d537(x20, x12, x17) for x20 in x15)
    x20 = {x21: x22 for x21, x22 in zip(x16, x19)}
    x21 = tuple(x20.get(x22, x18) for x22 in range(x4))
    return x21
