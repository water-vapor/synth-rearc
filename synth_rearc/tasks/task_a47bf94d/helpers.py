from __future__ import annotations

from collections import defaultdict

from synth_rearc.core import *


TRACK_VALUES_A47BF94D = frozenset({FIVE, EIGHT})
STRUCTURE_VALUES_A47BF94D = frozenset({ZERO, FIVE, EIGHT, NINE})
PAYLOAD_COLORS_A47BF94D = (ONE, TWO, THREE, FOUR, SIX, SEVEN)
PORT_COLUMNS_A47BF94D = (TWO, SIX, TEN, 14)
LANE_COLUMNS_A47BF94D = (17, 20, 23, 26)
TOP_PORT_ROW_A47BF94D = TWO
TOP_ENDPOINT_ROW_A47BF94D = FOUR
TOP_ROUTE_ROWS_A47BF94D = (FIVE, EIGHT, 11, 14)
BOARD_WIDTH_A47BF94D = 29
DIAMOND_OFFSETS_A47BF94D = frozenset(
    {
        (-ONE, ZERO),
        (ZERO, -ONE),
        (ZERO, ONE),
        (ONE, ZERO),
    }
)
X_OFFSETS_A47BF94D = frozenset(
    {
        (-ONE, -ONE),
        (-ONE, ONE),
        (ZERO, ZERO),
        (ONE, -ONE),
        (ONE, ONE),
    }
)
BLOCK_OFFSETS_A47BF94D = frozenset((i, j) for i in range(-ONE, TWO) for j in range(-ONE, TWO))
DIRECTION_VECTORS_A47BF94D = {
    "U": (-ONE, ZERO),
    "D": (ONE, ZERO),
    "L": (ZERO, -ONE),
    "R": (ZERO, ONE),
}
OPPOSITE_DIRECTIONS_A47BF94D = {
    "U": "D",
    "D": "U",
    "L": "R",
    "R": "L",
}


def shift_offsets_a47bf94d(
    center: IntegerTuple,
    offsets: Indices,
) -> Indices:
    x0, x1 = center
    return frozenset((x0 + i, x1 + j) for i, j in offsets)


def x_patch_a47bf94d(
    center: IntegerTuple,
) -> Indices:
    return shift_offsets_a47bf94d(center, X_OFFSETS_A47BF94D)


def diamond_patch_a47bf94d(
    center: IntegerTuple,
) -> Indices:
    return shift_offsets_a47bf94d(center, DIAMOND_OFFSETS_A47BF94D)


def block_patch_a47bf94d(
    center: IntegerTuple,
) -> Indices:
    return shift_offsets_a47bf94d(center, BLOCK_OFFSETS_A47BF94D)


def paint_diamond_a47bf94d(
    grid: Grid,
    color_value: Integer,
    center: IntegerTuple,
) -> Grid:
    return fill(grid, color_value, diamond_patch_a47bf94d(center))


def paint_x_a47bf94d(
    grid: Grid,
    color_value: Integer,
    center: IntegerTuple,
) -> Grid:
    return fill(grid, color_value, x_patch_a47bf94d(center))


def paint_block_a47bf94d(
    grid: Grid,
    color_value: Integer,
    center: IntegerTuple,
) -> Grid:
    return fill(grid, color_value, block_patch_a47bf94d(center))


def paint_port_symbol_a47bf94d(
    grid: Grid,
    color_value: Integer,
    center: IntegerTuple,
    outward: IntegerTuple,
) -> Grid:
    if outward in ((-ONE, ZERO), (ZERO, -ONE)):
        return paint_diamond_a47bf94d(grid, color_value, center)
    return paint_x_a47bf94d(grid, color_value, center)


def strip_payload_a47bf94d(
    grid: Grid,
) -> Grid:
    return tuple(
        tuple(value if value in STRUCTURE_VALUES_A47BF94D else ZERO for value in row)
        for row in grid
    )


