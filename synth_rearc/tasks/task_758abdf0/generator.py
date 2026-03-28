from synth_rearc.core import *


def _render_horizontal_758abdf0(
    height: int,
    width: int,
    top: bool,
    single_cols: frozenset[int],
    pair_cols: frozenset[int],
) -> tuple[Grid, Grid]:
    border_row = ZERO if top else height - ONE
    near0, near1 = ((ONE, TWO) if top else (height - TWO, height - THREE))
    far0, far1 = ((height - TWO, height - ONE) if top else (ZERO, ONE))
    x0 = connect((border_row, ZERO), (border_row, width - ONE))
    x1 = canvas(SEVEN, (height, width))
    gi = fill(x1, ZERO, x0)
    x2 = frozenset((near0, j) for j in single_cols)
    x3 = frozenset((i, j) for j in pair_cols for i in (near0, near1))
    gi = fill(gi, EIGHT, x2)
    gi = fill(gi, EIGHT, x3)
    go = fill(x1, ZERO, x0)
    x4 = frozenset((i, j) for j in single_cols for i in (near0, near1))
    x5 = frozenset((i, j) for j in pair_cols for i in (far0, far1))
    go = fill(go, EIGHT, x4)
    go = fill(go, ZERO, x5)
    return gi, go


def _render_vertical_758abdf0(
    height: int,
    width: int,
    left: bool,
    single_rows: frozenset[int],
    pair_rows: frozenset[int],
) -> tuple[Grid, Grid]:
    border_col = ZERO if left else width - ONE
    near0, near1 = ((ONE, TWO) if left else (width - TWO, width - THREE))
    far0, far1 = ((width - TWO, width - ONE) if left else (ZERO, ONE))
    x0 = connect((ZERO, border_col), (height - ONE, border_col))
    x1 = canvas(SEVEN, (height, width))
    gi = fill(x1, ZERO, x0)
    x2 = frozenset((i, near0) for i in single_rows)
    x3 = frozenset((i, j) for i in pair_rows for j in (near0, near1))
    gi = fill(gi, EIGHT, x2)
    gi = fill(gi, EIGHT, x3)
    go = fill(x1, ZERO, x0)
    x4 = frozenset((i, j) for i in single_rows for j in (near0, near1))
    x5 = frozenset((i, j) for i in pair_rows for j in (far0, far1))
    go = fill(go, EIGHT, x4)
    go = fill(go, ZERO, x5)
    return gi, go


def generate_758abdf0(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    horizontal = choice((T, F))
    span = unifint(diff_lb, diff_ub, (EIGHT, 16))
    near_edge = choice((T, F))
    if horizontal:
        height, width = EIGHT, span
        lane_count = width
    else:
        height, width = span, EIGHT
        lane_count = height
    max_active = min(lane_count - ONE, max(FOUR, lane_count // TWO))
    nactive = unifint(diff_lb, diff_ub, (TWO, max_active))
    npairs = unifint(diff_lb, diff_ub, (ONE, nactive - ONE))
    active = tuple(sample(interval(ZERO, lane_count, ONE), nactive))
    pairs = frozenset(sample(active, npairs))
    singles = frozenset(lane for lane in active if lane not in pairs)
    if horizontal:
        gi, go = _render_horizontal_758abdf0(height, width, near_edge, singles, pairs)
    else:
        gi, go = _render_vertical_758abdf0(height, width, near_edge, singles, pairs)
    return {"input": gi, "output": go}
