from __future__ import annotations

from arc2.core import *


LayerSpec40f6cd08 = tuple[int, int, int, int, int]
PlacedRect40f6cd08 = tuple[int, int, int, int]


def rectangle_patch_40f6cd08(
    upper_left: IntegerTuple,
    dims: IntegerTuple,
) -> Indices:
    i0, j0 = upper_left
    h, w = dims
    return frozenset((i, j) for i in range(i0, i0 + h) for j in range(j0, j0 + w))


def full_rectangle_components_40f6cd08(
    grid: Grid,
) -> tuple[Object, ...]:
    h, w = shape(grid)
    seen = set()
    rects = []
    for i in range(h):
        for j in range(w):
            if (i, j) in seen or index(grid, (i, j)) == ZERO:
                continue
            frontier = {(i, j)}
            cells = set()
            while len(frontier) > ZERO:
                cell = frontier.pop()
                if cell in seen or index(grid, cell) == ZERO:
                    continue
                seen.add(cell)
                cells.add(cell)
                frontier |= {nbr for nbr in dneighbors(cell) if ZERO <= nbr[0] < h and ZERO <= nbr[1] < w}
            obj = toobject(frozenset(cells), grid)
            if toindices(obj) == backdrop(obj):
                rects.append(obj)
    return tuple(sorted(rects, key=lambda obj: (uppermost(obj), leftmost(obj), height(obj), width(obj))))


def base_color_40f6cd08(
    rects: tuple[Object, ...],
) -> Integer:
    singletons = tuple(color(obj) for obj in rects if numcolors(obj) == ONE)
    if len(singletons) > ZERO:
        return mostcommon(singletons)
    return mostcommon(tuple(mostcolor(obj) for obj in rects))


def decorated_rectangle_40f6cd08(
    rects: tuple[Object, ...],
) -> Object:
    mixed = tuple(obj for obj in rects if numcolors(obj) > ONE)
    return first(tuple(sorted(mixed, key=lambda obj: (uppermost(obj), leftmost(obj)))))


def layer_specs_40f6cd08(
    template: Object,
    grid: Grid,
    base_color: Integer,
) -> tuple[LayerSpec40f6cd08, ...]:
    piece = subgrid(template, grid)
    h, w = shape(piece)
    parts = tuple(obj for obj in partition(piece) if color(obj) != base_color)
    specs = tuple(
        (
            color(obj),
            uppermost(obj),
            leftmost(obj),
            h - ONE - lowermost(obj),
            w - ONE - rightmost(obj),
        )
        for obj in parts
    )
    return tuple(sorted(specs, key=lambda spec: (spec[ONE] + spec[TWO] + spec[THREE] + spec[FOUR], spec[ONE], spec[TWO], spec[THREE], spec[FOUR])))


def apply_layers_to_rectangle_40f6cd08(
    grid: Grid,
    rect: Patch,
    layers: tuple[LayerSpec40f6cd08, ...],
) -> Grid:
    out = grid
    i0, j0 = ulcorner(rect)
    h, w = shape(rect)
    for value, top, left, bottom, right in layers:
        ih = h - top - bottom
        jw = w - left - right
        if ih <= ZERO or jw <= ZERO:
            continue
        patch = rectangle_patch_40f6cd08((i0 + top, j0 + left), (ih, jw))
        out = fill(out, value, patch)
    return out


def bbox_to_patch_40f6cd08(
    rect: PlacedRect40f6cd08,
) -> Indices:
    i0, j0, h, w = rect
    return rectangle_patch_40f6cd08((i0, j0), (h, w))
