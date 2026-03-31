from __future__ import annotations

from synth_rearc.core import *


PIECE_KIND_POOL_5DBC8537 = (
    "mono",
    "mono",
    "mono",
    "mono",
    "checker",
    "checker",
    "stripe_h",
    "stripe_v",
    "center",
    "frame",
    "singleton",
)

MASK_SIDES_5DBC8537 = ("left", "right", "top", "bottom")


def _non_hole_count_5dbc8537(
    grid: Grid,
    hole_color: Integer,
) -> Integer:
    return sum(value != hole_color for row in grid for value in row)


def _layout_candidate_5dbc8537(
    mask: Grid,
    piece: Grid,
) -> tuple[Integer, Grid, Grid, Integer, Integer] | None:
    x0 = palette(mask)
    x1 = palette(piece)
    if len(x0) != TWO or len(x1) <= TWO:
        return None
    x2 = intersection(x0, x1)
    if len(x2) != ONE:
        return None
    x3 = first(x2)
    if mostcolor(piece) != x3:
        return None
    x4 = other(x0, x3)
    x5 = colorcount(mask, x3)
    x6 = _non_hole_count_5dbc8537(piece, x3)
    if x5 != x6:
        return None
    x7 = multiply(height(mask), width(mask))
    return (x7, mask, piece, x3, x4)


def detect_layout_5dbc8537(
    grid: Grid,
) -> tuple[Grid, Grid, Integer, Integer]:
    x0 = []
    x1 = height(grid)
    x2 = width(grid)
    for x3 in range(ONE, x2):
        x4 = crop(grid, ORIGIN, (x1, x3))
        x5 = crop(grid, (ZERO, x3), (x1, subtract(x2, x3)))
        x6 = _layout_candidate_5dbc8537(x4, x5)
        if x6 is not None:
            x0.append(x6)
        x7 = _layout_candidate_5dbc8537(x5, x4)
        if x7 is not None:
            x0.append(x7)
    for x8 in range(ONE, x1):
        x9 = crop(grid, ORIGIN, (x8, x2))
        x10 = crop(grid, (x8, ZERO), (subtract(x1, x8), x2))
        x11 = _layout_candidate_5dbc8537(x9, x10)
        if x11 is not None:
            x0.append(x11)
        x12 = _layout_candidate_5dbc8537(x10, x9)
        if x12 is not None:
            x0.append(x12)
    if len(x0) == ZERO:
        raise ValueError("could not detect a valid mask/piece split")
    x13 = max(x0, key=lambda x14: x14[0])
    return x13[1], x13[2], x13[3], x13[4]


def piece_objects_5dbc8537(
    piece_grid: Grid,
) -> tuple[Object, ...]:
    x0 = objects(piece_grid, F, F, T)
    return tuple(sorted(x0, key=ulcorner))


def _placement_positions_5dbc8537(
    remaining: frozenset[IntegerTuple],
    obj: Object,
) -> tuple[IntegerTuple, ...]:
    x0 = normalize(obj)
    x1 = []
    for x2 in remaining:
        x3 = shift(x0, x2)
        if toindices(x3).issubset(remaining):
            x1.append(ulcorner(x3))
    return tuple(sorted(set(x1)))


def pack_objects_5dbc8537(
    hole_patch: Patch,
    objs: tuple[Object, ...],
    dims: IntegerTuple,
    background_color: Integer,
) -> Grid | None:
    x0 = frozenset(toindices(hole_patch))
    x1 = canvas(background_color, dims)
    x2 = list(objs)
    while len(x2) > ZERO:
        x3 = []
        for x4, x5 in enumerate(x2):
            x6 = _placement_positions_5dbc8537(x0, x5)
            x3.append((len(x6), x4, x6, x5))
        x3.sort(key=lambda x7: (x7[0], x7[1]))
        x8, x9, x10, x11 = first(x3)
        if x8 == ZERO:
            return None
        x12 = shift(normalize(x11), first(x10))
        x1 = paint(x1, x12)
        x0 = difference(x0, toindices(x12))
        x2.pop(x9)
    if len(x0) != ZERO:
        return None
    return x1


