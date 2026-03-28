from synth_rearc.core import *

from .verifier import verify_1efba499


COLOR_POOL_1EFBA499 = tuple(x0 for x0 in range(ONE, TEN))


def _paint_cell_1efba499(
    grid: Grid,
    value: int,
    loc: tuple[int, int],
) -> Grid:
    return fill(grid, value, frozenset((loc,)))


def _horizontal_profile_1efba499(
    height: int,
    width: int,
    diff_lb: float,
    diff_ub: float,
) -> dict[int, tuple[int, int]]:
    x0 = randint(ZERO, TWO)
    x1 = randint(ZERO, TWO)
    x2 = width - x0 - x1
    x3 = randint(THREE, height - FOUR)
    x4 = {x5: [x3, x3] for x5 in range(x0, x0 + x2)}
    x5 = max(THREE, x2 - THREE)
    x6 = unifint(diff_lb, diff_ub, (THREE, x5))
    x7 = randint(x0, x0 + x2 - x6)
    x8 = x7 + x6 - ONE
    for x9 in range(x7, x8 + ONE):
        x4[x9][ZERO] = max(ONE, x4[x9][ZERO] - ONE)
        x4[x9][ONE] = min(height - TWO, x4[x9][ONE] + ONE)
    x9 = randint(ONE, THREE)
    for _ in range(x9):
        x10 = choice(("up", "down", "both"))
        x11 = choice((ONE, ONE, TWO))
        x12 = randint(TWO, max(TWO, x2 - ONE))
        x13 = randint(x0, x0 + x2 - x12)
        x14 = x13 + x12 - ONE
        for x15 in range(x13, x14 + ONE):
            if x10 in ("up", "both"):
                x4[x15][ZERO] = max(ONE, x4[x15][ZERO] - x11)
            if x10 in ("down", "both"):
                x4[x15][ONE] = min(height - TWO, x4[x15][ONE] + x11)
    return {x15: (x16[ZERO], x16[ONE]) for x15, x16 in x4.items()}


def _paint_profile_1efba499(
    height: int,
    width: int,
    color_value: int,
    profile: dict[int, tuple[int, int]],
) -> Grid:
    x0 = canvas(ZERO, (height, width))
    x1 = set()
    for x2, (x3, x4) in profile.items():
        for x5 in range(x3, x4 + ONE):
            x1.add((x5, x2))
    return fill(x0, color_value, frozenset(x1))


def _sample_line_sets_1efba499(
    lines: tuple[int, ...],
    diff_lb: float,
    diff_ub: float,
) -> tuple[tuple[int, ...], tuple[int, ...], tuple[int, ...]]:
    x0 = len(lines)
    x1 = min(max(TWO, unifint(diff_lb, diff_ub, (TWO, FOUR))), x0 - TWO)
    x2 = tuple(sample(lines, x1))
    x3 = tuple(x4 for x4 in lines if x4 not in x2)
    x4 = min(max(ONE, unifint(diff_lb, diff_ub, (ONE, THREE))), len(x3) - ONE)
    x5 = tuple(sample(x3, x4))
    x6 = tuple(x7 for x7 in x3 if x7 not in x5)
    x7 = min(max(ONE, unifint(diff_lb, diff_ub, (ONE, THREE))), len(x6))
    x8 = tuple(sample(x6, x7))
    return x2, x5, x8


def _decorate_horizontal_1efba499(
    grid: Grid,
    profile: dict[int, tuple[int, int]],
    dominant_color: int,
    top_palette: tuple[int, ...],
    bottom_palette: tuple[int, ...],
    diff_lb: float,
    diff_ub: float,
) -> tuple[Grid, Grid]:
    x0 = height(grid)
    x1 = tuple(profile.keys())
    x2, x3, x4 = _sample_line_sets_1efba499(x1, diff_lb, diff_ub)
    x5 = grid
    x6 = grid
    for x7 in x2:
        x8, x9 = profile[x7]
        x10 = randint(ONE, min(FOUR, x8))
        x11 = randint(ONE, min(FOUR, x0 - ONE - x9))
        x12 = x8 - x10
        x13 = x9 + x11
        x14 = choice(top_palette)
        x15 = choice(bottom_palette)
        x5 = _paint_cell_1efba499(x5, x14, (x12, x7))
        x5 = _paint_cell_1efba499(x5, x15, (x13, x7))
        x6 = _paint_cell_1efba499(x6, x15, (x8 - ONE, x7))
        x6 = _paint_cell_1efba499(x6, x14, (x9 + ONE, x7))
    for x7 in x3:
        x8, _ = profile[x7]
        x9 = randint(ONE, min(FOUR, x8))
        x10 = x8 - x9
        x11 = choice(top_palette)
        x5 = _paint_cell_1efba499(x5, x11, (x10, x7))
        x6 = _paint_cell_1efba499(x6, x11, (x10, x7))
    for x7 in x4:
        _, x8 = profile[x7]
        x9 = randint(ONE, min(FOUR, x0 - ONE - x8))
        x10 = x8 + x9
        x11 = choice(bottom_palette)
        x5 = _paint_cell_1efba499(x5, x11, (x10, x7))
        x6 = _paint_cell_1efba499(x6, x11, (x10, x7))
    return x5, x6


def _base_example_1efba499(
    height: int,
    width: int,
    diff_lb: float,
    diff_ub: float,
) -> tuple[Grid, Grid]:
    x0 = choice(COLOR_POOL_1EFBA499)
    x1 = tuple(x2 for x2 in COLOR_POOL_1EFBA499 if x2 != x0)
    x2 = choice((ONE, ONE, TWO))
    x3 = choice((ONE, TWO))
    x4 = tuple(sample(x1, x2))
    x5 = tuple(x6 for x6 in x1 if x6 not in x4)
    x6 = tuple(sample(x5, x3))
    x7 = _horizontal_profile_1efba499(height, width, diff_lb, diff_ub)
    x8 = _paint_profile_1efba499(height, width, x0, x7)
    return _decorate_horizontal_1efba499(x8, x7, x0, x4, x6, diff_lb, diff_ub)


def generate_1efba499(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = choice((12, 12, 14))
        x1 = choice((12, 14, 14, 16))
        x2 = choice((T, F))
        x3 = x1 if x2 else x0
        x4 = x0 if x2 else x1
        x5, x6 = _base_example_1efba499(x3, x4, diff_lb, diff_ub)
        if x2:
            x5 = dmirror(x5)
            x6 = dmirror(x6)
        if choice((T, F)):
            x5 = hmirror(x5)
            x6 = hmirror(x6)
        if choice((T, F)):
            x5 = vmirror(x5)
            x6 = vmirror(x6)
        if x5 == x6:
            continue
        if verify_1efba499(x5) != x6:
            continue
        return {"input": x5, "output": x6}
