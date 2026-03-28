from synth_rearc.core import *


BOARD_SHAPE_D19F7514 = (SIX, FOUR)
UNIVERSE_D19F7514 = frozenset((i, j) for i in range(SIX) for j in range(FOUR))

TOP_ONLY_D19F7514 = ONE
BOTTOM_ONLY_D19F7514 = TWO
BOTH_D19F7514 = THREE

STATE_BAG_D19F7514 = (
    TOP_ONLY_D19F7514,
    TOP_ONLY_D19F7514,
    BOTTOM_ONLY_D19F7514,
    BOTTOM_ONLY_D19F7514,
    BOTH_D19F7514,
    BOTH_D19F7514,
    BOTH_D19F7514,
)

OUTPUT_COUNTS_D19F7514 = (
    12,
    14,
    15,
    16,
    17,
    17,
    18,
    18,
    18,
    19,
    19,
    19,
    20,
    21,
)


def _row_counts_d19f7514(
    patch: frozenset[IntegerTuple],
) -> tuple[Integer, ...]:
    return tuple(sum((i, j) in patch for j in range(FOUR)) for i in range(SIX))


def _col_counts_d19f7514(
    patch: frozenset[IntegerTuple],
) -> tuple[Integer, ...]:
    return tuple(sum((i, j) in patch for i in range(SIX)) for j in range(FOUR))


def _patch_profile_ok_d19f7514(
    patch: frozenset[IntegerTuple],
) -> Boolean:
    x0 = len(patch)
    x1 = _row_counts_d19f7514(patch)
    x2 = _col_counts_d19f7514(patch)
    if not (12 <= x0 <= 21):
        return F
    if x1.count(ZERO) > ONE:
        return F
    if x1.count(ONE) > ONE:
        return F
    if min(x2) < TWO:
        return F
    if max(x1) < THREE:
        return F
    return T


def _panel_profile_ok_d19f7514(
    panel: Grid,
    lower: Integer,
    upper: Integer,
) -> Boolean:
    x0 = ofcolor(panel, mostcolor(panel))
    x1 = difference(asindices(panel), x0)
    x2 = len(x1)
    x3 = _row_counts_d19f7514(x1)
    x4 = _col_counts_d19f7514(x1)
    if not (lower <= x2 <= upper):
        return F
    if x3.count(ZERO) > TWO:
        return F
    if min(x4) == ZERO:
        return F
    if max(x3) < THREE:
        return F
    if len(set(panel)) < FOUR:
        return F
    return T


def _render_panels_d19f7514(
    patch: frozenset[IntegerTuple],
    assignments: dict[IntegerTuple, Integer],
) -> tuple[Grid, Grid, Grid]:
    x0 = frozenset(
        loc for loc in patch
        if assignments[loc] != BOTTOM_ONLY_D19F7514
    )
    x1 = frozenset(
        loc for loc in patch
        if assignments[loc] != TOP_ONLY_D19F7514
    )
    x2 = canvas(ZERO, BOARD_SHAPE_D19F7514)
    x3 = fill(x2, THREE, x0)
    x4 = fill(x2, FIVE, x1)
    x5 = fill(x2, FOUR, patch)
    return x3, x4, x5


def _sample_patch_d19f7514(
    diff_lb: float,
    diff_ub: float,
) -> frozenset[IntegerTuple] | None:
    x0 = unifint(diff_lb, diff_ub, (ZERO, len(OUTPUT_COUNTS_D19F7514) - ONE))
    x1 = OUTPUT_COUNTS_D19F7514[x0]
    for _ in range(60):
        x2 = frozenset(sample(tuple(UNIVERSE_D19F7514), x1))
        if _patch_profile_ok_d19f7514(x2):
            return x2
    return None


def generate_d19f7514(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = _sample_patch_d19f7514(diff_lb, diff_ub)
        if x0 is None:
            continue
        for _ in range(80):
            x1 = {loc: choice(STATE_BAG_D19F7514) for loc in x0}
            x2 = tuple(x1.values())
            if len(set(x2)) < THREE:
                continue
            x3 = x2.count(BOTH_D19F7514)
            if not (FIVE <= x3 <= TEN):
                continue
            x4, x5, go = _render_panels_d19f7514(x0, x1)
            if not _panel_profile_ok_d19f7514(x4, NINE, 16):
                continue
            if not _panel_profile_ok_d19f7514(x5, EIGHT, 18):
                continue
            gi = vconcat(x4, x5)
            return {"input": gi, "output": go}
