from arc2.core import *

from .verifier import verify_60a26a3e


HEIGHT_BOUNDS_60A26A3E = (NINE, 16)
WIDTH_BOUNDS_60A26A3E = (12, 18)
ROW_GAP_BOUNDS_60A26A3E = (FOUR, SEVEN)
COL_PAIR_GAP_BOUNDS_60A26A3E = (FIVE, EIGHT)
COL_TRIPLE_GAP_BOUNDS_60A26A3E = (FOUR, SEVEN)
TEMPLATE_ATTEMPTS_60A26A3E = 64


def _plus_cells_60a26a3e(
    center_cell: IntegerTuple,
) -> Indices:
    x0, x1 = center_cell
    return frozenset(
        {
            (x0 - ONE, x1),
            (x0 + ONE, x1),
            (x0, x1 - ONE),
            (x0, x1 + ONE),
        }
    )


def _plus_centers_from_grid_60a26a3e(
    grid: Grid,
):
    x0 = []
    for x1 in ofcolor(grid, ZERO):
        x2 = T
        for x3 in dneighbors(x1):
            if not equality(index(grid, x3), TWO):
                x2 = F
                break
        if x2:
            x0.append(x1)
    return tuple(sorted(x0))


def _render_input_60a26a3e(
    height: Integer,
    width: Integer,
    centers,
) -> Grid:
    x0 = canvas(ZERO, (height, width))
    x1 = frozenset()
    for x2 in centers:
        x1 = combine(x1, _plus_cells_60a26a3e(x2))
    return fill(x0, TWO, x1)


def _render_output_60a26a3e(
    gi: Grid,
    centers,
) -> Grid:
    x0 = {}
    x1 = {}
    for x2 in centers:
        x3, x4 = x2
        if x3 not in x0:
            x0[x3] = []
        if x4 not in x1:
            x1[x4] = []
        x0[x3].append(x2)
        x1[x4].append(x2)
    x5 = gi
    for x6 in x0.values():
        x7 = tuple(sorted(x6))
        for x8, x9 in zip(x7, x7[ONE:]):
            x10 = difference(difference(connect(x8, x9), initset(x8)), initset(x9))
            x5 = underfill(x5, ONE, x10)
    for x6 in x1.values():
        x7 = tuple(sorted(x6))
        for x8, x9 in zip(x7, x7[ONE:]):
            x10 = difference(difference(connect(x8, x9), initset(x8)), initset(x9))
            x5 = underfill(x5, ONE, x10)
    return x5


def _sample_positions_60a26a3e(
    limit: Integer,
    count: Integer,
    min_gap: Integer,
    max_gap: Integer,
):
    x0 = tuple(range(ONE, limit - ONE))
    if len(x0) < count:
        return None
    for _ in range(TEMPLATE_ATTEMPTS_60A26A3E):
        x1 = tuple(sorted(sample(x0, count)))
        x2 = T
        for x3, x4 in zip(x1, x1[ONE:]):
            x5 = x4 - x3
            if x5 < min_gap or x5 > max_gap:
                x2 = F
                break
        if x2:
            return x1
    return None


def _offset_partner_60a26a3e(
    value: Integer,
    limit: Integer,
    min_gap: Integer,
    max_gap: Integer,
):
    x0 = set()
    for x1 in range(min_gap, max_gap + ONE):
        x2 = value - x1
        x3 = value + x1
        if ONE <= x2 < limit - ONE:
            x0.add(x2)
        if ONE <= x3 < limit - ONE:
            x0.add(x3)
    if len(x0) == ZERO:
        return None
    return choice(tuple(x0))


def _can_place_center_60a26a3e(
    center_cell: IntegerTuple,
    centers,
    height: Integer,
    width: Integer,
) -> Boolean:
    x0, x1 = center_cell
    if not (ONE <= x0 < height - ONE and ONE <= x1 < width - ONE):
        return F
    if center_cell in centers:
        return F
    x2 = set()
    for x3 in centers:
        x2.update(_plus_cells_60a26a3e(x3))
    if center_cell in x2:
        return F
    x4 = _plus_cells_60a26a3e(center_cell)
    if len(x4 & x2) != ZERO:
        return F
    for x5 in centers:
        if x5 in x4:
            return F
    return T


def _sample_singleton_60a26a3e(
    height: Integer,
    width: Integer,
    centers,
    blocked_rows,
    blocked_cols,
):
    x0 = []
    for x1 in range(ONE, height - ONE):
        if x1 in blocked_rows:
            continue
        for x2 in range(ONE, width - ONE):
            if x2 in blocked_cols:
                continue
            x3 = (x1, x2)
            if _can_place_center_60a26a3e(x3, centers, height, width):
                x0.append(x3)
    if len(x0) == ZERO:
        return None
    return choice(tuple(x0))


def _finalize_centers_60a26a3e(
    height: Integer,
    width: Integer,
    centers,
):
    x0 = tuple(sorted(centers))
    x1 = _render_input_60a26a3e(height, width, x0)
    if _plus_centers_from_grid_60a26a3e(x1) != x0:
        return None
    return x0


