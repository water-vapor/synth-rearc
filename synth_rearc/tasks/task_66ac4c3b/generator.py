from synth_rearc.core import *


GRID_SIZE_66AC4C3B = 22
MARKER_GAP_66AC4C3B = SIX
MARKER_STEPS_66AC4C3B = (THREE, FOUR)
GRID_TRANSFORMS_66AC4C3B = (
    identity,
    rot90,
    rot180,
    rot270,
    hmirror,
    vmirror,
    dmirror,
    cmirror,
)


def _sample_local_patch_66ac4c3b(
    height: Integer,
    width: Integer,
) -> Indices:
    x0 = []
    x1 = randint(ZERO, width - ONE)
    x2 = randint(x1, width - ONE)
    for x3 in range(height):
        if x3 > ZERO:
            x4 = max(ZERO, min(width - ONE, x1 + choice((-ONE, ZERO, ONE))))
            x5 = max(x4, min(width - ONE, x2 + choice((-ONE, ZERO, ONE))))
            x1, x2 = x4, x5
        x0.append([x1, x2])
    x6 = randint(ZERO, height - ONE)
    x7 = randint(ZERO, height - ONE)
    x0[x6][ZERO] = ZERO
    x0[x7][ONE] = width - ONE
    x8 = frozenset(
        (x9, x10)
        for x9, (x11, x12) in enumerate(x0)
        for x10 in range(x11, x12 + ONE)
    )
    return x8


def generate_66ac4c3b(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    x0 = GRID_SIZE_66AC4C3B
    x1, x2, x3 = sample(interval(ZERO, TEN, ONE), THREE)
    x4 = choice(MARKER_STEPS_66AC4C3B)
    x5 = tuple(range(ZERO, x0, x4))
    x6 = unifint(diff_lb, diff_ub, (ONE, TWO))
    x7 = unifint(diff_lb, diff_ub, (THREE, SIX))
    x8 = unifint(diff_lb, diff_ub, (ZERO, TWO))
    x9 = unifint(diff_lb, diff_ub, (ZERO, TWO))
    x10 = subtract(subtract(x0, x8), x9)
    x11 = add(x6, x7)
    x12 = add(x11, MARKER_GAP_66AC4C3B)
    x13 = _sample_local_patch_66ac4c3b(x10, x7)
    x14 = shift(recolor(x3, x13), (x8, x6))
    x15 = canvas(x1, (x0, x0))
    x16 = frozenset((x17, x11) for x17 in x5)
    x17 = frozenset((x18, x12) for x18 in x5)
    x18 = fill(x15, x2, x16)
    x19 = fill(x18, x3, x17)
    x20 = paint(x19, x14)
    x21 = crop(x20, (x8, x6), (x10, x7))
    x22 = vmirror(x21)
    x23 = shift(ofcolor(x22, x3), (x8, increment(x12)))
    x24 = fill(x20, x2, x23)
    x25 = choice(GRID_TRANSFORMS_66AC4C3B)
    x26 = x25(x20)
    x27 = x25(x24)
    return {"input": x26, "output": x27}
