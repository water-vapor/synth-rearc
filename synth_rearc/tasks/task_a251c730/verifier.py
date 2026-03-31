from __future__ import annotations

from collections import defaultdict

from synth_rearc.core import *


def _frame_specs_a251c730(
    I: Grid,
) -> tuple[tuple[Integer, Integer, Integer, Integer, Integer, Integer], ...]:
    x0 = len(I)
    x1 = len(I[ZERO])
    x2: dict[tuple[Integer, Integer, Integer], list[Integer]] = defaultdict(list)
    for x3, x4 in enumerate(I):
        x5 = ZERO
        while x5 < x1:
            x6 = x5 + ONE
            while x6 < x1 and equality(x4[x6], x4[x5]):
                x6 += ONE
            if greater(x6 - x5, THREE):
                x2[(x4[x5], x5, x6 - ONE)].append(x3)
            x5 = x6
    x7 = []
    for x8, x9 in x2.items():
        x10, x11, x12 = x8
        x13 = sorted(x9)
        for x14, x15 in enumerate(x13):
            for x16 in x13[x14 + ONE :]:
                if x16 - x15 < THREE:
                    continue
                x17 = all(
                    both(equality(I[x18][x11], x10), equality(I[x18][x12], x10))
                    for x18 in range(x15, x16 + ONE)
                )
                if not x17:
                    continue
                x18 = crop(I, (x15, x11), (x16 - x15 + ONE, x12 - x11 + ONE))
                x19 = trim(x18)
                x20 = mostcolor(x19)
                x21 = (x16 - x15 - ONE) * (x12 - x11 - ONE)
                x22 = sum(x23 == x20 for x24 in x19 for x23 in x24)
                if both(x20 != x10, x22 * 20 >= x21 * 11):
                    x7.append((x15, x11, x16, x12, x10, x20, x22))
    x25 = sorted(
        x7,
        key=lambda x26: (((x26[2] - x26[0] + ONE) * (x26[3] - x26[1] + ONE)), x26[6]),
        reverse=True,
    )
    x27 = []
    for x28 in x25:
        x29, x30, x31, x32, x33, x34, _ = x28
        x35 = any(
            both(
                both(x29 >= x36[ZERO], x30 >= x36[ONE]),
                both(x31 <= x36[TWO], x32 <= x36[THREE]),
            )
            for x36 in x27
        )
        if not x35:
            x27.append((x29, x30, x31, x32, x33, x34))
    return tuple(x27)


def _panel_bundle_a251c730(
    I: Grid,
    spec: tuple[Integer, Integer, Integer, Integer, Integer, Integer],
) -> tuple[Grid, tuple[Object, ...]]:
    x0, x1, x2, x3, _, _ = spec
    x4 = crop(I, (x0, x1), (x2 - x0 + ONE, x3 - x1 + ONE))
    x5 = trim(x4)
    x6 = objects(x5, F, F, T)
    return x4, x6


def verify_a251c730(
    I: Grid,
) -> Grid:
    x0 = _frame_specs_a251c730(I)
    x1 = tuple(_panel_bundle_a251c730(I, x2) for x2 in x0)
    x2 = next(x3 for x3 in x1 if any(greater(size(x4), ONE) for x4 in x3[ONE]))
    x3 = next(x4 for x4 in x1 if all(equality(size(x5), ONE) for x5 in x4[ONE]))
    x4 = frozenset(x5 for x6 in x3[ONE] for x5 in palette(x6))
    x5 = {}
    for x6 in x2[ONE]:
        x7 = set(palette(x6)) & set(x4)
        if len(x7) != ONE:
            continue
        x8 = next(iter(x7))
        x9 = next(x10 for x11, x10 in x6 if x11 == x8)
        x5[x8] = shift(x6, invert(x9))
    x10 = x3[ZERO]
    for x11 in x3[ONE]:
        x12 = first(toindices(x11))
        x13 = first(palette(x11))
        x10 = paint(x10, shift(x5[x13], add(x12, (ONE, ONE))))
    return x10
