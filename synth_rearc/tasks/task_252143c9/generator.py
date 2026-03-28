from synth_rearc.core import *

from .verifier import verify_252143c9


GRID_SIDES_252143C9 = (SEVEN, NINE, 11, 11, 13, 13)
COLOR_POOL_252143C9 = tuple(
    x0 for x0 in interval(ZERO, TEN, ONE)
    if x0 != SEVEN
)
TARGET_QUADRANTS_252143C9 = ("ur", "ll")


def _quadrant_spec_252143c9(
    side: Integer,
    name: str,
) -> tuple[tuple[int, ...], tuple[int, ...], bool, bool]:
    x0 = side // TWO
    x1 = tuple(range(x0))
    x2 = tuple(range(add(x0, ONE), side))
    if name == "ul":
        return x1, x1, T, T
    if name == "ur":
        return x1, x2, T, F
    if name == "ll":
        return x2, x1, F, T
    return x2, x2, F, F


def _count_bounds_252143c9(
    cells_per_quadrant: Integer,
    target: Boolean,
) -> tuple[int, int]:
    x0 = max(THREE, divide(multiply(cells_per_quadrant, THREE), TEN))
    x1 = max(add(x0, ONE), divide(add(cells_per_quadrant, ONE), TWO))
    if target:
        x0 = max(FOUR, divide(cells_per_quadrant, THREE))
    x1 = min(cells_per_quadrant, x1)
    return (x0, x1)


def _weighted_patch_252143c9(
    rows: tuple[int, ...],
    cols: tuple[int, ...],
    mid: Integer,
    toward_top: Boolean,
    toward_left: Boolean,
    count: Integer,
    strong_bias: Boolean,
    require_outer_edges: Boolean,
) -> frozenset[tuple[int, int]] | None:
    x0 = tuple((x1, x2) for x1 in rows for x2 in cols)
    x1 = []
    for x2, x3 in x0:
        x4 = subtract(mid, x2) if toward_top else subtract(x2, mid)
        x5 = subtract(mid, x3) if toward_left else subtract(x3, mid)
        x6 = multiply(x4, x5) if strong_bias else add(x4, x5)
        x7 = add(x6, ONE)
        x1.extend([astuple(x2, x3)] * x7)
    x8 = first(rows) if toward_top else last(rows)
    x9 = first(cols) if toward_left else last(cols)
    for _ in range(80):
        x10 = list(x1)
        shuffle(x10)
        x11 = []
        x12 = set()
        for x13 in x10:
            if x13 in x12:
                continue
            x12.add(x13)
            x11.append(x13)
            if len(x11) == count:
                break
        x14 = frozenset(x11)
        x15 = {x16 for x16, _ in x14}
        x17 = {x18 for _, x18 in x14}
        if len(x15) < TWO or len(x17) < TWO:
            continue
        if require_outer_edges:
            x18 = any(x19 == x8 for x19, _ in x14)
            x19 = any(x20 == x9 for _, x20 in x14)
            if not (x18 and x19):
                continue
        return x14
    return None


def generate_252143c9(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    x0 = ("ul", "ur", "ll", "lr")
    while True:
        x1 = choice(GRID_SIDES_252143C9)
        x2 = x1 // TWO
        x3 = multiply(x2, x2)
        x4 = choice(TARGET_QUADRANTS_252143C9)
        x5 = sample(COLOR_POOL_252143C9, FOUR)
        x6 = {x7: x8 for x7, x8 in zip(x0, x5)}
        gi = canvas(SEVEN, (x1, x1))
        x7 = F
        for x8 in x0:
            x9, x10, x11, x12 = _quadrant_spec_252143c9(x1, x8)
            x13, x14 = _count_bounds_252143c9(x3, equality(x8, x4))
            x15 = unifint(diff_lb, diff_ub, (x13, x14))
            x16 = _weighted_patch_252143c9(
                x9,
                x10,
                x2,
                x11,
                x12,
                x15,
                equality(x8, x4),
                equality(x8, x4),
            )
            if x16 is None:
                x7 = T
                break
            gi = fill(gi, x6[x8], x16)
        if x7:
            continue
        x17 = astuple(x2, x2)
        x18 = x6[x4]
        gi = fill(gi, x18, initset(x17))
        go = verify_252143c9(gi)
        x19 = ofcolor(gi, x18)
        x20 = difference(x19, initset(x17))
        if len(x20) < THREE:
            continue
        if gi == go:
            continue
        if verify_252143c9(gi) != go:
            continue
        return {"input": gi, "output": go}