def is_track_a47bf94d(
    grid: Grid,
    loc: IntegerTuple,
) -> bool:
    x0, x1 = loc
    x2, x3 = shape(grid)
    return ZERO <= x0 < x2 and ZERO <= x1 < x3 and grid[x0][x1] in TRACK_VALUES_A47BF94D


def track_neighbors_a47bf94d(
    grid: Grid,
    loc: IntegerTuple,
) -> dict[str, IntegerTuple]:
    x0, x1 = loc
    x2 = {}
    for x3, (x4, x5) in DIRECTION_VECTORS_A47BF94D.items():
        x6 = (x0 + x4, x1 + x5)
        if is_track_a47bf94d(grid, x6):
            x2[x3] = x6
    return x2


def crossing_centers_a47bf94d(
    grid: Grid,
) -> frozenset[IntegerTuple]:
    x0 = set()
    for x1, x2 in ofcolor(grid, EIGHT):
        x3 = track_neighbors_a47bf94d(grid, (x1, x2))
        if size(x3) == FOUR:
            x0.add((x1, x2))
    return frozenset(x0)


def tunnel_rectangles_a47bf94d(
    grid: Grid,
) -> tuple[tuple[Integer, Integer, Integer, Integer], ...]:
    x0 = []
    for x1 in colorfilter(objects(grid, T, F, F), NINE):
        x2 = toindices(x1)
        x3, x4 = ulcorner(x2)
        x5, x6 = lrcorner(x2)
        x0.append((x3, x4, x5, x6))
    x0.sort()
    return tuple(x0)


def split_node_a47bf94d(
    crossings: frozenset[IntegerTuple],
    loc: IntegerTuple,
    direction: str,
) -> tuple[IntegerTuple, str | None]:
    if loc not in crossings:
        return (loc, None)
    if direction in ("L", "R"):
        return (loc, "h")
    return (loc, "v")


def build_track_graph_a47bf94d(
    grid: Grid,
) -> dict[tuple[IntegerTuple, str | None], set[tuple[IntegerTuple, str | None]]]:
    x0 = crossing_centers_a47bf94d(grid)
    x1 = defaultdict(set)
    x2 = frozenset((i, j) for i, j in asindices(grid) if is_track_a47bf94d(grid, (i, j)))
    x3 = {x4: size(track_neighbors_a47bf94d(grid, x4)) for x4 in x2}
    for x4, x5 in x2:
        for x6, x7 in track_neighbors_a47bf94d(grid, (x4, x5)).items():
            x8 = split_node_a47bf94d(x0, (x4, x5), x6)
            x9 = split_node_a47bf94d(x0, x7, OPPOSITE_DIRECTIONS_A47BF94D[x6])
            x1[x8].add(x9)
            x1[x9].add(x8)
    for x10, x11, x12, x13 in tunnel_rectangles_a47bf94d(grid):
        x14 = {}
        x15 = {}
        x16 = {}
        x17 = {}
        for x18 in range(x11, x13 + ONE):
            x19 = (x10 - ONE, x18)
            x20 = (x12 + ONE, x18)
            if both(is_track_a47bf94d(grid, x19), x3.get(x19, ZERO) <= ONE):
                x14[x18 - x11] = x19
            if both(is_track_a47bf94d(grid, x20), x3.get(x20, ZERO) <= ONE):
                x15[x18 - x11] = x20
        for x21 in range(x10, x12 + ONE):
            x22 = (x21, x11 - ONE)
            x23 = (x21, x13 + ONE)
            if both(is_track_a47bf94d(grid, x22), x3.get(x22, ZERO) <= ONE):
                x16[x21 - x10] = x22
            if both(is_track_a47bf94d(grid, x23), x3.get(x23, ZERO) <= ONE):
                x17[x21 - x10] = x23
        x24 = set()
        for x25, x26 in ((x14, x15), (x16, x17)):
            for x27 in set(x25) & set(x26):
                x28 = x25[x27]
                x29 = x26[x27]
                x30 = branch(x25 is x14, "D", "R")
                x31 = branch(x26 is x15, "U", "L")
                x32 = split_node_a47bf94d(x0, x28, x30)
                x33 = split_node_a47bf94d(x0, x29, x31)
                x1[x32].add(x33)
                x1[x33].add(x32)
                x24.add(x28)
                x24.add(x29)
        x34 = []
        for x35, x36 in combine(tuple(x14.items()), tuple(x15.items())):
            if x36 not in x24:
                x34.append((x35, x36, "V"))
        for x37, x38 in combine(tuple(x16.items()), tuple(x17.items())):
            if x38 not in x24:
                x34.append((x37, x38, "H"))
        x34.sort(key=lambda item: item[ZERO])
        x39 = defaultdict(list)
        for x40, x41, x42 in x34:
            x39[x40].append((x41, x42))
        for x43 in tuple(x39):
            x44 = x39[x43]
            while len(x44) >= TWO:
                (x45, x46) = x44.pop(ZERO)
                (x47, x48) = x44.pop(ZERO)
                x49 = branch(x46 == "V", "D", "R")
                x50 = branch(x48 == "V", "U", "L")
                x51 = split_node_a47bf94d(x0, x45, x49)
                x52 = split_node_a47bf94d(x0, x47, x50)
                x1[x51].add(x52)
                x1[x52].add(x51)
    return x1


