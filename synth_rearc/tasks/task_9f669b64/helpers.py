from synth_rearc.core import *


def rect_patch_9f669b64(
    top: Integer,
    left: Integer,
    height_value: Integer,
    width_value: Integer,
) -> Indices:
    return frozenset(
        (i, j)
        for i in range(top, top + height_value)
        for j in range(left, left + width_value)
    )


def tee_patch_9f669b64(
    top: Integer,
    left: Integer,
    width_value: Integer,
) -> Indices:
    stem_left = left + width_value // 2 - 1
    bar = rect_patch_9f669b64(top, left, 2, width_value)
    stem = rect_patch_9f669b64(top + 2, stem_left, 1, 2)
    return combine(bar, stem)


def taper_patch_9f669b64(
    top: Integer,
    left: Integer,
    width_value: Integer,
    point_side: str,
) -> Indices:
    band = max(2, width_value // 2)
    if point_side == "left":
        row0 = frozenset({(top, left)})
        row1 = frozenset((top + 1, j) for j in range(left, left + band))
        row4 = frozenset((top + 4, j) for j in range(left, left + band))
        row5 = frozenset({(top + 5, left)})
    else:
        row0 = frozenset({(top, left + width_value - 1)})
        row1 = frozenset((top + 1, j) for j in range(left + width_value - band, left + width_value))
        row4 = frozenset((top + 4, j) for j in range(left + width_value - band, left + width_value))
        row5 = frozenset({(top + 5, left + width_value - 1)})
    row23 = rect_patch_9f669b64(top + 2, left, 2, width_value)
    return combine(combine(row0, row1), combine(row23, combine(row4, row5)))


def _bbox_9f669b64(
    patch: Patch,
) -> tuple[Integer, Integer, Integer, Integer]:
    top, left = ulcorner(patch)
    bottom, right = lrcorner(patch)
    return top, left, bottom, right


def _is_solid_box_9f669b64(
    obj: Object,
) -> Boolean:
    return size(obj) == height(obj) * width(obj)


def _mover_key_9f669b64(
    obj: Object,
) -> tuple[Integer, Integer, Integer]:
    return (max(shape(obj)), size(obj), color(obj))


def _destination_key_9f669b64(
    obj: Object,
) -> tuple[Integer, Integer]:
    solid_penalty = 0 if _is_solid_box_9f669b64(obj) else 1
    return (solid_penalty, -color(obj))


def select_roles_9f669b64(
    grid: Grid,
) -> tuple[Object, Object, Object]:
    objs = tuple(objects(grid, T, F, T))
    mover = min(objs, key=_mover_key_9f669b64)
    others = tuple(obj for obj in objs if obj != mover)
    destination = min(others, key=_destination_key_9f669b64)
    static = first(tuple(obj for obj in others if obj != destination))
    return destination, mover, static


def split_destination_9f669b64(
    destination: Object,
) -> Object:
    top, left, bottom, right = _bbox_9f669b64(destination)
    height_value, width_value = shape(destination)
    value = color(destination)
    if width_value >= height_value:
        half = width_value // 2
        left_half = frozenset(
            (i, j - 1)
            for i in range(top, bottom + 1)
            for j in range(left, left + half)
        )
        right_half = frozenset(
            (i, j + 1)
            for i in range(top, bottom + 1)
            for j in range(left + half, right + 1)
        )
        return recolor(value, combine(left_half, right_half))
    half = height_value // 2
    top_half = frozenset(
        (i - 1, j)
        for i in range(top, top + half)
        for j in range(left, right + 1)
    )
    bottom_half = frozenset(
        (i + 1, j)
        for i in range(top + half, bottom + 1)
        for j in range(left, right + 1)
    )
    return recolor(value, combine(top_half, bottom_half))


def mirror_mover_across_destination_9f669b64(
    mover: Object,
    destination: Object,
    dims: tuple[Integer, Integer],
) -> Object:
    dtop, dleft, dbottom, dright = _bbox_9f669b64(destination)
    _, _, mbottom, mright = _bbox_9f669b64(mover)
    mover_height, mover_width = shape(mover)
    max_top = dims[0] - mover_height
    max_left = dims[1] - mover_width
    new_top = max(0, min(dtop + dbottom - mbottom, max_top))
    new_left = max(0, min(dleft + dright - mright, max_left))
    return shift(normalize(mover), (new_top, new_left))


def compose_output_9f669b64(
    destination: Object,
    mover: Object,
    static: Object,
    dims: tuple[Integer, Integer],
    bg: Integer,
) -> Grid:
    out = canvas(bg, dims)
    out = paint(out, static)
    out = paint(out, split_destination_9f669b64(destination))
    out = paint(out, mirror_mover_across_destination_9f669b64(mover, destination, dims))
    return out


def solve_9f669b64(
    grid: Grid,
) -> Grid:
    destination, mover, static = select_roles_9f669b64(grid)
    return compose_output_9f669b64(destination, mover, static, shape(grid), mostcolor(grid))
