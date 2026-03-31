from __future__ import annotations

from synth_rearc.core import *


INPUT_SIDE_BOUNDS_BF45CF4B = (12, 20)
TILE_SIDE_BOUNDS_BF45CF4B = (THREE, FIVE)
MARKER_SIDE_BOUNDS_BF45CF4B = (THREE, FIVE)
PLACEMENT_GAP_BF45CF4B = ONE


def _palette_without_bf45cf4b(
    blocked: tuple[Integer, ...],
) -> tuple[Integer, ...]:
    return tuple(x0 for x0 in interval(ZERO, TEN, ONE) if x0 not in blocked)


def _corners_patch_bf45cf4b(
    side: Integer,
) -> Indices:
    x0 = side - ONE
    return frozenset({(ZERO, ZERO), (ZERO, x0), (x0, ZERO), (x0, x0)})


def _inner_patch_bf45cf4b(
    side: Integer,
    inset: Integer,
) -> Indices:
    return frozenset(
        (i, j)
        for i in range(inset, side - inset)
        for j in range(inset, side - inset)
    )


def _middle_cross_patch_bf45cf4b(
    side: Integer,
) -> Indices:
    x0 = side // TWO
    x1 = frozenset((x0, j) for j in range(side))
    x2 = frozenset((i, x0) for i in range(side))
    return frozenset(x1 | x2)


def _cross_accent_patch_bf45cf4b(
    side: Integer,
) -> Indices:
    x0 = side // TWO
    if side < FIVE:
        return frozenset({(x0, x0)})
    return frozenset(
        {
            (x0 - ONE, x0 - ONE),
            (x0 - ONE, x0 + ONE),
            (x0 + ONE, x0 - ONE),
            (x0 + ONE, x0 + ONE),
        }
    )


def _build_corner_frame_tile_bf45cf4b(
    side: Integer,
    bg: Integer,
    color_a: Integer,
    color_b: Integer,
    color_c: Integer,
) -> Grid:
    x0 = canvas(color_b, (side, side))
    x1 = fill(x0, color_a, _corners_patch_bf45cf4b(side))
    x2 = fill(x1, color_c, _inner_patch_bf45cf4b(side, ONE))
    if not even(side):
        x3 = side // TWO
        x4 = choice((bg, color_c, color_c))
        x2 = fill(x2, x4, frozenset({(x3, x3)}))
    return x2


def _build_rings_tile_bf45cf4b(
    side: Integer,
    bg: Integer,
    color_a: Integer,
    color_b: Integer,
    color_c: Integer,
) -> Grid:
    x0 = canvas(color_a, (side, side))
    x1 = fill(x0, color_b, _inner_patch_bf45cf4b(side, ONE))
    if side == FIVE:
        x1 = fill(x1, color_c, _inner_patch_bf45cf4b(side, TWO))
    if side == FIVE and choice((T, F, F)):
        x2 = side // TWO
        x3 = choice((color_b, color_c, bg))
        x1 = fill(x1, x3, frozenset({(x2, x2)}))
    return x1


def _build_cross_tile_bf45cf4b(
    side: Integer,
    bg: Integer,
    color_a: Integer,
    color_b: Integer,
    color_c: Integer,
) -> Grid:
    x0 = canvas(color_a, (side, side))
    x1 = fill(x0, color_b, _middle_cross_patch_bf45cf4b(side))
    x2 = fill(x1, color_c, _cross_accent_patch_bf45cf4b(side))
    return x2


def sample_tile_bf45cf4b(
    diff_lb: float,
    diff_ub: float,
    bg: Integer,
) -> Grid:
    x0 = unifint(diff_lb, diff_ub, TILE_SIDE_BOUNDS_BF45CF4B)
    x1 = _palette_without_bf45cf4b((bg,))
    x2 = sample(x1, THREE)
    x3 = (_build_corner_frame_tile_bf45cf4b, _build_rings_tile_bf45cf4b)
    if not even(x0):
        x3 = x3 + (_build_cross_tile_bf45cf4b,)
    x4 = choice(x3)
    x5 = x4(x0, bg, x2[ZERO], x2[ONE], x2[TWO])
    return x5


def _neighbors_bf45cf4b(
    cell: IntegerTuple,
    dims: IntegerTuple,
) -> tuple[IntegerTuple, ...]:
    x0, x1 = cell
    x2, x3 = dims
    x4 = []
    for x5, x6 in ((NEG_ONE, ZERO), (ONE, ZERO), (ZERO, NEG_ONE), (ZERO, ONE)):
        x7 = x0 + x5
        x8 = x1 + x6
        if 0 <= x7 < x2 and 0 <= x8 < x3:
            x4.append((x7, x8))
    return tuple(x4)


def _connected_patch_bf45cf4b(
    cells: Indices,
    dims: IntegerTuple,
) -> Boolean:
    if len(cells) == ZERO:
        return F
    x0 = {next(iter(cells))}
    x1 = set()
    while x0:
        x2 = x0.pop()
        if x2 in x1:
            continue
        x1.add(x2)
        for x3 in _neighbors_bf45cf4b(x2, dims):
            if x3 in cells and x3 not in x1:
                x0.add(x3)
    return len(x1) == len(cells)


