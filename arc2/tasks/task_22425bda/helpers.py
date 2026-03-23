from __future__ import annotations

from arc2.core import *


Line22425bda = tuple[int, str, int]


def line_patch_22425bda(
    dims: tuple[int, int],
    kind: str,
    param: int,
) -> Indices:
    h, w = dims
    if kind == "h":
        return connect((param, ZERO), (param, w - ONE))
    if kind == "v":
        return connect((ZERO, param), (h - ONE, param))
    if kind == "d":
        x0 = max(ZERO, -param)
        x1 = max(ZERO, param)
        x2 = min(h - x0, w - x1)
        return frozenset((x0 + k, x1 + k) for k in range(x2))
    x0 = max(ZERO, param - (w - ONE))
    x1 = min(h - ONE, param)
    return frozenset((i, param - i) for i in range(x0, x1 + ONE))


def extract_lines_22425bda(
    grid: Grid,
) -> tuple[Line22425bda, ...]:
    x0 = mostcolor(grid)
    x1 = tuple(sorted(v for v in palette(grid) if v != x0))
    x2: list[Line22425bda] = []
    for x3 in x1:
        x4 = ofcolor(grid, x3)
        x5 = {i for i, _ in x4}
        x6 = {j for _, j in x4}
        x7 = {j - i for i, j in x4}
        x8 = {i + j for i, j in x4}
        if len(x5) == ONE:
            x9 = ("h", next(iter(x5)))
        elif len(x6) == ONE:
            x9 = ("v", next(iter(x6)))
        elif len(x7) == ONE:
            x9 = ("d", next(iter(x7)))
        elif len(x8) == ONE:
            x9 = ("a", next(iter(x8)))
        else:
            raise ValueError(f"color {x3} is not a single straight line")
        x2.append((x3, x9[ZERO], x9[ONE]))
    return tuple(x2)


def line_hidden_count_22425bda(
    grid: Grid,
    line: Line22425bda,
) -> int:
    x0, x1, x2 = line
    x3 = line_patch_22425bda(shape(grid), x1, x2)
    x4 = sum(ONE for i, j in x3 if grid[i][j] == x0)
    return size(x3) - x4


def line_sector_22425bda(
    grid: Grid,
    line: Line22425bda,
) -> int:
    _, x0, x1 = line
    x2 = width(grid) - ONE
    if x0 == "a":
        return ZERO if x1 < x2 else FIVE
    if x0 == "v":
        return ONE
    if x0 == "d":
        return TWO if x1 < ZERO else FOUR
    return THREE


def line_sort_key_22425bda(
    grid: Grid,
    line: Line22425bda,
) -> tuple[int, int, int]:
    x0 = line_hidden_count_22425bda(grid, line)
    x1 = line_sector_22425bda(grid, line)
    return (-x0, x1, line[TWO])


def paint_lines_22425bda(
    dims: tuple[int, int],
    bg: int,
    lines: tuple[Line22425bda, ...],
) -> Grid:
    x0 = canvas(bg, dims)
    for x1, x2, x3 in lines:
        x0 = fill(x0, x1, line_patch_22425bda(dims, x2, x3))
    return x0


def output_from_lines_22425bda(
    lines: tuple[Line22425bda, ...],
) -> Grid:
    return (tuple(x0 for x0, _, _ in lines),)


def order_lines_22425bda(
    grid: Grid,
) -> tuple[Line22425bda, ...]:
    x0 = extract_lines_22425bda(grid)
    return tuple(sorted(x0, key=lambda x1: line_sort_key_22425bda(grid, x1)))
