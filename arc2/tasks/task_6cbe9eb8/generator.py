from __future__ import annotations

from arc2.core import *

from .verifier import verify_6cbe9eb8


FAMILIES_6CBE9EB8 = (
    {
        "bg_kind": ZERO,
        "colors": (EIGHT, FOUR, FIVE, SIX),
        "kinds": (T, T, F, F),
    },
    {
        "bg_kind": ONE,
        "colors": (THREE, EIGHT, SIX, FOUR),
        "kinds": (T, T, F, F),
    },
    {
        "bg_kind": TWO,
        "colors": (THREE, EIGHT, FOUR),
        "kinds": (T, F, F),
    },
    {
        "bg_kind": THREE,
        "colors": (EIGHT, SIX, FOUR, NINE),
        "kinds": (T, T, F, F),
    },
)


def _tile_6cbe9eb8(kind: Integer) -> Grid:
    if kind == ZERO:
        x0 = sample((ZERO, ONE, TWO, THREE), FOUR)
        return (
            (x0[ZERO], x0[ONE], x0[TWO], x0[THREE]),
            (x0[ONE], x0[TWO], x0[THREE], x0[ZERO]),
        )
    if kind == ONE:
        x0 = sample((ZERO, ONE, TWO), THREE)
        return (
            (x0[ZERO], x0[ONE], x0[TWO]),
            (x0[ONE], x0[TWO], x0[ZERO]),
            (x0[ONE], x0[TWO], x0[ZERO]),
        )
    if kind == TWO:
        x0 = sample((ZERO, ONE), TWO)
        return (
            (x0[ZERO], x0[ONE]),
            (x0[ONE], x0[ZERO]),
        )
    x0 = sample((ONE, TWO, THREE), THREE)
    return (
        (x0[ONE], x0[TWO], x0[TWO]),
        (x0[ZERO], x0[ONE], x0[ONE]),
        (x0[TWO], x0[ZERO], x0[ZERO]),
    )


def _render_wallpaper_6cbe9eb8(
    tile: Grid,
    dims: IntegerTuple,
) -> Grid:
    x0, x1 = dims
    x2 = height(tile)
    x3 = width(tile)
    return tuple(tuple(tile[x4 % x2][x5 % x3] for x5 in range(x1)) for x4 in range(x0))


def _paint_rect_6cbe9eb8(
    grid: Grid,
    color_value: Integer,
    top: Integer,
    left: Integer,
    height_value: Integer,
    width_value: Integer,
    is_box: Boolean,
) -> Grid:
    x0 = astuple(top, left)
    x1 = astuple(top + height_value - ONE, left + width_value - ONE)
    x2 = frozenset({x0, x1})
    x3 = box(x2) if both(is_box, greater(height_value, ONE)) and both(is_box, greater(width_value, ONE)) else backdrop(x2)
    return fill(grid, color_value, x3)


def _output_layout_6cbe9eb8(
    heights: tuple[Integer, ...],
    widths: tuple[Integer, ...],
    kinds: tuple[Boolean, ...],
) -> tuple[tuple[Integer, Integer], ...]:
    x0 = []
    x1 = None
    for x2, x3, x4 in zip(heights, widths, kinds):
        if x1 is None:
            x5 = ZERO
            x6 = ZERO
        else:
            x7, x8, x9, x10, x11 = x1
            if x11:
                x12 = x7 + ONE
                x13 = x8 + ONE
                x14 = x9 - TWO
                x15 = x10 - TWO
            else:
                x12 = x7
                x13 = x8
                x14 = x9
                x15 = x10
            x5 = x12 + x14 - x2
            x6 = x13
        x0.append((x5, x6))
        x1 = (x5, x6, x2, x3, x4)
    return tuple(x0)


