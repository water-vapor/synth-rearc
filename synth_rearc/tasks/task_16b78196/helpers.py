from __future__ import annotations

from itertools import combinations as it_combinations
from itertools import permutations as it_permutations
from itertools import product as it_product

from synth_rearc.core import *


TEMPLATE_PATCHES_16B78196: dict[str, Indices] = {
    "vtop_8": frozenset({(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (1, 1), (1, 2), (1, 3)}),
    "vtop_9": frozenset({(0, 0), (0, 4), (1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (2, 1), (2, 3)}),
    "vtop_12": frozenset(
        {
            (0, 0),
            (0, 2),
            (0, 4),
            (1, 0),
            (1, 1),
            (1, 2),
            (1, 3),
            (1, 4),
            (2, 1),
            (2, 2),
            (2, 3),
            (3, 2),
        }
    ),
    "vbot_a_8": frozenset({(0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (1, 3), (2, 1), (2, 2)}),
    "vbot_a_12": frozenset(
        {
            (0, 0),
            (0, 3),
            (1, 0),
            (1, 1),
            (1, 2),
            (1, 3),
            (2, 0),
            (2, 1),
            (2, 2),
            (3, 0),
            (3, 1),
            (4, 0),
        }
    ),
    "vbot_a_10": frozenset(
        {(0, 3), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3), (3, 0), (3, 1), (3, 2), (3, 3)}
    ),
    "vbot_b_9": frozenset({(0, 1), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2), (2, 3), (3, 0), (3, 3)}),
    "vbot_b_10": frozenset(
        {(0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (1, 3), (2, 0), (2, 1), (2, 3), (3, 1)}
    ),
    "vbot_b_8": frozenset({(0, 2), (1, 0), (1, 2), (1, 3), (2, 0), (2, 1), (2, 2), (2, 3)}),
    "hleft_10": frozenset({(0, 0), (1, 0), (1, 1), (2, 0), (2, 1), (2, 2), (3, 0), (3, 1), (3, 2), (3, 3)}),
    "hleft_13": frozenset(
        {
            (0, 0),
            (0, 1),
            (0, 2),
            (0, 3),
            (1, 1),
            (1, 2),
            (1, 3),
            (1, 4),
            (2, 2),
            (2, 3),
            (2, 4),
            (2, 5),
            (3, 3),
        }
    ),
    "hright_10": frozenset(
        {(0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (1, 3), (2, 0), (2, 1), (3, 1), (3, 2)}
    ),
    "hright_12": frozenset(
        {
            (0, 1),
            (0, 2),
            (0, 3),
            (0, 4),
            (1, 2),
            (2, 0),
            (2, 1),
            (2, 2),
            (3, 1),
            (3, 2),
            (3, 3),
            (3, 4),
        }
    ),
    "hright_8": frozenset({(0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2), (3, 2)}),
}


GROUP_SPECS_16B78196: dict[str, dict[str, object]] = {
    "vertical_top": {
        "axis": "vertical",
        "side": "top",
        "templates": ("vtop_8", "vtop_9", "vtop_12"),
        "overlaps": (1, 1),
    },
    "vertical_bottom_a": {
        "axis": "vertical",
        "side": "bottom",
        "templates": ("vbot_a_8", "vbot_a_12", "vbot_a_10"),
        "overlaps": (1, 3),
    },
    "vertical_bottom_b": {
        "axis": "vertical",
        "side": "bottom",
        "templates": ("vbot_b_9", "vbot_b_10", "vbot_b_8"),
        "overlaps": (1, 2),
    },
    "horizontal_left": {
        "axis": "horizontal",
        "side": "left",
        "templates": ("hleft_10", "hleft_13"),
        "overlaps": (3,),
    },
    "horizontal_right": {
        "axis": "horizontal",
        "side": "right",
        "templates": ("hright_10", "hright_12", "hright_8"),
        "overlaps": (2, 2),
    },
}


TEMPLATE_SIGNATURES_16B78196 = {
    tuple(sorted(cells)): name for name, cells in TEMPLATE_PATCHES_16B78196.items()
}


def make_object_16b78196(
    color_value: Integer,
    cells: Indices,
) -> Object:
    return frozenset((color_value, loc) for loc in cells)


def normalize_indices_16b78196(
    patch: Patch,
) -> Indices:
    return toindices(normalize(patch))


def object_sort_key_16b78196(
    obj: Object,
) -> tuple:
    x0 = tuple(sorted(normalize_indices_16b78196(obj)))
    return (color(obj), uppermost(obj), leftmost(obj), height(obj), width(obj), x0)


def non_anchor_objects_16b78196(
    grid: Grid,
) -> tuple[Object, tuple[Object, ...]]:
    x0 = tuple(sorted(objects(grid, T, F, T), key=object_sort_key_16b78196))
    x1 = max(x0, key=lambda obj: (len(obj), height(obj) * width(obj), color(obj)))
    x2 = tuple(obj for obj in x0 if obj != x1)
    return x1, x2


def row_patterns_16b78196(
    patch: Patch,
) -> tuple[tuple[Indices, ...], Integer]:
    x0 = normalize_indices_16b78196(patch)
    x1 = height(x0)
    x2 = width(x0)
    x3 = tuple(frozenset(j for i, j in x0 if i == k) for k in range(x1))
    return x3, x2


def column_patterns_16b78196(
    patch: Patch,
) -> tuple[tuple[Indices, ...], Integer]:
    x0 = normalize_indices_16b78196(patch)
    x1 = height(x0)
    x2 = width(x0)
    x3 = tuple(frozenset(i for i, j in x0 if j == k) for k in range(x2))
    return x3, x1


def construct_strip_16b78196(
    order: tuple[Patch, ...],
    overlaps: tuple[int, ...],
    axis: str,
) -> tuple[tuple[Indices, ...], tuple[int, ...], Integer] | None:
    if axis == "vertical":
        x0, x1 = row_patterns_16b78196(order[0])
    else:
        x0, x1 = column_patterns_16b78196(order[0])
    x2 = [set(part) for part in x0]
    x3 = [ZERO]
    x4 = len(x2)
    for x5, x6 in zip(order[1:], overlaps):
        if axis == "vertical":
            x7, x8 = row_patterns_16b78196(x5)
        else:
            x7, x8 = column_patterns_16b78196(x5)
        if x8 != x1:
            return None
        x9 = subtract(x4, x6)
        if x9 < ZERO:
            return None
        x10 = add(x9, len(x7))
        if x10 > len(x2):
            x2.extend(set() for _ in range(subtract(x10, len(x2))))
        for x11, x12 in enumerate(x7):
            x13 = add(x9, x11)
            if x2[x13] & set(x12):
                return None
            x2[x13] |= set(x12)
        x3.append(x9)
        x4 = max(x4, x10)
    x14 = tuple(frozenset(part) for part in x2)
    return x14, tuple(x3), x1


def contact_patterns_16b78196(
    strip: tuple[Indices, ...],
    span: Integer,
    side: str,
) -> tuple[Indices, ...]:
    x0 = frozenset(range(span))
    if side in ("top", "left"):
        for x1 in range(ONE, add(len(strip), ONE)):
            if all(part == x0 for part in strip[:-x1]):
                return strip[-x1:]
    for x2 in range(ONE, add(len(strip), ONE)):
        if all(part == x0 for part in strip[x2:]):
            return strip[:x2]
    raise ValueError("strip has no valid contact pattern")


def template_group_16b78196(
    spec_name: str,
    colors: tuple[Integer, ...],
) -> dict[str, object]:
    x0 = GROUP_SPECS_16B78196[spec_name]
    x1 = tuple(TEMPLATE_PATCHES_16B78196[name] for name in x0["templates"])
    x2 = x0["axis"]
    x3 = construct_strip_16b78196(x1, x0["overlaps"], x2)
    if x3 is None:
        raise ValueError(f"invalid strip spec {spec_name}")
    x4, x5, x6 = x3
    x7 = contact_patterns_16b78196(x4, x6, x0["side"])
    x8 = []
    for x9, x10, x11 in zip(x1, colors, x5):
        if x2 == "vertical":
            x12 = (x11, ZERO)
        else:
            x12 = (ZERO, x11)
        x8.append(make_object_16b78196(x10, shift(x9, x12)))
    return {
        "name": spec_name,
        "axis": x2,
        "side": x0["side"],
        "span": x6,
        "length": len(x4),
        "contact": x7,
        "objects": tuple(x8),
    }


def template_name_16b78196(
    obj: Object,
) -> str:
    x0 = tuple(sorted(normalize_indices_16b78196(obj)))
    if x0 not in TEMPLATE_SIGNATURES_16B78196:
        raise ValueError(f"unknown template signature for 16b78196: {x0}")
    return TEMPLATE_SIGNATURES_16B78196[x0]


def contact_for_offset_16b78196(
    anchor: Object,
    axis: str,
    side: str,
    span: Integer,
    offset: Integer,
) -> tuple[Indices, ...]:
    x0 = uppermost(anchor)
    x1 = leftmost(anchor)
    x2 = height(anchor)
    x3 = width(anchor)
    x4 = toindices(anchor)
    if axis == "vertical":
        x5 = add(x1, offset)
        x6: list[Indices] = []
        if side == "top":
            x7 = ZERO
            while x7 < x2:
                x8 = frozenset(j - x5 for j in range(x5, add(x5, span)) if (add(x0, x7), j) not in x4)
                if not x8:
                    break
                x6.append(x8)
                x7 = increment(x7)
            return tuple(x6)
        x9 = decrement(x2)
        x10: list[Indices] = []
        while x9 >= ZERO:
            x11 = frozenset(j - x5 for j in range(x5, add(x5, span)) if (add(x0, x9), j) not in x4)
            if not x11:
                break
            x10.append(x11)
            x9 = decrement(x9)
        return tuple(reversed(x10))
    x5 = add(x0, offset)
    x6: list[Indices] = []
    if side == "left":
        x7 = ZERO
        while x7 < x3:
            x8 = frozenset(i - x5 for i in range(x5, add(x5, span)) if (i, add(x1, x7)) not in x4)
            if not x8:
                break
            x6.append(x8)
            x7 = increment(x7)
        return tuple(x6)
    x9 = decrement(x3)
    x10: list[Indices] = []
    while x9 >= ZERO:
        x11 = frozenset(i - x5 for i in range(x5, add(x5, span)) if (i, add(x1, x9)) not in x4)
        if not x11:
            break
        x10.append(x11)
        x9 = decrement(x9)
    return tuple(reversed(x10))


def direct_groups_16b78196(
    grid: Grid,
) -> tuple[Object, tuple[dict[str, object], ...]] | None:
    x0, x1 = non_anchor_objects_16b78196(grid)
    x2 = {template_name_16b78196(obj): obj for obj in x1}
    x3 = []
    x4 = set()
    for x5 in ("vertical_top", "vertical_bottom_a", "vertical_bottom_b", "horizontal_left", "horizontal_right"):
        x6 = GROUP_SPECS_16B78196[x5]["templates"]
        if all(name in x2 for name in x6):
            x3.append(x5)
            x4 |= set(x6)
    if x4 != set(x2):
        return None
    x7 = []
    x8 = toindices(x0)
    for x9 in x3:
        x10 = GROUP_SPECS_16B78196[x9]
        x11 = tuple(color(x2[name]) for name in x10["templates"])
        x12 = template_group_16b78196(x9, x11)
        x13 = width(x0) if x12["axis"] == "vertical" else height(x0)
        x14 = subtract(x13, x12["span"])
        x15 = []
        for x16 in range(add(x14, ONE)):
            if contact_for_offset_16b78196(x0, x12["axis"], x12["side"], x12["span"], x16) != x12["contact"]:
                continue
            x17, _ = place_group_16b78196(x12, ulcorner(x0), shape(x0), x16)
            x18 = set()
            x19 = False
            for x20 in x17:
                x18 |= set(toindices(x20))
            if x18 & x8:
                continue
            for x21 in x18:
                if not both(both(x21[0] >= ZERO, x21[0] < len(grid)), both(x21[1] >= ZERO, x21[1] < len(grid[0]))):
                    x19 = True
                    break
            if x19:
                continue
            x15.append({"ids": frozenset({x9}), "placements": tuple((idx, obj) for idx, obj in enumerate(x17))})
        if not x15:
            return None
        x7.append(tuple(x15))
    x22: list[tuple[dict[str, object], ...]] = []

    def _search(x23: Integer, x24: tuple[dict[str, object], ...], x25: frozenset[IntegerTuple]) -> None:
        if x23 == len(x7):
            x22.append(x24)
            return
        for x26 in x7[x23]:
            x27 = set()
            for _, x28 in x26["placements"]:
                x27 |= set(toindices(x28))
            if x27 & x25:
                continue
            _search(add(x23, ONE), x24 + (x26,), combine(x25, frozenset(x27)))

    _search(ZERO, (), frozenset())
    if len(x22) != ONE:
        return None
    return x0, x22[0]


def place_group_16b78196(
    group: dict[str, object],
    anchor_ul: IntegerTuple,
    anchor_dims: IntegerTuple,
    offset: Integer,
) -> tuple[tuple[Object, ...], Indices]:
    x0, x1 = anchor_ul
    x2, x3 = anchor_dims
    x4 = group["axis"]
    x5 = group["side"]
    x6 = group["span"]
    x7 = group["length"]
    x8 = group["contact"]
    x9 = len(x8)
    if x4 == "vertical":
        x10 = add(x1, offset)
        x11 = add(x0, subtract(x9, x7)) if x5 == "top" else add(x0, subtract(x2, x9))
        x12 = tuple(shift(obj, (x11, x10)) for obj in group["objects"])
        x14 = x0 if x5 == "top" else add(x0, subtract(x2, x9))
        x15 = frozenset((add(x14, i), add(x10, j)) for i, row in enumerate(x8) for j in row)
        return x12, x15
    x10 = add(x0, offset)
    x11 = add(x1, subtract(x9, x7)) if x5 == "left" else add(x1, subtract(x3, x9))
    x12 = tuple(shift(obj, (x10, x11)) for obj in group["objects"])
    x14 = x1 if x5 == "left" else add(x1, subtract(x3, x9))
    x15 = frozenset((add(x10, i), add(x14, j)) for j, col in enumerate(x8) for i in col)
    return x12, x15


def axis_for_objects_16b78196(
    objs: tuple[Object, ...],
) -> str:
    x0 = {width(obj) for obj in objs}
    x1 = {height(obj) for obj in objs}
    return "vertical" if len(x0) <= len(x1) else "horizontal"


def candidate_groups_16b78196(
    grid: Grid,
) -> tuple[str, Object, tuple[dict[str, object], ...]]:
    x0, x1 = non_anchor_objects_16b78196(grid)
    x2 = axis_for_objects_16b78196(x1)
    x3 = uppermost(x0)
    x4 = leftmost(x0)
    x5 = height(x0)
    x6 = width(x0)
    x7 = toindices(x0)
    x8 = tuple((idx, color(obj), obj) for idx, obj in enumerate(x1))
    x9: list[dict[str, object]] = []
    for x10 in range(ONE, add(len(x8), ONE)):
        for x11 in it_combinations(x8, x10):
            x12 = tuple(obj for _, _, obj in x11)
            if x2 == "vertical":
                x13 = {width(obj) for obj in x12}
                if len(x13) != ONE:
                    continue
                x14 = next(iter(x13))
                x15 = frozenset(range(x14))
                for x16 in ("top", "bottom"):
                    for x17 in range(x4, add(add(x4, x6), NEG_ONE - x14 + TWO)):
                        x18: list[Indices] = []
                        if x16 == "top":
                            x19 = ZERO
                            while x19 < x5:
                                x20 = frozenset(j - x17 for j in range(x17, add(x17, x14)) if (add(x3, x19), j) not in x7)
                                if not x20:
                                    break
                                x18.append(x20)
                                x19 = increment(x19)
                        else:
                            x21 = decrement(x5)
                            x22: list[Indices] = []
                            while x21 >= ZERO:
                                x23 = frozenset(j - x17 for j in range(x17, add(x17, x14)) if (add(x3, x21), j) not in x7)
                                if not x23:
                                    break
                                x22.append(x23)
                                x21 = decrement(x21)
                            x18 = list(reversed(x22))
                        if not x18:
                            continue
                        x24 = tuple(x18)
                        for x25 in it_permutations(x11):
                            x26 = [height(obj) for _, _, obj in x25]
                            x27 = [range(ONE, min(x26[i], x26[i + ONE])) for i in range(len(x25) - ONE)]
                            for x28 in it_product(*x27) if x27 else [()]:
                                x29 = construct_strip_16b78196(tuple(obj for _, _, obj in x25), tuple(x28), x2)
                                if x29 is None:
                                    continue
                                x30, x31, _ = x29
                                if x16 == "top":
                                    if both(len(x30) >= len(x24), both(x30[-len(x24) :] == x24, all(part == x15 for part in x30[: -len(x24)]))):
                                        x32 = add(x3, subtract(len(x24), len(x30)))
                                        x33 = []
                                        for x34, x35 in zip(x25, x31):
                                            x36 = shift(normalize(x34[2]), (add(x32, x35), x17))
                                            x33.append((x34[0], x36))
                                        x9.append({"ids": frozenset(idx for idx, _, _ in x11), "placements": tuple(x33)})
                                else:
                                    if both(len(x30) >= len(x24), both(x30[: len(x24)] == x24, all(part == x15 for part in x30[len(x24) :]))):
                                        x37 = add(x3, subtract(x5, len(x24)))
                                        x38 = []
                                        for x39, x40 in zip(x25, x31):
                                            x41 = shift(normalize(x39[2]), (add(x37, x40), x17))
                                            x38.append((x39[0], x41))
                                        x9.append({"ids": frozenset(idx for idx, _, _ in x11), "placements": tuple(x38)})
            else:
                x13 = {height(obj) for obj in x12}
                if len(x13) != ONE:
                    continue
                x14 = next(iter(x13))
                x15 = frozenset(range(x14))
                for x16 in ("left", "right"):
                    for x17 in range(x3, add(add(x3, x5), NEG_ONE - x14 + TWO)):
                        x18: list[Indices] = []
                        if x16 == "left":
                            x19 = ZERO
                            while x19 < x6:
                                x20 = frozenset(i - x17 for i in range(x17, add(x17, x14)) if (i, add(x4, x19)) not in x7)
                                if not x20:
                                    break
                                x18.append(x20)
                                x19 = increment(x19)
                        else:
                            x21 = decrement(x6)
                            x22: list[Indices] = []
                            while x21 >= ZERO:
                                x23 = frozenset(i - x17 for i in range(x17, add(x17, x14)) if (i, add(x4, x21)) not in x7)
                                if not x23:
                                    break
                                x22.append(x23)
                                x21 = decrement(x21)
                            x18 = list(reversed(x22))
                        if not x18:
                            continue
                        x24 = tuple(x18)
                        for x25 in it_permutations(x11):
                            x26 = [width(obj) for _, _, obj in x25]
                            x27 = [range(ONE, min(x26[i], x26[i + ONE])) for i in range(len(x25) - ONE)]
                            for x28 in it_product(*x27) if x27 else [()]:
                                x29 = construct_strip_16b78196(tuple(obj for _, _, obj in x25), tuple(x28), x2)
                                if x29 is None:
                                    continue
                                x30, x31, _ = x29
                                if x16 == "left":
                                    if both(len(x30) >= len(x24), both(x30[-len(x24) :] == x24, all(part == x15 for part in x30[: -len(x24)]))):
                                        x32 = add(x4, subtract(len(x24), len(x30)))
                                        x33 = []
                                        for x34, x35 in zip(x25, x31):
                                            x36 = shift(normalize(x34[2]), (x17, add(x32, x35)))
                                            x33.append((x34[0], x36))
                                        x9.append({"ids": frozenset(idx for idx, _, _ in x11), "placements": tuple(x33)})
                                else:
                                    if both(len(x30) >= len(x24), both(x30[: len(x24)] == x24, all(part == x15 for part in x30[len(x24) :]))):
                                        x37 = add(x4, subtract(x6, len(x24)))
                                        x38 = []
                                        for x39, x40 in zip(x25, x31):
                                            x41 = shift(normalize(x39[2]), (x17, add(x37, x40)))
                                            x38.append((x39[0], x41))
                                        x9.append({"ids": frozenset(idx for idx, _, _ in x11), "placements": tuple(x38)})
    x42: list[dict[str, object]] = []
    for x43 in x9:
        x44 = set()
        x45 = False
        for _, x46 in x43["placements"]:
            for _, x47 in x46:
                if x47 in x44:
                    x45 = True
                    break
                x44.add(x47)
                if x47 in x7:
                    x45 = True
                    break
                if not both(both(x47[0] >= ZERO, x47[0] < len(grid)), both(x47[1] >= ZERO, x47[1] < len(grid[0]))):
                    x45 = True
                    break
            if x45:
                break
        if not x45:
            x42.append(x43)
    return x2, x0, tuple(x42)


def choose_cover_16b78196(
    candidates: tuple[dict[str, object], ...],
    n_small: Integer,
) -> tuple[dict[str, object], ...]:
    x0 = frozenset(range(n_small))
    x1: list[tuple[dict[str, object], ...]] = []

    def _search(x2: tuple[dict[str, object], ...], x3: frozenset[int]) -> None:
        if not x3:
            x1.append(x2)
            return
        x4 = min(x3)
        x5 = set()
        for x6 in x2:
            for _, x7 in x6["placements"]:
                x5 |= {loc for _, loc in x7}
        for x8 in candidates:
            x9 = x8["ids"]
            if either(x4 not in x9, not x9 <= x3):
                continue
            x10 = set()
            for _, x11 in x8["placements"]:
                x10 |= {loc for _, loc in x11}
            if x10 & x5:
                continue
            _search(x2 + (x8,), difference(x3, x9))

    _search((), x0)
    if not x1:
        raise ValueError("no valid arrangement cover")
    return min(
        x1,
        key=lambda sol: tuple(sorted(tuple(sorted(loc for _, loc in obj)) for cand in sol for _, obj in cand["placements"])),
    )


def render_output_16b78196(
    grid: Grid,
) -> Grid:
    x0 = direct_groups_16b78196(grid)
    if x0 is not None:
        x1, x2 = x0
        x3 = canvas(ZERO, shape(grid))
        x4 = paint(x3, x1)
        for x5 in x2:
            for _, x6 in x5["placements"]:
                x4 = paint(x4, x6)
        return x4
    x7, x8 = non_anchor_objects_16b78196(grid)
    _, _, x9 = candidate_groups_16b78196(grid)
    x10 = choose_cover_16b78196(x9, len(x8))
    x11 = canvas(ZERO, shape(grid))
    x12 = paint(x11, x7)
    for x13 in x10:
        for _, x14 in x13["placements"]:
            x12 = paint(x12, x14)
    return x12
