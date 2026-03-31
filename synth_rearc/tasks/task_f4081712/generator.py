from synth_rearc.core import *

from .verifier import verify_f4081712


GRID_SIDE_F4081712 = 24
QUARTER_SIDE_F4081712 = 12
TILE_SIDE_F4081712 = 6
PATCH_BOUNDS_F4081712 = (TWO, EIGHT)
NCOLOR_OPTIONS_F4081712 = (FOUR, FIVE, FIVE, SIX, SIX, SEVEN)
COLOR_POOL_F4081712 = remove(THREE, remove(ZERO, interval(ZERO, TEN, ONE)))
STAMP_DIMS_F4081712 = (
    (ONE, ONE),
    (ONE, TWO),
    (TWO, ONE),
    (ONE, THREE),
    (THREE, ONE),
    (TWO, TWO),
    (TWO, THREE),
    (THREE, TWO),
)


def _rect_patch_f4081712(
    dims: tuple[int, int],
    loc: tuple[int, int],
) -> Indices:
    x0 = asindices(canvas(ZERO, dims))
    x1 = shift(x0, loc)
    return x1


def _random_tile_f4081712(
    colors: tuple[int, ...],
) -> Grid:
    while True:
        x0 = choice(colors)
        x1 = canvas(x0, (TILE_SIDE_F4081712, TILE_SIDE_F4081712))
        x2 = tuple(x3 for x3 in colors if x3 != x0)
        x3 = randint(EIGHT, 14)
        for _ in range(x3):
            x4 = choice(x2)
            x5 = choice(STAMP_DIMS_F4081712)
            x6 = randint(ZERO, TILE_SIDE_F4081712 - x5[ZERO])
            x7 = randint(ZERO, TILE_SIDE_F4081712 - x5[ONE])
            x8 = _rect_patch_f4081712(x5, (x6, x7))
            x1 = fill(x1, x4, x8)
        if numcolors(x1) < min(THREE, len(colors)):
            continue
        return x1


def _build_full_f4081712(
    colors: tuple[int, ...],
) -> Grid:
    while True:
        x0 = _random_tile_f4081712(colors)
        x1 = _random_tile_f4081712(colors)
        x2 = _random_tile_f4081712(colors)
        if equality(x0, x1) or equality(x1, x2):
            continue
        x3 = hconcat(x0, x1)
        x4 = hconcat(x1, x2)
        x5 = vconcat(x3, x4)
        x6 = vmirror(x5)
        x7 = hconcat(x5, x6)
        x8 = hmirror(x7)
        x9 = vconcat(x7, x8)
        return x9


def generate_f4081712(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = choice(NCOLOR_OPTIONS_F4081712)
        x1 = tuple(sample(COLOR_POOL_F4081712, x0))
        x2 = _build_full_f4081712(x1)
        x3 = unifint(diff_lb, diff_ub, PATCH_BOUNDS_F4081712)
        x4 = unifint(diff_lb, diff_ub, PATCH_BOUNDS_F4081712)
        x5 = randint(ZERO, QUARTER_SIDE_F4081712 - x3)
        x6 = randint(ZERO, GRID_SIDE_F4081712 - x4)
        x7 = astuple(x5, x6)
        x8 = astuple(x3, x4)
        x9 = crop(x2, x7, x8)
        if numcolors(x9) < TWO:
            continue
        x10 = _rect_patch_f4081712(x8, x7)
        x11 = fill(x2, THREE, x10)
        if choice((T, F)):
            x11 = hmirror(x11)
            x9 = hmirror(x9)
        if choice((T, F)):
            x11 = vmirror(x11)
            x9 = vmirror(x9)
        if verify_f4081712(x11) != x9:
            continue
        return {"input": x11, "output": x9}
