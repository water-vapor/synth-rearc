from arc2.core import *


TEMPLATE_COLORS_98c475bf = (ONE, TWO, THREE, SIX, SEVEN)
GRID_SHAPE_98c475bf = (20, 20)
MARKER_COLUMNS_98c475bf = (ONE, 18)

_ROW_FULL = frozenset((ZERO, x0) for x0 in range(1, 19))

_TEMPLATE_PATCHES_98c475bf = {
    ONE: _ROW_FULL.union({(-ONE, 14), (-ONE, 16), (ONE, 14), (ONE, 16)}),
    TWO: _ROW_FULL.union({(-TWO, 6), (-TWO, 8), (-ONE, 7), (ONE, 7), (TWO, 6), (TWO, 8)}),
    THREE: frozenset(
        {(ZERO, x0) for x0 in (1, 2, 3)}
        | {(ZERO, x0) for x0 in range(7, 19)}
        | {(-TWO, 5), (-ONE, 4), (-ONE, 6), (ONE, 4), (ONE, 6), (TWO, 5)}
    ),
    SIX: frozenset(
        {(ZERO, x0) for x0 in (1, 2)}
        | {(ZERO, x0) for x0 in range(4, 19)}
        | {(-TWO, 2), (-TWO, 3), (-TWO, 4), (-ONE, 2), (-ONE, 4), (ONE, 2), (ONE, 4), (TWO, 2), (TWO, 4), (3, 2), (3, 3), (3, 4)}
    ),
    SEVEN: _ROW_FULL.union({(-TWO, 13), (-TWO, 15), (-ONE, 13), (-ONE, 15), (ONE, 13), (ONE, 15), (TWO, 13), (TWO, 15)}),
}


def template_patch_98c475bf(
    color_value: Integer,
) -> Indices:
    if color_value not in _TEMPLATE_PATCHES_98c475bf:
        raise ValueError(f"unsupported template color for 98c475bf: {color_value}")
    return _TEMPLATE_PATCHES_98c475bf[color_value]


def render_templates_98c475bf(
    specs: tuple[tuple[Integer, Integer], ...],
) -> Object:
    x0 = frozenset()
    for x1, x2 in specs:
        x3 = template_patch_98c475bf(x1)
        x4 = shift(x3, toivec(x2))
        x0 = x0.union(recolor(x1, x4))
    return x0


def template_anchor_rows_98c475bf(
    color_value: Integer,
    height_value: Integer = 20,
) -> tuple[Integer, ...]:
    x0 = template_patch_98c475bf(color_value)
    x1 = [x2 for x2, _ in x0]
    x3 = -min(x1)
    x4 = height_value - max(x1)
    return tuple(range(x3, x4))
