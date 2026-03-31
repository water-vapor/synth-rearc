from synth_rearc.core import *

from .helpers import ANTI_DIAG_PATCH_7491F3CF, ELBOW_SEPARATOR_PATCH_7491F3CF
from .helpers import FULL_PANEL_PATCH_7491F3CF, HORIZONTAL_SEPARATOR_PATCH_7491F3CF
from .helpers import MAIN_DIAG_PATCH_7491F3CF, MOTIF_PATCHES_7491F3CF
from .helpers import PANEL_SHAPE_7491F3CF, VERTICAL_SEPARATOR_PATCH_7491F3CF
from .helpers import mirror_patch_7491f3cf, panel_mask_from_marker_patch_7491f3cf
from .helpers import render_patch_panel_7491f3cf, rotate_patch_cw_7491f3cf


def _place_panel_7491f3cf(
    grid: Grid,
    panel: Grid,
    left: Integer,
) -> Grid:
    return paint(grid, shift(asobject(panel), (ONE, left)))


def _mix_panels_7491f3cf(
    mask: Indices,
    left_panel: Grid,
    right_panel: Grid,
) -> Grid:
    x0 = difference(FULL_PANEL_PATCH_7491F3CF, mask)
    x1 = toobject(mask, left_panel)
    x2 = toobject(x0, right_panel)
    x3 = canvas(mostcolor(left_panel), PANEL_SHAPE_7491F3CF)
    return paint(x3, combine(x1, x2))


def _sample_marker_patch_7491f3cf(
    diff_lb: float,
    diff_ub: float,
) -> Indices:
    x0 = choice(("anti", "anti", "main", "main", "vertical", "horizontal", "elbow"))
    if x0 == "anti":
        x1 = choice(((ZERO, ZERO), (FOUR, FOUR)))
        return combine(ANTI_DIAG_PATCH_7491F3CF, frozenset({x1}))
    if x0 == "main":
        x1 = choice(((ZERO, FOUR), (FOUR, ZERO)))
        return combine(MAIN_DIAG_PATCH_7491F3CF, frozenset({x1}))
    if x0 == "vertical":
        x1 = unifint(diff_lb, diff_ub, (ZERO, FOUR))
        x2 = choice((ZERO, FOUR))
        return combine(VERTICAL_SEPARATOR_PATCH_7491F3CF, frozenset({(x1, x2)}))
    if x0 == "horizontal":
        x1 = choice((ZERO, FOUR))
        x2 = unifint(diff_lb, diff_ub, (ZERO, FOUR))
        return combine(HORIZONTAL_SEPARATOR_PATCH_7491F3CF, frozenset({(x1, x2)}))
    x1 = ELBOW_SEPARATOR_PATCH_7491F3CF
    x2 = (ZERO, TWO)
    x3 = unifint(diff_lb, diff_ub, (ZERO, THREE))
    for _ in range(x3):
        x1 = frozenset((j, subtract(TWO, i)) for i, j in x1)
        x2 = (x2[1], subtract(TWO, x2[0]))
    x4 = unifint(diff_lb, diff_ub, (ZERO, TWO))
    x5 = unifint(diff_lb, diff_ub, (ZERO, TWO))
    x6 = shift(x1, (x4, x5))
    x7 = add(x2, (x4, x5))
    return combine(x6, frozenset({x7}))


def _sample_motif_patch_7491f3cf(
    diff_lb: float,
    diff_ub: float,
) -> Indices:
    x0 = choice(MOTIF_PATCHES_7491F3CF)
    x1 = unifint(diff_lb, diff_ub, (ZERO, THREE))
    for _ in range(x1):
        x0 = rotate_patch_cw_7491f3cf(x0)
    if choice((T, F)):
        x0 = mirror_patch_7491f3cf(x0)
    return x0


def generate_7491f3cf(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0, x1, x2, x3, x4 = sample(tuple(interval(ZERO, TEN, ONE)), FIVE)
        x5 = _sample_marker_patch_7491f3cf(diff_lb, diff_ub)
        x6 = panel_mask_from_marker_patch_7491f3cf(x5)
        x7 = _sample_motif_patch_7491f3cf(diff_lb, diff_ub)
        x8 = _sample_motif_patch_7491f3cf(diff_lb, diff_ub)
        x9 = render_patch_panel_7491f3cf(x1, x2, x5)
        x10 = render_patch_panel_7491f3cf(x1, x3, x7)
        x11 = render_patch_panel_7491f3cf(x1, x4, x8)
        x12 = _mix_panels_7491f3cf(x6, x10, x11)
        if colorcount(x12, x3) < TWO or colorcount(x12, x4) < TWO:
            continue
        if equality(x12, x10) or equality(x12, x11):
            continue
        x13 = canvas(x1, PANEL_SHAPE_7491F3CF)
        x14 = canvas(x0, (SEVEN, 25))
        x15 = _place_panel_7491f3cf(x14, x9, ONE)
        x16 = _place_panel_7491f3cf(x15, x10, 7)
        x17 = _place_panel_7491f3cf(x16, x11, 13)
        x18 = _place_panel_7491f3cf(x17, x13, 19)
        x19 = _place_panel_7491f3cf(x18, x12, 19)
        if equality(x18, x19):
            continue
        from .verifier import verify_7491f3cf

        if verify_7491f3cf(x18) != x19:
            continue
        return {"input": x18, "output": x19}
