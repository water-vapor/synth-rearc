from synth_rearc.core import *

from .verifier import verify_5ecac7f7


ACTIVE_COLORS_5ECAC7F7 = tuple(v for v in interval(ZERO, TEN, ONE) if v != SEVEN)
ACTIVE_COLORS_NO_SIX_5ECAC7F7 = tuple(v for v in ACTIVE_COLORS_5ECAC7F7 if v != SIX)
PANEL_SIDES_5ECAC7F7 = (FIVE, FIVE, FIVE, SIX, SIX)
PANEL_LAYOUTS_5ECAC7F7 = {
    FIVE: (
        ((ZERO, ONE), (TWO, TWO), (THREE, FOUR)),
        ((ZERO, ONE), (TWO, THREE), (FOUR, FOUR)),
    ),
    SIX: (
        ((ZERO, ONE), (TWO, THREE), (FOUR, FIVE)),
        ((ZERO, ONE), (TWO, FOUR), (FIVE, FIVE)),
    ),
}


def _touches_divider_5ecac7f7(
    panel_idx: Integer,
    slot_idx: Integer,
) -> Boolean:
    return (panel_idx in (ONE, TWO) and slot_idx == ZERO) or (
        panel_idx in (ZERO, ONE) and slot_idx == TWO
    )


def _color_pool_5ecac7f7(
    panel_idx: Integer,
    slot_idx: Integer,
    span: tuple[Integer, Integer],
) -> tuple[Integer, ...]:
    x0 = increment(subtract(span[ONE], span[ZERO]))
    if _touches_divider_5ecac7f7(panel_idx, slot_idx) and x0 == ONE:
        return ACTIVE_COLORS_NO_SIX_5ECAC7F7
    return ACTIVE_COLORS_5ECAC7F7


def _sample_colors_5ecac7f7(
    panel_idx: Integer,
    layout: tuple[tuple[Integer, Integer], ...],
) -> tuple[Integer, Integer, Integer]:
    x0 = choice(_color_pool_5ecac7f7(panel_idx, ZERO, layout[ZERO]))
    x1 = tuple(v for v in _color_pool_5ecac7f7(panel_idx, ONE, layout[ONE]) if v != x0)
    x2 = choice(x1)
    x3 = tuple(v for v in _color_pool_5ecac7f7(panel_idx, TWO, layout[TWO]) if v != x2)
    x4 = choice(x3)
    if x0 == SIX and x4 == SIX:
        x5 = tuple(v for v in x3 if v != SIX)
        if len(x5) > ZERO:
            x4 = choice(x5)
            x3 = x5
    if randint(ZERO, FOUR) == ZERO and x0 != x2 and contained(x0, x3):
        x4 = x0
    return (x0, x2, x4)


def _zone_cells_5ecac7f7(
    side: Integer,
    span: tuple[Integer, Integer],
    panel_idx: Integer,
    slot_idx: Integer,
    color_value: Integer,
) -> Indices:
    x0 = interval(span[ZERO], increment(span[ONE]), ONE)
    if color_value == SIX:
        if panel_idx in (ONE, TWO) and slot_idx == ZERO:
            x0 = x0[ONE:]
        if panel_idx in (ZERO, ONE) and slot_idx == TWO:
            x0 = x0[:-ONE]
    return frozenset((i, j) for i in range(side) for j in x0)


def _grow_shape_5ecac7f7(
    cells: Indices,
    seed_patch: Indices,
    target: Integer,
) -> Indices:
    x0 = set(seed_patch)
    while len(x0) < target:
        x1 = {n for c in x0 for n in dneighbors(c) if n in cells and n not in x0}
        if len(x1) == ZERO:
            break
        x0.add(choice(tuple(x1)))
    return frozenset(x0)


def _build_panel_5ecac7f7(
    side: Integer,
    panel_idx: Integer,
) -> tuple[Grid, tuple[Object, Object, Object]] | None:
    x0 = choice(PANEL_LAYOUTS_5ECAC7F7[side])
    x1 = _sample_colors_5ecac7f7(panel_idx, x0)
    x2 = tuple(
        _zone_cells_5ecac7f7(side, x0[x3], panel_idx, x3, x1[x3])
        for x3 in range(THREE)
    )
    if any(len(x3) == ZERO for x3 in x2):
        return None
    x3 = randint(ZERO, decrement(side))
    x4 = maximum(apply(last, x2[ZERO]))
    x5 = minimum(apply(last, x2[ONE]))
    x6 = maximum(apply(last, x2[ONE]))
    x7 = minimum(apply(last, x2[TWO]))
    x8 = (
        frozenset({(x3, x4)}),
        connect((x3, x5), (x3, x6)),
        frozenset({(x3, x7)}),
    )
    x9 = canvas(SEVEN, (side, side))
    x10 = tuple()
    for x11 in range(THREE):
        x12 = x1[x11]
        x13 = len(set(j for _, j in x2[x11]))
        x14 = min(len(x2[x11]), side + x13)
        x15 = randint(len(x8[x11]), max(len(x8[x11]), x14))
        if x12 == SIX and x15 == len(x2[x11]) and x13 == ONE:
            x15 = max(len(x8[x11]), decrement(len(x2[x11])))
        x16 = _grow_shape_5ecac7f7(x2[x11], x8[x11], x15)
        x17 = recolor(x12, x16)
        x9 = paint(x9, x17)
        x10 = x10 + (x17,)
    if len(objects(x9, T, F, T)) != THREE:
        return None
    if len(objects(x9, F, F, T)) != ONE:
        return None
    return x9, x10


def generate_5ecac7f7(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = choice(PANEL_SIDES_5ECAC7F7)
        x1 = canvas(SIX, (x0, ONE))
        x2 = tuple()
        x3 = tuple()
        x4 = True
        for x5 in range(THREE):
            x6 = _build_panel_5ecac7f7(x0, x5)
            if x6 is None:
                x4 = False
                break
            x2 = x2 + (x6[ZERO],)
            x3 = x3 + (x6[ONE],)
        if not x4:
            continue
        x7 = hconcat(hconcat(hconcat(hconcat(x2[ZERO], x1), x2[ONE]), x1), x2[TWO])
        x8 = colorfilter(sfilter(frontiers(x7), vline), SIX)
        if len(x8) != TWO:
            continue
        x9 = canvas(SEVEN, (x0, x0))
        x10 = paint(x9, x3[ZERO][ZERO])
        x11 = paint(x10, x3[ONE][ONE])
        x12 = paint(x11, x3[TWO][TWO])
        if verify_5ecac7f7(x7) != x12:
            continue
        return {"input": x7, "output": x12}
