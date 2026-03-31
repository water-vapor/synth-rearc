from synth_rearc.core import *


PATTERN_4_DFADAB01 = box(frozenset({(ZERO, ZERO), (THREE, THREE)}))
PATTERN_1_DFADAB01 = frozenset(
    {
        (ZERO, ONE),
        (ZERO, TWO),
        (ONE, ZERO),
        (ONE, THREE),
        (TWO, ZERO),
        (TWO, THREE),
        (THREE, ONE),
        (THREE, TWO),
    }
)
PATTERN_6_DFADAB01 = frozenset(
    {
        (ZERO, ZERO),
        (ZERO, ONE),
        (ONE, ZERO),
        (ONE, ONE),
        (TWO, TWO),
        (TWO, THREE),
        (THREE, TWO),
        (THREE, THREE),
    }
)
PATTERN_7_DFADAB01 = frozenset(
    {
        (ZERO, ZERO),
        (ZERO, THREE),
        (ONE, ONE),
        (ONE, TWO),
        (TWO, ONE),
        (TWO, TWO),
        (THREE, ZERO),
        (THREE, THREE),
    }
)
LABEL_OFFSET_DFADAB01 = (FOUR, FOUR)
MARKER_SPECS_DFADAB01 = (
    (TWO, FOUR, PATTERN_4_DFADAB01),
    (THREE, ONE, PATTERN_1_DFADAB01),
    (FIVE, SIX, PATTERN_6_DFADAB01),
    (EIGHT, SEVEN, PATTERN_7_DFADAB01),
)


def visible_markers_dfadab01(
    I: Grid,
    marker_color: Integer,
    output_color: Integer,
    pattern: Indices,
) -> Indices:
    x0 = ofcolor(I, marker_color)
    x1 = recolor(output_color, pattern)
    x2 = occurrences(I, x1)
    x3 = shift(x2, LABEL_OFFSET_DFADAB01)
    x4 = difference(x0, x3)
    return x4


def assemble_output_dfadab01(
    I: Grid,
) -> Grid:
    x0 = canvas(ZERO, shape(I))
    for x1, x2, x3 in MARKER_SPECS_DFADAB01:
        x4 = visible_markers_dfadab01(I, x1, x2, x3)
        x5 = mapply(lbind(shift, x3), x4)
        x0 = fill(x0, x2, x5)
    return x0
