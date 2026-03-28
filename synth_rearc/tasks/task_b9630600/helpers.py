from synth_rearc.core import *


HORIZONTAL_B9630600 = ZERO
VERTICAL_B9630600 = ONE
ROOM_COLOR_B9630600 = THREE
GRID_SHAPE_B9630600 = (30, 30)


def room_bbox_b9630600(
    patch: Patch,
) -> Tuple:
    return (uppermost(patch), leftmost(patch), lowermost(patch), rightmost(patch))


def room_patch_b9630600(
    room: Tuple,
) -> Indices:
    r0, c0, r1, c1 = room
    return box(frozenset({(r0, c0), (r1, c1)}))


def shift_room_b9630600(
    room: Tuple,
    offset: Tuple,
) -> Tuple:
    di, dj = offset
    r0, c0, r1, c1 = room
    return (r0 + di, c0 + dj, r1 + di, c1 + dj)


def rooms_touch_b9630600(
    room_a: Tuple,
    room_b: Tuple,
) -> bool:
    ar0, ac0, ar1, ac1 = room_a
    br0, bc0, br1, bc1 = room_b
    return not (
        ar1 + ONE < br0
        or br1 + ONE < ar0
        or ac1 + ONE < bc0
        or bc1 + ONE < ac0
    )


def is_room_outline_b9630600(
    obj: Object,
) -> bool:
    x0 = toindices(obj)
    return x0 == box(x0) and greater(height(x0), TWO) and greater(width(x0), TWO)


def build_candidate_edges_b9630600(
    rooms: Tuple,
) -> Tuple:
    edges = []
    for i, room_a in enumerate(rooms):
        ar0, ac0, ar1, ac1 = room_a
        for j, room_b in enumerate(rooms[i + ONE :], start=i + ONE):
            br0, bc0, br1, bc1 = room_b
            top = max(ar0 + ONE, br0 + ONE)
            bottom = min(ar1 - ONE, br1 - ONE)
            left = max(ac0 + ONE, bc0 + ONE)
            right = min(ac1 - ONE, bc1 - ONE)
            if ac1 < bc0 and top <= bottom:
                edges.append((bc0 - ac1 - ONE, HORIZONTAL_B9630600, top, bottom, i, j))
            elif bc1 < ac0 and top <= bottom:
                edges.append((ac0 - bc1 - ONE, HORIZONTAL_B9630600, top, bottom, j, i))
            if ar1 < br0 and left <= right:
                edges.append((br0 - ar1 - ONE, VERTICAL_B9630600, left, right, i, j))
            elif br1 < ar0 and left <= right:
                edges.append((ar0 - br1 - ONE, VERTICAL_B9630600, left, right, j, i))
    return tuple(sorted(edges))


def kruskal_edges_b9630600(
    edges: Tuple,
    nrooms: Integer,
) -> Tuple:
    parents = list(range(nrooms))

    def root(index):
        while parents[index] != index:
            parents[index] = parents[parents[index]]
            index = parents[index]
        return index

    chosen = []
    for edge in edges:
        _, _, _, _, room_a, room_b = edge
        root_a = root(room_a)
        root_b = root(room_b)
        if root_a == root_b:
            continue
        parents[root_b] = root_a
        chosen.append(edge)
        if len(chosen) == nrooms - ONE:
            break
    return tuple(chosen)


def draw_edge_b9630600(
    grid: Grid,
    rooms: Tuple,
    edge: Tuple,
) -> Grid:
    _, axis, span_start, span_end, room_a_idx, room_b_idx = edge
    room_a = rooms[room_a_idx]
    room_b = rooms[room_b_idx]
    if axis == HORIZONTAL_B9630600:
        _, _, _, ac1 = room_a
        _, bc0, _, _ = room_b
        x0 = connect((span_start, ac1), (span_start, bc0))
        x1 = connect((span_end, ac1), (span_end, bc0))
        x2 = fill(grid, ROOM_COLOR_B9630600, combine(x0, x1))
        if span_start + ONE >= span_end:
            return x2
        x3 = connect((span_start + ONE, ac1), (span_end - ONE, ac1))
        x4 = connect((span_start + ONE, bc0), (span_end - ONE, bc0))
        return fill(x2, ZERO, combine(x3, x4))
    _, _, ar1, _ = room_a
    br0, _, _, _ = room_b
    x0 = connect((ar1, span_start), (br0, span_start))
    x1 = connect((ar1, span_end), (br0, span_end))
    x2 = fill(grid, ROOM_COLOR_B9630600, combine(x0, x1))
    if span_start + ONE >= span_end:
        return x2
    x3 = connect((ar1, span_start + ONE), (ar1, span_end - ONE))
    x4 = connect((br0, span_start + ONE), (br0, span_end - ONE))
    return fill(x2, ZERO, combine(x3, x4))


def render_input_b9630600(
    rooms: Tuple,
) -> Grid:
    grid = canvas(ZERO, GRID_SHAPE_B9630600)
    for room in rooms:
        grid = fill(grid, ROOM_COLOR_B9630600, room_patch_b9630600(room))
    return grid


def render_output_b9630600(
    rooms: Tuple,
) -> Grid:
    grid = render_input_b9630600(rooms)
    edges = build_candidate_edges_b9630600(rooms)
    chosen = kruskal_edges_b9630600(edges, len(rooms))
    for edge in chosen:
        grid = draw_edge_b9630600(grid, rooms, edge)
    return grid
