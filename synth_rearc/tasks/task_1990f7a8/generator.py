from synth_rearc.core import *


def _shape_grid(patch: Indices) -> Grid:
    x0 = canvas(ZERO, THREE_BY_THREE)
    x1 = fill(x0, TWO, patch)
    return x1


def _valid_shape(patch: Indices) -> bool:
    x0 = len(patch) >= FOUR
    x1 = height(patch) == THREE
    x2 = width(patch) == THREE
    x3 = _shape_grid(patch)
    x4 = objects(x3, T, T, F)
    x5 = colorfilter(x4, TWO)
    x6 = len(x5) == ONE
    return x0 and x1 and x2 and x6


VALID_SHAPES = tuple(
    patch
    for patch in (
        frozenset(
            (i, j)
            for i in range(THREE)
            for j in range(THREE)
            if mask & (ONE << (i * THREE + j))
        )
        for mask in range(ONE, ONE << NINE)
    )
    if _valid_shape(patch)
)


def _paint_shape(grid: Grid, patch: Indices, loc: tuple[int, int]) -> Grid:
    x0 = shift(patch, loc)
    x1 = fill(grid, TWO, x0)
    return x1


def generate_1990f7a8(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    h = unifint(diff_lb, diff_ub, (16, 24))
    w = unifint(diff_lb, diff_ub, (16, 24))
    hi = h // TWO
    wi = w // TWO
    patches = sample(VALID_SHAPES, FOUR)
    loci = (
        (randint(ONE, hi - FOUR), randint(ONE, wi - FOUR)),
        (randint(ONE, hi - FOUR), randint(wi + ONE, w - FOUR)),
        (randint(hi + ONE, h - FOUR), randint(ONE, wi - FOUR)),
        (randint(hi + ONE, h - FOUR), randint(wi + ONE, w - FOUR)),
    )
    slots = ((ZERO, ZERO), (ZERO, FOUR), (FOUR, ZERO), (FOUR, FOUR))
    gi = canvas(ZERO, (h, w))
    go = canvas(ZERO, (SEVEN, SEVEN))
    for patch, loc, slot in zip(patches, loci, slots):
        gi = _paint_shape(gi, patch, loc)
        go = _paint_shape(go, patch, slot)
    return {"input": gi, "output": go}