def _template_pair_pair_60a26a3e(
    height: Integer,
    width: Integer,
):
    for _ in range(TEMPLATE_ATTEMPTS_60A26A3E):
        x0 = _sample_positions_60a26a3e(width, TWO, COL_PAIR_GAP_BOUNDS_60A26A3E[ZERO], COL_PAIR_GAP_BOUNDS_60A26A3E[ONE])
        if x0 is None:
            return None
        x1 = randint(ONE, height - TWO)
        x2 = _offset_partner_60a26a3e(x1, height, ROW_GAP_BOUNDS_60A26A3E[ZERO], ROW_GAP_BOUNDS_60A26A3E[ONE])
        if x2 is None:
            continue
        x3 = {(x1, x0[ZERO]), (x1, x0[ONE]), (x2, choice((x0[ZERO], x0[ONE])))}
        x4 = _finalize_centers_60a26a3e(height, width, x3)
        if x4 is not None:
            return x4
    return None


def _template_row_triplet_60a26a3e(
    height: Integer,
    width: Integer,
):
    for _ in range(TEMPLATE_ATTEMPTS_60A26A3E):
        x0 = _sample_positions_60a26a3e(width, THREE, COL_TRIPLE_GAP_BOUNDS_60A26A3E[ZERO], COL_TRIPLE_GAP_BOUNDS_60A26A3E[ONE])
        if x0 is None:
            return None
        x1 = randint(ONE, height - TWO)
        x2 = _offset_partner_60a26a3e(x1, height, ROW_GAP_BOUNDS_60A26A3E[ZERO], ROW_GAP_BOUNDS_60A26A3E[ONE])
        if x2 is None:
            continue
        x3 = {(x1, x0[ZERO]), (x1, x0[ONE]), (x1, x0[TWO]), (x2, x0[ONE])}
        if randint(ZERO, ONE) == ONE:
            x4 = _sample_singleton_60a26a3e(height, width, x3, {x1, x2}, set(x0))
            if x4 is not None:
                x3.add(x4)
        x5 = _finalize_centers_60a26a3e(height, width, x3)
        if x5 is not None:
            return x5
    return None


def _template_rectangle_60a26a3e(
    height: Integer,
    width: Integer,
):
    for _ in range(TEMPLATE_ATTEMPTS_60A26A3E):
        x0 = _sample_positions_60a26a3e(height, TWO, ROW_GAP_BOUNDS_60A26A3E[ZERO], ROW_GAP_BOUNDS_60A26A3E[ONE])
        x1 = _sample_positions_60a26a3e(width, TWO, COL_PAIR_GAP_BOUNDS_60A26A3E[ZERO], COL_PAIR_GAP_BOUNDS_60A26A3E[ONE])
        if x0 is None or x1 is None:
            return None
        x2 = {(x0[ZERO], x1[ZERO]), (x0[ZERO], x1[ONE]), (x0[ONE], x1[ZERO]), (x0[ONE], x1[ONE])}
        if randint(ZERO, ONE) == ONE:
            x3 = []
            for x4 in range(THREE, SIX):
                x5 = x0[ZERO] - x4
                x6 = x0[ONE] + x4
                if ONE <= x5 < height - ONE:
                    x3.append(x5)
                if ONE <= x6 < height - ONE:
                    x3.append(x6)
            x7 = tuple(x8 for x8 in range(add(x1[ZERO], TWO), subtract(x1[ONE], ONE)) if x8 not in x1)
            if len(x3) > ZERO and len(x7) > ZERO:
                x8 = (choice(tuple(x3)), choice(x7))
                if _can_place_center_60a26a3e(x8, x2, height, width):
                    x2.add(x8)
        x9 = _finalize_centers_60a26a3e(height, width, x2)
        if x9 is not None:
            return x9
    return None


def _sample_centers_60a26a3e(
    height: Integer,
    width: Integer,
):
    x0 = (
        _template_pair_pair_60a26a3e,
        _template_pair_pair_60a26a3e,
        _template_row_triplet_60a26a3e,
        _template_row_triplet_60a26a3e,
        _template_rectangle_60a26a3e,
    )
    for _ in range(TEMPLATE_ATTEMPTS_60A26A3E):
        x1 = choice(x0)(height, width)
        if x1 is not None:
            return x1
    return None


def generate_60a26a3e(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = unifint(diff_lb, diff_ub, HEIGHT_BOUNDS_60A26A3E)
        x1 = unifint(diff_lb, diff_ub, WIDTH_BOUNDS_60A26A3E)
        x2 = _sample_centers_60a26a3e(x0, x1)
        if x2 is None:
            continue
        x3 = _render_input_60a26a3e(x0, x1, x2)
        if _plus_centers_from_grid_60a26a3e(x3) != x2:
            continue
        x4 = _render_output_60a26a3e(x3, x2)
        if x3 == x4:
            continue
        if verify_60a26a3e(x3) != x4:
            continue
        return {"input": x3, "output": x4}
