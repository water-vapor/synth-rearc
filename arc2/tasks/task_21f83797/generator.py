from arc2.core import *

from .verifier import verify_21f83797


CANVAS_SIDE_21F83797 = 13
CANVAS_SHAPE_21F83797 = (CANVAS_SIDE_21F83797, CANVAS_SIDE_21F83797)
INNER_HEIGHT_BOUNDS_21F83797 = (THREE, EIGHT)
INNER_WIDTH_BOUNDS_21F83797 = (THREE, EIGHT)


def _seed_patch_21f83797(
    top: int,
    left: int,
    bottom: int,
    right: int,
    anti: bool,
) -> Indices:
    if anti:
        return frozenset({(top, right), (bottom, left)})
    return frozenset({(top, left), (bottom, right)})


def _render_21f83797(
    top: int,
    left: int,
    bottom: int,
    right: int,
    anti: bool,
) -> tuple[Grid, Grid]:
    x0 = canvas(ZERO, CANVAS_SHAPE_21F83797)
    x1 = _seed_patch_21f83797(top, left, bottom, right, anti)
    x2 = fill(x0, TWO, x1)
    x3 = hfrontier((top, left))
    x4 = vfrontier((top, left))
    x5 = hfrontier((bottom, right))
    x6 = vfrontier((bottom, right))
    x7 = combine(x3, x4)
    x8 = combine(x5, x6)
    x9 = combine(x7, x8)
    x10 = fill(x2, TWO, x9)
    x11 = difference(backdrop(x1), box(x1))
    x12 = fill(x10, ONE, x11)
    return x2, x12


def generate_21f83797(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = unifint(diff_lb, diff_ub, INNER_HEIGHT_BOUNDS_21F83797)
        x1 = unifint(diff_lb, diff_ub, INNER_WIDTH_BOUNDS_21F83797)
        x2 = subtract(subtract(CANVAS_SIDE_21F83797, x0), THREE)
        x3 = subtract(subtract(CANVAS_SIDE_21F83797, x1), THREE)
        x4 = randint(ONE, x2)
        x5 = randint(ONE, x3)
        x6 = add(x4, increment(x0))
        x7 = add(x5, increment(x1))
        x8, x9 = _render_21f83797(x4, x5, x6, x7, choice((T, F)))
        if verify_21f83797(x8) != x9:
            continue
        return {"input": x8, "output": x9}
