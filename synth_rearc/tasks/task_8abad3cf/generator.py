from synth_rearc.core import *


PRIMARY_8ABAD3CF = ONE
SECONDARY_8ABAD3CF = TWO
MARKER_8ABAD3CF = THREE
NON_BG_COLORS_8ABAD3CF = tuple(color for color in range(TEN) if color != SEVEN)

TEMPLATE_A_8ABAD3CF = (
    (PRIMARY_8ABAD3CF, PRIMARY_8ABAD3CF, PRIMARY_8ABAD3CF, PRIMARY_8ABAD3CF, PRIMARY_8ABAD3CF, SEVEN, SEVEN),
    (PRIMARY_8ABAD3CF, SEVEN, SEVEN, SEVEN, PRIMARY_8ABAD3CF, SEVEN, SECONDARY_8ABAD3CF),
    (PRIMARY_8ABAD3CF, SEVEN, MARKER_8ABAD3CF, SEVEN, PRIMARY_8ABAD3CF, SEVEN, SECONDARY_8ABAD3CF),
    (PRIMARY_8ABAD3CF, SEVEN, SEVEN, SEVEN, PRIMARY_8ABAD3CF, SEVEN, SEVEN),
    (PRIMARY_8ABAD3CF, PRIMARY_8ABAD3CF, PRIMARY_8ABAD3CF, PRIMARY_8ABAD3CF, PRIMARY_8ABAD3CF, SEVEN, SECONDARY_8ABAD3CF),
    (SEVEN, SEVEN, SEVEN, SEVEN, SEVEN, SEVEN, SECONDARY_8ABAD3CF),
    (SECONDARY_8ABAD3CF, SECONDARY_8ABAD3CF, SECONDARY_8ABAD3CF, SECONDARY_8ABAD3CF, SECONDARY_8ABAD3CF, SEVEN, SEVEN),
)

TEMPLATE_B_8ABAD3CF = (
    (PRIMARY_8ABAD3CF, PRIMARY_8ABAD3CF, PRIMARY_8ABAD3CF, PRIMARY_8ABAD3CF),
    (SEVEN, SEVEN, PRIMARY_8ABAD3CF, SEVEN),
    (PRIMARY_8ABAD3CF, PRIMARY_8ABAD3CF, PRIMARY_8ABAD3CF, PRIMARY_8ABAD3CF),
    (SEVEN, SEVEN, SEVEN, SEVEN),
    (SEVEN, SECONDARY_8ABAD3CF, SEVEN, SECONDARY_8ABAD3CF),
    (SEVEN, SECONDARY_8ABAD3CF, SEVEN, SECONDARY_8ABAD3CF),
    (SEVEN, SEVEN, SEVEN, SEVEN),
)

TEMPLATE_C_8ABAD3CF = (
    (SEVEN, SEVEN, SEVEN, PRIMARY_8ABAD3CF, PRIMARY_8ABAD3CF, PRIMARY_8ABAD3CF, SEVEN, SEVEN, SEVEN, SECONDARY_8ABAD3CF),
    (PRIMARY_8ABAD3CF, PRIMARY_8ABAD3CF, SEVEN, PRIMARY_8ABAD3CF, SEVEN, PRIMARY_8ABAD3CF, SEVEN, MARKER_8ABAD3CF, SEVEN, SECONDARY_8ABAD3CF),
    (PRIMARY_8ABAD3CF, PRIMARY_8ABAD3CF, SEVEN, PRIMARY_8ABAD3CF, PRIMARY_8ABAD3CF, PRIMARY_8ABAD3CF, SEVEN, SEVEN, SEVEN, SECONDARY_8ABAD3CF),
    (SEVEN, SEVEN, SEVEN, SEVEN, SEVEN, SEVEN, SEVEN, PRIMARY_8ABAD3CF, SEVEN, SECONDARY_8ABAD3CF),
    (SEVEN, SEVEN, SEVEN, SEVEN, SEVEN, PRIMARY_8ABAD3CF, PRIMARY_8ABAD3CF, PRIMARY_8ABAD3CF, SEVEN, SEVEN),
)

TEMPLATE_SPECS_8ABAD3CF = (
    (TEMPLATE_A_8ABAD3CF, FOUR, THREE, T),
    (TEMPLATE_B_8ABAD3CF, THREE, TWO, F),
    (TEMPLATE_C_8ABAD3CF, FOUR, TWO, T),
)

GRID_TRANSFORMS_8ABAD3CF = (
    identity,
    hmirror,
    vmirror,
    rot180,
    rot90,
    rot270,
)


def _render_output_8abad3cf(
    primary_color: Integer,
    primary_side: Integer,
    secondary_color: Integer,
    secondary_side: Integer,
    marker_color: Integer | None,
) -> Grid:
    x0 = canvas(primary_color, (primary_side, primary_side))
    x1 = THREE if marker_color is not None else ONE
    x2 = canvas(SEVEN, (primary_side, secondary_side + x1))
    x3 = interval(primary_side - secondary_side, primary_side, ONE)
    x4 = TWO if marker_color is not None else ZERO
    x5 = interval(x4, x4 + secondary_side, ONE)
    x6 = fill(x2, secondary_color, product(x3, x5))
    if marker_color is not None:
        x6 = fill(x6, marker_color, frozenset({(primary_side - ONE, ZERO)}))
    return hconcat(x6, x0)


def _sample_pads_8abad3cf(
    diff_lb: float,
    diff_ub: float,
) -> tuple[int, int]:
    x0 = unifint(diff_lb, diff_ub, (ZERO, TWO))
    x1 = unifint(diff_lb, diff_ub, (ZERO, TWO))
    if both(greater(x0, ZERO), greater(x1, ZERO)):
        if choice((T, F)):
            x0 = ZERO
        else:
            x1 = ZERO
    return x0, x1


def generate_8abad3cf(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    x0, x1, x2, x3 = choice(TEMPLATE_SPECS_8ABAD3CF)
    x4 = choice(GRID_TRANSFORMS_8ABAD3CF)(x0)
    x5 = sample(NON_BG_COLORS_8ABAD3CF, THREE if x3 else TWO)
    x6 = x5[ZERO]
    x7 = x5[ONE]
    x8 = x5[TWO] if x3 else None
    x9 = ofcolor(x4, PRIMARY_8ABAD3CF)
    x10 = ofcolor(x4, SECONDARY_8ABAD3CF)
    x11 = ofcolor(x4, MARKER_8ABAD3CF)
    x12, x13 = shape(x4)
    x14, x15 = _sample_pads_8abad3cf(diff_lb, diff_ub)
    x16, x17 = _sample_pads_8abad3cf(diff_lb, diff_ub)
    x18 = canvas(SEVEN, (x12 + x14 + x15, x13 + x16 + x17))
    x19 = astuple(x14, x16)
    x20 = fill(x18, x6, shift(x9, x19))
    x21 = fill(x20, x7, shift(x10, x19))
    if x3:
        x21 = fill(x21, x8, shift(x11, x19))
    x22 = _render_output_8abad3cf(x6, x1, x7, x2, x8)
    return {"input": x21, "output": x22}
