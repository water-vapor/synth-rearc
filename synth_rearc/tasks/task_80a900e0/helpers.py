from __future__ import annotations

from synth_rearc.core import *


SIDES_80A900E0 = ("left", "top", "bottom", "right")


def checkerboard_80a900e0(
    dims: IntegerTuple,
) -> Grid:
    x0, x1 = dims
    return tuple(
        tuple(ONE if (i + j) % TWO == ZERO else ZERO for j in range(x1))
        for i in range(x0)
    )


def loc_to_uv_80a900e0(
    loc: IntegerTuple,
) -> IntegerTuple:
    x0, x1 = loc
    return (x0 + x1, x0 - x1)


def uv_to_loc_80a900e0(
    uv: IntegerTuple,
) -> IntegerTuple:
    x0, x1 = uv
    return (divide(add(x0, x1), TWO), divide(subtract(x0, x1), TWO))


def inbounds_loc_80a900e0(
    loc: IntegerTuple,
    dims: IntegerTuple,
) -> Boolean:
    x0, x1 = loc
    x2, x3 = dims
    return 0 <= x0 < x2 and 0 <= x1 < x3


def colored_cells_80a900e0(
    grid: Grid,
) -> dict[IntegerTuple, Integer]:
    return {
        (i, j): value
        for i, row in enumerate(grid)
        for j, value in enumerate(row)
        if value not in (ZERO, ONE)
    }


def motif_objects_80a900e0(
    grid: Grid,
) -> tuple[Object, ...]:
    x0 = tuple(
        tuple(TWO if value not in (ZERO, ONE) else ZERO for value in row)
        for row in grid
    )
    x1 = tuple(toobject(toindices(obj), grid) for obj in objects(x0, T, T, T))
    return tuple(sorted(x1, key=lambda obj: ulcorner(obj)))


def _is_center_ring_80a900e0(
    uv_cells: set[IntegerTuple],
) -> Boolean:
    if len(uv_cells) != EIGHT:
        return False
    x0 = tuple(sorted({u for u, _ in uv_cells}))
    x1 = tuple(sorted({v for _, v in uv_cells}))
    if len(x0) != THREE or len(x1) != THREE:
        return False
    if x0[ONE] - x0[ZERO] != TWO or x0[TWO] - x0[ONE] != TWO:
        return False
    if x1[ONE] - x1[ZERO] != TWO or x1[TWO] - x1[ONE] != TWO:
        return False
    x2 = {(u, v) for u in x0 for v in x1}
    x3 = {(x0[ONE], x1[ONE])}
    return uv_cells == x2 - x3


def analyze_motif_80a900e0(
    obj: Object,
) -> tuple[Integer, tuple[Integer, ...], tuple[Integer, ...], tuple[tuple[str, Integer, tuple[Integer, ...]], ...]]:
    x0 = {}
    x1 = {}
    for value, loc in obj:
        x2 = loc_to_uv_80a900e0(loc)
        x1[x2] = value
        x0.setdefault(value, set()).add(x2)
    x3 = None
    x4 = tuple(sorted(x0))
    for x5 in x4:
        x6 = x0[x5]
        if _is_center_ring_80a900e0(x6):
            x3 = x5
            break
    if x3 is None:
        raise ValueError("failed to locate center ring")
    x7 = tuple(sorted({u for u, _ in x0[x3]}))
    x8 = tuple(sorted({v for _, v in x0[x3]}))
    x9 = []
    x10 = (
        ("left", x7[ZERO] - TWO, x8),
        ("top", x8[ZERO] - TWO, x7),
        ("bottom", x8[TWO] + TWO, x7),
        ("right", x7[TWO] + TWO, x8),
    )
    for side, fixed_value, axis_values in x10:
        x11 = {}
        for axis_value in axis_values:
            x12 = (
                (fixed_value, axis_value)
                if side in ("left", "right")
                else (axis_value, fixed_value)
            )
            x13 = x1.get(x12)
            if x13 is None:
                continue
            x11.setdefault(x13, []).append(axis_value)
        for color_, values in sorted(x11.items()):
            x14 = tuple(sorted(values))
            x9.append((side, color_, x14))
    return x3, x7, x8, tuple(x9)