def render_output_5dbc8537(
    mask_grid: Grid,
    piece_grid: Grid,
    hole_color: Integer,
    background_color: Integer,
) -> Grid:
    x0 = ofcolor(mask_grid, hole_color)
    x1 = piece_objects_5dbc8537(piece_grid)
    x2 = pack_objects_5dbc8537(x0, x1, shape(mask_grid), background_color)
    if x2 is None:
        raise ValueError("inventory pieces do not pack into the detected hole region")
    return x2


def _rect_patch_5dbc8537(
    dims: IntegerTuple,
) -> Indices:
    x0, x1 = dims
    return frozenset((i, j) for i in range(x0) for j in range(x1))


def _frame_cells_5dbc8537(
    dims: IntegerTuple,
) -> Indices:
    x0, x1 = dims
    return frozenset(
        (i, j)
        for i in range(x0)
        for j in range(x1)
        if i in (ZERO, subtract(x0, ONE)) or j in (ZERO, subtract(x1, ONE))
    )


def _build_piece_object_5dbc8537(
    kind: str,
    colors: tuple[Integer, ...],
    dims: IntegerTuple,
) -> Object:
    x0, x1 = dims
    x2 = _rect_patch_5dbc8537(dims)
    if kind == "singleton":
        return frozenset({(colors[0], ORIGIN)})
    if kind == "mono":
        return recolor(colors[0], x2)
    if kind == "checker":
        return frozenset(
            (colors[(i + j) % TWO], (i, j))
            for i in range(x0)
            for j in range(x1)
        )
    if kind == "stripe_h":
        x3 = randint(ZERO, subtract(x0, ONE))
        return frozenset(
            (colors[1] if i == x3 else colors[0], (i, j))
            for i in range(x0)
            for j in range(x1)
        )
    if kind == "stripe_v":
        x4 = randint(ZERO, subtract(x1, ONE))
        return frozenset(
            (colors[1] if j == x4 else colors[0], (i, j))
            for i in range(x0)
            for j in range(x1)
        )
    if kind == "center":
        x6 = frozenset({(divide(x0, TWO), divide(x1, TWO))})
        x7 = paint(canvas(colors[0], dims), recolor(colors[1], x6))
        return asobject(x7)
    if kind == "frame":
        x8 = difference(x2, _frame_cells_5dbc8537(dims))
        x9 = paint(canvas(colors[0], dims), recolor(colors[1], x8))
        return asobject(x9)
    raise ValueError(kind)


def _sample_piece_object_5dbc8537(
    diff_lb: float,
    diff_ub: float,
    available_colors: tuple[Integer, ...],
) -> Object:
    x0 = choice(PIECE_KIND_POOL_5DBC8537)
    if x0 == "singleton":
        x1 = choice(available_colors)
        return _build_piece_object_5dbc8537(x0, (x1,), UNITY)
    if x0 == "mono":
        x2 = unifint(diff_lb, diff_ub, (ONE, FIVE))
        x3 = unifint(diff_lb, diff_ub, (TWO, SIX))
        if randint(ZERO, ONE) == ONE:
            x2, x3 = x3, x2
        x4 = choice(available_colors)
        return _build_piece_object_5dbc8537(x0, (x4,), (x2, x3))
    x5 = choice(available_colors)
    x6 = choice(tuple(x7 for x7 in available_colors if x7 != x5))
    if x0 == "checker":
        x8 = unifint(diff_lb, diff_ub, (TWO, FOUR))
        x9 = unifint(diff_lb, diff_ub, (THREE, SIX))
        return _build_piece_object_5dbc8537(x0, (x5, x6), (x8, x9))
    if x0 in ("stripe_h", "stripe_v"):
        x10 = unifint(diff_lb, diff_ub, (TWO, FIVE))
        x11 = unifint(diff_lb, diff_ub, (TWO, SIX))
        return _build_piece_object_5dbc8537(x0, (x5, x6), (x10, x11))
    if x0 == "center":
        x12 = choice((THREE, FIVE))
        x13 = choice((THREE, FIVE))
        return _build_piece_object_5dbc8537(x0, (x5, x6), (x12, x13))
    x14 = unifint(diff_lb, diff_ub, (THREE, FIVE))
    x15 = unifint(diff_lb, diff_ub, (THREE, FIVE))
    return _build_piece_object_5dbc8537(x0, (x5, x6), (x14, x15))


