from synth_rearc.core import *

from .verifier import verify_bf699163


RING_COLORS_BF699163 = (ONE, TWO, THREE, FOUR, SIX, EIGHT)


def _rect_patch_bf699163(
    top: Integer,
    left: Integer,
    height_: Integer,
    width_: Integer,
) -> Indices:
    return frozenset(
        (i, j)
        for i in range(top, top + height_)
        for j in range(left, left + width_)
    )


def _expand_patch_bf699163(
    patch: Indices,
    pad: Integer,
    dims: IntegerTuple,
) -> Indices:
    h, w = dims
    out = set()
    for i, j in patch:
        for di in range(-pad, pad + ONE):
            for dj in range(-pad, pad + ONE):
                a = i + di
                b = j + dj
                if ZERO <= a < h and ZERO <= b < w:
                    out.add((a, b))
    return frozenset(out)


def _ring_patch_bf699163(
    top: Integer,
    left: Integer,
) -> Indices:
    return frozenset(
        {
            (top, left),
            (top, left + ONE),
            (top, left + TWO),
            (top + ONE, left),
            (top + ONE, left + TWO),
            (top + TWO, left),
            (top + TWO, left + ONE),
            (top + TWO, left + TWO),
        }
    )


def _marker_line_bf699163(
    start: Integer,
    stop: Integer,
) -> tuple[Integer, ...]:
    x0 = tuple(range(start, stop + ONE))
    if len(x0) <= THREE:
        return x0
    x1 = list(x0[ONE:-ONE])
    shuffle(x1)
    x2 = randint(ZERO, min(THREE, len(x1)))
    x3 = set(x0[ONE:-ONE])
    for x4 in x1[:x2]:
        x3.discard(x4)
    x3 = sorted((x0[ZERO], x0[-ONE], *x3))
    return tuple(x3)


def _marker_patch_bf699163(
    top: Integer,
    left: Integer,
    bottom: Integer,
    right: Integer,
) -> Indices:
    x0 = choice(("lt", "lb", "rt", "rb", "ltr", "lbr"))
    x1 = set()
    if x0 in ("lt", "lb", "ltr", "lbr"):
        for x2 in _marker_line_bf699163(top, bottom):
            x1.add((x2, left))
    if x0 in ("rt", "rb", "ltr"):
        for x2 in _marker_line_bf699163(top, bottom):
            x1.add((x2, right))
    if x0 in ("lt", "rt", "ltr"):
        for x2 in _marker_line_bf699163(left, right):
            x1.add((top, x2))
    if x0 in ("lb", "rb", "lbr"):
        for x2 in _marker_line_bf699163(left, right):
            x1.add((bottom, x2))
    if top < bottom and left < right:
        x1.add((top, left))
        x1.add((bottom, right))
        if x0 in ("lt", "lb", "ltr", "lbr"):
            x1.add((bottom, left))
        if x0 in ("rt", "rb", "ltr"):
            x1.add((top, right))
    return frozenset(x1)


def _output_ring_bf699163(
    color_value: Integer,
) -> Grid:
    x0 = canvas(FIVE, (THREE, THREE))
    x1 = _ring_patch_bf699163(ZERO, ZERO)
    return fill(x0, color_value, x1)


def generate_bf699163(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = unifint(diff_lb, diff_ub, (13, 20))
        x1 = unifint(diff_lb, diff_ub, (13, 20))
        x2 = choice((FOUR, FIVE, FIVE))
        x3 = tuple(sample(RING_COLORS_BF699163, x2))
        x4 = randint(ZERO, x2 - ONE)
        x5 = x3[x4]
        x6 = choice((ONE, TWO, TWO, THREE, FOUR))
        x7 = choice((ONE, TWO, THREE, FOUR, FIVE))
        x8 = choice((ONE, TWO, TWO, THREE))
        x9 = choice((TWO, THREE, FOUR, FIVE))
        if x0 < x6 + THREE + x7 or x1 < x8 + THREE + x9:
            continue
        x10 = randint(x6, x0 - THREE - x7)
        x11 = randint(x8, x1 - THREE - x9)
        x12 = _ring_patch_bf699163(x10, x11)
        x13 = x10 - x6
        x14 = x11 - x8
        x15 = x10 + TWO + x7
        x16 = x11 + TWO + x9
        x17 = _rect_patch_bf699163(x13, x14, x15 - x13 + ONE, x16 - x14 + ONE)
        x18 = _marker_patch_bf699163(x13, x14, x15, x16)
        if len(x18) < FIVE:
            continue
        x19 = _expand_patch_bf699163(x17, ONE, (x0, x1))
        x20 = [(x10, x11, x5)]
        x21 = []
        for x22 in range(x0 - TWO):
            for x23 in range(x1 - TWO):
                x24 = _ring_patch_bf699163(x22, x23)
                x25 = _expand_patch_bf699163(x24, ONE, (x0, x1))
                if len(intersection(x25, x19)) > ZERO:
                    continue
                x21.append((x22, x23))
        if len(x21) < x2 - ONE:
            continue
        shuffle(x21)
        x26 = set(x19)
        x27 = []
        for x28, x29 in x21:
            x30 = _ring_patch_bf699163(x28, x29)
            x31 = _expand_patch_bf699163(x30, ONE, (x0, x1))
            if len(intersection(x31, x26)) > ZERO:
                continue
            x27.append((x28, x29))
            x26 |= set(x31)
            if len(x27) == x2 - ONE:
                break
        if len(x27) != x2 - ONE:
            continue
        x32 = tuple(x3[i] for i in range(x2) if i != x4)
        x20.extend((x33, x34, x35) for (x33, x34), x35 in zip(x27, x32))
        x36 = canvas(FIVE, (x0, x1))
        x36 = fill(x36, SEVEN, x18)
        for x37, x38, x39 in x20:
            x40 = _ring_patch_bf699163(x37, x38)
            x36 = fill(x36, x39, x40)
        x41 = _output_ring_bf699163(x5)
        if verify_bf699163(x36) != x41:
            continue
        return {"input": x36, "output": x41}