def endpoint_port_a47bf94d(
    grid: Grid,
    node: tuple[IntegerTuple, str | None],
) -> tuple[IntegerTuple, IntegerTuple]:
    (x1, x2), _ = node
    x3 = tuple(track_neighbors_a47bf94d(grid, (x1, x2)).values())
    if len(x3) == ONE:
        x4, x5 = x3[ZERO]
        x6 = x4 - x1
        x7 = x5 - x2
    else:
        x6 = ZERO
        x7 = ZERO
        for x8, (x9, x10) in DIRECTION_VECTORS_A47BF94D.items():
            x11 = (x1 + x9, x2 + x10)
            if index(grid, x11) == NINE:
                x6 = x9
                x7 = x10
                break
    x12 = (-x6, -x7)
    x13 = (x1 + double(x12[ZERO]), x2 + double(x12[ONE]))
    return x13, x12


def port_pairs_a47bf94d(
    grid: Grid,
) -> tuple[tuple[tuple[IntegerTuple, IntegerTuple], tuple[IntegerTuple, IntegerTuple]], ...]:
    x0 = build_track_graph_a47bf94d(grid)
    x1 = set()
    x2 = []
    for x3 in tuple(x0):
        if x3 in x1:
            continue
        x4 = {x3}
        x5 = [x3]
        while len(x5) > ZERO:
            x6 = x5.pop()
            for x7 in x0[x6]:
                if x7 not in x4:
                    x4.add(x7)
                    x5.append(x7)
        x1 |= x4
        x8 = tuple(x6 for x6 in x4 if size(x0[x6]) == ONE)
        if size(x8) != TWO:
            continue
        x9 = tuple(sorted(endpoint_port_a47bf94d(grid, x6) for x6 in x8))
        x2.append(x9)
    x2.sort()
    return tuple(x2)


def payload_color_a47bf94d(
    grid: Grid,
    center: IntegerTuple,
) -> Integer:
    x0 = index(grid, center)
    if x0 in STRUCTURE_VALUES_A47BF94D:
        return ZERO
    return x0


def pair_color_a47bf94d(
    grid: Grid,
    pair_ports: tuple[tuple[IntegerTuple, IntegerTuple], tuple[IntegerTuple, IntegerTuple]],
) -> Integer:
    x0 = tuple(
        payload_color_a47bf94d(grid, x1[ZERO])
        for x1 in pair_ports
        if payload_color_a47bf94d(grid, x1[ZERO]) != ZERO
    )
    if len(x0) == ZERO:
        return ZERO
    return x0[ZERO]


