from synth_rearc.core import *


GRID_SHAPES_A934301B = (
    (13, 12),
    (13, 14),
    (13, 15),
    (14, 14),
    (14, 14),
    (14, 15),
)

OBJECT_COUNT_BAG_A934301B = (5, 6, 6, 6, 7, 7)
KEEP_COUNT_BAG_A934301B = (2, 3, 3, 3, 4)
RECT_HEIGHT_BAG_A934301B = (2, 3, 3, 3, 4, 4)
RECT_WIDTH_BAG_A934301B = (2, 3, 3, 4, 4, 4, 5)
KEEP_MARKER_BAG_A934301B = (0, 0, 1, 1, 1)
DROP_MARKER_BAG_A934301B = (2, 2, 3, 3, 4)


def _rect_patch_a934301b(
    top: Integer,
    bottom: Integer,
    left: Integer,
    right: Integer,
) -> Indices:
    x0 = interval(top, bottom + ONE, ONE)
    x1 = interval(left, right + ONE, ONE)
    x2 = product(x0, x1)
    return x2


def _margin_patch_a934301b(
    dims: tuple[Integer, Integer],
    top: Integer,
    bottom: Integer,
    left: Integer,
    right: Integer,
) -> Indices:
    x0, x1 = dims
    x2 = max(ZERO, top - ONE)
    x3 = min(x0 - ONE, bottom + ONE)
    x4 = max(ZERO, left - ONE)
    x5 = min(x1 - ONE, right + ONE)
    x6 = _rect_patch_a934301b(x2, x3, x4, x5)
    return x6


def _sample_marker_counts_a934301b(
    nobjs: Integer,
) -> tuple[Integer, ...]:
    x0 = choice(KEEP_COUNT_BAG_A934301B)
    x1 = min(x0, nobjs - ONE)
    x2 = nobjs - x1
    x3 = [choice(KEEP_MARKER_BAG_A934301B) for _ in range(x1)]
    x4 = [choice(DROP_MARKER_BAG_A934301B) for _ in range(x2)]
    x5 = x3 + x4
    shuffle(x5)
    return tuple(x5)


def _sample_specs_a934301b(
    dims: tuple[Integer, Integer],
    marker_counts: tuple[Integer, ...],
) -> tuple[tuple[Integer, Integer, Integer, Integer, tuple[tuple[Integer, Integer], ...]], ...] | None:
    x0, x1 = dims
    x2 = set()
    x3 = []
    for x4 in marker_counts:
        x5 = F
        for _ in range(300):
            x6 = choice(RECT_HEIGHT_BAG_A934301B)
            x7 = choice(RECT_WIDTH_BAG_A934301B)
            x8 = x6 * x7
            if x4 >= x8:
                continue
            if x6 >= x0 or x7 >= x1:
                continue
            x9 = randint(ZERO, x0 - x6)
            x10 = randint(ZERO, x1 - x7)
            x11 = x9 + x6 - ONE
            x12 = x10 + x7 - ONE
            x13 = _rect_patch_a934301b(x9, x11, x10, x12)
            if x13 & x2:
                continue
            x14 = tuple(x13)
            x15 = tuple(sample(x14, x4))
            x3.append((x9, x11, x10, x12, x15))
            x2 |= _margin_patch_a934301b(dims, x9, x11, x10, x12)
            x5 = T
            break
        if not x5:
            return None
    return tuple(x3)


def _paint_specs_a934301b(
    dims: tuple[Integer, Integer],
    specs: tuple[tuple[Integer, Integer, Integer, Integer, tuple[tuple[Integer, Integer], ...]], ...],
    keep_all: Boolean,
) -> Grid:
    x0 = canvas(ZERO, dims)
    for x1, x2, x3, x4, x5 in specs:
        if (not keep_all) and len(x5) > ONE:
            continue
        x6 = _rect_patch_a934301b(x1, x2, x3, x4)
        x0 = fill(x0, ONE, x6)
        if len(x5) > ZERO:
            x0 = fill(x0, EIGHT, frozenset(x5))
    return x0


def generate_a934301b(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = choice(GRID_SHAPES_A934301B)
        x1 = choice(OBJECT_COUNT_BAG_A934301B)
        x2 = _sample_marker_counts_a934301b(x1)
        x3 = _sample_specs_a934301b(x0, x2)
        if x3 is None:
            continue
        x4 = _paint_specs_a934301b(x0, x3, T)
        x5 = _paint_specs_a934301b(x0, x3, F)
        if x4 == x5:
            continue
        return {"input": x4, "output": x5}
