from synth_rearc.core import *


HEIGHT_BOUNDS_6F473927 = (THREE, 12)
WIDTH_BOUNDS_6F473927 = (THREE, SIX)
MIN_RED_CELLS_6F473927 = FOUR
MIN_DENSITY_NUM_6F473927 = ONE
MIN_DENSITY_DEN_6F473927 = FIVE
MAX_DENSITY_NUM_6F473927 = FOUR
MAX_DENSITY_DEN_6F473927 = FIVE


def _walk_local_shape_6f473927(
    h: int,
    w: int,
    diff_lb: float,
    diff_ub: float,
) -> frozenset[tuple[int, int]]:
    x0 = w - ONE
    x1 = min(FOUR, h)
    x2 = unifint(diff_lb, diff_ub, (ONE, x1))
    x3 = set()
    for _ in range(x2):
        x4 = randint(ZERO, h - ONE)
        x5 = ZERO
        x6 = max(x0 + ONE, h // TWO + ONE)
        x7 = max(x6, h + double(x0))
        x8 = randint(x6, x7)
        for _ in range(x8):
            x3.add((x4, x5))
            x9 = choice((
                (ZERO, ZERO),
                (ZERO, ONE),
                (ZERO, ONE),
                (ZERO, ONE),
                (ZERO, NEG_ONE),
                (ONE, ZERO),
                (NEG_ONE, ZERO),
            ))
            x10 = min(max(x4 + x9[ZERO], ZERO), h - ONE)
            x11 = min(max(x5 + x9[ONE], ZERO), x0 - ONE)
            x4, x5 = x10, x11
            x3.add((x4, x5))
    x12 = {}
    for x13, x14 in x3:
        x12.setdefault(x13, []).append(x14)
    x15 = set()
    for x16, x17 in x12.items():
        x18 = min(x17)
        x19 = max(x17)
        for x20 in range(x18, x19 + ONE):
            x15.add((x16, x20))
        x21 = x19 - x18 + ONE
        if x21 >= THREE and choice((ZERO, ONE, TWO)) == ZERO:
            x22 = randint(x18 + ONE, x19 - ONE)
            x15.discard((x16, x22))
        if x21 >= FOUR and choice((ZERO, ONE, TWO, THREE, FOUR)) == ZERO:
            x23 = randint(x18 + ONE, x19 - ONE)
            x15.discard((x16, x23))
    return frozenset(x15)


def _place_local_shape_6f473927(
    shp: frozenset[tuple[int, int]],
    w: int,
    left_anchor: bool,
) -> frozenset[tuple[int, int]]:
    if left_anchor:
        return shp
    return frozenset((i, w - ONE - j) for i, j in shp)


def _mirror_half_6f473927(
    g: Grid,
) -> Grid:
    x0 = vmirror(g)
    x1 = replace(x0, ZERO, EIGHT)
    x2 = replace(x1, TWO, ZERO)
    return x2


def generate_6f473927(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = unifint(diff_lb, diff_ub, HEIGHT_BOUNDS_6F473927)
        x1 = unifint(diff_lb, diff_ub, WIDTH_BOUNDS_6F473927)
        x2 = choice((T, F))
        x3 = _walk_local_shape_6f473927(x0, x1, diff_lb, diff_ub)
        x4 = size(x3)
        x5 = x0 * (x1 - ONE)
        if x4 < MIN_RED_CELLS_6F473927:
            continue
        if x4 * MIN_DENSITY_DEN_6F473927 < x5 * MIN_DENSITY_NUM_6F473927:
            continue
        if x4 * MAX_DENSITY_DEN_6F473927 > x5 * MAX_DENSITY_NUM_6F473927:
            continue
        x6 = apply(first, x3)
        if size(x6) < TWO:
            continue
        x7 = sfilter(x3, matcher(last, ZERO))
        if size(x7) == ZERO:
            continue
        x8 = _place_local_shape_6f473927(x3, x1, x2)
        x9 = canvas(ZERO, (x0, x1))
        x10 = fill(x9, TWO, x8)
        x11 = _mirror_half_6f473927(x10)
        x12 = branch(x2, hconcat(x11, x10), hconcat(x10, x11))
        if numcolors(x10) != TWO:
            continue
        return {"input": x10, "output": x12}
