from synth_rearc.core import *

from .helpers import (
    AVAILABLE_COLORS_903D1B4A,
    GRID_SIZE_903D1B4A,
    UPPER_TRIANGLE_CELLS_903D1B4A,
    rect_patch_903d1b4a,
    render_output_903d1b4a,
)


def _sample_block_palette_903d1b4a(
    color_pool: tuple[int, ...],
) -> tuple[int, ...]:
    x0 = choice((TWO, THREE, THREE))
    x1 = min(x0, len(color_pool))
    return tuple(sample(color_pool, x1))


def _sample_block_903d1b4a(
    palette: tuple[int, ...],
) -> Grid:
    x0 = choice(palette)
    x1 = tuple(x2 for x2 in palette if x2 != x0)
    x3 = [[x0 for _ in range(FOUR)] for _ in range(FOUR)]
    x4 = list(UPPER_TRIANGLE_CELLS_903D1B4A)
    shuffle(x4)
    if len(x1) == ONE:
        x5 = randint(TWO, FOUR)
        x6 = x4[:x5]
        for x7, x8 in x6:
            x3[x7][x8] = x1[ZERO]
    else:
        x5 = randint(TWO, THREE)
        x6 = randint(ONE, TWO)
        x7 = x4[:x5]
        x8 = x4[x5 : add(x5, x6)]
        x9 = choice(x1)
        x10 = other(x1, x9)
        for x11, x12 in x7:
            x3[x11][x12] = x9
        for x13, x14 in x8:
            x3[x13][x14] = x10
    for x15, x16 in UPPER_TRIANGLE_CELLS_903D1B4A:
        x3[x16][x15] = x3[x15][x16]
    return tuple(tuple(x17) for x17 in x3)


def _sample_output_903d1b4a(
    diff_lb: float,
    diff_ub: float,
) -> Grid:
    while True:
        x0 = unifint(diff_lb, diff_ub, (FIVE, EIGHT))
        x1 = tuple(sample(AVAILABLE_COLORS_903D1B4A, x0))
        x2 = _sample_block_palette_903d1b4a(x1)
        x3 = _sample_block_palette_903d1b4a(x1)
        x4 = _sample_block_palette_903d1b4a(x1)
        x5 = _sample_block_903d1b4a(x2)
        x6 = _sample_block_903d1b4a(x3)
        x7 = _sample_block_903d1b4a(x4)
        x8 = set(palette(x5)) | set(palette(x6)) | set(palette(x7))
        if len(x8) < FIVE:
            continue
        if equality(x5, x6) or equality(x5, x7) or equality(x6, x7):
            continue
        return render_output_903d1b4a(x5, x6, x7)


def _symmetry_orbit_903d1b4a(
    i: Integer,
    j: Integer,
):
    x0 = subtract(GRID_SIZE_903D1B4A, ONE)
    return frozenset(
        {
            (i, j),
            (subtract(x0, i), j),
            (i, subtract(x0, j)),
            (subtract(x0, i), subtract(x0, j)),
            (j, i),
            (j, subtract(x0, i)),
            (subtract(x0, j), i),
            (subtract(x0, j), subtract(x0, i)),
        }
    )


def _recoverable_mask_903d1b4a(
    mask,
) -> Boolean:
    x0 = set(mask)
    x1 = set()
    for x2 in range(GRID_SIZE_903D1B4A):
        for x3 in range(GRID_SIZE_903D1B4A):
            x4 = _symmetry_orbit_903d1b4a(x2, x3)
            x5 = tuple(sorted(x4))
            if x5 in x1:
                continue
            x1.add(x5)
            if x4.issubset(x0):
                return F
    return T


def _sample_mask_903d1b4a(
    diff_lb: float,
    diff_ub: float,
):
    while True:
        x0 = frozenset()
        x1 = T
        for _ in range(TWO):
            x2 = unifint(diff_lb, diff_ub, (TWO, FOUR))
            x3 = choice((TWO, TWO, THREE))
            x4 = randint(ZERO, subtract(GRID_SIZE_903D1B4A, x2))
            x5 = randint(ZERO, subtract(GRID_SIZE_903D1B4A, x3))
            x6 = rect_patch_903d1b4a(x4, x5, x2, x3)
            if size(intersection(x0, x6)) > ZERO:
                x1 = F
                break
            x0 = combine(x0, x6)
        x7 = size(x0)
        if flip(x1):
            continue
        if x7 < EIGHT or x7 > 20:
            continue
        if _recoverable_mask_903d1b4a(x0):
            return x0


def generate_903d1b4a(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = _sample_output_903d1b4a(diff_lb, diff_ub)
        x1 = _sample_mask_903d1b4a(diff_lb, diff_ub)
        x2 = fill(x0, THREE, x1)
        if equality(x0, x2):
            continue
        return {"input": x2, "output": x0}
