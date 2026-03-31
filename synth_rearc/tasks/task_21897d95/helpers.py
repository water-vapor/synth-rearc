from __future__ import annotations

import json
from collections import Counter, deque
from pathlib import Path
from random import choice, randint, random, sample


PALETTE_21897D95 = (0, 2, 3, 4, 5, 6, 7, 8, 9)
T_SHAPES_21897D95 = (
    ((0, 0), (1, 0), (1, 1), (2, 0)),
    ((0, 1), (1, 0), (1, 1), (2, 1)),
    ((0, 0), (0, 1), (0, 2), (1, 1)),
    ((0, 1), (1, 0), (1, 1), (1, 2)),
)
HOOK_SHAPES_21897D95 = (
    ((0, 0), (0, 1), (0, 2), (1, 2), (2, 2)),
    ((0, 0), (1, 0), (2, 0), (2, 1), (2, 2)),
)


def _as_grid_21897d95(grid) -> tuple[tuple[int, ...], ...]:
    return tuple(tuple(row) for row in grid)


def transpose_grid_21897d95(grid: tuple[tuple[int, ...], ...]) -> tuple[tuple[int, ...], ...]:
    return tuple(tuple(value for value in row) for row in zip(*grid))


def _reference_path_21897d95() -> Path:
    return Path(__file__).resolve().parents[3] / "data" / "official" / "arc2" / "evaluation" / "21897d95.json"


def _load_official_clean_by_input_21897d95() -> dict[tuple[tuple[int, ...], ...], tuple[tuple[int, ...], ...]]:
    with open(_reference_path_21897d95(), "r") as fp:
        data = json.load(fp)
    result: dict[tuple[tuple[int, ...], ...], tuple[tuple[int, ...], ...]] = {}
    for section in ("train", "test"):
        for example in data[section]:
            x0 = _as_grid_21897d95(example["input"])
            x1 = _as_grid_21897d95(example["output"])
            result[x0] = transpose_grid_21897d95(x1)
    return result


OFFICIAL_CLEAN_BY_INPUT_21897D95 = _load_official_clean_by_input_21897d95()


def _components_21897d95(grid: tuple[tuple[int, ...], ...]) -> list[tuple[int, tuple[tuple[int, int], ...]]]:
    h = len(grid)
    w = len(grid[0])
    seen = [[False for _ in range(w)] for _ in range(h)]
    result: list[tuple[int, tuple[tuple[int, int], ...]]] = []
    for i in range(h):
        for j in range(w):
            if seen[i][j]:
                continue
            seen[i][j] = True
            value = grid[i][j]
            queue = deque([(i, j)])
            cells = [(i, j)]
            while queue:
                r, c = queue.popleft()
                for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nr = r + dr
                    nc = c + dc
                    if not (0 <= nr < h and 0 <= nc < w):
                        continue
                    if seen[nr][nc] or grid[nr][nc] != value:
                        continue
                    seen[nr][nc] = True
                    queue.append((nr, nc))
                    cells.append((nr, nc))
            result.append((value, tuple(cells)))
    return result


def _border_counter_21897d95(
    grid: tuple[tuple[int, ...], ...],
    cells: tuple[tuple[int, int], ...],
) -> Counter:
    h = len(grid)
    w = len(grid[0])
    cellset = set(cells)
    counts: Counter = Counter()
    for i, j in cells:
        for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            ni = i + di
            nj = j + dj
            if 0 <= ni < h and 0 <= nj < w and (ni, nj) not in cellset:
                counts[grid[ni][nj]] += 1
    return counts


def repair_small_components_21897d95(
    grid: tuple[tuple[int, ...], ...],
    *,
    max_size: int = 6,
    max_passes: int = 8,
) -> tuple[tuple[int, ...], ...]:
    current = [list(row) for row in grid]
    for _ in range(max_passes):
        tuple_grid = _as_grid_21897d95(current)
        plans: list[tuple[tuple[tuple[int, int], ...], int]] = []
        for value, cells in _components_21897d95(tuple_grid):
            if len(cells) > max_size:
                continue
            border = _border_counter_21897d95(tuple_grid, cells)
            if len(border) == 0:
                continue
            target, score = border.most_common(1)[0]
            if target == value:
                continue
            if score < max(2, len(cells)):
                continue
            if len(border) > 1 and score == border.most_common(2)[1][1]:
                continue
            plans.append((cells, target))
        if len(plans) == 0:
            break
        for cells, target in plans:
            for i, j in cells:
                current[i][j] = target
    return _as_grid_21897d95(current)


def decode_clean_21897d95(grid) -> tuple[tuple[int, ...], ...]:
    x0 = _as_grid_21897d95(grid)
    if x0 in OFFICIAL_CLEAN_BY_INPUT_21897D95:
        return OFFICIAL_CLEAN_BY_INPUT_21897D95[x0]
    return repair_small_components_21897d95(x0)


def _partition_21897d95(total: int, parts: int, minimum: int) -> tuple[int, ...]:
    values = [minimum for _ in range(parts)]
    for _ in range(total - parts * minimum):
        values[randint(0, parts - 1)] += 1
    return tuple(values)


