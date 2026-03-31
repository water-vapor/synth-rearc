from synth_rearc.core import *

from .verifier import verify_8f3a5a89


GRID_BOUNDS_8F3A5A89 = (10, 22)
TEMPLATES_8F3A5A89 = ("vertical", "cavity", "stair")
ISLAND_SHAPES_8F3A5A89 = ((ONE, ONE), (ONE, TWO), (TWO, ONE), (TWO, TWO))


def _rect_patch_8f3a5a89(
    top: Integer,
    left: Integer,
    height_value: Integer,
    width_value: Integer,
) -> Indices:
    return frozenset((i, j) for i in range(top, top + height_value) for j in range(left, left + width_value))


def _stair_patch_8f3a5a89(
    top: Integer,
    widths: tuple[Integer, ...],
) -> Indices:
    return frozenset((top + i, j) for i, width_value in enumerate(widths) for j in range(width_value))


def _paint_input_8f3a5a89(
    side: Integer,
    walls: Indices,
) -> Grid:
    x0 = canvas(EIGHT, (side, side))
    x1 = fill(x0, ONE, walls)
    x2 = fill(x1, SIX, frozenset({(side - ONE, ZERO)}))
    return x2


def _analysis_8f3a5a89(
    grid: Grid,
) -> tuple[Grid, Indices, Indices, Indices, Indices]:
    h, w = len(grid), len(grid[0])
    anchor = (h - 1, 0)
    region = {anchor}
    frontier = [anchor]
    while frontier:
        i, j = frontier.pop()
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = i + di, j + dj
            if not (0 <= ni < h and 0 <= nj < w):
                continue
            if (ni, nj) in region or grid[ni][nj] == ONE:
                continue
            region.add((ni, nj))
            frontier.append((ni, nj))
    all_cells = {(i, j) for i in range(h) for j in range(w)}
    complement = all_cells - region
    outside = set()
    shell = []
    for cell in complement:
        i, j = cell
        if i in (0, h - 1) or j in (0, w - 1):
            outside.add(cell)
            shell.append(cell)
    while shell:
        i, j = shell.pop()
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = i + di, j + dj
            nxt = (ni, nj)
            if 0 <= ni < h and 0 <= nj < w and nxt in complement and nxt not in outside:
                outside.add(nxt)
                shell.append(nxt)
    filled = region | (complement - outside)
    boundary = set()
    for i, j in region:
        if (i, j) == anchor:
            continue
        for di in (-1, 0, 1):
            for dj in (-1, 0, 1):
                if (di, dj) == (0, 0):
                    continue
                if (i + di, j + dj) not in filled:
                    boundary.add((i, j))
                    break
            else:
                continue
            break
    kept_walls = mapply(
        toindices,
        sfilter(objects(grid, T, F, F), lambda x: both(equality(color(x), ONE), adjacent(x, region))),
    )
    unreachable = frozenset((i, j) for i, j in outside if grid[i][j] == EIGHT)
    output = canvas(EIGHT, (h, w))
    output = fill(output, ONE, kept_walls)
    output = fill(output, SEVEN, boundary)
    output = fill(output, SIX, frozenset({anchor}))
    return output, frozenset(region), frozenset(filled), frozenset(boundary), unreachable


def _add_island_8f3a5a89(
    side: Integer,
    walls: Indices,
) -> Indices:
    grid = _paint_input_8f3a5a89(side, walls)
    _, region, _, boundary, _ = _analysis_8f3a5a89(grid)
    region = region - frozenset({(side - ONE, ZERO)})
    choices = []
    for height_value, width_value in ISLAND_SHAPES_8F3A5A89:
        limit_i = side - height_value
        limit_j = side - width_value
        for top in range(ONE, limit_i):
            for left in range(ONE, limit_j):
                patch = _rect_patch_8f3a5a89(top, left, height_value, width_value)
                halo = frozenset(
                    (i, j)
                    for i in range(top - ONE, top + height_value + ONE)
                    for j in range(left - ONE, left + width_value + ONE)
                )
                if not patch <= region:
                    continue
                if not halo <= region:
                    continue
                if patch & boundary:
                    continue
                choices.append(patch)
    if len(choices) == ZERO:
        return walls
    x0 = choice(choices)
    return combine(walls, x0)


