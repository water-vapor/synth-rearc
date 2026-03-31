from __future__ import annotations

from synth_rearc.core import *

from .verifier import verify_a251c730


GRID_SIDE_251C730 = 30
PANEL_MARGIN_251C730 = ONE
PANEL_PADDING_251C730 = ONE
BACKGROUND_MODES_251C730 = ("rows", "cols", "rows")
TEMPLATE_OFFSETS_251C730 = (
    frozenset({(-TWO, -ONE), (-TWO, ONE), (-ONE, -ONE), (-ONE, ZERO), (-ONE, ONE)}),
    frozenset({(-ONE, ZERO), (ZERO, -ONE), (ZERO, ONE), (ONE, ZERO)}),
    frozenset({(-ONE, ZERO), (ZERO, -ONE), (ZERO, ONE), (ONE, -ONE), (ONE, ZERO), (ONE, ONE)}),
    frozenset({(-ONE, -ONE), (-ONE, ZERO), (-ONE, ONE), (ZERO, -ONE), (ZERO, ONE)}),
)


def _background_grid_a251c730(
    mode: str,
    cycle: tuple[Integer, ...],
    phase: Integer,
) -> Grid:
    x0 = len(cycle)
    if mode == "rows":
        return tuple(
            tuple(cycle[(j + phase) % x0] for j in range(GRID_SIDE_251C730))
            for _ in range(GRID_SIDE_251C730)
        )
    return tuple(
        tuple(cycle[(i + phase) % x0] for _ in range(GRID_SIDE_251C730))
        for i in range(GRID_SIDE_251C730)
    )


def _template_object_a251c730(
    center_color: Integer,
    surround_color: Integer,
    offsets: Indices,
) -> Object:
    x0 = frozenset({(center_color, ORIGIN)})
    x1 = frozenset((surround_color, x2) for x2 in offsets)
    return x0 | x1


def _bounds_a251c730(
    patch: Patch,
) -> tuple[Integer, Integer, Integer, Integer]:
    x0 = toindices(patch)
    x1 = tuple(x2[ZERO] for x2 in x0)
    x2 = tuple(x3[ONE] for x3 in x0)
    return minimum(x1), minimum(x2), maximum(x1), maximum(x2)


def _halo_a251c730(
    patch: Patch,
    h: Integer,
    w: Integer,
    padding: Integer,
) -> Indices:
    x0, x1, x2, x3 = _bounds_a251c730(patch)
    x4 = max(ZERO, x0 - padding)
    x5 = max(ZERO, x1 - padding)
    x6 = min(h - ONE, x2 + padding)
    x7 = min(w - ONE, x3 + padding)
    return frozenset((i, j) for i in range(x4, x6 + ONE) for j in range(x5, x7 + ONE))


def _place_objects_a251c730(
    h: Integer,
    w: Integer,
    objects_to_place: tuple[Object, ...],
    padding: Integer,
) -> tuple[Object, ...] | None:
    x0: Indices = frozenset()
    x1 = []
    for x2 in objects_to_place:
        x3, x4, x5, x6 = _bounds_a251c730(x2)
        x7 = tuple(
            (i, j)
            for i in range(-x3, h - x5)
            for j in range(-x4, w - x6)
        )
        x8 = sample(x7, len(x7))
        x9 = None
        for x10 in x8:
            x11 = shift(x2, x10)
            x12 = _halo_a251c730(x11, h, w, padding)
            if len(x12 & x0) != ZERO:
                continue
            x9 = x11
            x0 = x0 | x12
            break
        if x9 is None:
            return None
        x1.append(x9)
    return tuple(x1)


def _sample_panel_layout_a251c730(
    diff_lb: float,
    diff_ub: float,
    objects_to_place: tuple[Object, ...],
    *,
    area_factor: Integer,
) -> tuple[Integer, Integer, tuple[Object, ...]] | None:
    x0 = maximum(tuple(height(x1) for x1 in objects_to_place))
    x1 = maximum(tuple(width(x2) for x2 in objects_to_place))
    x2 = sum(size(x3) for x3 in objects_to_place)
    x3 = max(SIX, x0 + TWO)
    x4 = max(SIX, x1 + TWO)
    x5 = min(18, max(x3, x0 + area_factor + len(objects_to_place) * TWO))
    x6 = min(20, max(x4, x1 + area_factor + len(objects_to_place) * THREE))
    for _ in range(80):
        x7 = unifint(diff_lb, diff_ub, (x3, x5))
        x8 = unifint(diff_lb, diff_ub, (x4, x6))
        if x7 * x8 < x2 * TWO + len(objects_to_place) * SIX:
            continue
        x9 = _place_objects_a251c730(x7, x8, objects_to_place, PANEL_PADDING_251C730)
        if x9 is not None:
            return x7, x8, x9
    return None