def sample_piece_set_5dbc8537(
    diff_lb: float,
    diff_ub: float,
    available_colors: tuple[Integer, ...],
) -> tuple[Object, ...]:
    while True:
        x0 = unifint(diff_lb, diff_ub, (FOUR, NINE))
        x1 = tuple(_sample_piece_object_5dbc8537(diff_lb, diff_ub, available_colors) for _ in range(x0))
        x2 = frozenset(value for x3 in x1 for value, _ in x3)
        x3 = sum(size(x4) for x4 in x1)
        if len(x2) < TWO:
            continue
        if x3 < 20 or x3 > 90:
            continue
        return x1


def _touches_occupied_5dbc8537(
    patch: Indices,
    occupied: frozenset[IntegerTuple],
) -> Boolean:
    for x0 in patch:
        if len(intersection(dneighbors(x0), occupied)) > ZERO:
            return True
    return False


def _halo_5dbc8537(
    patch: Patch,
) -> frozenset[IntegerTuple]:
    x0 = frozenset(toindices(patch))
    x1 = set(x0)
    for x2 in x0:
        x1.update(neighbors(x2))
    return frozenset(x1)


def build_connected_hole_5dbc8537(
    objs: tuple[Object, ...],
    dims: IntegerTuple,
) -> Indices | None:
    x0 = tuple(sorted((normalize(toindices(x1)) for x1 in objs), key=size, reverse=T))
    for _ in range(30):
        x1: frozenset[IntegerTuple] = frozenset()
        for x2 in x0:
            x3 = height(x2)
            x4 = width(x2)
            x5 = []
            for x6 in range(add(subtract(dims[0], x3), ONE)):
                for x7 in range(add(subtract(dims[1], x4), ONE)):
                    x8 = shift(x2, (x6, x7))
                    if len(intersection(x8, x1)) > ZERO:
                        continue
                    if len(x1) > ZERO and not _touches_occupied_5dbc8537(x8, x1):
                        continue
                    x5.append(x8)
            if len(x5) == ZERO:
                x1 = frozenset()
                break
            x9 = choice(x5)
            x1 = frozenset(x1.union(x9))
        if len(x1) == ZERO:
            continue
        if len(objects(fill(canvas(ZERO, dims), ONE, x1), T, F, T)) != ONE:
            continue
        return x1
    return None


def layout_inventory_5dbc8537(
    objs: tuple[Object, ...],
    dims: IntegerTuple,
    hole_color: Integer,
) -> Grid | None:
    x0 = canvas(hole_color, dims)
    x1: frozenset[IntegerTuple] = frozenset()
    x2 = tuple(sorted(objs, key=size, reverse=T))
    x3 = []
    for x4 in x2:
        x5 = normalize(x4)
        x6 = height(x5)
        x7 = width(x5)
        x8 = []
        for x9 in range(add(subtract(dims[0], x6), ONE)):
            for x10 in range(add(subtract(dims[1], x7), ONE)):
                x11 = shift(x5, (x9, x10))
                x12 = toindices(x11)
                if len(intersection(x12, x1)) > ZERO:
                    continue
                x8.append(x11)
        if len(x8) == ZERO:
            return None
        x13 = choice(x8)
        x3.append(x13)
        x1 = frozenset(x1.union(_halo_5dbc8537(x13)))
    x14 = canvas(hole_color, dims)
    for x15 in x3:
        x14 = paint(x14, x15)
    if mostcolor(x14) != hole_color:
        return None
    return x14


def combine_regions_5dbc8537(
    mask_grid: Grid,
    piece_grid: Grid,
    side: str,
) -> Grid:
    if side == "left":
        return tuple(x0 + x1 for x0, x1 in zip(mask_grid, piece_grid))
    if side == "right":
        return tuple(x0 + x1 for x0, x1 in zip(piece_grid, mask_grid))
    if side == "top":
        return mask_grid + piece_grid
    if side == "bottom":
        return piece_grid + mask_grid
    raise ValueError(side)
