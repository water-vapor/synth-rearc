from synth_rearc.core import *


HEIGHT_5D2A5C43 = SIX
PANEL_WIDTH_5D2A5C43 = FOUR
DIVIDER_WIDTH_5D2A5C43 = ONE
FULL_PANEL_5D2A5C43 = product(
    interval(ZERO, HEIGHT_5D2A5C43, ONE),
    interval(ZERO, PANEL_WIDTH_5D2A5C43, ONE),
)
ASSIGNMENTS_5D2A5C43 = (ONE, ONE, TWO, TWO, THREE, THREE)


def _sample_output_mask_5d2a5c43(
    diff_lb: float,
    diff_ub: float,
) -> Indices:
    x0 = unifint(diff_lb, diff_ub, (FOUR, SIX))
    x1 = totuple(FULL_PANEL_5D2A5C43)
    while True:
        x2 = frozenset(sample(x1, x0))
        x3 = tuple(sum(loc[0] == i for loc in x2) for i in range(HEIGHT_5D2A5C43))
        if maximum(x3) <= TWO:
            return difference(FULL_PANEL_5D2A5C43, x2)


def _split_mask_5d2a5c43(mask: Indices) -> tuple[Indices, Indices]:
    x0 = totuple(mask)
    while True:
        x1 = set()
        x2 = set()
        for x3 in x0:
            x4 = choice(ASSIGNMENTS_5D2A5C43)
            if x4 != TWO:
                x1.add(x3)
            if x4 != ONE:
                x2.add(x3)
        x5 = frozenset(x1)
        x6 = frozenset(x2)
        x7 = difference(x5, x6)
        x8 = difference(x6, x5)
        x9 = intersection(x5, x6)
        if (
            SIX <= size(x5) <= 18
            and SIX <= size(x6) <= 18
            and size(x7) >= TWO
            and size(x8) >= TWO
            and size(x9) >= TWO
        ):
            return x5, x6


def _paint_panel_5d2a5c43(
    cells: Indices,
    value: int,
) -> Grid:
    x0 = canvas(ZERO, (HEIGHT_5D2A5C43, PANEL_WIDTH_5D2A5C43))
    x1 = fill(x0, value, cells)
    return x1


def generate_5d2a5c43(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    x0 = _sample_output_mask_5d2a5c43(diff_lb, diff_ub)
    x1, x2 = _split_mask_5d2a5c43(x0)
    x3 = _paint_panel_5d2a5c43(x1, FOUR)
    x4 = canvas(ONE, (HEIGHT_5D2A5C43, DIVIDER_WIDTH_5D2A5C43))
    x5 = _paint_panel_5d2a5c43(x2, FOUR)
    x6 = hconcat(hconcat(x3, x4), x5)
    x7 = _paint_panel_5d2a5c43(x0, EIGHT)
    return {"input": x6, "output": x7}
