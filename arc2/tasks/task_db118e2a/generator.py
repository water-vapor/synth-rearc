from __future__ import annotations

from arc2.core import *


COLORS_DB118E2A = remove(SEVEN, interval(ONE, TEN, ONE))
INNER_HEIGHT_BOUNDS_DB118E2A = (FOUR, SEVEN)
INNER_WIDTH_BOUNDS_DB118E2A = (THREE, SEVEN)


def _sample_full_bbox_cells_db118e2a(
    diff_lb: float,
    diff_ub: float,
) -> Indices:
    x0 = canvas(ZERO, THREE_BY_THREE)
    x1 = totuple(asindices(x0))
    x2 = unifint(diff_lb, diff_ub, (TWO, SIX))
    for _ in range(120):
        x3 = frozenset(sample(x1, x2))
        x4 = frozenset(i for i, _ in x3)
        x5 = frozenset(j for _, j in x3)
        x6 = equality(minimum(x4), ZERO)
        x7 = equality(maximum(x4), TWO)
        x8 = both(x6, x7)
        x9 = equality(minimum(x5), ZERO)
        x10 = equality(maximum(x5), TWO)
        x11 = both(x9, x10)
        if both(x8, x11):
            return x3
    return frozenset({ORIGIN, TWO_BY_TWO})


def _sample_palette_db118e2a(
    diff_lb: float,
    diff_ub: float,
    frame_color: Integer,
    count: Integer,
) -> tuple[Integer, ...]:
    x0 = min(THREE, count)
    x1 = unifint(diff_lb, diff_ub, (ONE, x0))
    x2 = remove(frame_color, COLORS_DB118E2A)
    if equality(count, ONE):
        x3 = choice((T, T, F))
        if x3:
            return (frame_color,)
        return (choice(x2),)
    x4 = choice((T, F))
    if x4:
        x5 = sample(x2, x1 - ONE)
        return (frame_color,) + tuple(x5)
    return tuple(sample(x2, x1))


def _colorize_cells_db118e2a(
    cells: Indices,
    palette_values: tuple[Integer, ...],
) -> Object:
    x0 = tuple(cells)
    x1 = list(palette_values)
    while len(x1) < len(x0):
        x1.append(choice(palette_values))
    shuffle(x1)
    return frozenset((value, loc) for value, loc in zip(x1, x0))


def _sample_motif_db118e2a(
    diff_lb: float,
    diff_ub: float,
    frame_color: Integer,
) -> Grid:
    x0 = choice((T, F, F, F))
    x1 = initset(UNITY) if x0 else _sample_full_bbox_cells_db118e2a(diff_lb, diff_ub)
    x2 = _sample_palette_db118e2a(diff_lb, diff_ub, frame_color, len(x1))
    x3 = _colorize_cells_db118e2a(x1, x2)
    x4 = canvas(SEVEN, THREE_BY_THREE)
    x5 = paint(x4, x3)
    return x5


def _wrap_tile_db118e2a(
    motif: Grid,
    frame_color: Integer,
) -> Grid:
    x0 = astuple(FIVE, FIVE)
    x1 = canvas(SEVEN, x0)
    x2 = asindices(x1)
    x3 = box(x2)
    x4 = corners(x2)
    x5 = difference(x3, x4)
    x6 = fill(x1, frame_color, x5)
    x7 = shift(asobject(motif), UNITY)
    x8 = paint(x6, x7)
    return x8


def _build_input_db118e2a(
    inner: Grid,
    frame_color: Integer,
) -> Grid:
    x0 = shape(inner)
    x1 = add(x0, TWO_BY_TWO)
    x2 = canvas(frame_color, x1)
    x3 = shift(asindices(inner), UNITY)
    x4 = fill(x2, SEVEN, x3)
    x5 = shift(asobject(inner), UNITY)
    x6 = paint(x4, x5)
    x7 = asindices(x6)
    x8 = corners(x7)
    x9 = fill(x6, SEVEN, x8)
    return x9


def _build_output_db118e2a(tile: Grid) -> Grid:
    x0 = multiply(THREE, FIVE)
    x1 = astuple(x0, x0)
    x2 = canvas(SEVEN, x1)
    x3 = asobject(tile)
    x4 = shift(x3, TWO_BY_TWO)
    x5 = paint(x2, x4)
    x6 = astuple(EIGHT, EIGHT)
    x7 = shift(x3, x6)
    x8 = paint(x5, x7)
    return x8


def generate_db118e2a(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    x0 = choice(COLORS_DB118E2A)
    x1 = _sample_motif_db118e2a(diff_lb, diff_ub, x0)
    x2 = unifint(diff_lb, diff_ub, INNER_HEIGHT_BOUNDS_DB118E2A)
    x3 = unifint(diff_lb, diff_ub, INNER_WIDTH_BOUNDS_DB118E2A)
    x4 = astuple(x2, x3)
    x5 = canvas(SEVEN, x4)
    x6 = choice(interval(ZERO, x2 - TWO, ONE))
    x7 = choice(interval(ZERO, x3 - TWO, ONE))
    x8 = astuple(x6, x7)
    x9 = shift(asobject(x1), x8)
    x10 = paint(x5, x9)
    x11 = _build_input_db118e2a(x10, x0)
    x12 = _wrap_tile_db118e2a(x1, x0)
    x13 = _build_output_db118e2a(x12)
    return {"input": x11, "output": x13}
