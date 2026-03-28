from synth_rearc.core import *


GRID_SHAPE_F1BCBC2C = (TEN, TEN)

DIRECTIONS_F1BCBC2C = (
    ("U", (-ONE, ZERO)),
    ("D", (ONE, ZERO)),
    ("L", (ZERO, -ONE)),
    ("R", (ZERO, ONE)),
)

PERPENDICULAR_F1BCBC2C = {
    "U": ("L", "R"),
    "D": ("L", "R"),
    "L": ("U", "D"),
    "R": ("U", "D"),
}

STRAIGHT_DIRECTIONS_F1BCBC2C = (
    frozenset({"U", "D"}),
    frozenset({"L", "R"}),
)


def adjacent_seven_dirs_f1bcbc2c(
    grid: Grid,
    loc: tuple[int, int],
) -> tuple[str, ...]:
    h, w = shape(grid)
    i, j = loc
    dirs = []
    for name, (di, dj) in DIRECTIONS_F1BCBC2C:
        ni, nj = i + di, j + dj
        if 0 <= ni < h and 0 <= nj < w and grid[ni][nj] == SEVEN:
            dirs.append(name)
    return tuple(dirs)


def is_straight_dirs_f1bcbc2c(
    dirs: tuple[str, ...],
) -> bool:
    return frozenset(dirs) in STRAIGHT_DIRECTIONS_F1BCBC2C


def corridor_cells_f1bcbc2c(
    grid: Grid,
) -> Indices:
    h, w = shape(grid)
    cells = set()
    for i in range(h):
        for j in range(w):
            if grid[i][j] == SEVEN:
                continue
            if len(adjacent_seven_dirs_f1bcbc2c(grid, (i, j))) == TWO:
                cells.add((i, j))
    return frozenset(cells)


def connected_components_f1bcbc2c(
    cells: Patch,
) -> tuple[Indices, ...]:
    remaining = set(toindices(cells))
    comps = []
    while len(remaining) > ZERO:
        start = remaining.pop()
        frontier = {start}
        comp = {start}
        while len(frontier) > ZERO:
            next_frontier = set()
            for cell in frontier:
                for nb in dneighbors(cell):
                    if nb in remaining:
                        remaining.remove(nb)
                        comp.add(nb)
                        next_frontier.add(nb)
            frontier = next_frontier
        comps.append(frozenset(comp))
    return tuple(comps)


def walk_segment_f1bcbc2c(
    start: tuple[int, int],
    end: tuple[int, int],
) -> tuple[tuple[int, int], ...]:
    i0, j0 = start
    i1, j1 = end
    if i0 == i1:
        step = ONE if j1 >= j0 else -ONE
        return tuple((i0, j) for j in range(j0, j1 + step, step))
    step = ONE if i1 >= i0 else -ONE
    return tuple((i, j0) for i in range(i0, i1 + step, step))


def polyline_f1bcbc2c(
    points: tuple[tuple[int, int], ...],
) -> tuple[tuple[int, int], ...]:
    path = []
    for idx in range(len(points) - ONE):
        seg = walk_segment_f1bcbc2c(points[idx], points[idx + ONE])
        if idx > ZERO:
            seg = seg[ONE:]
        path.extend(seg)
    return tuple(path)


def path_neighbors_f1bcbc2c(
    path: Patch,
    loc: tuple[int, int],
) -> tuple[str, ...]:
    patch = toindices(path)
    i, j = loc
    dirs = []
    for name, (di, dj) in DIRECTIONS_F1BCBC2C:
        if (i + di, j + dj) in patch:
            dirs.append(name)
    return tuple(dirs)


def walls_from_path_f1bcbc2c(
    path: tuple[tuple[int, int], ...],
) -> Indices:
    patch = frozenset(path)
    walls = set()
    for loc in path:
        dirs = path_neighbors_f1bcbc2c(patch, loc)
        if len(dirs) == ONE:
            wall_dirs = PERPENDICULAR_F1BCBC2C[first(dirs)]
        elif is_straight_dirs_f1bcbc2c(dirs):
            wall_dirs = PERPENDICULAR_F1BCBC2C[first(dirs)]
        else:
            wall_dirs = tuple(name for name, _ in DIRECTIONS_F1BCBC2C if name not in dirs)
        i, j = loc
        offsets = []
        for name in wall_dirs:
            di, dj = dict(DIRECTIONS_F1BCBC2C)[name]
            walls.add((i + di, j + dj))
            offsets.append((di, dj))
        if len(dirs) == TWO and not is_straight_dirs_f1bcbc2c(dirs):
            (di0, dj0), (di1, dj1) = offsets
            walls.add((i + di0 + di1, j + dj0 + dj1))
    return frozenset(walls)
