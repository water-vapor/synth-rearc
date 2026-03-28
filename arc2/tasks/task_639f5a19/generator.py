from arc2.core import *

from .verifier import verify_639f5a19


GRID_SHAPE_639F5A19 = (23, 23)
PRIMARY_RECTANGLE_639F5A19 = (TEN, 12)
SECONDARY_RECTANGLES_639F5A19 = ((EIGHT, EIGHT), (EIGHT, 12))
LAYOUTS_639F5A19 = (
    ((ONE, FIVE, TEN, 12), (14, ONE, EIGHT, 12)),
    ((ONE, TWO, EIGHT, EIGHT), (TEN, SEVEN, TEN, 12)),
)
SYMMETRIES_639F5A19 = (identity, rot90, rot180, rot270, hmirror, vmirror, dmirror, cmirror)


def _rectangle_patch_639f5a19(
    top: Integer,
    left: Integer,
    height_value: Integer,
    width_value: Integer,
) -> Indices:
    x0 = interval(top, add(top, height_value), ONE)
    x1 = interval(left, add(left, width_value), ONE)
    return product(x0, x1)


def _expanded_patch_639f5a19(
    top: Integer,
    left: Integer,
    height_value: Integer,
    width_value: Integer,
    pad: Integer = ONE,
) -> Indices:
    x0, x1 = GRID_SHAPE_639F5A19
    x2 = max(ZERO, top - pad)
    x3 = max(ZERO, left - pad)
    x4 = min(x0, top + height_value + pad)
    x5 = min(x1, left + width_value + pad)
    x6 = interval(x2, x4, ONE)
    x7 = interval(x3, x5, ONE)
    return product(x6, x7)


def _decorate_rectangle_639f5a19(
    grid: Grid,
    top: Integer,
    left: Integer,
    height_value: Integer,
    width_value: Integer,
) -> Grid:
    x0 = add(top, halve(height_value))
    x1 = add(left, halve(width_value))
    x2 = interval(top, x0, ONE)
    x3 = interval(x0, add(top, height_value), ONE)
    x4 = interval(left, x1, ONE)
    x5 = interval(x1, add(left, width_value), ONE)
    x6 = product(x2, x4)
    x7 = product(x2, x5)
    x8 = product(x3, x4)
    x9 = product(x3, x5)
    x10 = interval(add(top, TWO), add(top, height_value - TWO), ONE)
    x11 = interval(add(left, TWO), add(left, width_value - TWO), ONE)
    x12 = product(x10, x11)
    x13 = fill(grid, SIX, x6)
    x14 = fill(x13, ONE, x7)
    x15 = fill(x14, TWO, x8)
    x16 = fill(x15, THREE, x9)
    return fill(x16, FOUR, x12)


def _make_example_639f5a19(
    rectangles,
) -> dict:
    x0 = canvas(ZERO, GRID_SHAPE_639F5A19)
    for x1, x2, x3, x4 in rectangles:
        x5 = _rectangle_patch_639f5a19(x1, x2, x3, x4)
        x0 = fill(x0, EIGHT, x5)
    x6 = x0
    for x1, x2, x3, x4 in rectangles:
        x6 = _decorate_rectangle_639f5a19(x6, x1, x2, x3, x4)
    return {
        "input": x0,
        "output": x6,
    }


def _sample_rectangles_639f5a19() -> tuple | None:
    x0, x1 = GRID_SHAPE_639F5A19
    x2 = tuple(
        sorted(
            (
                PRIMARY_RECTANGLE_639F5A19,
                choice(SECONDARY_RECTANGLES_639F5A19),
            ),
            key=lambda x: multiply(x[0], x[1]),
            reverse=True,
        )
    )
    x3 = []
    x4 = frozenset()
    for x5, x6 in x2:
        x7 = []
        for x8 in range(ONE, x0 - x5):
            for x9 in range(ONE, x1 - x6):
                x10 = _expanded_patch_639f5a19(x8, x9, x5, x6)
                if len(intersection(x10, x4)) == ZERO:
                    x7.append((x8, x9, x5, x6, x10))
        if len(x7) == ZERO:
            return None
        x11, x12, x13, x14, x15 = choice(x7)
        x3.append((x11, x12, x13, x14))
        x4 = combine(x4, x15)
    return tuple(x3)


def _fallback_example_639f5a19() -> dict:
    x0 = choice(LAYOUTS_639F5A19)
    x1 = _make_example_639f5a19(x0)
    x2 = choice(SYMMETRIES_639F5A19)
    return {
        "input": x2(x1["input"]),
        "output": x2(x1["output"]),
    }


def generate_639f5a19(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    for _ in range(40):
        x0 = _sample_rectangles_639f5a19()
        if x0 is None:
            continue
        x1 = _make_example_639f5a19(x0)
        if verify_639f5a19(x1["input"]) == x1["output"]:
            return x1
    x2 = _fallback_example_639f5a19()
    if verify_639f5a19(x2["input"]) != x2["output"]:
        raise RuntimeError("fallback example for 639f5a19 is invalid")
    return x2
