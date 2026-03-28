from synth_rearc.core import *

from .verifier import verify_642d658d


BACKGROUND_COLORS_642D658D = (TWO, FIVE, EIGHT, NINE)


def _sample_row_template_642d658d(
    width: int,
    bg: int,
) -> tuple[int, ...]:
    x0 = choice(("solid", "motif", "motif", "motif", "banded"))
    x1 = [bg] * width
    if x0 != "solid":
        x2 = choice((THREE, FOUR, FIVE, SIX))
        x3 = [bg] * x2
        x4 = randint(ONE, max(ONE, x2 - TWO))
        for x5 in sample(range(x2), x4):
            x3[x5] = ZERO
        x1 = [x3[x6 % x2] for x6 in range(width)]
    if x0 == "banded":
        x7 = randint(ZERO, max(ZERO, width // FIVE))
        x8 = randint(ZERO, max(ZERO, width // FIVE))
        for x9 in range(x7):
            x1[x9] = ZERO
        for x10 in range(width - x8, width):
            x1[x10] = ZERO
    for _ in range(randint(ZERO, TWO)):
        x11 = randint(ZERO, width - ONE)
        x12 = randint(ONE, min(FOUR, width - x11))
        x13 = choice((ZERO, bg))
        for x14 in range(x11, x11 + x12):
            x1[x14] = x13
    x15 = [x16 for x16, x17 in enumerate(x1) if x17 == ZERO]
    shuffle(x15)
    x18 = width // THREE
    while len(x15) > x18:
        x19 = x15.pop()
        x1[x19] = bg
    if ZERO not in x1:
        x1[randint(ZERO, width - ONE)] = ZERO
    return tuple(x1)


def _build_background_642d658d(
    height: int,
    width: int,
    bg: int,
) -> Grid:
    x0 = choice((THREE, FOUR, FIVE, SIX))
    x1 = tuple(_sample_row_template_642d658d(width, bg) for _ in range(x0))
    return tuple(x1[x2 % x0] for x2 in range(height))


def _flower_cells_642d658d(
    center: tuple[int, int],
) -> tuple[tuple[int, int], ...]:
    x0, x1 = center
    return (
        center,
        (x0 - ONE, x1),
        (x0 + ONE, x1),
        (x0, x1 - ONE),
        (x0, x1 + ONE),
    )


def _paint_points_642d658d(
    grid: Grid,
    color: int,
    cells: tuple[tuple[int, int], ...],
) -> Grid:
    x0 = grid
    for x1 in cells:
        x0 = fill(x0, color, initset(x1))
    return x0


def _place_flower_642d658d(
    grid: Grid,
    center: tuple[int, int],
    petal_color: int,
) -> Grid:
    x0, x1 = center
    x2 = (
        (x0 - ONE, x1),
        (x0 + ONE, x1),
        (x0, x1 - ONE),
        (x0, x1 + ONE),
    )
    x3 = _paint_points_642d658d(grid, petal_color, x2)
    x4 = fill(x3, FOUR, initset(center))
    return x4


def _sample_centers_642d658d(
    height: int,
    width: int,
    count: int,
) -> tuple[tuple[int, int], ...]:
    x0: list[tuple[int, int]] = []
    x1 = ZERO
    while len(x0) < count:
        x1 += ONE
        if x1 > 5000:
            raise RuntimeError("failed to place flowers")
        x2 = randint(ONE, height - TWO)
        x3 = randint(ONE, width - TWO)
        x4 = (x2, x3)
        x5 = all(max(abs(x2 - x6), abs(x3 - x7)) > TWO for x6, x7 in x0)
        if x5:
            x0.append(x4)
    return tuple(x0)


def _in_bounds_neighbors_642d658d(
    cell: tuple[int, int],
    height: int,
    width: int,
) -> tuple[tuple[int, int], ...]:
    x0, x1 = cell
    x2 = (
        (x0 - ONE, x1),
        (x0 + ONE, x1),
        (x0, x1 - ONE),
        (x0, x1 + ONE),
    )
    return tuple(x3 for x3 in x2 if 0 <= x3[0] < height and 0 <= x3[1] < width)


def _scatter_color_642d658d(
    grid: Grid,
    color: int,
    count: int,
    blocked: frozenset[tuple[int, int]],
) -> tuple[Grid, frozenset[tuple[int, int]]]:
    x0 = height(grid)
    x1 = width(grid)
    x2 = [
        (x3, x4)
        for x3 in range(x0)
        for x4 in range(x1)
        if (x3, x4) not in blocked
    ]
    shuffle(x2)
    x5 = grid
    x6 = set(blocked)
    x7 = ZERO
    for x8 in (T, F):
        for x9 in x2:
            if x7 == count:
                break
            if x9 in x6:
                continue
            x10 = _in_bounds_neighbors_642d658d(x9, x0, x1)
            x11 = any(index(x5, x12) == color for x12 in x10)
            if both(x8, x11):
                continue
            x5 = fill(x5, color, initset(x9))
            x6.add(x9)
            x7 += ONE
        if x7 == count:
            break
    return x5, frozenset(x6)


def _sample_noise_mode_642d658d() -> str:
    return choice(("light", "medium", "medium", "heavy"))


def _sample_noise_count_642d658d(
    mode: str,
    height: int,
    is_favorite: bool,
) -> int:
    if mode == "light":
        x0 = randint(ZERO, THREE)
        x1 = randint(ZERO, TWO)
    elif mode == "medium":
        x0 = randint(ONE, max(THREE, height // THREE))
        x1 = randint(ZERO, max(TWO, height // FOUR))
    else:
        x0 = randint(TWO, max(FIVE, height // TWO))
        x1 = randint(ONE, max(THREE, height // TWO))
    return x0 + x1 if is_favorite else x0


def _maybe_mirror_642d658d(grid: Grid) -> Grid:
    x0 = grid
    if choice((T, F)):
        x0 = hmirror(x0)
    if choice((T, F)):
        x0 = vmirror(x0)
    return x0


def generate_642d658d(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = unifint(diff_lb, diff_ub, (20, 28))
        x1 = choice((22, 24))
        x2 = choice(BACKGROUND_COLORS_642D658D)
        x3 = _build_background_642d658d(x0, x1, x2)
        x4 = tuple(x5 for x5 in interval(ONE, TEN, ONE) if x5 not in (FOUR, x2))
        x5 = choice((THREE, FOUR, FIVE, SIX))
        x6 = sample(x4, x5 - ONE)
        x7 = choice(x6)
        x8 = [x7, x7] + [x9 for x9 in x6 if x9 != x7]
        shuffle(x8)
        x9 = _sample_centers_642d658d(x0, x1, x5)
        x10 = x3
        x11 = set()
        for x12, x13 in zip(x9, x8):
            x10 = _place_flower_642d658d(x10, x12, x13)
            x11.update(_flower_cells_642d658d(x12))
        x14 = _sample_noise_mode_642d658d()
        x15 = choice(tuple(x6))
        x16 = frozenset(x11)
        for x17 in x6:
            x18 = _sample_noise_count_642d658d(x14, x0, x17 == x15)
            x10, x16 = _scatter_color_642d658d(x10, x17, x18, x16)
        x19 = _maybe_mirror_642d658d(x10)
        x20 = canvas(x7, UNITY)
        if verify_642d658d(x19) != x20:
            continue
        return {"input": x19, "output": x20}