def extend_segment_80a900e0(
    output_grid: Grid,
    input_grid: Grid,
    us: tuple[Integer, ...],
    vs: tuple[Integer, ...],
    side: str,
    color_: Integer,
    values: tuple[Integer, ...],
) -> Grid:
    if len(values) == ZERO:
        return output_grid
    x0 = values[ZERO]
    x1 = values[-ONE]
    x2 = (x0,) if x0 == x1 else (x0, x1)
    if side == "left":
        x3 = us[ZERO] - TWO
        x4 = -TWO
        x5 = ZERO
        x6 = tuple((x3, value) for value in x2)
    elif side == "right":
        x3 = us[TWO] + TWO
        x4 = TWO
        x5 = ZERO
        x6 = tuple((x3, value) for value in x2)
    elif side == "top":
        x3 = vs[ZERO] - TWO
        x4 = ZERO
        x5 = -TWO
        x6 = tuple((value, x3) for value in x2)
    elif side == "bottom":
        x3 = vs[TWO] + TWO
        x4 = ZERO
        x5 = TWO
        x6 = tuple((value, x3) for value in x2)
    else:
        raise ValueError(f"unknown side {side}")
    x7 = output_grid
    x8 = shape(input_grid)
    for x9, x10 in x6:
        x11 = x9
        x12 = x10
        while True:
            x11 = x11 + x4
            x12 = x12 + x5
            x13 = uv_to_loc_80a900e0((x11, x12))
            if not inbounds_loc_80a900e0(x13, x8):
                break
            if index(input_grid, x13) not in (ZERO, ONE):
                break
            x7 = fill(x7, color_, frozenset({x13}))
    return x7


def render_output_80a900e0(
    grid: Grid,
) -> Grid:
    x0 = grid
    x1 = motif_objects_80a900e0(grid)
    for x2 in x1:
        _, x3, x4, x5 = analyze_motif_80a900e0(x2)
        for x6, x7, x8 in x5:
            x0 = extend_segment_80a900e0(x0, grid, x3, x4, x6, x7, x8)
    return x0


def motif_cell_map_80a900e0(
    us: tuple[Integer, ...],
    vs: tuple[Integer, ...],
    center_color: Integer,
    segments: tuple[tuple[str, Integer, tuple[Integer, ...]], ...],
) -> dict[IntegerTuple, Integer]:
    x0 = {}
    for u in us:
        for v in vs:
            if (u, v) == (us[ONE], vs[ONE]):
                continue
            x0[(u, v)] = center_color
    for side, color_, values in segments:
        if side == "left":
            x1 = us[ZERO] - TWO
            for value in values:
                x0[(x1, value)] = color_
        elif side == "right":
            x1 = us[TWO] + TWO
            for value in values:
                x0[(x1, value)] = color_
        elif side == "top":
            x1 = vs[ZERO] - TWO
            for value in values:
                x0[(value, x1)] = color_
        elif side == "bottom":
            x1 = vs[TWO] + TWO
            for value in values:
                x0[(value, x1)] = color_
    return x0


def cell_map_in_bounds_80a900e0(
    cell_map: dict[IntegerTuple, Integer],
    dims: IntegerTuple,
) -> Boolean:
    return all(inbounds_loc_80a900e0(uv_to_loc_80a900e0(uv), dims) for uv in cell_map)


def paint_cell_map_80a900e0(
    grid: Grid,
    cell_map: dict[IntegerTuple, Integer],
) -> Grid:
    x0 = frozenset(
        (value, uv_to_loc_80a900e0(uv))
        for uv, value in cell_map.items()
    )
    return paint(grid, x0)
