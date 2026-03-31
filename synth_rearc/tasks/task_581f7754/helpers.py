from __future__ import annotations

from synth_rearc.core import *


TEMPLATE_GRIDS_581F7754 = {
    "tee": (
        "MMM",
        "MKM",
    ),
    "bar": (
        "M",
        "M",
        "M",
        "M",
        "K",
    ),
    "ring": (
        "MMM",
        "MKM",
        "MMM",
    ),
    "arch": (
        "MMM",
        ".M.",
        ".K.",
        "MMM",
    ),
    "u": (
        "MMM",
        "M.M",
        "M.M",
        "MKM",
    ),
    "tail": (
        "...M",
        "MKMM",
        "...M",
    ),
    "frame": (
        "MMMMM",
        "M...M",
        "MMMKM",
    ),
    "cross": (
        ".M.",
        "MMM",
        "MKM",
        ".M.",
    ),
    "three_color_spine": (
        "AM",
        "AM",
        ".M",
        ".M",
        ".M",
        ".K",
    ),
}

TEMPLATE_NAMES_581F7754 = tuple(TEMPLATE_GRIDS_581F7754)


def _transform_loc_581f7754(
    loc: IntegerTuple,
    variant: Integer,
) -> IntegerTuple:
    x0, x1 = loc
    if variant == ZERO:
        return (x0, x1)
    if variant == ONE:
        return (x1, invert(x0))
    if variant == TWO:
        return (invert(x0), invert(x1))
    if variant == THREE:
        return (invert(x1), x0)
    if variant == FOUR:
        return (invert(x0), x1)
    if variant == FIVE:
        return (x0, invert(x1))
    if variant == SIX:
        return (x1, x0)
    return (invert(x1), invert(x0))


def _normalize_indices_581f7754(
    cells: frozenset[IntegerTuple],
) -> frozenset[IntegerTuple]:
    x0 = minimum(frozenset(i for i, _ in cells))
    x1 = minimum(frozenset(j for _, j in cells))
    return frozenset((subtract(i, x0), subtract(j, x1)) for i, j in cells)


def component_blueprint_581f7754(
    name: str,
    variant: Integer,
) -> dict[str, frozenset[IntegerTuple]]:
    x0 = TEMPLATE_GRIDS_581F7754[name]
    x1 = {"key": set(), "main": set(), "accent": set()}
    for x2, x3 in enumerate(x0):
        for x4, x5 in enumerate(x3):
            if x5 == ".":
                continue
            x6 = _transform_loc_581f7754((x2, x4), variant)
            if x5 == "K":
                x1["key"].add(x6)
            elif x5 == "A":
                x1["accent"].add(x6)
            else:
                x1["main"].add(x6)
    x7 = frozenset()
    for x8 in x1.values():
        x7 = combine(x7, frozenset(x8))
    x9 = _normalize_indices_581f7754(x7)
    x10 = minimum(frozenset(i for i, _ in x7))
    x11 = minimum(frozenset(j for _, j in x7))
    x12 = {}
    for x13, x14 in x1.items():
        x15 = frozenset((subtract(i, x10), subtract(j, x11)) for i, j in x14)
        x12[x13] = x15
    x12["all"] = x9
    return x12


def make_component_581f7754(
    name: str,
    origin: IntegerTuple,
    key_color: Integer,
    main_color: Integer,
    accent_color: Integer | None,
    variant: Integer,
) -> Object:
    x0 = component_blueprint_581f7754(name, variant)
    x1 = shift(x0["key"], origin)
    x2 = shift(x0["main"], origin)
    x3 = recolor(key_color, x1)
    x4 = recolor(main_color, x2)
    x5 = combine(x3, x4)
    if both(accent_color is not None, size(x0["accent"]) > ZERO):
        x6 = shift(x0["accent"], origin)
        x7 = recolor(accent_color, x6)
        x5 = combine(x5, x7)
    return x5


def key_location_581f7754(
    obj: Object,
    key_color: Integer,
) -> IntegerTuple:
    for x0, x1 in obj:
        if x0 == key_color:
            return x1
    raise ValueError(f"missing key color {key_color} in {obj}")


def padded_indices_581f7754(
    patch: Patch,
) -> Indices:
    x0 = set(toindices(patch))
    for x1 in toindices(patch):
        x0.update(dneighbors(x1))
    return frozenset(x0)


def object_fits_581f7754(
    obj: Object,
    dims: IntegerTuple,
) -> Boolean:
    x0, x1 = dims
    return all(ZERO <= i < x0 and ZERO <= j < x1 for _, (i, j) in obj)


def paint_objects_581f7754(
    grid: Grid,
    objs: tuple[Object, ...],
) -> Grid:
    x0 = grid
    for x1 in objs:
        x0 = paint(x0, x1)
    return x0


def shift_to_anchor_581f7754(
    obj: Object,
    key_color: Integer,
    axis: str,
    coord: Integer,
) -> Object:
    x0 = key_location_581f7754(obj, key_color)
    if axis == "row":
        x1 = subtract(coord, x0[0])
        return shift(obj, (x1, ZERO))
    x2 = subtract(coord, x0[1])
    return shift(obj, (ZERO, x2))
