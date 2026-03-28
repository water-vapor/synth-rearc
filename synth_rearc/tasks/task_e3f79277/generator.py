from synth_rearc.core import *

from .verifier import verify_e3f79277


INPUT_SIZE_E3F79277 = 6
OUTPUT_SIZE_E3F79277 = 16
COLORS_E3F79277 = interval(ZERO, TEN, ONE)
CORNERS_E3F79277 = ("tl", "tr", "bl", "br")
LEG_LENGTHS_E3F79277 = (TWO, THREE, FOUR, FIVE, SIX)


def _triangle_points_e3f79277(
    corner: str,
    side: Integer,
    full_side: Integer,
) -> tuple[IntegerTuple, IntegerTuple, IntegerTuple]:
    top = ZERO if corner in ("tl", "tr") else full_side - side
    left = ZERO if corner in ("tl", "bl") else full_side - side
    bottom = top + side - ONE
    right = left + side - ONE
    if corner == "tl":
        return (top, left), (top, right), (bottom, left)
    if corner == "tr":
        return (top, right), (top, left), (bottom, right)
    if corner == "bl":
        return (bottom, left), (top, left), (bottom, right)
    return (bottom, right), (top, right), (bottom, left)


def _triangle_outline_e3f79277(
    anchor: IntegerTuple,
    edge_a: IntegerTuple,
    edge_b: IntegerTuple,
) -> Patch:
    x0 = connect(anchor, edge_a)
    x1 = connect(anchor, edge_b)
    x2 = connect(edge_a, edge_b)
    x3 = combine(x0, x1)
    return combine(x3, x2)


def generate_e3f79277(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = choice(CORNERS_E3F79277)
        x1 = choice(LEG_LENGTHS_E3F79277)
        x2, x3 = sample(COLORS_E3F79277, TWO)
        x4 = canvas(x2, (INPUT_SIZE_E3F79277, INPUT_SIZE_E3F79277))
        x5, x6, x7 = _triangle_points_e3f79277(x0, x1, INPUT_SIZE_E3F79277)
        x8 = combine(connect(x5, x6), connect(x5, x7))
        x9 = fill(x4, x3, x8)
        x10 = canvas(x2, (OUTPUT_SIZE_E3F79277, OUTPUT_SIZE_E3F79277))
        x11 = double(x1)
        x12, x13, x14 = _triangle_points_e3f79277(x0, x11, OUTPUT_SIZE_E3F79277)
        x15 = _triangle_outline_e3f79277(x12, x13, x14)
        x16 = fill(x10, x3, x15)
        if verify_e3f79277(x9) != x16:
            continue
        return {"input": x9, "output": x16}
