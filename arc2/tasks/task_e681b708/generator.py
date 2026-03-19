from __future__ import annotations

from collections import Counter

from arc2.core import *

from .helpers import (
    HSegment,
    RoomBounds,
    VSegment,
    build_room_color_map,
    choose_isolated_points,
    extract_rooms,
    extract_wall_indices,
    render_structure,
    room_marker_positions,
    segment_nodes,
)


ROOM_COLORS_E681B708 = (TWO, THREE, FOUR, SIX, EIGHT)
GRID_BOUNDS_E681B708 = (18, 29)


def _vertical_positions(room: RoomBounds, min_width: Integer) -> tuple[Integer, ...]:
    _, _, left, right = room
    start = left + min_width + ONE
    stop = right - min_width - ONE
    if start > stop:
        return tuple()
    return tuple(range(start, stop + ONE))


def _horizontal_positions(room: RoomBounds, min_height: Integer) -> tuple[Integer, ...]:
    top, bottom, _, _ = room
    start = top + min_height + ONE
    stop = bottom - min_height - ONE
    if start > stop:
        return tuple()
    return tuple(range(start, stop + ONE))


def _split_room(
    room: RoomBounds,
    orientation: str,
    min_height: Integer,
    min_width: Integer,
) -> tuple[tuple[RoomBounds, RoomBounds], VSegment | HSegment] | None:
    top, bottom, left, right = room
    if orientation == "v":
        positions = _vertical_positions(room, min_width)
        if len(positions) == ZERO:
            return None
        col = choice(positions)
        return ((top, bottom, left, col), (top, bottom, col, right)), (col, top, bottom)
    positions = _horizontal_positions(room, min_height)
    if len(positions) == ZERO:
        return None
    row = choice(positions)
    return ((top, row, left, right), (row, bottom, left, right)), (row, left, right)


def _sample_partition(
    grid_h: Integer,
    grid_w: Integer,
    diff_lb: float,
    diff_ub: float,
) -> tuple[tuple[RoomBounds, ...], tuple[VSegment, ...], tuple[HSegment, ...]]:
    min_height = max(THREE, unifint(diff_lb, diff_ub, (THREE, FIVE)))
    min_width = max(THREE, unifint(diff_lb, diff_ub, (THREE, FIVE)))
    target_splits = unifint(diff_lb, diff_ub, (THREE, SIX))
    rooms = [(-ONE, grid_h, -ONE, grid_w)]
    vsegments: list[VSegment] = []
    hsegments: list[HSegment] = []
    used = set()
    for _ in range(target_splits):
        choices = []
        for idx, room in enumerate(rooms):
            if len(_vertical_positions(room, min_width)) > ZERO:
                choices.append((idx, "v"))
            if len(_horizontal_positions(room, min_height)) > ZERO:
                choices.append((idx, "h"))
        if len(choices) == ZERO:
            break
        pending = [item for item in choices if item[1] not in used]
        room_idx, orientation = choice(pending if len(pending) > ZERO else choices)
        room = rooms.pop(room_idx)
        result = _split_room(room, orientation, min_height, min_width)
        if result is None:
            rooms.insert(room_idx, room)
            continue
        new_rooms, segment = result
        rooms.extend(new_rooms)
        if orientation == "v":
            vsegments.append(segment)
        else:
            hsegments.append(segment)
        used.add(orientation)
    return tuple(rooms), tuple(vsegments), tuple(hsegments)


def _sample_node_colors(
    dims: IntegerTuple,
    vsegments: tuple[VSegment, ...],
    hsegments: tuple[HSegment, ...],
) -> Grid | None:
    nodes = segment_nodes(dims, vsegments, hsegments)
    if len(nodes) < THREE:
        return None
    palette_size = min(len(ROOM_COLORS_E681B708), randint(TWO, FOUR))
    palette_values = sample(ROOM_COLORS_E681B708, palette_size)
    for _ in range(120):
        node_colors = {node: choice(palette_values) for node in nodes}
        grid = render_structure(dims, vsegments, hsegments, node_colors)
        walls = extract_wall_indices(grid)
        room_map = build_room_color_map(grid, walls)
        if len(room_map) == ZERO:
            continue
        room_colors = []
        valid = True
        for room in extract_rooms(grid, walls):
            markers = room_marker_positions(grid, room, walls)
            if len(markers) == ZERO:
                valid = False
                break
            marker_colors = tuple(grid[i][j] for i, j in markers)
            counts = Counter(marker_colors)
            top = counts.most_common(ONE)[ZERO][ONE]
            if sum(value == top for value in counts.values()) != ONE:
                valid = False
                break
            room_colors.append(room_map[next(iter(room))])
        if not valid:
            continue
        if len(frozenset(room_colors)) < TWO:
            continue
        return grid
    return None


def _scatter_noise(
    structure: Grid,
    diff_lb: float,
    diff_ub: float,
) -> tuple[Grid, Grid] | None:
    walls = extract_wall_indices(structure)
    rooms = extract_rooms(structure, walls)
    room_map = build_room_color_map(structure, walls)
    if len(room_map) == ZERO:
        return None
    gi = structure
    go = structure
    total = ZERO
    painted_rooms = ZERO
    for room in rooms:
        color_value = room_map.get(next(iter(room)))
        if color_value is None:
            continue
        candidates = tuple(sorted(loc for loc in room if structure[loc[0]][loc[1]] == ZERO))
        if len(candidates) < ONE:
            continue
        max_pick = max(ONE, len(candidates) // max(FIVE, unifint(diff_lb, diff_ub, (FIVE, NINE))))
        target = randint(ZERO, max_pick)
        if target == ZERO and randint(ZERO, ONE) == ONE and len(candidates) > THREE:
            target = ONE
        chosen = choose_isolated_points(candidates, target)
        if len(chosen) == ZERO:
            continue
        gi = fill(gi, ONE, chosen)
        go = fill(go, color_value, chosen)
        total += len(chosen)
        painted_rooms += ONE
    area = len(structure) * len(structure[0])
    if total < THREE:
        return None
    if total * SIX > area:
        return None
    if painted_rooms < TWO:
        return None
    return gi, go


def generate_e681b708(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        grid_h = unifint(diff_lb, diff_ub, GRID_BOUNDS_E681B708)
        grid_w = unifint(diff_lb, diff_ub, GRID_BOUNDS_E681B708)
        rooms, vsegments, hsegments = _sample_partition(grid_h, grid_w, diff_lb, diff_ub)
        if len(vsegments) == ZERO or len(hsegments) == ZERO:
            continue
        if len(rooms) < FOUR:
            continue
        structure = _sample_node_colors((grid_h, grid_w), vsegments, hsegments)
        if structure is None:
            continue
        examples = _scatter_noise(structure, diff_lb, diff_ub)
        if examples is None:
            continue
        gi, go = examples
        return {"input": gi, "output": go}
