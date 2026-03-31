from __future__ import annotations

from synth_rearc.core import *

from .helpers import bar_patch_cb2d8a2c, trace_path_cb2d8a2c


def _row_specs_cb2d8a2c(
    ks: tuple[Integer, ...],
    diff_lb: float,
    diff_ub: float,
) -> tuple[tuple[Integer, Integer], ...]:
    x0 = []
    x1 = ZERO
    for x2, x3 in enumerate(ks):
        x4 = unifint(diff_lb, diff_ub, (ONE if x2 == ZERO else ZERO, THREE))
        x5 = x1 + x4 + x3 + ONE
        x0.append((x5, x3))
        x1 = x5 + x3 + ONE
    return tuple(x0)


def _paint_bar_cb2d8a2c(
    grid: Grid,
    row: Integer,
    start: Integer,
    stop: Integer,
    anchor: str,
    ones: Integer,
) -> Grid:
    x0 = fill(grid, TWO, connect((row, start), (row, stop)))
    if anchor == "left":
        x1 = frozenset((row, start + TWO * x2) for x2 in range(ones))
    else:
        x1 = frozenset((row, stop - TWO * x2) for x2 in range(ones))
    return fill(x0, ONE, x1)


def _canonical_example_cb2d8a2c(
    diff_lb: float,
    diff_ub: float,
) -> dict | None:
    x0 = choice((ONE, TWO, TWO, THREE, THREE, FOUR))
    x1 = tuple(choice((ONE, ONE, TWO, TWO, THREE, FOUR)) for _ in range(x0))
    x2 = _row_specs_cb2d8a2c(x1, diff_lb, diff_ub)
    x3 = first(last(x2))
    x4 = max(unifint(diff_lb, diff_ub, (12, 28)), x3 + unifint(diff_lb, diff_ub, (TWO, EIGHT)))
    if x4 > 30:
        return None
    x5 = unifint(diff_lb, diff_ub, (13, 19))
    x6 = choice(("left", "right"))
    x7 = randint(ONE, x5 - TWO)
    x8 = []
    for x9, (x10, x11) in enumerate(x2):
        x12 = x6 if x9 % TWO == ZERO else ("right" if x6 == "left" else "left")
        if x12 == "left":
            x13 = max(x7 + ONE, max(FIVE, TWO * x11 - ONE))
            x14 = x5 - x11 - TWO
            if x13 > x14:
                return None
            x15 = randint(x13, x14)
            x16 = ZERO
            x17 = decrement(x15)
            x18 = x15 + x11
        else:
            x13 = x11 + TWO
            x14 = min(x7, x5 - max(FIVE, TWO * x11 - ONE))
            if x13 > x14:
                return None
            x16 = randint(x13, x14)
            x17 = decrement(x5)
            x18 = x16 - x11 - ONE
        if not (x16 <= x7 <= x17):
            return None
        if not (ONE <= x18 < decrement(x5)):
            return None
        x8.append((x10, x16, x17, x12, x11))
        x7 = x18
    x19 = initset((ZERO, randint(ONE, x5 - TWO)))
    x20 = fill(canvas(EIGHT, (x4, x5)), THREE, x19)
    x21 = first(totuple(x19))
    x22 = x21[ONE]
    x23 = x20
    for x24, x25, x26, x27, x28 in x8:
        if not (x25 <= x22 <= x26):
            return None
        x23 = _paint_bar_cb2d8a2c(x23, x24, x25, x26, x27, x28)
        if x27 == "left":
            x22 = x26 + x28 + ONE
        else:
            x22 = x25 - x28 - ONE
    x29 = bar_patch_cb2d8a2c(x23)
    x30 = trace_path_cb2d8a2c(x23)
    x31 = fill(x23, TWO, x29)
    x32 = fill(x31, THREE, x30)
    if equality(x23, x32):
        return None
    return {"input": x23, "output": x32}


def generate_cb2d8a2c(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = _canonical_example_cb2d8a2c(diff_lb, diff_ub)
        if x0 is None:
            continue
        x1 = choice((identity, identity, dmirror, compose(vmirror, dmirror)))
        x2 = x1(x0["input"])
        x3 = x1(x0["output"])
        if equality(x2, x3):
            continue
        return {"input": x2, "output": x3}
