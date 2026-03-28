from __future__ import annotations

from collections import Counter, deque

from synth_rearc.core import *


RoomBounds = tuple[Integer, Integer, Integer, Integer]
VSegment = tuple[Integer, Integer, Integer]
HSegment = tuple[Integer, Integer, Integer]


def extract_wall_indices(grid: Grid) -> Indices:
    h = len(grid)
    w = len(grid[0])
    markers = tuple((i, j) for i in range(h) for j in range(w) if grid[i][j] not in (ZERO, ONE))
    by_row: dict[Integer, list[Integer]] = {}
    by_col: dict[Integer, list[Integer]] = {}
    for i, j in markers:
        by_row.setdefault(i, []).append(j)
        by_col.setdefault(j, []).append(i)
    walls = set()
    for i, cols in by_row.items():
        cols = sorted(cols)
        for left, right in zip(cols, cols[1:]):
            if all(grid[i][j] != ZERO for j in range(left, right + ONE)):
                walls |= {(i, j) for j in range(left, right + ONE)}
    for j, rows in by_col.items():
        rows = sorted(rows)
        for top, bottom in zip(rows, rows[1:]):
            if all(grid[i][j] != ZERO for i in range(top, bottom + ONE)):
                walls |= {(i, j) for i in range(top, bottom + ONE)}
    return frozenset(walls)


def extract_rooms(grid: Grid, walls: Indices | None = None) -> tuple[Indices, ...]:
    h = len(grid)
    w = len(grid[0])
    walls = extract_wall_indices(grid) if walls is None else walls
    seen = set()
    rooms = []
    for i in range(h):
        for j in range(w):
            loc = (i, j)
            if loc in walls or loc in seen:
                continue
            room = set()
            queue = deque([loc])
            seen.add(loc)
            while queue:
                cell = queue.popleft()
                room.add(cell)
                for ni, nj in dneighbors(cell):
                    if 0 <= ni < h and 0 <= nj < w:
                        nxt = (ni, nj)
                        if nxt not in walls and nxt not in seen:
                            seen.add(nxt)
                            queue.append(nxt)
            rooms.append(frozenset(room))
    return tuple(rooms)


def room_marker_positions(grid: Grid, room: Indices, walls: Indices | None = None) -> tuple[IntegerTuple, ...]:
    h = len(grid)
    w = len(grid[0])
    walls = extract_wall_indices(grid) if walls is None else walls
    top = min(i for i, _ in room)
    bottom = max(i for i, _ in room)
    left = min(j for _, j in room)
    right = max(j for _, j in room)
    top_edge = ZERO if top == ZERO else top - ONE
    bottom_edge = h - ONE if bottom == h - ONE else bottom + ONE
    left_edge = ZERO if left == ZERO else left - ONE
    right_edge = w - ONE if right == w - ONE else right + ONE
    markers = set()
    for j in range(left_edge, right_edge + ONE):
        if (top_edge, j) in walls and grid[top_edge][j] not in (ZERO, ONE):
            markers.add((top_edge, j))
        if (bottom_edge, j) in walls and grid[bottom_edge][j] not in (ZERO, ONE):
            markers.add((bottom_edge, j))
    for i in range(top_edge, bottom_edge + ONE):
        if (i, left_edge) in walls and grid[i][left_edge] not in (ZERO, ONE):
            markers.add((i, left_edge))
        if (i, right_edge) in walls and grid[i][right_edge] not in (ZERO, ONE):
            markers.add((i, right_edge))
    return tuple(sorted(markers))


def room_color(grid: Grid, room: Indices, walls: Indices | None = None) -> Integer | None:
    markers = room_marker_positions(grid, room, walls)
    if len(markers) == ZERO:
        return None
    counts = Counter(grid[i][j] for i, j in markers)
    color, count = counts.most_common(ONE)[ZERO]
    if sum(value == count for value in counts.values()) != ONE:
        return None
    return color


def build_room_color_map(grid: Grid, walls: Indices | None = None) -> dict[IntegerTuple, Integer]:
    walls = extract_wall_indices(grid) if walls is None else walls
    room_map: dict[IntegerTuple, Integer] = {}
    for room in extract_rooms(grid, walls):
        color_value = room_color(grid, room, walls)
        if color_value is None:
            continue
        for cell in room:
            room_map[cell] = color_value
    return room_map


def render_structure(
    dims: IntegerTuple,
    vsegments: tuple[VSegment, ...],
    hsegments: tuple[HSegment, ...],
    node_colors: dict[IntegerTuple, Integer],
) -> Grid:
    h, w = dims
    grid = [list(row) for row in canvas(ZERO, dims)]
    for col, top, bottom in vsegments:
        start = ZERO if top == NEG_ONE else top + ONE
        stop = h - ONE if bottom == h else bottom - ONE
        for i in range(start, stop + ONE):
            grid[i][col] = ONE
    for row, left, right in hsegments:
        start = ZERO if left == NEG_ONE else left + ONE
        stop = w - ONE if right == w else right - ONE
        for j in range(start, stop + ONE):
            grid[row][j] = ONE
    for (i, j), value in node_colors.items():
        grid[i][j] = value
    return tuple(tuple(row) for row in grid)


def segment_nodes(
    dims: IntegerTuple,
    vsegments: tuple[VSegment, ...],
    hsegments: tuple[HSegment, ...],
) -> tuple[IntegerTuple, ...]:
    h, w = dims
    nodes = set()
    for col, top, bottom in vsegments:
        nodes.add((ZERO if top == NEG_ONE else top, col))
        nodes.add((h - ONE if bottom == h else bottom, col))
    for row, left, right in hsegments:
        nodes.add((row, ZERO if left == NEG_ONE else left))
        nodes.add((row, w - ONE if right == w else right))
    return tuple(sorted(nodes))


def choose_isolated_points(candidates: tuple[IntegerTuple, ...], target: Integer) -> Indices:
    pool = list(candidates)
    shuffle(pool)
    chosen = set()
    blocked = set()
    for cell in pool:
        if cell in blocked:
            continue
        chosen.add(cell)
        blocked.add(cell)
        blocked |= neighbors(cell)
        if len(chosen) == target:
            break
    return frozenset(chosen)