def _covers_bbox_bf45cf4b(
    cells: Indices,
    dims: IntegerTuple,
) -> Boolean:
    x0, x1 = dims
    x2 = {i for i, _ in cells}
    x3 = {j for _, j in cells}
    return both(len(x2) == x0, len(x3) == x1)


def sample_marker_patch_bf45cf4b(
    diff_lb: float,
    diff_ub: float,
    dims: IntegerTuple,
) -> Indices | None:
    x0, x1 = dims
    x2 = x0 * x1
    x3 = max(x0 + x1 - ONE, (x2 + ONE) // TWO)
    x4 = x2 - ONE
    if x3 > x4:
        return None
    x5 = unifint(diff_lb, diff_ub, (x3, x4))
    x6 = [(i, j) for i in range(x0) for j in range(x1)]
    for _ in range(96):
        x7 = set(x6)
        x8 = list(x6)
        shuffle(x8)
        x9 = T
        while len(x7) > x5 and x9:
            x9 = F
            x10 = list(x7)
            shuffle(x10)
            for x11 in x10:
                x12 = frozenset(x7 - {x11})
                if not _covers_bbox_bf45cf4b(x12, dims):
                    continue
                if not _connected_patch_bf45cf4b(x12, dims):
                    continue
                x7.remove(x11)
                x9 = T
                if len(x7) == x5:
                    break
        x13 = frozenset(x7)
        if len(x13) != x5:
            continue
        if not _covers_bbox_bf45cf4b(x13, dims):
            continue
        if not _connected_patch_bf45cf4b(x13, dims):
            continue
        if choice((T, T, T, F)):
            return x13
        x14 = list(x13)
        shuffle(x14)
        for x15 in x14:
            x16 = frozenset(x13 - {x15})
            if len(x16) < x3:
                continue
            if not _covers_bbox_bf45cf4b(x16, dims):
                continue
            if _connected_patch_bf45cf4b(x16, dims):
                continue
            return x16
        return x13
    return None


def render_output_bf45cf4b(
    tile: Grid,
    marker_patch: Indices,
    bg: Integer,
) -> Grid:
    x0 = shape(tile)
    x1 = shape(marker_patch)
    x2 = multiply(x1, x0)
    x3 = canvas(bg, x2)
    x4 = lbind(multiply, x0)
    x5 = apply(x4, marker_patch)
    x6 = asobject(tile)
    x7 = lbind(shift, x6)
    x8 = mapply(x7, x5)
    x9 = paint(x3, x8)
    return x9


def _rectangles_separated_bf45cf4b(
    loc_a: IntegerTuple,
    dims_a: IntegerTuple,
    loc_b: IntegerTuple,
    dims_b: IntegerTuple,
    gap: Integer = PLACEMENT_GAP_BF45CF4B,
) -> Boolean:
    x0, x1 = loc_a
    x2, x3 = dims_a
    x4, x5 = loc_b
    x6, x7 = dims_b
    x8 = x0 + x2 + gap <= x4
    x9 = x4 + x6 + gap <= x0
    x10 = x1 + x3 + gap <= x5
    x11 = x5 + x7 + gap <= x1
    return x8 or x9 or x10 or x11


def sample_layout_bf45cf4b(
    diff_lb: float,
    diff_ub: float,
    tile_dims: IntegerTuple,
    marker_dims: IntegerTuple,
) -> tuple[IntegerTuple, IntegerTuple, IntegerTuple] | None:
    x0 = max(maximum(tile_dims), maximum(marker_dims))
    x1 = max(INPUT_SIDE_BOUNDS_BF45CF4B[ZERO], x0 + SIX)
    x2 = INPUT_SIDE_BOUNDS_BF45CF4B[ONE]
    for _ in range(128):
        x3 = unifint(diff_lb, diff_ub, (x1, x2))
        x4 = unifint(diff_lb, diff_ub, (x1, x2))
        x5, x6 = tile_dims
        x7, x8 = marker_dims
        for _ in range(128):
            x9 = (randint(ZERO, x3 - x5), randint(ZERO, x4 - x6))
            x10 = (randint(ZERO, x3 - x7), randint(ZERO, x4 - x8))
            if _rectangles_separated_bf45cf4b(x9, tile_dims, x10, marker_dims):
                return (x3, x4), x9, x10
    return None


def compose_input_bf45cf4b(
    dims: IntegerTuple,
    bg: Integer,
    tile: Grid,
    tile_loc: IntegerTuple,
    marker_patch: Indices,
    marker_color: Integer,
    marker_loc: IntegerTuple,
) -> Grid:
    x0 = canvas(bg, dims)
    x1 = shift(asobject(tile), tile_loc)
    x2 = fill(x0, marker_color, shift(marker_patch, marker_loc))
    x3 = paint(x2, x1)
    return x3
