from arc2.core import *


GRID_SHAPE_1E81D6F9 = (15, 15)
MARKER_PATCH_1E81D6F9 = combine(
    connect((ZERO, THREE), (THREE, THREE)),
    connect((THREE, ZERO), (THREE, THREE)),
)
MARKER_ZONE_1E81D6F9 = backdrop(MARKER_PATCH_1E81D6F9)
AVAILABLE_CELLS_1E81D6F9 = difference(asindices(canvas(ZERO, GRID_SHAPE_1E81D6F9)), MARKER_ZONE_1E81D6F9)
TARGET_COLORS_1E81D6F9 = (ONE, TWO, THREE, FOUR)
NOISE_COLORS_1E81D6F9 = interval(ONE, TEN, ONE)


def _target_cells_1e81d6f9(count: Integer) -> Indices:
    x0 = totuple(AVAILABLE_CELLS_1E81D6F9)
    while True:
        x1 = sample(x0, count)
        x2 = all(
            abs(a[0] - b[0]) + abs(a[1] - b[1]) > ONE
            for idx, a in enumerate(x1)
            for b in x1[idx + ONE :]
        )
        if x2:
            return frozenset(x1)


def generate_1e81d6f9(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    x0 = canvas(ZERO, GRID_SHAPE_1E81D6F9)
    x1 = choice(TARGET_COLORS_1E81D6F9)
    x2 = fill(x0, FIVE, MARKER_PATCH_1E81D6F9)
    x3 = fill(x2, x1, initset(UNITY))
    x4 = unifint(diff_lb, diff_ub, (THREE, FIVE))
    x5 = _target_cells_1e81d6f9(x4)
    x6 = fill(x3, x1, x5)
    x7 = difference(AVAILABLE_CELLS_1E81D6F9, x5)
    x8 = unifint(diff_lb, diff_ub, (13, 27))
    x9 = sample(totuple(x7), x8)
    x10 = remove(x1, NOISE_COLORS_1E81D6F9)
    x11 = x6
    for x12 in x9:
        x11 = fill(x11, choice(x10), initset(x12))
    x13 = fill(x11, ZERO, x5)
    return {"input": x11, "output": x13}
