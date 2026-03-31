from __future__ import annotations

from synth_rearc.core import *

from .verifier import verify_47996f11


GRID_SIZE_47996F11 = 30
DRAW_COLORS_47996F11 = tuple(remove(SIX, remove(ZERO, interval(ZERO, TEN, ONE))))
TEMPLATES_47996F11 = (
    (
        ".#.",
        "###",
        ".#.",
    ),
    (
        "###",
        "#.#",
        "###",
    ),
    (
        "##.",
        ".##",
        "##.",
    ),
    (
        "#.#",
        "###",
        "#.#",
    ),
    (
        ".##.",
        "####",
        ".##.",
    ),
    (
        "###.",
        ".###",
        "###.",
        ".###",
    ),
    (
        "##",
        "##",
    ),
    (
        "####",
        "#..#",
        "####",
    ),
)


def _parse_template_47996f11(
    rows: tuple[str, ...],
) -> Indices:
    return frozenset((i, j) for i, row in enumerate(rows) for j, value in enumerate(row) if value == "#")


PARSED_TEMPLATES_47996F11 = tuple(_parse_template_47996f11(rows) for rows in TEMPLATES_47996F11)


def _shift_indices_47996f11(
    patch: Indices,
    offset: IntegerTuple,
) -> Indices:
    di, dj = offset
    return frozenset((i + di, j + dj) for i, j in patch)


def _transpose_indices_47996f11(
    patch: Indices,
) -> Indices:
    return frozenset((j, i) for i, j in patch)


def _paint_indices_47996f11(
    grid: list[list[int]],
    color: Integer,
    patch: Indices,
) -> None:
    for i, j in patch:
        if 0 <= i < GRID_SIZE_47996F11 and 0 <= j < GRID_SIZE_47996F11:
            grid[i][j] = color


