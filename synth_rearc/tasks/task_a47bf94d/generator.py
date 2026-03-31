from synth_rearc.core import *

from .helpers import maybe_rotate_example_a47bf94d
from .helpers import paint_block_a47bf94d
from .helpers import paint_diamond_a47bf94d
from .helpers import paint_x_a47bf94d
from .helpers import strip_payload_a47bf94d


GEN_HEIGHT_A47BF94D = 29
GEN_WIDTH_A47BF94D = 29
GEN_PORT_COLUMNS_A47BF94D = (THREE, TEN, 17, 24)
GEN_TOP_CENTER_ROW_A47BF94D = TWO
GEN_BOTTOM_CENTER_ROW_A47BF94D = 26
GEN_TOP_ENDPOINT_ROW_A47BF94D = FOUR
GEN_BOTTOM_ENDPOINT_ROW_A47BF94D = 24
GEN_TOP_BANDS_A47BF94D = ((SIX, EIGHT), (SEVEN, NINE), (EIGHT, TEN), (NINE, 11))
GEN_BOTTOM_BANDS_A47BF94D = ((17, 19), (18, 20), (19, 21), (20, 22))
GEN_SHIFTS_A47BF94D = (-TWO, -ONE, ONE, TWO)


def _paint_segment_a47bf94d(
    grid: Grid,
    a: IntegerTuple,
    b: IntegerTuple,
    color_value: Integer = EIGHT,
) -> Grid:
    return fill(grid, color_value, connect(a, b))


def _maybe_tunnel_vertical_a47bf94d(
    grid: Grid,
    col_value: Integer,
    row_start: Integer,
    row_end: Integer,
) -> Grid:
    return _paint_segment_a47bf94d(grid, (row_start, col_value), (row_end, col_value))


def _render_structure_a47bf94d() -> tuple[Grid, tuple[tuple[IntegerTuple, IntegerTuple], ...]]:
    x0 = canvas(ZERO, (GEN_HEIGHT_A47BF94D, GEN_WIDTH_A47BF94D))
    x1 = []
    for x2, x3 in enumerate(GEN_PORT_COLUMNS_A47BF94D):
        x4 = choice(tuple(j for j in (x3 + s for s in GEN_SHIFTS_A47BF94D) if ZERO < j < GEN_WIDTH_A47BF94D - ONE))
        x5 = choice(tuple(j for j in (x3 + s for s in GEN_SHIFTS_A47BF94D) if ZERO < j < GEN_WIDTH_A47BF94D - ONE))
        x6 = randint(*GEN_TOP_BANDS_A47BF94D[x2])
        x7 = randint(x6 + TWO, x6 + FOUR)
        x8 = randint(*GEN_BOTTOM_BANDS_A47BF94D[x2])
        x9 = min(x8 + TWO, GEN_BOTTOM_ENDPOINT_ROW_A47BF94D - ONE)
        x0 = _paint_segment_a47bf94d(x0, (GEN_TOP_ENDPOINT_ROW_A47BF94D, x3), (x6, x3))
        x0 = _paint_segment_a47bf94d(x0, (x6, x3), (x6, x4))
        x0 = _maybe_tunnel_vertical_a47bf94d(x0, x4, x6, x7)
        x0 = _paint_segment_a47bf94d(x0, (x7, x4), (x7, x5))
        x0 = _maybe_tunnel_vertical_a47bf94d(x0, x5, x7, x8)
        x0 = _paint_segment_a47bf94d(x0, (x8, x5), (x8, x3))
        x0 = _paint_segment_a47bf94d(x0, (x8, x3), (GEN_BOTTOM_ENDPOINT_ROW_A47BF94D, x3))
        x1.append(((GEN_TOP_CENTER_ROW_A47BF94D, x3), (GEN_BOTTOM_CENTER_ROW_A47BF94D, x3)))
    return x0, tuple(x1)


def _paint_input_payloads_a47bf94d(
    grid: Grid,
    pair_centers: tuple[tuple[IntegerTuple, IntegerTuple], ...],
    colors: tuple[Integer, Integer, Integer, Integer],
) -> Grid:
    x0 = grid
    x1 = []
    for _ in range(FOUR):
        x2 = choice(
            (
                ("block", None),
                ("block", None),
                ("block", "x"),
                (None, "x"),
                ("x", "x"),
            )
        )
        x1.append(x2)
    if not any("block" in x2 for x2 in x1):
        x3 = randint(ZERO, THREE)
        x4 = x1[x3]
        x1[x3] = ("block", x4[ONE])
    for x5, x6 in enumerate(pair_centers):
        x7 = colors[x5]
        x8, x9 = x6
        x10, x11 = x1[x5]
        if x10 == "block":
            x0 = paint_block_a47bf94d(x0, x7, x8)
        elif x10 == "x":
            x0 = paint_diamond_a47bf94d(x0, x7, x8)
        if x11 == "x":
            x0 = paint_x_a47bf94d(x0, x7, x9)
    return x0


def _paint_output_payloads_a47bf94d(
    grid: Grid,
    pair_centers: tuple[tuple[IntegerTuple, IntegerTuple], ...],
    colors: tuple[Integer, Integer, Integer, Integer],
) -> Grid:
    x0 = strip_payload_a47bf94d(grid)
    for x1, x2 in enumerate(pair_centers):
        x3 = colors[x1]
        x4, x5 = x2
        x0 = paint_diamond_a47bf94d(x0, x3, x4)
        x0 = paint_x_a47bf94d(x0, x3, x5)
    return x0


def generate_a47bf94d(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0, x1 = _render_structure_a47bf94d()
        x2 = tuple(sample((ONE, TWO, THREE, FOUR, SIX, SEVEN), FOUR))
        x3 = _paint_input_payloads_a47bf94d(x0, x1, x2)
        x4 = _paint_output_payloads_a47bf94d(x3, x1, x2)
        if x3 == x4:
            continue
        x5, x6 = maybe_rotate_example_a47bf94d(x3, x4)
        if x5 == x6:
            continue
        return {"input": x5, "output": x6}
