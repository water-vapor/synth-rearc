from synth_rearc.core import *


GRID_WIDTH_D2ACF2CB = NINE
GRID_HEIGHT_RANGE_D2ACF2CB = (SIX, TEN)
MAX_MARKED_LINES_D2ACF2CB = THREE
BASE_COLORS_D2ACF2CB = (ZERO, SIX)


def _toggle_patch_d2acf2cb(
    grid: Grid,
    patch: frozenset[IntegerTuple],
) -> Grid:
    x0 = intersection(ofcolor(grid, ZERO), patch)
    x1 = intersection(ofcolor(grid, EIGHT), patch)
    x2 = intersection(ofcolor(grid, SIX), patch)
    x3 = intersection(ofcolor(grid, SEVEN), patch)
    x4 = fill(grid, EIGHT, x0)
    x5 = fill(x4, ZERO, x1)
    x6 = fill(x5, SEVEN, x2)
    return fill(x6, SIX, x3)


def _make_base_grid_d2acf2cb(height_value: Integer) -> Grid:
    return tuple(
        tuple(choice(BASE_COLORS_D2ACF2CB) for _ in range(GRID_WIDTH_D2ACF2CB))
        for _ in range(height_value)
    )


def _line_patch_d2acf2cb(
    orientation: str,
    idx: Integer,
    height_value: Integer,
) -> frozenset[IntegerTuple]:
    if orientation == "horizontal":
        return frozenset((idx, j) for j in range(ONE, decrement(GRID_WIDTH_D2ACF2CB)))
    return frozenset((i, idx) for i in range(ONE, decrement(height_value)))


def _endpoint_patch_d2acf2cb(
    orientation: str,
    idx: Integer,
    height_value: Integer,
) -> frozenset[IntegerTuple]:
    if orientation == "horizontal":
        return frozenset({(idx, ZERO), (idx, decrement(GRID_WIDTH_D2ACF2CB))})
    return frozenset({(ZERO, idx), (decrement(height_value), idx)})


def generate_d2acf2cb(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    x0 = choice(("horizontal", "vertical"))
    x1 = unifint(diff_lb, diff_ub, GRID_HEIGHT_RANGE_D2ACF2CB)
    x2 = _make_base_grid_d2acf2cb(x1)
    x3 = tuple(range(ONE, decrement(x1))) if x0 == "horizontal" else tuple(range(ONE, decrement(GRID_WIDTH_D2ACF2CB)))
    x4 = min(MAX_MARKED_LINES_D2ACF2CB, len(x3))
    x5 = unifint(diff_lb, diff_ub, (ONE, x4))
    x6 = tuple(sorted(sample(x3, x5)))
    x7 = bool(randint(ZERO, ONE))
    x8 = x2
    for x9 in x6:
        x10 = _endpoint_patch_d2acf2cb(x0, x9, x1)
        x8 = fill(x8, FOUR, x10)
    x11 = x8
    x12 = x8
    if x7:
        for x13 in x6:
            x14 = _line_patch_d2acf2cb(x0, x13, x1)
            x11 = _toggle_patch_d2acf2cb(x11, x14)
    else:
        for x15 in x6:
            x16 = _line_patch_d2acf2cb(x0, x15, x1)
            x12 = _toggle_patch_d2acf2cb(x12, x16)
    return {"input": x11, "output": x12}
