from synth_rearc.core import *

from .helpers import (
    CARDINALS_DF978A02,
    LARGE_TEMPLATES_DF978A02,
    SMALL_TEMPLATES_DF978A02,
    cap_patch_df978a02,
    direction_df978a02,
    foreground_focus_df978a02,
    place_template_df978a02,
    tip_cell_df978a02,
)
from .verifier import verify_df978a02


def _fits_df978a02(
    patch: Patch,
    dims: IntegerTuple,
) -> Boolean:
    h, w = dims
    return all(ZERO <= i < h and ZERO <= j < w for i, j in toindices(patch))


def _tip_df978a02(
    focus: IntegerTuple,
    direction: IntegerTuple,
    gap: Integer,
    drift: Integer,
) -> IntegerTuple:
    fi, fj = focus
    if direction == (ONE, ZERO):
        return (fi - gap, fj + drift)
    if direction == (-1, ZERO):
        return (fi + gap, fj + drift)
    if direction == (ZERO, ONE):
        return (fi + drift, fj - gap)
    return (fi + drift, fj + gap)


def _apply_rule_df978a02(
    gi: Grid,
) -> Grid:
    x0 = mostcolor(gi)
    x1 = objects(gi, T, T, T)
    x2 = foreground_focus_df978a02(x1)
    x3 = argmax(x1, size)
    x4 = gi
    for x5 in x1:
        x6 = direction_df978a02(x5, x2)
        if x5 == x3:
            x7 = cap_patch_df978a02(x5, x6)
            x4 = fill(x4, color(x5), x7)
        else:
            x7 = tip_cell_df978a02(x5, x6)
            x8 = frozenset({x7})
            x4 = fill(x4, x0, x8)
    return x4


def generate_df978a02(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    dims = (16, 16)
    bg = EIGHT
    colors = tuple(sorted(remove(bg, interval(ZERO, TEN, ONE))))
    while True:
        focus = (
            unifint(diff_lb, diff_ub, (SIX, NINE)),
            unifint(diff_lb, diff_ub, (SIX, NINE)),
        )
        large_direction = choice(CARDINALS_DF978A02)
        palette_values = sample(colors, len(CARDINALS_DF978A02))
        gi = canvas(bg, dims)
        occupied = frozenset({})
        failed = F
        for x0, x1 in zip(CARDINALS_DF978A02, palette_values):
            x2 = LARGE_TEMPLATES_DF978A02 if x0 == large_direction else SMALL_TEMPLATES_DF978A02
            x3 = choice(x2)
            x4 = ONE if x0 == large_direction else TWO
            x5 = THREE if x0 == large_direction else FOUR
            x6 = unifint(diff_lb, diff_ub, (x4, x5))
            x7 = randint(-1, 1)
            x8 = _tip_df978a02(focus, x0, x6, x7)
            x9 = place_template_df978a02(x3, x0, x8)
            if not _fits_df978a02(x9, dims):
                failed = T
                break
            if len(intersection(occupied, x9)) != ZERO:
                failed = T
                break
            x10 = recolor(x1, x9)
            gi = paint(gi, x10)
            occupied = combine(occupied, x9)
        if failed:
            continue
        go = _apply_rule_df978a02(gi)
        if gi == go:
            continue
        if verify_df978a02(gi) != go:
            continue
        return {"input": gi, "output": go}
