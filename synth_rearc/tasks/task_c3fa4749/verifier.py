from synth_rearc.core import *


MIN_SIDE_C3FA4749 = FIVE
MIN_FILL_C3FA4749 = THREE


def _prefix_counts_c3fa4749(
    grid: Grid,
):
    h = len(grid)
    w = len(grid[ZERO])
    prefixes = []
    for value in range(TEN):
        prefix = [[ZERO for _ in range(w + ONE)] for _ in range(h + ONE)]
        for i in range(ONE, h + ONE):
            row_sum = ZERO
            for j in range(ONE, w + ONE):
                if grid[i - ONE][j - ONE] == value:
                    row_sum += ONE
                prefix[i][j] = prefix[i - ONE][j] + row_sum
        prefixes.append(prefix)
    return tuple(tuple(tuple(row) for row in prefix) for prefix in prefixes)


def _rect_count_c3fa4749(
    prefix,
    top: Integer,
    bottom: Integer,
    left: Integer,
    right: Integer,
) -> Integer:
    return (
        prefix[bottom + ONE][right + ONE]
        - prefix[top][right + ONE]
        - prefix[bottom + ONE][left]
        + prefix[top][left]
    )


def _rectangle_fill_ops_c3fa4749(
    grid: Grid,
    top: Integer,
    bottom: Integer,
    left: Integer,
    right: Integer,
    bg: Integer,
):
    rect = [row[left:right + ONE] for row in grid[top:bottom + ONE]]
    h = len(rect)
    w = len(rect[ZERO])
    seen = set()
    non_bg_components = []
    for i in range(h):
        for j in range(w):
            if rect[i][j] == bg or (i, j) in seen:
                continue
            stack = [(i, j)]
            seen.add((i, j))
            component = set()
            while stack:
                ci, cj = stack.pop()
                component.add((ci, cj))
                for ni, nj in ((ci - ONE, cj), (ci + ONE, cj), (ci, cj - ONE), (ci, cj + ONE)):
                    if not (ZERO <= ni < h and ZERO <= nj < w):
                        continue
                    if rect[ni][nj] == bg or (ni, nj) in seen:
                        continue
                    seen.add((ni, nj))
                    stack.append((ni, nj))
            non_bg_components.append(component)
    seen = set()
    bg_components = []
    for i in range(h):
        for j in range(w):
            if rect[i][j] != bg or (i, j) in seen:
                continue
            stack = [(i, j)]
            seen.add((i, j))
            component = set()
            touches_border = False
            while stack:
                ci, cj = stack.pop()
                component.add((ci, cj))
                if ci in (ZERO, h - ONE) or cj in (ZERO, w - ONE):
                    touches_border = True
                for ni, nj in ((ci - ONE, cj), (ci + ONE, cj), (ci, cj - ONE), (ci, cj + ONE)):
                    if not (ZERO <= ni < h and ZERO <= nj < w):
                        continue
                    if rect[ni][nj] != bg or (ni, nj) in seen:
                        continue
                    seen.add((ni, nj))
                    stack.append((ni, nj))
            bg_components.append((component, touches_border))
    fill_ops = []
    for component in non_bg_components:
        border_hits = frozenset(
            (i, j)
            for i, j in component
            if i in (ZERO, h - ONE) or j in (ZERO, w - ONE)
        )
        if len(border_hits) != ONE:
            continue
        hit_i, hit_j = next(iter(border_hits))
        fill_cells = set(component)
        for bg_component, touches_border in bg_components:
            if touches_border:
                continue
            adjacent = False
            for ai, aj in bg_component:
                if (
                    (ai - ONE, aj) in component
                    or (ai + ONE, aj) in component
                    or (ai, aj - ONE) in component
                    or (ai, aj + ONE) in component
                ):
                    adjacent = True
                    break
            if adjacent:
                fill_cells |= bg_component
        if len(fill_cells) < MIN_FILL_C3FA4749:
            continue
        color = rect[hit_i][hit_j]
        global_cells = frozenset((top + i, left + j) for i, j in fill_cells)
        fill_ops.append((color, global_cells))
    return tuple(fill_ops)


def verify_c3fa4749(
    I: Grid,
) -> Grid:
    x0 = len(I)
    x1 = len(I[ZERO])
    x2 = _prefix_counts_c3fa4749(I)
    x3 = []
    for x4 in range(x0 - MIN_SIDE_C3FA4749 + ONE):
        for x5 in range(x4 + MIN_SIDE_C3FA4749 - ONE, x0):
            x6 = x5 - x4 + ONE
            for x7 in range(x1 - MIN_SIDE_C3FA4749 + ONE):
                for x8 in range(x7 + MIN_SIDE_C3FA4749 - ONE, x1):
                    x9 = x8 - x7 + ONE
                    x10 = x6 * x9
                    x11 = tuple(_rect_count_c3fa4749(x2[value], x4, x5, x7, x8) for value in range(TEN))
                    x12 = max(range(TEN), key=x11.__getitem__)
                    x13 = x11[x12]
                    if x13 * TEN < x10 * SEVEN:
                        continue
                    x14 = _rectangle_fill_ops_c3fa4749(I, x4, x5, x7, x8, x12)
                    if len(x14) == ZERO:
                        continue
                    x15 = frozenset()
                    for _, x16 in x14:
                        x15 = x15 | x16
                    x3.append((len(x15), x10, x13, x4, x5, x7, x8, x14))
    x17 = sorted(x3, key=lambda item: item[:SEVEN], reverse=True)
    x18 = {}
    for _, _, _, _, _, _, _, x19 in x17:
        x20 = False
        x21 = False
        for x22, x23 in x19:
            for x24 in x23:
                if x24 in x18 and x18[x24] != x22:
                    x21 = True
                    break
                if x24 not in x18:
                    x20 = True
            if x21:
                break
        if x21 or not x20:
            continue
        for x22, x23 in x19:
            for x24 in x23:
                if x24 not in x18:
                    x18[x24] = x22
    x25 = I
    for x26, x27 in x18.items():
        x25 = fill(x25, x27, initset(x26))
    return x25
