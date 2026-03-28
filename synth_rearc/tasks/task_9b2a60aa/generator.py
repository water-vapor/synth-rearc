from synth_rearc.core import *


TEMPLATE_9B2A60AA = TWO
MARKER_COLORS_9B2A60AA = (THREE, FOUR, EIGHT)
TEMPLATES_9B2A60AA = (
    frozenset({(ZERO, ZERO), (ZERO, TWO), (ONE, ONE), (TWO, ZERO), (TWO, ONE), (TWO, TWO)}),
    frozenset({(ZERO, ZERO), (ZERO, ONE), (ZERO, TWO), (ONE, ONE), (TWO, ZERO), (TWO, ONE), (TWO, TWO)}),
    frozenset({(ZERO, ZERO), (ZERO, ONE), (ZERO, TWO), (ONE, ZERO), (ONE, TWO), (TWO, ZERO), (TWO, ONE)}),
    frozenset({(ZERO, ZERO), (ZERO, ONE), (ZERO, TWO), (ONE, ZERO), (ONE, TWO), (TWO, ONE), (TWO, TWO)}),
    frozenset({(ZERO, TWO), (ONE, ZERO), (ONE, ONE), (ONE, TWO), (TWO, ZERO), (TWO, ONE)}),
    frozenset({(ZERO, ZERO), (ONE, ZERO), (ONE, ONE), (ONE, TWO), (TWO, ONE), (TWO, TWO)}),
)


def _marker_offsets_9b2a60aa(nmarkers: Integer) -> tuple[int, ...]:
    x0 = (TWO, THREE, THREE, FOUR, FIVE)
    if nmarkers == FIVE:
        x0 = (TWO, TWO, THREE, THREE, FOUR)
    x1 = [ZERO]
    x2 = ZERO
    for _ in range(nmarkers - ONE):
        x2 = add(x2, choice(x0))
        x1.append(x2)
    return tuple(x1)


def _marker_colors_9b2a60aa(
    nmarkers: Integer,
    anchor_index: Integer,
) -> tuple[int, ...]:
    while True:
        x0 = [choice(MARKER_COLORS_9B2A60AA) for _ in range(nmarkers)]
        x0[anchor_index] = TEMPLATE_9B2A60AA
        if len(set(x0)) < THREE:
            continue
        return tuple(x0)


def _copy_deltas_9b2a60aa(
    marker_offsets: tuple[int, ...],
    anchor_index: Integer,
) -> tuple[int, ...]:
    x0 = marker_offsets[anchor_index]
    x1 = []
    for x2, x3 in enumerate(marker_offsets):
        x4 = subtract(x3, x0)
        x5 = multiply(subtract(x2, anchor_index), TWO)
        x1.append(add(x4, x5))
    return tuple(x1)


def _render_output_9b2a60aa(
    gi: Grid,
    template_patch: Indices,
    horizontal: Boolean,
    marker_colors: tuple[int, ...],
    marker_offsets: tuple[int, ...],
    anchor_index: Integer,
) -> Grid:
    x0 = normalize(template_patch)
    x1 = uppermost(template_patch)
    x2 = leftmost(template_patch)
    x3 = _copy_deltas_9b2a60aa(marker_offsets, anchor_index)
    go = gi
    for x4, x5 in zip(marker_colors, x3):
        x6 = branch(horizontal, (x1, add(x2, x5)), (add(x1, x5), x2))
        x7 = shift(x0, x6)
        x8 = recolor(x4, x7)
        go = underpaint(go, x8)
    return go


def generate_9b2a60aa(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = choice((T, F))
        x1 = choice((FOUR, FOUR, FOUR, FIVE))
        x2 = choice((ZERO, subtract(x1, ONE)))
        x3 = _marker_offsets_9b2a60aa(x1)
        x4 = _copy_deltas_9b2a60aa(x3, x2)
        x5 = choice(TEMPLATES_9B2A60AA)
        x6 = _marker_colors_9b2a60aa(x1, x2)
        x7 = add(subtract(max(x4), min(x4)), THREE)
        x8 = increment(last(x3))
        if x0:
            x9 = max(14, x7, x8)
            if x9 > 24:
                continue
            x10 = unifint(diff_lb, diff_ub, (x9, min(24, x9 + 7)))
            x11 = randint(ZERO, THREE)
            x12 = choice((FOUR, FIVE, SIX, SEVEN, EIGHT))
            x13 = randint(ZERO, FIVE)
            x14 = add(add(add(x11, ONE), x12), add(THREE, x13))
            if x14 < 13 or x14 > 24:
                continue
            x15 = x11
            x16 = add(x15, x12)
            x17 = max(ZERO, invert(min(x4)))
            x18 = subtract(subtract(x10, THREE), max(x4))
            x19 = subtract(x10, x8)
            if x17 > x18 or x19 < ZERO:
                continue
            x20 = randint(x17, x18)
            x21 = randint(ZERO, x19)
            gi = canvas(ZERO, (x14, x10))
            for x22, x23 in zip(x3, x6):
                gi = fill(gi, x23, {(x15, add(x21, x22))})
            x24 = shift(x5, (x16, x20))
            gi = fill(gi, TEMPLATE_9B2A60AA, x24)
            go = _render_output_9b2a60aa(gi, x24, T, x6, x3, x2)
            return {"input": gi, "output": go}
        x9 = max(14, x7, x8)
        if x9 > 24:
            continue
        x10 = unifint(diff_lb, diff_ub, (x9, min(24, x9 + 7)))
        x11 = randint(ZERO, THREE)
        x12 = choice((FOUR, FIVE, SIX, SEVEN, EIGHT))
        x13 = randint(ZERO, FIVE)
        x14 = add(add(add(x11, ONE), x12), add(THREE, x13))
        if x14 < 13 or x14 > 24:
            continue
        x15 = x11
        x16 = add(x15, x12)
        x17 = max(ZERO, invert(min(x4)))
        x18 = subtract(subtract(x10, THREE), max(x4))
        x19 = subtract(x10, x8)
        if x17 > x18 or x19 < ZERO:
            continue
        x20 = randint(x17, x18)
        x21 = randint(ZERO, x19)
        gi = canvas(ZERO, (x10, x14))
        for x22, x23 in zip(x3, x6):
            gi = fill(gi, x23, {(add(x21, x22), x15)})
        x24 = shift(x5, (x20, x16))
        gi = fill(gi, TEMPLATE_9B2A60AA, x24)
        go = _render_output_9b2a60aa(gi, x24, F, x6, x3, x2)
        return {"input": gi, "output": go}
