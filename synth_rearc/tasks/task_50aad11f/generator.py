from synth_rearc.core import *

from .verifier import verify_50aad11f


SHAPE_SIDE_50AAD11F = FOUR
SHAPE_COUNT_RANGE_50AAD11F = (TWO, THREE)
SHAPE_SIZE_CHOICES_50AAD11F = (SEVEN, EIGHT, EIGHT, EIGHT, NINE, NINE, TEN)
H_GAP_RANGE_50AAD11F = (TWO, THREE)
V_GAP_RANGE_50AAD11F = (TWO, THREE)
H_ROW_RANGE_50AAD11F = (ONE, THREE)
V_COL_RANGE_50AAD11F = (ONE, THREE)
MARKER_OFFSET_50AAD11F = TWO
OUTER_MARGIN_RANGE_50AAD11F = (ONE, TWO)
MARKER_COLORS_50AAD11F = remove(SIX, interval(ONE, TEN, ONE))


def _neighbor_cells_50aad11f(cell: tuple[int, int]) -> tuple[tuple[int, int], ...]:
    x0, x1 = cell
    x2 = []
    for x3, x4 in ((ONE, ZERO), (NEG_ONE, ZERO), (ZERO, ONE), (ZERO, NEG_ONE)):
        x5 = x0 + x3
        x6 = x1 + x4
        if 0 <= x5 < SHAPE_SIDE_50AAD11F and 0 <= x6 < SHAPE_SIDE_50AAD11F:
            x2.append((x5, x6))
    return tuple(x2)


def _random_shape_50aad11f() -> frozenset[tuple[int, int]]:
    while True:
        x0 = choice(SHAPE_SIZE_CHOICES_50AAD11F)
        x1 = {(randint(ZERO, THREE), randint(ZERO, THREE))}
        while len(x1) < x0:
            x2 = tuple(
                x3
                for x4 in tuple(x1)
                for x3 in _neighbor_cells_50aad11f(x4)
                if x3 not in x1
            )
            x1.add(choice(x2))
        x5 = frozenset(x1)
        x6 = uppermost(x5)
        x7 = lowermost(x5)
        x8 = leftmost(x5)
        x9 = rightmost(x5)
        if x6 != ZERO or x7 != THREE or x8 != ZERO or x9 != THREE:
            continue
        return x5


def _make_piece_50aad11f(
    shape_patch: frozenset[tuple[int, int]],
    color_value: int,
) -> Grid:
    x0 = canvas(ZERO, (SHAPE_SIDE_50AAD11F, SHAPE_SIDE_50AAD11F))
    return fill(x0, color_value, shape_patch)


def _assemble_output_50aad11f(
    shape_patches: tuple[frozenset[tuple[int, int]], ...],
    color_values: tuple[int, ...],
    horizontal: bool,
) -> Grid:
    x0 = tuple(_make_piece_50aad11f(x1, x2) for x1, x2 in zip(shape_patches, color_values))
    x1 = first(x0)
    x2 = hconcat if horizontal else vconcat
    for x3 in x0[1:]:
        x1 = x2(x1, x3)
    return x1


def _build_horizontal_input_50aad11f(
    shape_patches: tuple[frozenset[tuple[int, int]], ...],
    color_values: tuple[int, ...],
    diff_lb: float,
    diff_ub: float,
) -> Grid:
    x0 = len(shape_patches)
    x1 = [unifint(diff_lb, diff_ub, H_ROW_RANGE_50AAD11F) for _ in range(x0)]
    x2 = [unifint(diff_lb, diff_ub, OUTER_MARGIN_RANGE_50AAD11F) for _ in range(TWO)]
    x3 = [unifint(diff_lb, diff_ub, OUTER_MARGIN_RANGE_50AAD11F) for _ in range(TWO)]
    x4 = []
    x5 = x2[0]
    for x6 in range(x0):
        x4.append(x5)
        x5 = add(x5, SHAPE_SIDE_50AAD11F)
        if x6 < x0 - ONE:
            x5 = add(x5, unifint(diff_lb, diff_ub, H_GAP_RANGE_50AAD11F))
    x7 = add(max(x1), add(SHAPE_SIDE_50AAD11F, add(MARKER_OFFSET_50AAD11F, x3[1])))
    x8 = add(x4[-1], add(SHAPE_SIDE_50AAD11F, x2[1]))
    x9 = canvas(ZERO, (x7, x8))
    for x10, x11, x12, x13 in zip(shape_patches, color_values, x1, x4):
        x14 = shift(x10, (x12, x13))
        x15 = add(add(x12, SHAPE_SIDE_50AAD11F), decrement(MARKER_OFFSET_50AAD11F))
        x16 = add(x13, randint(ZERO, THREE))
        x17 = frozenset({(x15, x16)})
        x9 = fill(x9, SIX, x14)
        x9 = fill(x9, x11, x17)
    return x9


def _build_vertical_input_50aad11f(
    shape_patches: tuple[frozenset[tuple[int, int]], ...],
    color_values: tuple[int, ...],
    diff_lb: float,
    diff_ub: float,
) -> Grid:
    x0 = len(shape_patches)
    x1 = [unifint(diff_lb, diff_ub, V_COL_RANGE_50AAD11F) for _ in range(x0)]
    x2 = [unifint(diff_lb, diff_ub, OUTER_MARGIN_RANGE_50AAD11F) for _ in range(TWO)]
    x3 = [unifint(diff_lb, diff_ub, OUTER_MARGIN_RANGE_50AAD11F) for _ in range(TWO)]
    x4 = []
    x5 = x2[0]
    for x6 in range(x0):
        x4.append(x5)
        x5 = add(x5, SHAPE_SIDE_50AAD11F)
        if x6 < x0 - ONE:
            x5 = add(x5, unifint(diff_lb, diff_ub, V_GAP_RANGE_50AAD11F))
    x7 = add(x4[-1], add(SHAPE_SIDE_50AAD11F, x2[1]))
    x8 = add(max(x1), add(SHAPE_SIDE_50AAD11F, add(MARKER_OFFSET_50AAD11F, x3[1])))
    x9 = canvas(ZERO, (x7, x8))
    for x10, x11, x12, x13 in zip(shape_patches, color_values, x4, x1):
        x14 = shift(x10, (x12, x13))
        x15 = add(x12, randint(ZERO, THREE))
        x16 = add(add(x13, SHAPE_SIDE_50AAD11F), decrement(MARKER_OFFSET_50AAD11F))
        x17 = frozenset({(x15, x16)})
        x9 = fill(x9, SIX, x14)
        x9 = fill(x9, x11, x17)
    return x9


def generate_50aad11f(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = unifint(diff_lb, diff_ub, SHAPE_COUNT_RANGE_50AAD11F)
        x1 = []
        x2 = set()
        while len(x1) < x0:
            x3 = _random_shape_50aad11f()
            if x3 in x2:
                continue
            x2.add(x3)
            x1.append(x3)
        x4 = tuple(x1)
        x5 = tuple(sample(MARKER_COLORS_50AAD11F, x0))
        x6 = choice((T, F))
        x7 = _assemble_output_50aad11f(x4, x5, x6)
        x8 = branch(
            x6,
            _build_horizontal_input_50aad11f,
            _build_vertical_input_50aad11f,
        )(x4, x5, diff_lb, diff_ub)
        if verify_50aad11f(x8) != x7:
            continue
        return {"input": x8, "output": x7}