def _make_base_47996f11(
    colors: tuple[int, ...],
    diff_lb: float,
    diff_ub: float,
) -> list[list[int]]:
    center = unifint(diff_lb, diff_ub, (11, 17))
    step_a = unifint(diff_lb, diff_ub, (2, 4))
    step_b = unifint(diff_lb, diff_ub, (3, 6))
    mode = choice(("diamond", "square", "hybrid"))
    grid = []
    for i in range(GRID_SIZE_47996F11):
        row = []
        for j in range(GRID_SIZE_47996F11):
            x0 = (abs(i - center) + abs(j - center)) // step_a
            x1 = max(abs(i - center), abs(j - center)) // step_b
            if mode == "diamond":
                x2 = (x0 + ((i + j) % 2)) % len(colors)
            elif mode == "square":
                x2 = (x1 + ((i + j) // (step_a + ONE))) % len(colors)
            else:
                x2 = (x0 + x1 + ((i + j) % 2)) % len(colors)
            row.append(colors[x2])
        grid.append(row)
    return grid


def _diamond_frame_47996f11(
    center: Integer,
    radius: Integer,
    thickness: Integer,
) -> Indices:
    return frozenset(
        (i, j)
        for i in range(GRID_SIZE_47996F11)
        for j in range(GRID_SIZE_47996F11)
        if radius - thickness <= abs(i - center) + abs(j - center) <= radius
    )


def _square_frame_47996f11(
    center: Integer,
    radius: Integer,
    thickness: Integer,
) -> Indices:
    return frozenset(
        (i, j)
        for i in range(GRID_SIZE_47996F11)
        for j in range(GRID_SIZE_47996F11)
        if radius - thickness <= max(abs(i - center), abs(j - center)) <= radius
    )


def _decorate_with_centerpiece_47996f11(
    grid: list[list[int]],
    colors: tuple[int, ...],
    diff_lb: float,
    diff_ub: float,
) -> None:
    center = unifint(diff_lb, diff_ub, (12, 16))
    nring = unifint(diff_lb, diff_ub, (3, 5))
    radii = sorted(sample(tuple(range(2, 12)), nring))
    color_cycle = tuple(sample(colors, min(len(colors), nring + TWO)))
    for idx, radius in enumerate(radii):
        color = color_cycle[idx % len(color_cycle)]
        if idx % TWO == ZERO:
            patch = _diamond_frame_47996f11(center, radius + ONE, ONE)
        else:
            patch = _square_frame_47996f11(center, radius + TWO, ONE)
        _paint_indices_47996f11(grid, color, patch)
    core = frozenset(
        (i, j)
        for i in range(center - ONE, center + TWO)
        for j in range(center - ONE, center + TWO)
    )
    _paint_indices_47996f11(grid, choice(colors), core)
    spine = frozenset({(center - TWO, center), (center - ONE, center), (center, center - TWO), (center, center - ONE), (center, center + ONE), (center, center + TWO), (center + ONE, center), (center + TWO, center)})
    _paint_indices_47996f11(grid, choice(colors), spine)


def _decorate_with_tiles_47996f11(
    grid: list[list[int]],
    colors: tuple[int, ...],
    diff_lb: float,
    diff_ub: float,
) -> None:
    ntile = unifint(diff_lb, diff_ub, (8, 12))
    for _ in range(ntile):
        patch = choice(PARSED_TEMPLATES_47996F11)
        h = max(i for i, _ in patch) + 1
        w = max(j for _, j in patch) + 1
        i = randint(ZERO, GRID_SIZE_47996F11 - h)
        if randint(ZERO, FOUR) < THREE:
            j_lb = min(GRID_SIZE_47996F11 - w, i + ONE)
            j = randint(j_lb, GRID_SIZE_47996F11 - w)
        else:
            j = randint(ZERO, GRID_SIZE_47996F11 - w)
        shifted = _shift_indices_47996f11(patch, (i, j))
        color = choice(colors)
        _paint_indices_47996f11(grid, color, shifted)
        _paint_indices_47996f11(grid, color, _transpose_indices_47996f11(shifted))


def _decorate_with_diagonal_blocks_47996f11(
    grid: list[list[int]],
    colors: tuple[int, ...],
    diff_lb: float,
    diff_ub: float,
) -> None:
    nblock = unifint(diff_lb, diff_ub, (2, 5))
    for _ in range(nblock):
        color = choice(colors)
        a = randint(ONE, 12)
        b = randint(a + THREE, min(28, a + 10))
        patch = frozenset(
            (i, j)
            for i in range(a, b + ONE)
            for j in range(a, b + ONE)
            if max(abs(i - (a + b) // TWO), abs(j - (a + b) // TWO)) in (ZERO, ONE) or abs(i - j) <= ONE
        )
        _paint_indices_47996f11(grid, color, patch)


def _decorate_with_strips_47996f11(
    grid: list[list[int]],
    colors: tuple[int, ...],
    diff_lb: float,
    diff_ub: float,
) -> None:
    nstrip = unifint(diff_lb, diff_ub, (2, 4))
    for _ in range(nstrip):
        color = choice(colors)
        if choice((T, F)):
            h = randint(ONE, THREE)
            w = randint(FIVE, TEN)
        else:
            h = randint(FIVE, TEN)
            w = randint(ONE, THREE)
        if h >= w:
            i_lb = w + ONE
            i_ub = GRID_SIZE_47996F11 - h
            if i_lb > i_ub:
                continue
            i = randint(i_lb, i_ub)
            j = randint(ZERO, i - w - ONE)
        else:
            i = randint(ZERO, GRID_SIZE_47996F11 - h)
            j_lb = i + h + ONE
            j_ub = GRID_SIZE_47996F11 - w
            if j_lb > j_ub:
                continue
            j = randint(j_lb, j_ub)
        patch = frozenset((ii, jj) for ii in range(i, i + h) for jj in range(j, j + w))
        _paint_indices_47996f11(grid, color, patch)
        _paint_indices_47996f11(grid, color, _transpose_indices_47996f11(patch))


def _symmetrize_47996f11(
    grid: list[list[int]],
) -> Grid:
    for i in range(GRID_SIZE_47996F11):
        for j in range(i):
            grid[i][j] = grid[j][i]
    return tuple(tuple(row) for row in grid)


def _sample_mask_47996f11(
    output: Grid,
    diff_lb: float,
    diff_ub: float,
) -> Indices | None:
    used = set()
    patch = set()
    nrect = unifint(diff_lb, diff_ub, (2, 4))
    for _ in range(nrect):
        placed = False
        for _ in range(120):
            h = randint(TWO, SEVEN)
            w = randint(FOUR, TEN)
            side = choice(("above", "below"))
            if side == "above":
                i = randint(ZERO, GRID_SIZE_47996F11 - h)
                j_lb = i + h + ONE
                j_ub = GRID_SIZE_47996F11 - w
                if j_lb > j_ub:
                    continue
                j = randint(j_lb, j_ub)
            else:
                j = randint(ZERO, GRID_SIZE_47996F11 - w)
                i_lb = j + w + ONE
                i_ub = GRID_SIZE_47996F11 - h
                if i_lb > i_ub:
                    continue
                i = randint(i_lb, i_ub)
            rect = frozenset((ii, jj) for ii in range(i, i + h) for jj in range(j, j + w))
            if len(rect & used) > ZERO:
                continue
            if any((jj, ii) in used for ii, jj in rect):
                continue
            values = {output[ii][jj] for ii, jj in rect}
            if len(values) < TWO:
                continue
            patch |= rect
            used |= rect
            placed = True
            break
        if not placed:
            return None
    return frozenset(patch)


def generate_47996f11(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    for _ in range(400):
        ncolors = unifint(diff_lb, diff_ub, (FIVE, SEVEN))
        colors = tuple(sample(DRAW_COLORS_47996F11, ncolors))
        x0 = _make_base_47996f11(colors, diff_lb, diff_ub)
        _decorate_with_centerpiece_47996f11(x0, colors, diff_lb, diff_ub)
        _decorate_with_tiles_47996f11(x0, colors, diff_lb, diff_ub)
        _decorate_with_diagonal_blocks_47996f11(x0, colors, diff_lb, diff_ub)
        _decorate_with_strips_47996f11(x0, colors, diff_lb, diff_ub)
        x1 = _symmetrize_47996f11(x0)
        x2 = _sample_mask_47996f11(x1, diff_lb, diff_ub)
        if x2 is None or len(x2) < 30:
            continue
        x3 = fill(x1, SIX, x2)
        if len(palette(x1)) < FIVE:
            continue
        if verify_47996f11(x3) != x1:
            continue
        return {"input": x3, "output": x1}
    raise RuntimeError("failed to generate a verified 47996f11 example")
