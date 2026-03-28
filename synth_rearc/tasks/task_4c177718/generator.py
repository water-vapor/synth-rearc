from synth_rearc.core import *


INPUT_SHAPE_4C177718 = (15, 15)
OUTPUT_SHAPE_4C177718 = (9, 15)
FRAME_SHAPE_4C177718 = (3, 3)
TOP_LEFT_ANCHOR_4C177718 = (1, 2)
TOP_MIDDLE_ANCHOR_4C177718 = (1, 6)
TOP_RIGHT_ANCHOR_4C177718 = (1, 10)
BOTTOM_OFFSET_4C177718 = (6, 0)
DIVIDER_4C177718 = frozenset((5, j) for j in range(15))
FRAME_CELLS_4C177718 = totuple(asindices(canvas(ZERO, FRAME_SHAPE_4C177718)))
THIRD_COLOR_POOL_4C177718 = remove(
    FIVE,
    remove(TWO, remove(ONE, remove(ZERO, interval(ZERO, TEN, ONE)))),
)
TOP_HEAVY_CONNECTOR_4C177718 = frozenset({
    (0, 0),
    (0, 1),
    (0, 2),
    (1, 1),
    (2, 1),
})
BOTTOM_HEAVY_CONNECTOR_4C177718 = vmirror(hmirror(TOP_HEAVY_CONNECTOR_4C177718))


def _covers_frame_4c177718(x0: Patch) -> bool:
    x1 = frozenset(i for i, _ in x0)
    x2 = frozenset(j for _, j in x0)
    return x1 == frozenset((0, 1, 2)) and x2 == frozenset((0, 1, 2))


def _sample_motif_4c177718(
    diff_lb: float,
    diff_ub: float,
) -> Patch:
    while True:
        x0 = unifint(diff_lb, diff_ub, (4, 8))
        x1 = frozenset(sample(FRAME_CELLS_4C177718, x0))
        if _covers_frame_4c177718(x1):
            return x1


def generate_4c177718(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = _sample_motif_4c177718(diff_lb, diff_ub)
        x1 = _sample_motif_4c177718(diff_lb, diff_ub)
        x2 = choice((True, False))
        x3 = TOP_HEAVY_CONNECTOR_4C177718 if x2 else BOTTOM_HEAVY_CONNECTOR_4C177718
        if x0 == x1 or x0 == x3 or x1 == x3:
            continue
        x4 = choice(THIRD_COLOR_POOL_4C177718)
        x5 = choice((1, 3)) if x2 else choice((3, 5))
        x6 = unifint(diff_lb, diff_ub, (1, 8))
        x7 = x5
        x8 = astuple(x7, x6)
        x9 = add(BOTTOM_OFFSET_4C177718, x8)
        x10 = canvas(ZERO, INPUT_SHAPE_4C177718)
        x11 = fill(x10, FIVE, DIVIDER_4C177718)
        x12 = fill(x11, ONE, shift(x0, TOP_LEFT_ANCHOR_4C177718))
        x13 = fill(x12, TWO, shift(x3, TOP_MIDDLE_ANCHOR_4C177718))
        x14 = fill(x13, x4, shift(x1, TOP_RIGHT_ANCHOR_4C177718))
        x15 = fill(x14, ONE, shift(x0, x9))
        x16 = canvas(ZERO, OUTPUT_SHAPE_4C177718)
        x17 = fill(x16, ONE, shift(x0, x8))
        x18 = astuple(x5 + 3, x6) if x2 else astuple(x5 - 3, x6)
        x19 = fill(x17, x4, shift(x1, x18))
        return {"input": x15, "output": x19}
