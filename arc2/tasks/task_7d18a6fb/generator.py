from arc2.core import *


MOTIFS_7D18A6FB = (
    frozenset({(0, 0), (0, 2), (1, 1), (2, 0), (2, 1), (2, 2)}),
    frozenset({(0, 0), (0, 1), (1, 0), (1, 2), (2, 1)}),
    frozenset({(0, 2), (1, 0), (1, 1), (1, 2), (2, 1), (2, 2)}),
    frozenset({(0, 1), (1, 0), (1, 1), (1, 2), (2, 1), (2, 2)}),
    frozenset({(0, 1), (1, 0), (1, 1), (1, 2), (2, 1)}),
    frozenset({(0, 0), (0, 2), (1, 0), (1, 1), (2, 1)}),
    frozenset({(0, 1), (1, 0), (1, 2), (2, 1)}),
    frozenset({(0, 1), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)}),
    frozenset({(0, 0), (0, 2), (1, 1), (1, 2), (2, 2)}),
    frozenset({(0, 1), (1, 0), (1, 1), (2, 2)}),
    frozenset({(0, 1), (1, 0), (1, 2), (2, 0), (2, 1), (2, 2)}),
    frozenset({(0, 2), (1, 1), (2, 0), (2, 1), (2, 2)}),
    frozenset({(0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 2)}),
    frozenset({(0, 1), (0, 2), (1, 0), (1, 1), (2, 1), (2, 2)}),
    frozenset({(0, 0), (0, 1), (0, 2), (1, 1), (2, 0), (2, 1), (2, 2)}),
)

MARKERS_7D18A6FB = ((ONE, ONE), (ONE, FIVE), (FIVE, ONE), (FIVE, FIVE))
OUTPUT_ANCHORS_7D18A6FB = (ORIGIN, (ZERO, FOUR), (FOUR, ZERO), (FOUR, FOUR))


def _fits_7d18a6fb(
    anchor: IntegerTuple,
    reserved: tuple[tuple[int, int, int, int], ...],
) -> bool:
    top, left = anchor
    bottom = top + TWO
    right = left + TWO
    for r0, c0, r1, c1 in reserved:
        if not (
            bottom < r0 - ONE
            or top > r1 + ONE
            or right < c0 - ONE
            or left > c1 + ONE
        ):
            return False
    return True


def _anchor_7d18a6fb(
    h: int,
    w: int,
    reserved: tuple[tuple[int, int, int, int], ...],
) -> IntegerTuple | None:
    options = tuple(
        (i, j)
        for i in range(h - TWO)
        for j in range(w - TWO)
        if _fits_7d18a6fb((i, j), reserved)
    )
    if len(options) == ZERO:
        return None
    return choice(options)


def generate_7d18a6fb(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    x0 = interval(TWO, TEN, ONE)
    while True:
        x1 = unifint(diff_lb, diff_ub, (14, 19))
        x2 = unifint(diff_lb, diff_ub, (14, 19))
        x3 = choice(
            (
                ORIGIN,
                (ZERO, x2 - SEVEN),
                (x1 - SEVEN, ZERO),
                (x1 - SEVEN, x2 - SEVEN),
            )
        )
        x4, x5 = x3
        x6 = choice((ZERO, ONE))
        x7 = sample(x0, FOUR + x6)
        x8 = x7[:FOUR]
        x9 = sample(MOTIFS_7D18A6FB, FOUR + x6)
        x10 = x9[:FOUR]
        x11 = x9[FOUR:]
        x12 = canvas(ZERO, (x1, x2))
        x13 = shift(asindices(canvas(ONE, (SEVEN, SEVEN))), x3)
        x12 = fill(x12, ONE, x13)
        for x14, x15 in zip(MARKERS_7D18A6FB, x8):
            x12 = fill(x12, x15, frozenset({add(x3, x14)}))
        x16 = ((x4, x5, x4 + SIX, x5 + SIX),)
        x17 = ()
        for x18, x19 in zip(x8, x10):
            x20 = _anchor_7d18a6fb(x1, x2, x16)
            if x20 is None:
                break
            x17 = x17 + ((x18, x19, x20),)
            x21, x22 = x20
            x16 = x16 + ((x21, x22, x21 + TWO, x22 + TWO),)
        if len(x17) != FOUR:
            continue
        x23 = ()
        x24 = x0
        for x25 in x8:
            x24 = remove(x25, x24)
        for x26 in x11:
            x27 = _anchor_7d18a6fb(x1, x2, x16)
            if x27 is None:
                break
            x28 = choice(x24)
            x24 = remove(x28, x24)
            x23 = x23 + ((x28, x26, x27),)
            x29, x30 = x27
            x16 = x16 + ((x29, x30, x29 + TWO, x30 + TWO),)
        if len(x23) != x6:
            continue
        for x31, x32, x33 in x17:
            x12 = fill(x12, x31, shift(x32, x33))
        for x34, x35, x36 in x23:
            x12 = fill(x12, x34, shift(x35, x36))
        if mostcolor(x12) != ZERO:
            continue
        x37 = canvas(ZERO, (SEVEN, SEVEN))
        for x38, x39, x40 in zip(x8, x10, OUTPUT_ANCHORS_7D18A6FB):
            x37 = fill(x37, x38, shift(x39, x40))
        return {"input": x12, "output": x37}
