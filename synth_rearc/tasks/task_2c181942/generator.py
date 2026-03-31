from __future__ import annotations

from synth_rearc.core import *

from .helpers import (
    SIDES,
    assemble_output_indices,
    connector_object,
    find_connectors_2c181942,
    orient_payload_for_side,
    rotate_indices,
)
from .verifier import verify_2c181942


BG = EIGHT


def _bbox(indices: Indices) -> tuple[int, int, int, int]:
    return uppermost(indices), leftmost(indices), lowermost(indices), rightmost(indices)


def _reserve(indices: Indices, pad: int = ONE) -> Indices:
    x0, x1, x2, x3 = _bbox(indices)
    return frozenset(
        (i, j)
        for i in range(x0 - pad, x2 + pad + ONE)
        for j in range(x1 - pad, x3 + pad + ONE)
    )


def _can_place(indices: Indices, reserved: Indices, h: int, w: int) -> bool:
    if len(indices) == ZERO:
        return F
    x0, x1, x2, x3 = _bbox(indices)
    if x0 < ZERO or x1 < ZERO or x2 >= h or x3 >= w:
        return F
    return equality(intersection(indices, reserved), frozenset())


def _paint_indices(grid: Grid, value: int, indices: Indices) -> Grid:
    return fill(grid, value, indices)