def apply_turn_segment_a47bf94d(
    claims: defaultdict[IntegerTuple, set[Integer]],
    path_index: Integer,
    a: IntegerTuple,
    b: IntegerTuple,
) -> None:
    for x0 in connect(a, b):
        claims[x0].add(path_index)


def render_tracks_a47bf94d(
    height_value: Integer,
    permutation: tuple[Integer, Integer, Integer, Integer],
    tunnel_specs: tuple[tuple[Integer, Integer, Integer, Integer, Integer], ...],
) -> Grid:
    x0 = defaultdict(set)
    x1 = defaultdict(set)
    x2 = canvas(ZERO, (height_value, BOARD_WIDTH_A47BF94D))
    x3 = {}
    for x4, x5, x6, x7, x8 in tunnel_specs:
        x3[x4] = (x5, x6, x7, x8)
        x2 = fill(x2, NINE, frozenset((i, j) for i in range(x5, x6 + ONE) for j in range(x7, x8 + ONE)))
    x10 = height_value - FIVE
    x11 = (
        height_value - 13,
        height_value - 10,
        height_value - 7,
        height_value - 5,
    )
    for x12 in range(FOUR):
        x13 = PORT_COLUMNS_A47BF94D[x12]
        x14 = PORT_COLUMNS_A47BF94D[permutation[x12]]
        x15 = LANE_COLUMNS_A47BF94D[x12]
        x16 = TOP_ROUTE_ROWS_A47BF94D[x12]
        x17 = x11[x12]
        apply_turn_segment_a47bf94d(x1, x12, (TOP_ENDPOINT_ROW_A47BF94D, x13), (x16, x13))
        apply_turn_segment_a47bf94d(x0, x12, (x16, x13), (x16, x15))
        if x12 in x3:
            x18, x19, _, _ = x3[x12]
            apply_turn_segment_a47bf94d(x1, x12, (x16, x15), (x18 - ONE, x15))
            apply_turn_segment_a47bf94d(x1, x12, (x19 + ONE, x15), (x17, x15))
        else:
            apply_turn_segment_a47bf94d(x1, x12, (x16, x15), (x17, x15))
        apply_turn_segment_a47bf94d(x0, x12, (x17, x15), (x17, x14))
        apply_turn_segment_a47bf94d(x1, x12, (x17, x14), (x10, x14))
    x22 = frozenset(set(x0) | set(x1))
    x2 = fill(x2, EIGHT, x22)
    x23 = []
    for x24 in x22:
        if both(x24 in x0, x24 in x1):
            x25 = x0[x24]
            x26 = x1[x24]
            if any(x27 != x28 for x27 in x25 for x28 in x26):
                x23.append(x24)
    for x29, x30 in x23:
        if randint(ZERO, ONE) == ZERO:
            x31 = ((x29, x30 - ONE), (x29, x30 + ONE))
        else:
            x31 = ((x29 - ONE, x30), (x29 + ONE, x30))
        x32 = frozenset(x33 for x33 in x31 if x33 in x22)
        x2 = fill(x2, FIVE, x32)
    return x2


def pair_centers_from_permutation_a47bf94d(
    height_value: Integer,
    permutation: tuple[Integer, Integer, Integer, Integer],
) -> tuple[tuple[IntegerTuple, IntegerTuple], ...]:
    x0 = height_value - THREE
    x1 = []
    for x2 in range(FOUR):
        x3 = (TOP_PORT_ROW_A47BF94D, PORT_COLUMNS_A47BF94D[x2])
        x4 = (x0, PORT_COLUMNS_A47BF94D[permutation[x2]])
        x1.append((x3, x4))
    return tuple(x1)


def maybe_rotate_example_a47bf94d(
    input_grid: Grid,
    output_grid: Grid,
) -> tuple[Grid, Grid]:
    x1 = input_grid
    x2 = output_grid
    if randint(ZERO, ONE) == ONE:
        x1 = vmirror(x1)
        x2 = vmirror(x2)
    return x1, x2
