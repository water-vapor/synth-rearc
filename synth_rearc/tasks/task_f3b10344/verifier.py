from synth_rearc.core import *


def _bbox_patch_f3b10344(
    r0: Integer,
    r1: Integer,
    c0: Integer,
    c1: Integer,
) -> Indices:
    if r0 > r1 or c0 > c1:
        return frozenset({})
    return frozenset(
        (i, j)
        for i in range(r0, r1 + ONE)
        for j in range(c0, c1 + ONE)
    )


def _horizontal_bridge_f3b10344(
    I: Grid,
    bg: Integer,
    a: Object,
    b: Object,
) -> Indices:
    x0, x1 = (a, b) if leftmost(a) <= leftmost(b) else (b, a)
    x2 = max(uppermost(x0), uppermost(x1))
    x3 = min(lowermost(x0), lowermost(x1))
    x4 = rightmost(x0) + ONE
    x5 = leftmost(x1) - ONE
    x6 = _bbox_patch_f3b10344(x2, x3, x4, x5)
    if len(x6) == ZERO:
        return frozenset({})
    x7 = toobject(x6, I)
    x8 = equality(palette(x7), initset(bg))
    if not x8:
        return frozenset({})
    return _bbox_patch_f3b10344(x2 + ONE, x3 - ONE, x4, x5)


def _vertical_bridge_f3b10344(
    I: Grid,
    bg: Integer,
    a: Object,
    b: Object,
) -> Indices:
    x0, x1 = (a, b) if uppermost(a) <= uppermost(b) else (b, a)
    x2 = lowermost(x0) + ONE
    x3 = uppermost(x1) - ONE
    x4 = max(leftmost(x0), leftmost(x1))
    x5 = min(rightmost(x0), rightmost(x1))
    x6 = _bbox_patch_f3b10344(x2, x3, x4, x5)
    if len(x6) == ZERO:
        return frozenset({})
    x7 = toobject(x6, I)
    x8 = equality(palette(x7), initset(bg))
    if not x8:
        return frozenset({})
    return _bbox_patch_f3b10344(x2, x3, x4 + ONE, x5 - ONE)


def _candidate_bridges_f3b10344(
    I: Grid,
    rects: tuple[Object, ...],
) -> tuple[tuple[Integer, Integer, Integer, Integer, Integer, Indices], ...]:
    x0 = mostcolor(I)
    x1 = []
    for x2, x3 in enumerate(rects):
        for x4 in range(x2 + ONE, len(rects)):
            x5 = rects[x4]
            x6 = color(x3)
            if x6 != color(x5):
                continue
            if hmatching(x3, x5):
                x7 = _horizontal_bridge_f3b10344(I, x0, x3, x5)
                if len(x7) == ZERO:
                    continue
                x8, x9 = (x3, x5) if leftmost(x3) <= leftmost(x5) else (x5, x3)
                x10 = leftmost(x9) - rightmost(x8) - ONE
                x1.append((x6, x10, invert(size(x7)), x2, x4, x7))
                continue
            if vmatching(x3, x5):
                x7 = _vertical_bridge_f3b10344(I, x0, x3, x5)
                if len(x7) == ZERO:
                    continue
                x8, x9 = (x3, x5) if uppermost(x3) <= uppermost(x5) else (x5, x3)
                x10 = uppermost(x9) - lowermost(x8) - ONE
                x1.append((x6, x10, invert(size(x7)), x2, x4, x7))
    return tuple(sorted(x1))


def verify_f3b10344(I: Grid) -> Grid:
    x0 = objects(I, T, F, T)
    x1 = sfilter(x0, lambda x2: equality(size(x2), size(backdrop(x2))))
    x2 = tuple(
        sorted(
            x1,
            key=lambda x3: (
                color(x3),
                uppermost(x3),
                leftmost(x3),
                lowermost(x3),
                rightmost(x3),
            ),
        )
    )
    x3 = _candidate_bridges_f3b10344(I, x2)
    x4 = {x5: x5 for x5 in range(len(x2))}

    def x5(n: Integer) -> Integer:
        while x4[n] != n:
            x4[n] = x4[x4[n]]
            n = x4[n]
        return n

    x6 = I
    for _, _, _, x7, x8, x9 in x3:
        x10 = x5(x7)
        x11 = x5(x8)
        if x10 == x11:
            continue
        x4[x11] = x10
        x6 = fill(x6, EIGHT, x9)
    return x6
