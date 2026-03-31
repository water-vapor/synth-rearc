from __future__ import annotations

from synth_rearc.core import *

from .helpers import TEMPLATE_NAMES_581F7754
from .helpers import component_blueprint_581f7754
from .helpers import key_location_581f7754
from .helpers import make_component_581f7754
from .helpers import object_fits_581f7754
from .helpers import padded_indices_581f7754
from .helpers import paint_objects_581f7754
from .helpers import shift_to_anchor_581f7754
from .verifier import verify_581f7754


TEMPLATE_POOL_581F7754 = (
    "tee",
    "tee",
    "bar",
    "ring",
    "ring",
    "arch",
    "u",
    "tail",
    "frame",
    "cross",
    "three_color_spine",
)


def _non_bg_colors_581f7754(
    bg: Integer,
) -> tuple[Integer, ...]:
    return tuple(x0 for x0 in interval(ZERO, TEN, ONE) if x0 != bg)


def _sample_anchor_specs_581f7754(
    dims: IntegerTuple,
    colors: tuple[Integer, ...],
    diff_lb: float,
    diff_ub: float,
) -> tuple[dict[str, object], ...]:
    x0, x1 = dims
    x2 = min(len(colors), unifint(diff_lb, diff_ub, (ONE, THREE)))
    x3 = list(colors)
    shuffle(x3)
    x4 = []
    for x5 in x3[:x2]:
        x6 = choice(("row", "row", "col", "col"))
        if x6 == "row":
            x7 = randint(ONE, subtract(x0, TWO))
            x8 = choice(("left", "right", "both", "left"))
            x9 = []
            if x8 in ("left", "both"):
                x9.append((x7, ZERO))
            if x8 in ("right", "both"):
                x9.append((x7, subtract(x1, ONE)))
        else:
            x7 = randint(ONE, subtract(x1, TWO))
            x8 = choice(("top", "bottom", "both", "top"))
            x9 = []
            if x8 in ("top", "both"):
                x9.append((ZERO, x7))
            if x8 in ("bottom", "both"):
                x9.append((subtract(x0, ONE), x7))
        x10 = choice((ZERO, ONE, ONE, TWO))
        x11 = choice((ONE, ONE, TWO, TWO, THREE))
        if both(equality(x10, ZERO), equality(x11, ZERO)):
            x11 = ONE
        x4.append(
            {
                "color": x5,
                "axis": x6,
                "coord": x7,
                "anchors": tuple(x9),
                "n_singletons": x10,
                "n_multi": x11,
            }
        )
    return tuple(x4)


def _choose_body_colors_581f7754(
    key_color: Integer,
    bg: Integer,
    needs_accent: Boolean,
) -> tuple[Integer, Integer | None]:
    x0 = tuple(x1 for x1 in interval(ZERO, TEN, ONE) if x1 not in (bg, key_color))
    x2 = choice(x0)
    if not needs_accent:
        return x2, None
    x3 = tuple(x4 for x4 in x0 if x4 != x2)
    x5 = choice(x3 if len(x3) > ZERO else x0)
    return x2, x5


def _sample_delta_581f7754(
    low_value: Integer,
    high_value: Integer,
) -> Integer | None:
    x0 = [x1 for x1 in range(low_value, add(high_value, ONE)) if x1 != ZERO]
    if len(x0) == ZERO:
        return None
    shuffle(x0)
    x2 = [x3 for x3 in x0 if abs(x3) > ONE]
    if len(x2) > ZERO and randint(ZERO, TWO) != ZERO:
        return choice(tuple(x2))
    return choice(tuple(x0))


def _sample_output_origin_581f7754(
    blueprint: dict[str, frozenset[IntegerTuple]],
    axis: str,
    coord: Integer,
    dims: IntegerTuple,
) -> IntegerTuple | None:
    x0, x1 = dims
    x2 = next(iter(blueprint["key"]))
    x3 = height(blueprint["all"])
    x4 = width(blueprint["all"])
    if axis == "row":
        x5 = subtract(coord, x2[0])
        if both(x5 >= ZERO, add(x5, x3) <= x0):
            x6 = interval(ZERO, add(subtract(x1, x4), ONE), ONE)
            if len(x6) == ZERO:
                return None
            return (x5, choice(x6))
        return None
    x7 = subtract(coord, x2[1])
    if both(x7 >= ZERO, add(x7, x4) <= x1):
        x8 = interval(ZERO, add(subtract(x0, x3), ONE), ONE)
        if len(x8) == ZERO:
            return None
        return (choice(x8), x7)
    return None


def _place_anchor_581f7754(
    color_value: Integer,
    loc: IntegerTuple,
    dims: IntegerTuple,
    input_blocked: set[IntegerTuple],
    input_objs: list[Object],
    output_used: set[IntegerTuple],
    output_objs: list[Object],
) -> Boolean:
    x0 = frozenset({(color_value, loc)})
    x1 = toindices(x0)
    if not object_fits_581f7754(x0, dims):
        return False
    if x1 & input_blocked:
        return False
    if x1 & output_used:
        return False
    input_objs.append(x0)
    output_objs.append(x0)
    input_blocked.update(padded_indices_581f7754(x0))
    output_used.update(x1)
    return True