def _canonical_right_payload(diff_lb: float, diff_ub: float) -> Indices:
    while True:
        x0 = choice((TWO, FOUR, FOUR, SIX, SIX))
        x1 = unifint(diff_lb, diff_ub, (TWO, SIX))
        x2 = x0 // TWO - ONE
        x3 = frozenset({(x2, ZERO), (x2 + ONE, ZERO)})

        x4 = choice((ONE, TWO, TWO, THREE, FOUR))
        x4 = min(x4, x1)
        x5 = frozenset((i, j) for i in range(x2, x2 + TWO) for j in range(x4))
        x6 = combine(x3, x5)

        x7 = randint(ONE, THREE)
        for _ in range(x7):
            x8 = randint(ONE, x1 - ONE)
            x9 = randint(x8, x1 - ONE)
            x10 = randint(ZERO, x0 - ONE)
            x11 = randint(x10, x0 - ONE)
            x12 = frozenset((i, j) for i in range(x10, x11 + ONE) for j in range(x8, x9 + ONE))
            x6 = combine(x6, x12)

        x13 = choice((ZERO, ZERO, ONE, ONE, TWO))
        for _ in range(x13):
            x14 = choice(("single", "vdomino", "hdomino", "block"))
            if x14 == "single":
                x15 = choice(tuple((i, j) for i in range(x0) for j in range(ONE, x1)))
                x16 = frozenset({x15})
            elif x14 == "vdomino":
                if x0 < TWO:
                    continue
                x17 = randint(ZERO, x0 - TWO)
                x18 = randint(ONE, x1 - ONE)
                x16 = frozenset({(x17, x18), (x17 + ONE, x18)})
            elif x14 == "hdomino":
                if x1 < THREE:
                    continue
                x17 = randint(ZERO, x0 - ONE)
                x18 = randint(ONE, x1 - TWO)
                x16 = frozenset({(x17, x18), (x17, x18 + ONE)})
            else:
                if both(greater(x0, ONE), greater(x1, TWO)):
                    x17 = randint(ZERO, x0 - TWO)
                    x18 = randint(ONE, x1 - TWO)
                    x16 = frozenset(
                        {
                            (x17, x18),
                            (x17 + ONE, x18),
                            (x17, x18 + ONE),
                            (x17 + ONE, x18 + ONE),
                        }
                    )
                else:
                    continue
            if len(intersection(_reserve(x16, ZERO), _reserve(x6, ZERO))) == ZERO and len(intersection(x16, x6)) == ZERO:
                x6 = combine(x6, x16)

        x19 = normalize(x6)
        x20 = frozenset((i, j) for i, j in x19 if j == ZERO)
        if x20 != frozenset({(shape(x19)[ZERO] // TWO - ONE, ZERO), (shape(x19)[ZERO] // TWO, ZERO)}):
            continue
        try:
            x21 = orient_payload_for_side(x19, "right")
        except ValueError:
            continue
        if x21 != x19:
            continue
        if size(x19) <= TWO:
            continue
        return x19


def _payload_for_side(side: str, diff_lb: float, diff_ub: float) -> Indices:
    x0 = _canonical_right_payload(diff_lb, diff_ub)
    x1 = orient_payload_for_side(x0, side)
    return x1


def _decoy_payload(diff_lb: float, diff_ub: float) -> Indices:
    x0 = _canonical_right_payload(diff_lb, diff_ub)
    x1 = choice((ZERO, ONE, TWO, THREE))
    x2 = rotate_indices(x0, x1)
    return x2


def _quadrant_ranges(
    quadrant: str,
    patch: Indices,
    h: int,
    w: int,
    gap_ul: tuple[int, int],
) -> tuple[tuple[int, int], tuple[int, int]]:
    x0, x1 = shape(patch)
    x2, x3 = gap_ul
    if quadrant == "tl":
        return (ONE, x2 - x0 - FOUR), (ONE, x3 - x1 - FOUR)
    if quadrant == "tr":
        return (ONE, x2 - x0 - FOUR), (x3 + SIX, w - x1 - TWO)
    if quadrant == "bl":
        return (x2 + SIX, h - x0 - TWO), (ONE, x3 - x1 - FOUR)
    return (x2 + SIX, h - x0 - TWO), (x3 + SIX, w - x1 - TWO)


def _place_in_region(
    patch: Indices,
    reserved: Indices,
    h: int,
    w: int,
    row_range: tuple[int, int],
    col_range: tuple[int, int],
) -> Indices | None:
    x0, x1 = row_range
    x2, x3 = col_range
    if greater(x0, x1):
        return None
    if greater(x2, x3):
        return None
    x4 = [(i, j) for i in range(x0, x1 + ONE) for j in range(x2, x3 + ONE)]
    shuffle(x4)
    for x5 in x4:
        x6 = shift(patch, x5)
        if _can_place(x6, reserved, h, w):
            return x6
    return None


def _place_patch(
    patch: Indices,
    reserved: Indices,
    h: int,
    w: int,
    gap_ul: tuple[int, int],
    side: str | None,
) -> Indices | None:
    x0 = {
        "top": ("tl", "tr"),
        "bottom": ("bl", "br"),
        "left": ("tl", "bl"),
        "right": ("tr", "br"),
        None: ("tl", "tr", "bl", "br"),
    }[side]
    for x1 in x0:
        x2 = _quadrant_ranges(x1, patch, h, w, gap_ul)
        x3 = _place_in_region(patch, reserved, h, w, x2[ZERO], x2[ONE])
        if x3 is not None:
            return x3
    x5 = shape(patch)
    return _place_in_region(
        patch,
        reserved,
        h,
        w,
        (ONE, h - x5[ZERO] - TWO),
        (ONE, w - x5[ONE] - TWO),
    )


def _relative_output_patch(side: str, payload: Indices | None) -> Indices:
    x0 = connector_object(side, ONE, ORIGIN)
    return assemble_output_indices(side, x0, payload)


def _relative_output_bounds(payloads: dict[str, Indices | None]) -> tuple[int, int, int, int]:
    x0 = frozenset()
    for x1 in SIDES:
        x2 = _relative_output_patch(x1, payloads[x1])
        x0 = combine(x0, x2)
    return _bbox(x0)


def generate_2c181942(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    x0 = tuple(x1 for x1 in interval(ZERO, TEN, ONE) if x1 != BG)
    while True:
        x1 = sample(x0, FOUR)
        x2 = dict(zip(SIDES, x1))
        x3 = set(sample(SIDES, randint(TWO, FOUR)))
        x4 = {}
        for x5 in SIDES:
            x4[x5] = _payload_for_side(x5, diff_lb, diff_ub) if x5 in x3 else None

        x6 = tuple(x7 for x7 in x0 if x7 not in x1)
        x7 = randint(ZERO, min(TWO, len(x6)))
        x8 = sample(x6, x7) if x7 > ZERO else []
        x9 = {x10: _decoy_payload(diff_lb, diff_ub) for x10 in x8}

        x10, x11, x12, x13 = _relative_output_bounds(x4)
        x14 = x12 - x10 + ONE
        x15 = x13 - x11 + ONE
        x16 = max(18, x14 + TEN)
        x17 = max(18, x15 + TEN)
        if either(greater(x16, 28), greater(x17, 28)):
            continue
        x18 = randint(x16, 28)
        x19 = randint(x17, 28)

        x20 = randint(ONE - x10, x18 - x12 - TWO)
        x21 = randint(ONE - x11, x19 - x13 - TWO)
        x22 = astuple(x20 + ONE, x21)
        # x22 is the 2x2 gap upper-left corner.

        x23 = canvas(BG, (x18, x19))
        x24 = canvas(BG, (x18, x19))
        x25 = frozenset()

        x26 = frozenset((x22[ZERO] + di, x22[ONE] + dj) for di in range(TWO) for dj in range(TWO))
        x25 = combine(x25, _reserve(x26, TWO))

        for x27 in SIDES:
            x28 = connector_object(x27, x2[x27], x22)
            x23 = paint(x23, x28)
            x29 = fill(x24, x2[x27], toindices(x28))
            x24 = x29
            x25 = combine(x25, _reserve(toindices(x28), ONE))
            x30 = x4[x27]
            if x30 is None:
                continue
            x31 = assemble_output_indices(x27, x28, x30)
            x32 = fill(x24, x2[x27], x31)
            x24 = x32

        x33 = []
        for x34 in SIDES:
            x35 = x4[x34]
            if x35 is None:
                continue
            x36 = rotate_indices(x35, randint(ZERO, THREE))
            x33.append((x34, x2[x34], x36))
        for x37, x38 in x9.items():
            x33.append((None, x37, rotate_indices(x38, randint(ZERO, THREE))))
        shuffle(x33)

        x39 = T
        for x40, x41, x42 in x33:
            x43 = _place_patch(x42, x25, x18, x19, x22, x40)
            if x43 is None:
                x39 = F
                break
            x23 = fill(x23, x41, x43)
            x25 = combine(x25, _reserve(x43, ONE))
        if flip(x39):
            continue

        x44 = objects(x23, T, F, T)
        try:
            x45 = find_connectors_2c181942(x44)
        except ValueError:
            continue
        x46 = tuple(sorted(color(x47) for x47 in x45.values()))
        if x46 != tuple(sorted(x1)):
            continue
        if x23 == x24:
            continue
        if verify_2c181942(x23) != x24:
            continue
        return {"input": x23, "output": x24}
