from synth_rearc.core import *


DIMENSIONS_070DD51E = (
    (20, 10),
    (20, 20),
    (20, 20),
    (30, 20),
)

LAYOUTS_070DD51E = (
    (THREE, TWO),
    (THREE, TWO),
    (TWO, THREE),
    (TWO, THREE),
    (TWO, TWO),
    (THREE, THREE),
)


def _horizontal_patch_070dd51e(spec: tuple[int, int, int, int]) -> Indices:
    _, row, left, right = spec
    return connect((row, left), (row, right))


def _vertical_patch_070dd51e(spec: tuple[int, int, int, int]) -> Indices:
    _, top, bottom, col = spec
    return connect((top, col), (bottom, col))


def _build_input_070dd51e(
    dims: tuple[int, int],
    horizontals: Tuple,
    verticals: Tuple,
) -> Grid:
    gi = canvas(ZERO, dims)
    for color_value, row, left, right in horizontals:
        gi = fill(gi, color_value, frozenset({(row, left), (row, right)}))
    for color_value, top, bottom, col in verticals:
        gi = fill(gi, color_value, frozenset({(top, col), (bottom, col)}))
    return gi


def _build_output_070dd51e(
    dims: tuple[int, int],
    horizontals: Tuple,
    verticals: Tuple,
) -> Grid:
    go = canvas(ZERO, dims)
    for color_value, row, left, right in horizontals:
        go = fill(go, color_value, connect((row, left), (row, right)))
    for color_value, top, bottom, col in verticals:
        go = fill(go, color_value, connect((top, col), (bottom, col)))
    return go


def _intersection_count_070dd51e(
    horizontals: Tuple,
    verticals: Tuple,
) -> Integer:
    x0 = ZERO
    for _, row, left, right in horizontals:
        for _, top, bottom, col in verticals:
            if top < row < bottom and left < col < right:
                x0 += ONE
    return x0


def _endpoints_070dd51e(
    horizontals: Tuple,
    verticals: Tuple,
) -> Tuple:
    x0 = []
    for _, row, left, right in horizontals:
        x0.append((row, left))
        x0.append((row, right))
    for _, top, bottom, col in verticals:
        x0.append((top, col))
        x0.append((bottom, col))
    return tuple(x0)


def _has_endpoint_conflict_070dd51e(
    horizontals: Tuple,
    verticals: Tuple,
) -> Boolean:
    for _, row, left, right in horizontals:
        x0 = ((row, left), (row, right))
        for x1 in verticals:
            x2 = _vertical_patch_070dd51e(x1)
            if first(x0) in x2 or last(x0) in x2:
                return T
    for _, top, bottom, col in verticals:
        x0 = ((top, col), (bottom, col))
        for x1 in horizontals:
            x2 = _horizontal_patch_070dd51e(x1)
            if first(x0) in x2 or last(x0) in x2:
                return T
    return F


def _all_horizontals_intersect_070dd51e(
    horizontals: Tuple,
    verticals: Tuple,
) -> Boolean:
    for _, row, left, right in horizontals:
        x0 = F
        for _, top, bottom, col in verticals:
            if top < row < bottom and left < col < right:
                x0 = T
                break
        if not x0:
            return F
    return T


def _valid_layout_070dd51e(
    horizontals: Tuple,
    verticals: Tuple,
) -> Boolean:
    x0 = _endpoints_070dd51e(horizontals, verticals)
    if len(x0) != len(set(x0)):
        return F
    if _has_endpoint_conflict_070dd51e(horizontals, verticals):
        return F
    if not _all_horizontals_intersect_070dd51e(horizontals, verticals):
        return F
    x1 = _intersection_count_070dd51e(horizontals, verticals)
    return TWO <= x1 <= FOUR


def _sample_horizontals_070dd51e(
    rows: Tuple,
    colors: Tuple,
    width_value: Integer,
    diff_lb: float,
    diff_ub: float,
) -> Tuple:
    x0 = []
    for x1, x2 in enumerate(rows):
        x3 = unifint(diff_lb, diff_ub, (ONE, width_value - FIVE))
        x4 = unifint(diff_lb, diff_ub, (x3 + THREE, width_value - TWO))
        x0.append((colors[x1], x2, x3, x4))
    return tuple(x0)


def _sample_verticals_070dd51e(
    cols: Tuple,
    colors: Tuple,
    height_value: Integer,
    horizontal_count: Integer,
    diff_lb: float,
    diff_ub: float,
) -> Tuple:
    x0 = []
    x1 = max(FIVE, horizontal_count + THREE)
    for x2, x3 in enumerate(cols):
        x4 = unifint(diff_lb, diff_ub, (ONE, height_value - x1))
        x5 = unifint(diff_lb, diff_ub, (x4 + FOUR, height_value - TWO))
        x0.append((colors[x2], x4, x5, x3))
    return tuple(x0)


def generate_070dd51e(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    x0 = remove(ZERO, interval(ZERO, TEN, ONE))
    while True:
        x1 = choice(DIMENSIONS_070DD51E)
        x2, x3 = x1
        x4, x5 = choice(LAYOUTS_070DD51E if x3 > TEN else LAYOUTS_070DD51E[:-ONE])
        x6 = tuple(sorted(sample(tuple(range(ONE, x2 - ONE)), x4)))
        x7 = tuple(sorted(sample(tuple(range(ONE, x3 - ONE)), x5)))
        x8 = tuple(sample(x0, x4 + x5))
        x9 = _sample_horizontals_070dd51e(x6, x8[:x4], x3, diff_lb, diff_ub)
        x10 = _sample_verticals_070dd51e(x7, x8[x4:], x2, x4, diff_lb, diff_ub)
        if not _valid_layout_070dd51e(x9, x10):
            continue
        gi = _build_input_070dd51e(x1, x9, x10)
        go = _build_output_070dd51e(x1, x9, x10)
        if gi == go:
            continue
        return {"input": gi, "output": go}
