from arc2.core import *


BOX_SIZE_20981F0E = FOUR
CELL_STRIDE_20981F0E = FIVE
LAYOUTS_20981F0E = ((TWO, THREE), (THREE, TWO))
COLUMN_MODES_20981F0E = ("none", "right")
CENTER_OFFSET_20981F0E = (ONE, ONE)
INPUT_OFFSETS_20981F0E = (
    (TWO, ZERO),
    (TWO, ZERO),
    (TWO, ZERO),
    (TWO, ZERO),
    (TWO, ONE),
    (TWO, ONE),
    (TWO, ONE),
    (ONE, ONE),
    (ONE, ONE),
    (ONE, ONE),
    (ZERO, TWO),
    (ZERO, TWO),
    (ZERO, TWO),
    (ZERO, ZERO),
    (ZERO, ZERO),
    (ZERO, ONE),
    (ZERO, ONE),
    (ONE, ZERO),
    (ONE, ZERO),
)
OFF_CENTER_OFFSETS_20981F0E = (
    (TWO, ZERO),
    (TWO, ONE),
    (ZERO, TWO),
    (ZERO, ZERO),
    (ZERO, ONE),
    (ONE, ZERO),
)
SHAPES_20981F0E = (
    frozenset({(ZERO, ZERO), (ZERO, ONE), (ONE, ZERO), (ONE, ONE)}),
    frozenset({(ZERO, ZERO), (ONE, ZERO), (ONE, ONE)}),
    frozenset({(ZERO, ONE), (ONE, ZERO), (ONE, ONE)}),
    frozenset({(ZERO, ZERO), (ZERO, ONE), (ONE, ZERO)}),
    frozenset({(ZERO, ZERO), (ZERO, ONE), (ONE, ONE)}),
)


def _row_markers_20981f0e(diff_lb: float, diff_ub: float, nboxes: int) -> tuple[tuple[int, ...], int]:
    x0 = choice((ONE, TWO))
    x1 = choice((ZERO, TWO))
    x2 = tuple(x0 + CELL_STRIDE_20981F0E * x3 for x3 in range(nboxes + ONE))
    x3 = x2[-ONE] + x1 + ONE
    return x2, x3


def _column_markers_20981f0e(
    diff_lb: float,
    diff_ub: float,
    nboxes: int,
) -> tuple[tuple[int, ...], int]:
    x0 = choice(COLUMN_MODES_20981F0E)
    x1 = unifint(diff_lb, diff_ub, (ZERO, TWO))
    if x0 == "right":
        x2 = tuple(x1 + CELL_STRIDE_20981F0E * x3 for x3 in range(nboxes))
        x3 = x2[-ONE] + CELL_STRIDE_20981F0E
        return x2, x3
    x2 = unifint(diff_lb, diff_ub, (ZERO, TWO))
    x3 = tuple(x1 + CELL_STRIDE_20981F0E * x4 for x4 in range(nboxes + ONE))
    x4 = x3[-ONE] + x2 + ONE
    return x3, x4


def _active_spans_20981f0e(markers: tuple[int, ...], limit: int) -> tuple[tuple[int, int], ...]:
    x0 = (-ONE,) + markers + (limit,)
    return tuple((x1 + ONE, x2 - ONE) for x1, x2 in zip(x0, x0[ONE:]) if x2 - x1 == CELL_STRIDE_20981F0E)


def _marker_patch_20981f0e(rows: tuple[int, ...], cols: tuple[int, ...]) -> Indices:
    return frozenset((x0, x1) for x0 in rows for x1 in cols)


def generate_20981f0e(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    x0, x1 = choice(LAYOUTS_20981F0E)
    x2, x3 = _row_markers_20981f0e(diff_lb, diff_ub, x0)
    x4, x5 = _column_markers_20981f0e(diff_lb, diff_ub, x1)
    x6 = canvas(ZERO, (x3, x5))
    x7 = _marker_patch_20981f0e(x2, x4)
    x8 = fill(x6, TWO, x7)
    x9 = fill(x6, TWO, x7)
    x10 = _active_spans_20981f0e(x2, x3)
    x11 = _active_spans_20981f0e(x4, x5)
    x12 = [(x13, x14) for x13 in x10 for x14 in x11]
    x13 = [choice(INPUT_OFFSETS_20981F0E) for _ in x12]
    if all(x14 == CENTER_OFFSET_20981F0E for x14 in x13):
        x13[choice(tuple(range(len(x13))))] = choice(OFF_CENTER_OFFSETS_20981F0E)
    for (x14, x15), x16 in zip(x12, x13):
        x17 = choice(SHAPES_20981F0E)
        x18 = astuple(x14[ZERO], x15[ZERO])
        x19 = shift(x17, add(x18, x16))
        x20 = shift(x17, add(x18, CENTER_OFFSET_20981F0E))
        x8 = fill(x8, ONE, x19)
        x9 = fill(x9, ONE, x20)
    return {"input": x8, "output": x9}
