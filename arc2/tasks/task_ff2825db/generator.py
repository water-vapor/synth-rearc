from arc2.core import *

from .verifier import verify_ff2825db


HEADER_FF2825DB = ((ONE, ONE, TWO, TWO, THREE, THREE, FOUR, FOUR, FIVE, FIVE),)
LOWER_SHAPE_FF2825DB = (NINE, TEN)
COLORS_FF2825DB = interval(ONE, SIX, ONE)
PANEL_RECT_FF2825DB = product(interval(ZERO, NINE, ONE), interval(ZERO, TEN, ONE))
PANEL_BORDER_FF2825DB = box(PANEL_RECT_FF2825DB)
INNER_PANEL_FF2825DB = product(interval(ONE, EIGHT, ONE), interval(ONE, NINE, ONE))


def _rect_patch_ff2825db(
    top: Integer,
    left: Integer,
    height_: Integer,
    width_: Integer,
) -> Indices:
    x0 = interval(top, add(top, height_), ONE)
    x1 = interval(left, add(left, width_), ONE)
    return product(x0, x1)


def _grow_patch_ff2825db(
    region: Indices,
    seeds: Indices,
    target_size: Integer,
    prefer_cluster: Boolean,
) -> Indices:
    x0 = set(region)
    x1 = set(seeds)
    while len(x1) < target_size:
        x2 = set()
        for x3 in x1:
            x2 |= set(dneighbors(x3)) & x0
        x2 -= x1
        if len(x2) > ZERO and (prefer_cluster or choice((T, F))):
            x4 = tuple(x2)
        else:
            x4 = tuple(x0 - x1)
        x1.add(choice(x4))
    return frozenset(x1)


def generate_ff2825db(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0, x1, x2 = sample(COLORS_FF2825DB, THREE)
        x3 = unifint(diff_lb, diff_ub, (TWO, SEVEN))
        x4 = unifint(diff_lb, diff_ub, (TWO, SEVEN))
        x5 = randint(ONE, subtract(EIGHT, x3))
        x6 = randint(ONE, subtract(NINE, x4))
        x7 = add(x5, subtract(x3, ONE))
        x8 = add(x6, subtract(x4, ONE))
        x9 = _rect_patch_ff2825db(x5, x6, x3, x4)
        x10 = frozenset({
            (x5, randint(x6, x8)),
            (x7, randint(x6, x8)),
            (randint(x5, x7), x6),
            (randint(x5, x7), x8),
        })
        if len(x10) == len(x9):
            continue
        x11 = len(x9)
        x12 = max(len(x10), max(TWO, x11 // SIX))
        x13 = min(x11 - ONE, max(x12, x11 // TWO))
        x14 = randint(x12, x13)
        x15 = _grow_patch_ff2825db(x9, x10, x14, T)
        x16 = min(FIVE, len(x15) - ONE)
        x17 = randint(ONE, x16)
        x18 = frozenset({choice(tuple(difference(INNER_PANEL_FF2825DB, x15)))})
        x19 = _grow_patch_ff2825db(difference(INNER_PANEL_FF2825DB, x15), x18, x17, F)
        x20 = canvas(ZERO, LOWER_SHAPE_FF2825DB)
        x21 = fill(x20, x0, PANEL_BORDER_FF2825DB)
        x22 = fill(x21, x1, x15)
        x23 = fill(x22, x2, x19)
        x24 = box(x15)
        x25 = canvas(ZERO, LOWER_SHAPE_FF2825DB)
        x26 = fill(x25, x1, PANEL_BORDER_FF2825DB)
        x27 = fill(x26, x1, x24)
        x28 = vconcat(HEADER_FF2825DB, x23)
        x29 = vconcat(HEADER_FF2825DB, x27)
        if x28 == x29:
            continue
        if verify_ff2825db(x28) != x29:
            continue
        return {"input": x28, "output": x29}