def _place_singleton_581f7754(
    spec: dict[str, object],
    dims: IntegerTuple,
    input_blocked: set[IntegerTuple],
    input_objs: list[Object],
    output_used: set[IntegerTuple],
    output_objs: list[Object],
) -> Boolean:
    x0, x1 = dims
    x2 = spec["color"]
    x3 = spec["axis"]
    x4 = spec["coord"]
    x5 = set(spec["anchors"])
    for _ in range(80):
        if x3 == "row":
            x6 = randint(ONE, subtract(x1, TWO))
            x7 = (x4, x6)
            x8 = _sample_delta_581f7754(invert(x4), subtract(subtract(x0, ONE), x4))
            if x8 is None:
                continue
            x9 = (add(x4, x8), x6)
        else:
            x6 = randint(ONE, subtract(x0, TWO))
            x7 = (x6, x4)
            x8 = _sample_delta_581f7754(invert(x4), subtract(subtract(x1, ONE), x4))
            if x8 is None:
                continue
            x9 = (x6, add(x4, x8))
        if x7 in x5:
            continue
        x10 = frozenset({(x2, x9)})
        x11 = frozenset({(x2, x7)})
        x12 = toindices(x10)
        x13 = toindices(x11)
        if x12 & input_blocked:
            continue
        if x13 & output_used:
            continue
        input_objs.append(x10)
        output_objs.append(x11)
        input_blocked.update(padded_indices_581f7754(x10))
        output_used.update(x13)
        return True
    return False


def _place_multicolor_581f7754(
    spec: dict[str, object],
    bg: Integer,
    dims: IntegerTuple,
    input_blocked: set[IntegerTuple],
    input_objs: list[Object],
    output_used: set[IntegerTuple],
    output_objs: list[Object],
) -> Boolean:
    x0 = spec["color"]
    x1 = spec["axis"]
    x2 = spec["coord"]
    for _ in range(120):
        x3 = choice(TEMPLATE_POOL_581F7754)
        x4 = randint(ZERO, SEVEN)
        x5 = component_blueprint_581f7754(x3, x4)
        x6, x7 = _choose_body_colors_581f7754(x0, bg, size(x5["accent"]) > ZERO)
        x8 = _sample_output_origin_581f7754(x5, x1, x2, dims)
        if x8 is None:
            continue
        x9 = make_component_581f7754(x3, x8, x0, x6, x7, x4)
        x10 = key_location_581f7754(x9, x0)
        if x1 == "row":
            x11 = _sample_delta_581f7754(invert(x10[0]), subtract(subtract(dims[0], ONE), x10[0]))
            if x11 is None:
                continue
            x12 = shift(x9, (x11, ZERO))
        else:
            x11 = _sample_delta_581f7754(invert(x10[1]), subtract(subtract(dims[1], ONE), x10[1]))
            if x11 is None:
                continue
            x12 = shift(x9, (ZERO, x11))
        x13 = toindices(x12)
        x14 = toindices(x9)
        if not object_fits_581f7754(x12, dims):
            continue
        if x13 & input_blocked:
            continue
        if x14 & output_used:
            continue
        input_objs.append(x12)
        output_objs.append(x9)
        input_blocked.update(padded_indices_581f7754(x12))
        output_used.update(x14)
        return True
    return False


def generate_581f7754(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = unifint(diff_lb, diff_ub, (TEN, 24))
        x1 = unifint(diff_lb, diff_ub, (TEN, 24))
        x2 = (x0, x1)
        x3 = randint(ZERO, NINE)
        x4 = _non_bg_colors_581f7754(x3)
        x5 = _sample_anchor_specs_581f7754(x2, x4, diff_lb, diff_ub)
        x6: list[Object] = []
        x7: list[Object] = []
        x8: set[IntegerTuple] = set()
        x9: set[IntegerTuple] = set()
        x10 = T
        x11 = ZERO
        x12 = ZERO
        for x13 in x5:
            for x14 in x13["anchors"]:
                if not _place_anchor_581f7754(x13["color"], x14, x2, x8, x6, x9, x7):
                    x10 = F
                    break
            if not x10:
                break
            for _ in range(x13["n_singletons"]):
                if not _place_singleton_581f7754(x13, x2, x8, x6, x9, x7):
                    x10 = F
                    break
                x11 = increment(x11)
            if not x10:
                break
            for _ in range(x13["n_multi"]):
                if not _place_multicolor_581f7754(x13, x3, x2, x8, x6, x9, x7):
                    x10 = F
                    break
                x11 = increment(x11)
                x12 = increment(x12)
            if not x10:
                break
        if not x10:
            continue
        if x11 < TWO:
            continue
        if x12 == ZERO:
            continue
        x15 = canvas(x3, x2)
        x16 = paint_objects_581f7754(x15, tuple(x6))
        x17 = paint_objects_581f7754(x15, tuple(x7))
        if x16 == x17:
            continue
        if verify_581f7754(x16) != x17:
            continue
        return {"input": x16, "output": x17}