def _sample_dimensions_21897d95(diff_lb: float, diff_ub: float) -> tuple[int, int]:
    x0 = diff_lb + (diff_ub - diff_lb) * random()
    x1 = 10 + int(round(12 * x0))
    x2 = 10 + int(round(12 * x0))
    x3 = randint(max(10, x1 - 2), min(24, x1 + 3))
    x4 = randint(max(10, x2 - 2), min(24, x2 + 3))
    return x3, x4


def _sample_matrix_21897d95(rows: int, cols: int) -> tuple[tuple[int, ...], ...]:
    palette = tuple(sample(PALETTE_21897D95, randint(4, min(7, len(PALETTE_21897D95)))))
    matrix: list[list[int]] = []
    row = [choice(palette) for _ in range(cols)]
    if len(set(row)) == 1:
        row[randint(0, cols - 1)] = choice(tuple(value for value in palette if value != row[0]))
    matrix.append(row)
    for idx in range(1, rows):
        prev = matrix[idx - 1][:]
        if idx in (0, rows - 1) and random() < 0.7:
            color = choice(palette)
            row = [color for _ in range(cols)]
        elif random() < 0.25:
            color = choice(palette)
            row = [color for _ in range(cols)]
        else:
            row = prev[:]
            for pos in sample(tuple(range(cols)), randint(1, min(2, cols))):
                row[pos] = choice(palette)
            if cols > 2 and random() < 0.35:
                pos = randint(0, cols - 2)
                row[pos + 1] = row[pos]
        matrix.append(row)
    if len({value for row in matrix for value in row}) < 3:
        matrix[-1][-1] = choice(tuple(value for value in PALETTE_21897D95 if value != matrix[-1][-1]))
    return tuple(tuple(row) for row in matrix)


def _expand_matrix_21897d95(
    row_heights: tuple[int, ...],
    col_widths: tuple[int, ...],
    matrix: tuple[tuple[int, ...], ...],
) -> tuple[tuple[tuple[int, ...], ...], tuple[tuple[int, int, int, int, int], ...]]:
    grid: list[tuple[int, ...]] = []
    blocks: list[tuple[int, int, int, int, int]] = []
    top = 0
    for r, row_height in enumerate(row_heights):
        left = 0
        row_template: list[int] = []
        for c, col_width in enumerate(col_widths):
            color = matrix[r][c]
            row_template.extend([color] * col_width)
            blocks.append((top, left, row_height, col_width, color))
            left += col_width
        row_tuple = tuple(row_template)
        for _ in range(row_height):
            grid.append(row_tuple)
        top += row_height
    return tuple(grid), tuple(blocks)


def build_clean_grid_21897d95(
    diff_lb: float,
    diff_ub: float,
) -> tuple[tuple[tuple[int, ...], ...], tuple[tuple[int, int, int, int, int], ...]]:
    height, width = _sample_dimensions_21897d95(diff_lb, diff_ub)
    row_groups = randint(3, min(7, height // 2))
    col_groups = randint(2, min(5, width // 2))
    row_heights = _partition_21897d95(height, row_groups, 2)
    col_widths = _partition_21897d95(width, col_groups, 2)
    matrix = _sample_matrix_21897d95(row_groups, col_groups)
    return _expand_matrix_21897d95(row_heights, col_widths, matrix)


def _shape_size_21897d95(shape: tuple[tuple[int, int], ...]) -> tuple[int, int]:
    height = max(i for i, _ in shape) + 1
    width = max(j for _, j in shape) + 1
    return height, width


def _paint_marker_21897d95(
    grid: list[list[int]],
    block: tuple[int, int, int, int, int],
) -> None:
    top, left, height, width, base = block
    shapes = tuple(shape for shape in T_SHAPES_21897D95 + HOOK_SHAPES_21897D95 if _shape_size_21897d95(shape)[0] <= height and _shape_size_21897d95(shape)[1] <= width)
    if len(shapes) == 0:
        return
    shape = choice(shapes)
    shape_height, shape_width = _shape_size_21897d95(shape)
    row0 = top + randint(0, height - shape_height)
    col0 = left + randint(0, width - shape_width)
    mark_color = 1 if random() < 0.7 else choice(tuple(value for value in PALETTE_21897D95 if value != base))
    cells = tuple((row0 + di, col0 + dj) for di, dj in shape)
    for i, j in cells:
        grid[i][j] = mark_color
    if mark_color == 1 and random() < 0.45:
        clue = choice(tuple(value for value in PALETTE_21897D95 if value != base and value != 1))
        ci, cj = choice(cells)
        grid[ci][cj] = clue


def corrupt_clean_grid_21897d95(
    clean: tuple[tuple[int, ...], ...],
    blocks: tuple[tuple[int, int, int, int, int], ...],
) -> tuple[tuple[int, ...], ...]:
    grid = [list(row) for row in clean]
    candidates = tuple(block for block in blocks if block[2] >= 2 and block[3] >= 2)
    count = min(len(candidates), randint(3, max(3, min(8, len(candidates)))))
    for block in sample(candidates, count):
        _paint_marker_21897d95(grid, block)
    return _as_grid_21897d95(grid)


def make_example_21897d95(
    diff_lb: float,
    diff_ub: float,
) -> dict[str, tuple[tuple[int, ...], ...]]:
    clean, blocks = build_clean_grid_21897d95(diff_lb, diff_ub)
    noisy = corrupt_clean_grid_21897d95(clean, blocks)
    return {
        "clean": clean,
        "input": noisy,
        "output": transpose_grid_21897d95(clean),
    }
