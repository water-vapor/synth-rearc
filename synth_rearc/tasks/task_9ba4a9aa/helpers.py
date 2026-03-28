from __future__ import annotations

from collections import deque

from synth_rearc.core import *


GRID_SHAPE_9BA4A9AA = (22, 22)
LATTICE_SIZE_9BA4A9AA = 10
SIDES_9BA4A9AA = ("left", "right", "top", "bottom")


def lattice_to_actual_9ba4a9aa(
    node: tuple[int, int],
    col_phase: int,
) -> tuple[int, int]:
    return (node[0] * 2 + 2, node[1] * 2 + col_phase)


def lattice_neighbors_9ba4a9aa(
    node: tuple[int, int],
) -> tuple[tuple[int, int], ...]:
    x0, x1 = node
    x2 = []
    if x0 > 0:
        x2.append((x0 - 1, x1))
    if x0 < LATTICE_SIZE_9BA4A9AA - 1:
        x2.append((x0 + 1, x1))
    if x1 > 0:
        x2.append((x0, x1 - 1))
    if x1 < LATTICE_SIZE_9BA4A9AA - 1:
        x2.append((x0, x1 + 1))
    return tuple(x2)


def side_nodes_9ba4a9aa(
    side: str,
) -> tuple[tuple[int, int], ...]:
    if side == "left":
        return tuple((x0, 0) for x0 in range(LATTICE_SIZE_9BA4A9AA))
    if side == "right":
        return tuple((x0, LATTICE_SIZE_9BA4A9AA - 1) for x0 in range(LATTICE_SIZE_9BA4A9AA))
    if side == "top":
        return tuple((0, x0) for x0 in range(LATTICE_SIZE_9BA4A9AA))
    return tuple((LATTICE_SIZE_9BA4A9AA - 1, x0) for x0 in range(LATTICE_SIZE_9BA4A9AA))


def inward_neighbor_9ba4a9aa(
    node: tuple[int, int],
    side: str,
) -> tuple[int, int]:
    x0, x1 = node
    if side == "left":
        return (x0, x1 + 1)
    if side == "right":
        return (x0, x1 - 1)
    if side == "top":
        return (x0 + 1, x1)
    return (x0 - 1, x1)


def ring_grid_9ba4a9aa(
    outer_color: int,
    center_color: int,
) -> Grid:
    return (
        (outer_color, outer_color, outer_color),
        (outer_color, center_color, outer_color),
        (outer_color, outer_color, outer_color),
    )


def ring_object_9ba4a9aa(
    center_node: tuple[int, int],
    col_phase: int,
    outer_color: int,
    center_color: int,
) -> Object:
    x0, x1 = lattice_to_actual_9ba4a9aa(center_node, col_phase)
    x2 = {
        (outer_color, (x0 + x3, x1 + x4))
        for x3 in (-1, 0, 1)
        for x4 in (-1, 0, 1)
        if (x3, x4) != (0, 0)
    }
    x2.add((center_color, (x0, x1)))
    return frozenset(x2)


def checker_object_9ba4a9aa(
    center_node: tuple[int, int],
    col_phase: int,
    color_a: int,
    color_b: int,
) -> Object:
    x0, x1 = lattice_to_actual_9ba4a9aa(center_node, col_phase)
    x2 = set()
    for x3 in (-1, 0, 1):
        for x4 in (-1, 0, 1):
            x5 = color_a if (x3 + x4) % 2 == 0 else color_b
            x2.add((x5, (x0 + x3, x1 + x4)))
    return frozenset(x2)


def paint_lattice_nodes_9ba4a9aa(
    grid: Grid,
    nodes: tuple[tuple[int, int], ...] | list[tuple[int, int]],
    col_phase: int,
    color_value: int,
) -> Grid:
    x0 = frozenset(lattice_to_actual_9ba4a9aa(x1, col_phase) for x1 in nodes)
    return fill(grid, color_value, x0)


def line_nodes_9ba4a9aa(
    start: tuple[int, int],
    end: tuple[int, int],
) -> tuple[tuple[int, int], ...]:
    x0, x1 = start
    x2, x3 = end
    if x0 == x2:
        x4 = 1 if x1 <= x3 else -1
        return tuple((x0, x5) for x5 in range(x1, x3 + x4, x4))
    x4 = 1 if x0 <= x2 else -1
    return tuple((x5, x1) for x5 in range(x0, x2 + x4, x4))


def expand_polyline_9ba4a9aa(
    points: tuple[tuple[int, int], ...],
) -> tuple[tuple[int, int], ...]:
    x0 = []
    for x1, x2 in zip(points, points[1:]):
        x3 = line_nodes_9ba4a9aa(x1, x2)
        if len(x0) == 0:
            x0.extend(x3)
        else:
            x0.extend(x3[1:])
    return tuple(x0)


def sample_trunk_9ba4a9aa(
    start: tuple[int, int],
    end: tuple[int, int],
    min_length: int,
) -> tuple[tuple[int, int], ...] | None:
    x0, x1 = start
    x2, x3 = end
    for _ in range(300):
        x4 = choice(("hv", "vh", "hvh", "vhv", "hvhv", "vhvh"))
        if x4 == "hv":
            x5 = (start, (x0, x3), end)
        elif x4 == "vh":
            x5 = (start, (x2, x1), end)
        elif x4 == "hvh":
            x6 = randint(0, LATTICE_SIZE_9BA4A9AA - 1)
            x5 = (start, (x0, x6), (x2, x6), end)
        elif x4 == "vhv":
            x6 = randint(0, LATTICE_SIZE_9BA4A9AA - 1)
            x5 = (start, (x6, x1), (x6, x3), end)
        elif x4 == "hvhv":
            x6 = randint(0, LATTICE_SIZE_9BA4A9AA - 1)
            x7 = randint(0, LATTICE_SIZE_9BA4A9AA - 1)
            x5 = (start, (x0, x6), (x7, x6), (x7, x3), end)
        else:
            x6 = randint(0, LATTICE_SIZE_9BA4A9AA - 1)
            x7 = randint(0, LATTICE_SIZE_9BA4A9AA - 1)
            x5 = (start, (x6, x1), (x6, x7), (x2, x7), end)
        x8 = expand_polyline_9ba4a9aa(x5)
        if len(x8) < min_length:
            continue
        if len(set(x8)) != len(x8):
            continue
        return x8
    return None


def chebyshev_9ba4a9aa(
    a: tuple[int, int],
    b: tuple[int, int],
) -> int:
    return max(abs(a[0] - b[0]), abs(a[1] - b[1]))


def bfs_path_9ba4a9aa(
    starts: tuple[tuple[int, int], ...],
    goals: frozenset[tuple[int, int]],
    blocked: frozenset[tuple[int, int]],
) -> tuple[tuple[int, int], ...] | None:
    x0 = deque()
    x1 = {}
    for x2 in starts:
        if x2 in blocked:
            continue
        x0.append(x2)
        x1[x2] = None
    while len(x0) > 0:
        x2 = x0.popleft()
        if x2 in goals:
            x3 = []
            while x2 is not None:
                x3.append(x2)
                x2 = x1[x2]
            x3.reverse()
            return tuple(x3)
        for x4 in lattice_neighbors_9ba4a9aa(x2):
            if x4 in blocked or x4 in x1:
                continue
            x1[x4] = x2
            x0.append(x4)
    return None
