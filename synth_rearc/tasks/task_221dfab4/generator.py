from __future__ import annotations

from synth_rearc.core import *

from .verifier import verify_221dfab4


COLOR_POOL_221DFAB4 = tuple(value for value in interval(ZERO, TEN, ONE) if value not in (THREE, FOUR))
TRANSFORMS_221DFAB4 = (identity, rot90, rot180, rot270)


def _clamp_221dfab4(
    value: Integer,
    lower: Integer,
    upper: Integer,
) -> Integer:
    return max(lower, min(upper, value))


def _segment_221dfab4(
    row: Integer,
    start: Integer,
    stop: Integer,
) -> Indices:
    return connect((row, start), (row, stop))


def _render_horizontal_221dfab4(I: Grid) -> Grid:
    x0 = mostcolor(I)
    x1 = objects(I, T, F, T)
    x2 = first(colorfilter(x1, FOUR))
    x3 = uppermost(x2)
    x4 = leftmost(x2)
    x5 = rightmost(x2)
    x6 = I
    x7 = height(I)
    for x8 in range(x7):
        x9 = connect((x8, x4), (x8, x5))
        x10 = abs(x8 - x3)
        if x10 % TWO == ONE:
            x6 = fill(x6, x0, x9)
            continue
        x11 = x10 // TWO
        if x11 % THREE == TWO:
            x12 = frozenset((x8, x13) for x13, x14 in enumerate(I[x8]) if x14 != x0)
            x13 = combine(x12, x9)
            x6 = fill(x6, THREE, x13)
        else:
            x6 = fill(x6, FOUR, x9)
    return x6


def _blob_patch_221dfab4(
    nr: Integer,
    nc: Integer,
    top: Integer,
    height_value: Integer,
    mode: str,
    band_left: Integer,
    band_right: Integer,
) -> Indices:
    if mode == "cross":
        x0 = randint(max(ONE, band_left - SIX), band_left)
        x1 = randint(band_right, min(nc - TWO, band_right + SIX))
    elif mode == "left":
        x0 = randint(ONE, max(ONE, band_left - FOUR))
        x1 = randint(max(x0 + ONE, TWO), max(x0 + ONE, max(TWO, band_left)))
    else:
        x0 = randint(min(nc - THREE, band_right), nc - THREE)
        x1 = randint(x0 + ONE, nc - TWO)
    x2 = set()
    x3, x4 = x0, x1
    for x5 in range(height_value):
        x6 = top + x5
        x2 |= set(_segment_221dfab4(x6, x3, x4))
        if x5 == height_value - ONE:
            continue
        x7 = _clamp_221dfab4(x3 + choice((-ONE, ZERO, ZERO, ONE)), ONE, nc - TWO)
        x8 = _clamp_221dfab4(x4 + choice((-ONE, ZERO, ZERO, ONE)), ONE, nc - TWO)
        if x8 <= x7:
            x8 = min(nc - TWO, x7 + ONE)
        if x7 > x4:
            x7 = x4
        if x8 < x3:
            x8 = x3
        if x8 <= x7:
            x8 = min(nc - TWO, x7 + ONE)
        x3, x4 = x7, x8
    return frozenset(x2)


def _good_221dfab4(
    gi: Grid,
    go: Grid,
    fg: Integer,
    band_left: Integer,
    band_right: Integer,
) -> Boolean:
    x0 = colorcount(gi, fg)
    x1 = colorcount(go, THREE)
    x2 = colorcount(go, FOUR)
    x3 = tuple(obj for obj in objects(gi, T, F, T) if color(obj) == fg)
    x4 = band_right - band_left + ONE
    x5 = height(gi) - ONE
    x6 = tuple(
        x7 for x7 in range(x5)
        if abs(x7 - x5) % TWO == ZERO
        and (abs(x7 - x5) // TWO) % THREE == TWO
        and any(value == fg for value in gi[x7])
    )
    x7 = tuple(
        x8 for x8 in range(x5)
        if any(gi[x8][x9] == fg for x9 in range(band_left, band_right + ONE))
    )
    return (
        18 <= x0 <= (height(gi) * width(gi)) // TWO
        and len(x3) >= TWO
        and len(x6) >= TWO
        and len(x7) >= ONE
        and x1 >= 2 * x4
        and x2 >= 4 * x4
    )


def generate_221dfab4(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = unifint(diff_lb, diff_ub, (21, 30))
        x1 = unifint(diff_lb, diff_ub, (20, 30))
        x2, x3 = sample(COLOR_POOL_221DFAB4, TWO)
        x4 = unifint(diff_lb, diff_ub, (THREE, min(EIGHT, x1 - TWO)))
        x5 = randint(ONE, x1 - x4 - ONE)
        x6 = x5 + x4 - ONE
        x7 = canvas(x2, (x0, x1))
        x8 = [
            x9 for x9 in range(x0 - ONE)
            if abs(x9 - (x0 - ONE)) % TWO == ZERO
            and (abs(x9 - (x0 - ONE)) // TWO) % THREE == TWO
        ]
        shuffle(x8)
        x9 = ZERO
        x10 = x7
        for x11 in x8:
            if choice((F, T, T)):
                x12 = choice(("cross", "cross", "left", "right"))
                x13 = randint(TWO, min(SIX, x0 - ONE))
                x14 = randint(ZERO, x13 - ONE)
                x15 = _clamp_221dfab4(x11 - x14, ONE, x0 - x13 - ONE)
                x16 = _blob_patch_221dfab4(x0, x1, x15, x13, x12, x5, x6)
                x10 = fill(x10, x3, x16)
                if any(x5 <= x17 <= x6 for _, x17 in x16):
                    x9 += ONE
        x18 = randint(ONE, THREE)
        for _ in range(x18):
            x19 = choice(("cross", "left", "right"))
            x20 = randint(TWO, min(FIVE, x0 - ONE))
            x21 = randint(ONE, x0 - x20 - ONE)
            x22 = _blob_patch_221dfab4(x0, x1, x21, x20, x19, x5, x6)
            x10 = fill(x10, x3, x22)
            if any(x5 <= x23 <= x6 for _, x23 in x22):
                x9 += ONE
        if x9 == ZERO:
            continue
        x24 = _segment_221dfab4(x0 - ONE, x5, x6)
        x25 = fill(x10, FOUR, x24)
        x26 = _render_horizontal_221dfab4(x25)
        if not _good_221dfab4(x25, x26, x3, x5, x6):
            continue
        x27 = choice(TRANSFORMS_221DFAB4)
        x28 = x27(x25)
        x29 = x27(x26)
        if verify_221dfab4(x28) != x29:
            continue
        return {"input": x28, "output": x29}