def _vertical_candidate_8f3a5a89(
    diff_lb: float,
    diff_ub: float,
) -> Grid:
    x0 = unifint(diff_lb, diff_ub, GRID_BOUNDS_8F3A5A89)
    x1 = unifint(diff_lb, diff_ub, (max(3, x0 // 4), x0 - FOUR))
    x2 = choice((ONE, ONE, TWO, TWO, THREE))
    x3 = _rect_patch_8f3a5a89(ZERO, x1, x0, x2)
    x4 = [x3]
    x5 = unifint(diff_lb, diff_ub, (ONE, THREE))
    for _ in range(x5):
        x6 = choice(("top", "middle", "bottom"))
        x7 = unifint(diff_lb, diff_ub, (TWO, max(TWO, x0 // 3)))
        x8 = unifint(diff_lb, diff_ub, (TWO, max(TWO, x0 // 3)))
        x9 = unifint(diff_lb, diff_ub, (x1 + x2 + ONE, x0 - x8))
        if x6 == "top":
            x10 = ZERO
        elif x6 == "bottom":
            x10 = x0 - x7
        else:
            x10 = unifint(diff_lb, diff_ub, (ONE, x0 - x7 - ONE))
        x4.append(_rect_patch_8f3a5a89(x10, x9, x7, x8))
    x11 = merge(tuple(x4))
    if choice((T, F)):
        x11 = _add_island_8f3a5a89(x0, x11)
    return _paint_input_8f3a5a89(x0, x11)


def _cavity_candidate_8f3a5a89(
    diff_lb: float,
    diff_ub: float,
) -> Grid:
    x0 = unifint(diff_lb, diff_ub, GRID_BOUNDS_8F3A5A89)
    x1 = unifint(diff_lb, diff_ub, (ONE, TWO))
    x2 = unifint(diff_lb, diff_ub, (ONE, THREE))
    x3 = unifint(diff_lb, diff_ub, (TWO, max(TWO, x0 // 3)))
    x4 = unifint(diff_lb, diff_ub, (TWO, x0 - x3 - THREE))
    x5 = _rect_patch_8f3a5a89(ZERO, x4, x1, x3)
    x6 = unifint(diff_lb, diff_ub, (ONE, THREE))
    x7 = unifint(diff_lb, diff_ub, (TWO, max(TWO, x0 // 3)))
    x8 = unifint(diff_lb, diff_ub, (TWO, x0 - x7 - THREE))
    x9 = _rect_patch_8f3a5a89(x8, x0 - x6, x7, x6)
    x10 = unifint(diff_lb, diff_ub, (ONE, TWO))
    x11 = unifint(diff_lb, diff_ub, (TWO, max(TWO, x0 // 3)))
    x12 = unifint(diff_lb, diff_ub, (TWO, x0 - x11 - THREE))
    x13 = _rect_patch_8f3a5a89(x0 - x10, x12, x10, x11)
    x14 = choice((ONE, ONE, TWO))
    x15 = unifint(diff_lb, diff_ub, (ONE, max(ONE, x0 // 4)))
    x16 = unifint(diff_lb, diff_ub, (ONE, x0 - x15 - THREE))
    x17 = _rect_patch_8f3a5a89(x16, ZERO, x15, x14)
    x18 = [x5, x9, x13, x17]
    if choice((T, T, F)):
        x19 = unifint(diff_lb, diff_ub, (ONE, TWO))
        x20 = unifint(diff_lb, diff_ub, (ONE, max(ONE, x0 // 4)))
        x21 = unifint(diff_lb, diff_ub, (ONE, x0 - x20 - TWO))
        x22 = unifint(diff_lb, diff_ub, (ONE, x0 - x19 - TWO))
        x18.append(_rect_patch_8f3a5a89(x21, x22, x20, x19))
    x23 = merge(tuple(x18))
    if choice((T, F)):
        x23 = _add_island_8f3a5a89(x0, x23)
    return _paint_input_8f3a5a89(x0, x23)


def _stair_candidate_8f3a5a89(
    diff_lb: float,
    diff_ub: float,
) -> Grid:
    x0 = unifint(diff_lb, diff_ub, (12, 22))
    x1 = unifint(diff_lb, diff_ub, (TWO, max(TWO, x0 // 4)))
    x2 = unifint(diff_lb, diff_ub, (FOUR, max(FOUR, x0 // 2)))
    x3 = choice((ONE, TWO))
    x4 = []
    x5 = x3
    x6 = choice((TWO, THREE, FOUR))
    for x7 in range(x2):
        if x7 < x6:
            x5 = min(x0 // 2, x5 + choice((ZERO, ONE)))
        else:
            x5 = max(ONE, x5 - choice((ZERO, ONE)))
        x4.append(x5)
    x8 = _stair_patch_8f3a5a89(x1, tuple(x4))
    x9 = unifint(diff_lb, diff_ub, (max(x4) + THREE, x0 - FOUR))
    x10 = choice((ONE, ONE, TWO))
    x11 = unifint(diff_lb, diff_ub, (x0 - THREE, x0))
    x12 = _rect_patch_8f3a5a89(ZERO, x9, x11, x10)
    x13 = unifint(diff_lb, diff_ub, (TWO, max(TWO, x0 // 3)))
    x14 = unifint(diff_lb, diff_ub, (THREE, max(THREE, x0 // 3)))
    x15 = _rect_patch_8f3a5a89(x0 - x13, x0 - x14, x13, x14)
    x16 = [x8, x12, x15]
    if choice((T, F)):
        x17 = choice((ONE, TWO))
        x18 = unifint(diff_lb, diff_ub, (TWO, max(TWO, x0 // 4)))
        x19 = unifint(diff_lb, diff_ub, (ONE, x0 - x18 - TWO))
        x20 = unifint(diff_lb, diff_ub, (x9 + x10 + ONE, x0 - x17 - ONE))
        x16.append(_rect_patch_8f3a5a89(x19, x20, x18, x17))
    x21 = merge(tuple(x16))
    if choice((T, T, F)):
        x21 = _add_island_8f3a5a89(x0, x21)
    return _paint_input_8f3a5a89(x0, x21)


def _candidate_8f3a5a89(
    diff_lb: float,
    diff_ub: float,
) -> Grid:
    x0 = choice(TEMPLATES_8F3A5A89)
    if x0 == "vertical":
        return _vertical_candidate_8f3a5a89(diff_lb, diff_ub)
    if x0 == "cavity":
        return _cavity_candidate_8f3a5a89(diff_lb, diff_ub)
    return _stair_candidate_8f3a5a89(diff_lb, diff_ub)


def generate_8f3a5a89(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = _candidate_8f3a5a89(diff_lb, diff_ub)
        x1, x2, _, x3, x4 = _analysis_8f3a5a89(x0)
        x5 = size(x2)
        x6 = size(x3)
        x7 = size(x4)
        x8 = size(ofcolor(x0, ONE))
        x9 = size(colorfilter(objects(x0, T, F, F), ONE))
        x10 = height(x0)
        if x7 < max(FIVE, x10 // TWO):
            continue
        if x6 < max(TEN, x10 + x10 // TWO):
            continue
        if x8 < x10:
            continue
        if x9 < TWO:
            continue
        if x5 <= x6:
            continue
        if x1 != verify_8f3a5a89(x0):
            continue
        return {"input": x0, "output": x1}