def _sample_family_dims_6cbe9eb8(
    family_id: Integer,
) -> tuple[tuple[Integer, ...], tuple[Integer, ...]]:
    if family_id == ZERO:
        x0 = randint(10, 14)
        x1 = randint(10, 12)
        x2 = randint(max(FIVE, x0 - SEVEN), x0 - FOUR)
        x3 = randint(max(SIX, x1 - FIVE), x1 - THREE)
        x4 = x2 - TWO
        x5 = x3 - TWO
        x6 = choice((TWO, TWO, TWO, THREE))
        x7 = choice((TWO, TWO, THREE))
        return (x0, x2, x4, x6), (x1, x3, x5, x7)
    if family_id == ONE:
        x0 = randint(8, 10)
        x1 = randint(11, 13)
        x2 = randint(FIVE, min(SIX, x0 - TWO))
        x3 = x2
        x4 = x2 - TWO
        return (x0, x2, x4, TWO), (x1, x3, x4, TWO)
    if family_id == TWO:
        x0 = randint(8, 10)
        x1 = x0
        x2 = x0 - TWO
        x3 = randint(THREE, max(THREE, x2 - TWO))
        return (x0, x2, x3), (x1, x2, x3)
    x0 = randint(13, 16)
    x1 = randint(12, 14)
    x2 = randint(SIX, min(EIGHT, x0 - FOUR))
    x3 = randint(max(SEVEN, x1 - FIVE), x1 - THREE)
    x4 = randint(THREE, min(FOUR, x2 - TWO))
    x5 = randint(FOUR, min(FIVE, x3 - TWO))
    return (x0, x2, x4, TWO), (x1, x3, x5, TWO)


def _drifts_6cbe9eb8(
    family_id: Integer,
    outer_w: Integer,
    second_w: Integer,
) -> tuple[IntegerTuple, ...]:
    if family_id == TWO:
        x0 = astuple(randint(ZERO, ONE), randint(ONE, THREE))
        x1 = astuple(x0[ZERO] - randint(ZERO, ONE), x0[ONE] + randint(second_w + ONE, second_w + FOUR))
        return (ORIGIN, x0, x1)
    x0 = astuple(-randint(ONE, THREE), randint(max(THREE, outer_w // TWO), outer_w + TWO))
    x1 = astuple(x0[ZERO] - randint(ZERO, TWO), x0[ONE] + randint(max(TWO, second_w // TWO), second_w + THREE))
    return (ORIGIN, x0, x0, x1)


def generate_6cbe9eb8(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = randint(ZERO, len(FAMILIES_6CBE9EB8) - ONE)
        x1 = FAMILIES_6CBE9EB8[x0]
        x2 = _tile_6cbe9eb8(x1["bg_kind"])
        x3, x4 = _sample_family_dims_6cbe9eb8(x0)
        x5 = _output_layout_6cbe9eb8(x3, x4, x1["kinds"])
        x6 = canvas(ZERO, astuple(x3[ZERO], x4[ZERO]))
        for x7, x8, x9, x10, x11 in zip(x5, x3, x4, x1["colors"], x1["kinds"]):
            x6 = _paint_rect_6cbe9eb8(x6, x10, x7[ZERO], x7[ONE], x8, x9, x11)
        x12 = _drifts_6cbe9eb8(x0, x4[ZERO], x4[ONE])
        x13 = []
        for x14, x15, x16, x17, x18, x19 in zip(x5, x12, x3, x4, x1["colors"], x1["kinds"]):
            x20 = x14[ZERO] + x15[ZERO]
            x21 = x14[ONE] + x15[ONE]
            x13.append((x20, x21, x16, x17, x18, x19))
        x22 = min(x23[ZERO] for x23 in x13)
        x24 = max(x25[ZERO] + x25[TWO] for x25 in x13)
        x26 = min(x27[ONE] for x27 in x13)
        x28 = max(x29[ONE] + x29[THREE] for x29 in x13)
        x30 = randint(ONE, THREE)
        x31 = randint(ONE, THREE)
        x32 = randint(ONE, THREE)
        x33 = randint(ONE, THREE)
        x34 = x30 - x22
        x35 = x31 - x26
        x36 = x24 - x22 + x30 + x32
        x37 = x28 - x26 + x31 + x33
        if x36 < 13 or x37 < 18:
            continue
        if x36 > 22 or x37 > 28:
            continue
        x38 = _render_wallpaper_6cbe9eb8(x2, astuple(x36, x37))
        for x39, x40, x41, x42, x43, x44 in x13:
            x45 = x39 + x34
            x46 = x40 + x35
            x38 = _paint_rect_6cbe9eb8(x38, x43, x45, x46, x41, x42, x44)
        if verify_6cbe9eb8(x38) != x6:
            continue
        return {"input": x38, "output": x6}
