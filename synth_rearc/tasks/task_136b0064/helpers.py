from synth_rearc.core import *


MOTIF_PATCHES_136b0064 = {
    ONE: frozenset({(ZERO, ZERO), (ZERO, ONE), (ONE, ZERO), (ONE, TWO), (TWO, ONE)}),
    TWO: frozenset({
        (ZERO, ZERO),
        (ZERO, TWO),
        (ONE, ZERO),
        (ONE, TWO),
        (TWO, ZERO),
        (TWO, ONE),
        (TWO, TWO),
    }),
    THREE: frozenset({(ZERO, ZERO), (ZERO, ONE), (ZERO, TWO), (ONE, ONE), (TWO, ZERO), (TWO, TWO)}),
    SIX: frozenset({(ZERO, ZERO), (ZERO, TWO), (ONE, ONE), (TWO, ONE)}),
}


def segment_patch_136b0064(
    start: IntegerTuple,
    value: Integer,
) -> Indices:
    if value == ONE:
        return connect(add(start, (ONE, ZERO)), add(start, (ONE, TWO)))
    if value == TWO:
        return connect(add(start, (ONE, NEG_ONE)), add(start, (ONE, ZERO)))
    if value == THREE:
        return connect(add(start, (ONE, invert(THREE))), add(start, (ONE, ZERO)))
    return connect(add(start, (ONE, ZERO)), add(start, (TWO, ZERO)))


def advance_cursor_136b0064(
    start: IntegerTuple,
    value: Integer,
) -> IntegerTuple:
    if value == ONE:
        return add(start, (ONE, TWO))
    if value == TWO:
        return add(start, (ONE, NEG_ONE))
    if value == THREE:
        return add(start, (ONE, invert(THREE)))
    return add(start, (TWO, ZERO))


def render_trace_136b0064(
    grid: Grid,
    start: IntegerTuple,
    values: tuple[int, ...],
) -> Grid:
    x0 = grid
    x1 = start
    for x2 in values:
        x3 = segment_patch_136b0064(x1, x2)
        x0 = fill(x0, x2, x3)
        x1 = advance_cursor_136b0064(x1, x2)
    return x0


def extract_sequence_136b0064(
    grid: Grid,
) -> tuple[int, ...]:
    x0 = height(grid)
    x1 = interval(ZERO, x0, FOUR)
    x2 = []
    for x3 in (ZERO, FOUR):
        for x4 in x1:
            x5 = crop(grid, (x4, x3), THREE_BY_THREE)
            x6 = remove(ZERO, palette(x5))
            x2.append(first(x6))
    return tuple(x2)


def motif_object_136b0064(
    value: Integer,
    origin: IntegerTuple,
) -> Object:
    x0 = shift(MOTIF_PATCHES_136b0064[value], origin)
    return recolor(value, x0)


def build_input_136b0064(
    values: tuple[int, ...],
    start_col: Integer,
) -> Grid:
    x0 = halve(len(values))
    x1 = subtract(multiply(FOUR, x0), ONE)
    x2 = canvas(ZERO, (x1, 15))
    x3 = fill(x2, FOUR, connect((ZERO, 7), (subtract(x1, ONE), 7)))
    x4 = fill(x3, FIVE, {(ZERO, add(start_col, EIGHT))})
    x5 = x4
    for x6, x7 in enumerate(values[:x0]):
        x8 = paint(x5, motif_object_136b0064(x7, (multiply(FOUR, x6), ZERO)))
        x5 = x8
    for x9, x10 in enumerate(values[x0:]):
        x11 = paint(x5, motif_object_136b0064(x10, (multiply(FOUR, x9), FOUR)))
        x5 = x11
    return x5