def _panel_from_objects_a251c730(
    h: Integer,
    w: Integer,
    border_color: Integer,
    bg_color: Integer,
    objects_to_paint: tuple[Object, ...],
) -> Grid:
    x0 = canvas(border_color, (h + TWO, w + TWO))
    x1 = frozenset((i, j) for i in range(ONE, h + ONE) for j in range(ONE, w + ONE))
    x2 = fill(x0, bg_color, x1)
    x3 = x2
    for x4 in objects_to_paint:
        x3 = paint(x3, shift(x4, (ONE, ONE)))
    return x3


def _singleton_centers_a251c730(
    objects_to_place: tuple[Object, ...],
    center_colors: tuple[Integer, ...],
) -> tuple[Object, ...]:
    return tuple(
        frozenset({(x1, next(x2 for x3, x2 in x0 if x3 == x1))})
        for x0, x1 in zip(objects_to_place, center_colors)
    )


def _place_panels_a251c730(
    panel_shapes: tuple[IntegerTuple, IntegerTuple],
) -> tuple[IntegerTuple, IntegerTuple] | None:
    x0: Indices = frozenset()
    x1 = []
    for x2, x3 in panel_shapes:
        x4 = tuple(
            (i, j)
            for i in range(PANEL_MARGIN_251C730, GRID_SIDE_251C730 - x2 - PANEL_MARGIN_251C730 + ONE)
            for j in range(PANEL_MARGIN_251C730, GRID_SIDE_251C730 - x3 - PANEL_MARGIN_251C730 + ONE)
        )
        x5 = sample(x4, len(x4))
        x6 = None
        for x7 in x5:
            x8 = frozenset(
                (i, j)
                for i in range(x7[ZERO], x7[ZERO] + x2)
                for j in range(x7[ONE], x7[ONE] + x3)
            )
            x9 = _halo_a251c730(x8, GRID_SIDE_251C730, GRID_SIDE_251C730, PANEL_PADDING_251C730)
            if len(x9 & x0) != ZERO:
                continue
            x6 = x7
            x0 = x0 | x9
            break
        if x6 is None:
            return None
        x1.append(x6)
    return tuple(x1)


def _overlay_panel_a251c730(
    grid: Grid,
    panel: Grid,
    top_left: IntegerTuple,
) -> Grid:
    x0 = frozenset(
        (panel[i][j], add(top_left, (i, j)))
        for i in range(len(panel))
        for j in range(len(panel[ZERO]))
    )
    return paint(grid, x0)


def generate_a251c730(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    x0 = tuple(range(TEN))
    while True:
        x1 = choice((ONE, ONE, TWO))
        x2 = sample(x0, x1 * TWO + FOUR)
        x3, x4, x5, x6 = x2[:FOUR]
        x7 = tuple(x2[FOUR + x8] for x8 in range(x1))
        x8 = tuple(x2[FOUR + x1 + x9] for x9 in range(x1))
        x9 = sample(tuple(range(len(TEMPLATE_OFFSETS_251C730))), x1)
        x10 = choice(BACKGROUND_MODES_251C730)
        x11 = choice((FOUR, FIVE))
        x12 = tuple(x13 for x13 in x0 if x13 not in (x3, x5))
        x13 = tuple(sample(x12, x11))
        x14 = randint(ZERO, x11 - ONE)
        x15 = tuple(
            _template_object_a251c730(x16, x17, TEMPLATE_OFFSETS_251C730[x18])
            for x16, x17, x18 in zip(x7, x8, x9)
        )
        x16 = _background_grid_a251c730(x10, x13, x14)

        x17 = []
        x18 = []
        for x19, x20 in zip(x15, x7):
            x21 = choice((ONE, TWO, TWO, THREE)) if x1 == ONE else choice((ONE, ONE, TWO))
            x22 = choice((ONE, TWO, TWO, THREE)) if x1 == ONE else choice((ONE, TWO))
            x17.extend((x19, x20) for _ in range(x21))
            x18.extend((x19, x20) for _ in range(x22))

        x19 = _sample_panel_layout_a251c730(
            diff_lb,
            diff_ub,
            tuple(x20 for x20, _ in x17),
            area_factor=FOUR,
        )
        x20 = _sample_panel_layout_a251c730(
            diff_lb,
            diff_ub,
            tuple(x21 for x21, _ in x18),
            area_factor=SIX,
        )
        if either(x19 is None, x20 is None):
            continue

        x21, x22, x23 = x19
        x24, x25, x26 = x20
        x27 = _panel_from_objects_a251c730(x21, x22, x3, x4, x23)
        x28 = _panel_from_objects_a251c730(
            x24,
            x25,
            x5,
            x6,
            _singleton_centers_a251c730(x26, tuple(x29 for _, x29 in x18)),
        )
        x29 = _panel_from_objects_a251c730(x24, x25, x5, x6, x26)

        x30 = _place_panels_a251c730(
            (shape(x27), shape(x28))
        )
        if x30 is None:
            continue

        x31 = _overlay_panel_a251c730(x16, x27, x30[ZERO])
        x32 = _overlay_panel_a251c730(x31, x28, x30[ONE])
        if x32 == x29:
            continue
        if verify_a251c730(x32) != x29:
            continue
        return {"input": x32, "output": x29}
