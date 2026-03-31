from __future__ import annotations

from itertools import combinations

from synth_rearc.core import *


TRANSFORM_NAMES_A25697E4 = (
    "id",
    "rot90",
    "rot180",
    "rot270",
    "hmirror",
    "vmirror",
    "dmirror",
    "cmirror",
)

REFLECTION_NAMES_A25697E4 = frozenset({"hmirror", "vmirror", "dmirror", "cmirror"})


def _bbox_a25697e4(
    patch: Indices,
) -> tuple[Integer, Integer, Integer, Integer]:
    x0 = tuple(i for i, _ in patch)
    x1 = tuple(j for _, j in patch)
    return (min(x0), min(x1), max(x0), max(x1))


def _bbox_key_a25697e4(
    patch: Indices,
) -> tuple[Integer, Integer, Integer, Integer, Integer]:
    x0 = _bbox_a25697e4(patch)
    return (x0[ZERO], x0[ONE], x0[TWO], x0[THREE], len(patch))


def _shift_patch_a25697e4(
    patch: Indices,
    offset: IntegerTuple,
) -> Indices:
    return frozenset((i + offset[ZERO], j + offset[ONE]) for i, j in patch)


def _rect_patch_a25697e4(
    bbox: tuple[Integer, Integer, Integer, Integer],
) -> Indices:
    return frozenset(
        (i, j)
        for i in range(bbox[ZERO], bbox[TWO] + ONE)
        for j in range(bbox[ONE], bbox[THREE] + ONE)
    )


def _union_bbox_a25697e4(
    a: Indices,
    b: Indices,
) -> tuple[Integer, Integer, Integer, Integer]:
    x0 = _bbox_a25697e4(a)
    x1 = _bbox_a25697e4(b)
    return (
        min(x0[ZERO], x1[ZERO]),
        min(x0[ONE], x1[ONE]),
        max(x0[TWO], x1[TWO]),
        max(x0[THREE], x1[THREE]),
    )


def _normalize_patch_a25697e4(
    patch: Indices,
) -> Indices:
    return frozenset(normalize(patch))


def _dims_a25697e4(
    patch: Indices,
) -> IntegerTuple:
    x0 = _normalize_patch_a25697e4(patch)
    return (height(x0), width(x0))


def _apply_transform_a25697e4(
    patch: Indices,
    name: str,
) -> Indices:
    x0 = _normalize_patch_a25697e4(patch)
    x1, x2 = _dims_a25697e4(x0)
    if name == "id":
        return x0
    if name == "rot90":
        return frozenset((j, x1 - ONE - i) for i, j in x0)
    if name == "rot180":
        return frozenset((x1 - ONE - i, x2 - ONE - j) for i, j in x0)
    if name == "rot270":
        return frozenset((x2 - ONE - j, i) for i, j in x0)
    if name == "hmirror":
        return frozenset((x1 - ONE - i, j) for i, j in x0)
    if name == "vmirror":
        return frozenset((i, x2 - ONE - j) for i, j in x0)
    if name == "dmirror":
        return frozenset((j, i) for i, j in x0)
    if name == "cmirror":
        return frozenset((x2 - ONE - j, x1 - ONE - i) for i, j in x0)
    raise ValueError(f"unknown transform {name}")


def _split_patch_a25697e4(
    patch: Indices,
) -> tuple[Indices, ...]:
    x0 = set(patch)
    x1 = []
    while x0:
        x2 = {next(iter(x0))}
        x3 = set(x2)
        while x2:
            x4 = x2.pop()
            x5 = frozenset(y0 for y0 in dneighbors(x4) if y0 in x0)
            x2.update(x5 - x3)
            x3.update(x5)
        x0 -= x3
        x1.append(frozenset(x3))
    return tuple(sorted(x1, key=_bbox_key_a25697e4))


def _parse_rows_a25697e4(
    rows: tuple[str, ...],
) -> dict[str, Indices]:
    x0 = {}
    for i, row in enumerate(rows):
        for j, value in enumerate(row):
            if value == ".":
                continue
            x0.setdefault(value, set()).add((i, j))
    return {key: frozenset(value) for key, value in x0.items()}


def _template_from_rows_a25697e4(
    name: str,
    anchor_rows: tuple[str, ...],
    source_rows: tuple[str, ...],
) -> dict:
    x0 = _parse_rows_a25697e4(anchor_rows)
    x1 = _split_patch_a25697e4(x0["A"])
    x2 = _parse_rows_a25697e4(source_rows)
    x3 = tuple(
        {"label": key, "patch": value}
        for key, value in sorted(x2.items(), key=lambda item: _bbox_key_a25697e4(item[ONE]))
    )
    x4 = frozenset().union(*(y0["patch"] for y0 in x3))
    x5 = _union_bbox_a25697e4(x1[ZERO], x1[ONE])
    x6 = _rect_patch_a25697e4(x5) - frozenset().union(*x1)
    return {
        "name": name,
        "anchor_components": x1,
        "source_components": x3,
        "anchor_bbox": x5,
        "complement_size": len(x6),
    }


PAIR_TEMPLATES_A25697E4 = (
    _template_from_rows_a25697e4(
        "train0",
        (
            "AAAA",
            "AA..",
            "....",
            "AAAA",
        ),
        (
            ".B.",
            ".B.",
            "BB.",
            "BB.",
            "CCC",
            "..C",
        ),
    ),
    _template_from_rows_a25697e4(
        "train1",
        (
            "AAAA",
            "....",
            "AA..",
            "AAAA",
        ),
        (
            ".B.",
            ".B.",
            "BB.",
            "BB.",
            "CCC",
            "..C",
        ),
    ),
    _template_from_rows_a25697e4(
        "train2",
        (
            "A...A",
            "A.AAA",
            "A.AAA",
        ),
        (
            ".B....",
            "BB....",
            ".BBB..",
            "...CCC",
            "...C..",
            "...C..",
        ),
    ),
    _template_from_rows_a25697e4(
        "test0a",
        (
            "AAA.A",
            "AAA.A",
            "AAA.A",
            "AAA.A",
            "AA..A",
        ),
        (
            "CCCCC",
            "...BC",
            "...B.",
            "BBB..",
            "BBB..",
        ),
    ),
    _template_from_rows_a25697e4(
        "test0b",
        (
            "AAAAA",
            "...AA",
            ".....",
            "AAAAA",
            "AAAAA",
            "AAAAA",
            "AAAAA",
        ),
        (
            "CCCCC",
            "CCC..",
            "B....",
            "BB...",
            "B....",
        ),
    ),
    _template_from_rows_a25697e4(
        "test1a",
        (
            "AA.AAA",
            "AA..AA",
            "AA...A",
        ),
        (
            ".....CCC",
            "...BBCC.",
            "BBBB.C..",
            "BBBB....",
        ),
    ),
    _template_from_rows_a25697e4(
        "test1b",
        (
            "AAAA",
            "AAAA",
            "....",
            ".AAA",
            "AAAA",
        ),
        (
            "....B.",
            ".BBBB.",
            ".....C",
            "....CC",
            "....C.",
        ),
    ),
)


def _component_records_a25697e4(
    I: Grid,
) -> tuple[dict, ...]:
    x0 = tuple(sorted(objects(I, T, F, T), key=lambda item: _bbox_key_a25697e4(frozenset(toindices(item)))))
    x1 = []
    for index, obj in enumerate(x0):
        x2 = frozenset(toindices(obj))
        x1.append(
            {
                "index": index,
                "color": color(obj),
                "cells": x2,
                "bbox": _bbox_a25697e4(x2),
            }
        )
    return tuple(x1)


def _anchor_candidates_a25697e4(
    components: tuple[dict, ...],
) -> tuple[dict, ...]:
    x0 = []
    for x1, x2 in combinations(components, TWO):
        if x1["color"] != x2["color"]:
            continue
        x3 = x1["cells"] | x2["cells"]
        x4 = _union_bbox_a25697e4(x1["cells"], x2["cells"])
        x5 = _rect_patch_a25697e4(x4)
        x6 = x5 - x3
        if len(x6) == ZERO:
            continue
        if any(
            y0["index"] not in (x1["index"], x2["index"]) and len(y0["cells"] & x5) > ZERO
            for y0 in components
        ):
            continue
        x0.append(
            {
                "index": len(x0),
                "component_indices": (x1["index"], x2["index"]),
                "color": x1["color"],
                "union": x3,
                "bbox": x4,
                "rect": x5,
                "complement": x6,
            }
        )
    return tuple(sorted(x0, key=lambda item: (*item["bbox"], len(item["complement"]))))


def _source_candidates_a25697e4(
    components: tuple[dict, ...],
) -> tuple[dict, ...]:
    x0 = []
    for x1, x2 in combinations(components, TWO):
        if x1["color"] == x2["color"]:
            continue
        x3 = x1["cells"] | x2["cells"]
        x4 = _union_bbox_a25697e4(x1["cells"], x2["cells"])
        x5 = _rect_patch_a25697e4(x4)
        if any(
            y0["index"] not in (x1["index"], x2["index"]) and len(y0["cells"] & x5) > ZERO
            for y0 in components
        ):
            continue
        x6 = tuple(sorted((x1, x2), key=lambda item: (*item["bbox"], item["color"])))
        x0.append(
            {
                "index": len(x0),
                "component_indices": (x6[ZERO]["index"], x6[ONE]["index"]),
                "components": x6,
                "bbox": x4,
                "union": x3,
            }
        )
    return tuple(sorted(x0, key=lambda item: (*item["bbox"], len(item["union"]))))


def _pair_candidates_a25697e4(
    I: Grid,
    components: tuple[dict, ...],
    anchors: tuple[dict, ...],
    sources: tuple[dict, ...],
) -> tuple[dict, ...]:
    x0 = frozenset(y0 for y1 in components for y0 in y1["cells"])
    x1 = shape(I)
    x2 = []
    for anchor in anchors:
        x3 = _normalize_patch_a25697e4(anchor["complement"])
        for source in sources:
            x4 = x0 - anchor["union"] - source["union"]
            x5 = _normalize_patch_a25697e4(source["union"])
            for inside_index, part in enumerate(source["components"]):
                x6 = _normalize_patch_a25697e4(part["cells"])
                x7 = source["components"][ONE - inside_index]
                for transform_name in TRANSFORM_NAMES_A25697E4:
                    if _apply_transform_a25697e4(x6, transform_name) != x3:
                        continue
                    x8 = _apply_transform_a25697e4(x5, transform_name)
                    for x9 in x8:
                        for x10 in anchor["complement"]:
                            x11 = (x10[ZERO] - x9[ZERO], x10[ONE] - x9[ONE])
                            x12 = _shift_patch_a25697e4(x8, x11)
                            x13 = frozenset(
                                y0
                                for y0 in x12
                                if anchor["bbox"][ZERO] <= y0[ZERO] <= anchor["bbox"][TWO]
                                and anchor["bbox"][ONE] <= y0[ONE] <= anchor["bbox"][THREE]
                            )
                            if not anchor["complement"].issubset(x12):
                                continue
                            if len(x12 & anchor["union"]) > ZERO:
                                continue
                            if x13 != anchor["complement"]:
                                continue
                            if any(
                                not (ZERO <= y0[ZERO] < x1[ZERO] and ZERO <= y0[ONE] < x1[ONE])
                                for y0 in x12
                            ):
                                continue
                            if len(x12 & x4) > ZERO:
                                continue
                            x14 = part["color"]
                            x15 = x7["color"]
                            if transform_name in REFLECTION_NAMES_A25697E4:
                                x14, x15 = x15, x14
                            x16 = {
                                "anchor_index": anchor["index"],
                                "source_index": source["index"],
                                "source_component_indices": source["component_indices"],
                                "anchor_component_indices": anchor["component_indices"],
                                "inside_component_index": inside_index,
                                "transform_name": transform_name,
                                "offset": x11,
                                "union": x12,
                                "inside_patch": anchor["complement"],
                                "outside_patch": x12 - anchor["complement"],
                                "inside_color": x14,
                                "outside_color": x15,
                                "sort_key": (
                                    *anchor["bbox"],
                                    *source["bbox"],
                                    TRANSFORM_NAMES_A25697E4.index(transform_name),
                                    inside_index,
                                ),
                            }
                            x2.append(x16)
    x17 = {}
    for item in x2:
        x18 = (
            item["anchor_index"],
            item["source_index"],
            item["inside_component_index"],
            item["transform_name"],
            item["offset"],
        )
        x17[x18] = item
    return tuple(sorted(x17.values(), key=lambda item: item["sort_key"]))


def _better_selection_a25697e4(
    a: tuple[dict, ...],
    b: tuple[dict, ...],
) -> Boolean:
    if len(a) != len(b):
        return len(a) > len(b)
    x0 = tuple(item["sort_key"] for item in a)
    x1 = tuple(item["sort_key"] for item in b)
    return x0 < x1


def _select_pairings_a25697e4(
    candidates: tuple[dict, ...],
    anchors: tuple[dict, ...],
    sources: tuple[dict, ...],
) -> tuple[dict, ...]:
    del anchors, sources
    x0 = {}
    for item in candidates:
        x0.setdefault(item["anchor_index"], []).append(item)
    x1 = tuple(sorted(x0))

    def search(
        pos: Integer,
        used_sources: frozenset,
        occupied: Indices,
    ) -> tuple[dict, ...]:
        if pos == len(x1):
            return ()
        x2 = x1[pos]
        x3 = search(pos + ONE, used_sources, occupied)
        for item in x0[x2]:
            if item["source_index"] in used_sources:
                continue
            if len(item["union"] & occupied) > ZERO:
                continue
            x4 = (item,) + search(
                pos + ONE,
                used_sources | frozenset({item["source_index"]}),
                occupied | item["union"],
            )
            if _better_selection_a25697e4(x4, x3):
                x3 = x4
        return x3

    x5 = search(ZERO, frozenset(), frozenset())
    x6 = frozenset(item["anchor_index"] for item in candidates)
    x7 = frozenset(item["source_index"] for item in candidates)
    if len(x5) != min(len(x6), len(x7)):
        raise ValueError("unable to resolve all source-anchor pairings")
    return tuple(sorted(x5, key=lambda item: item["sort_key"]))


def relocate_cluster_pairs_a25697e4(
    I: Grid,
) -> Grid:
    x0 = mostcolor(I)
    x1 = _component_records_a25697e4(I)
    x2 = _anchor_candidates_a25697e4(x1)
    x3 = _source_candidates_a25697e4(x1)
    x4 = _pair_candidates_a25697e4(I, x1, x2, x3)
    x5 = _select_pairings_a25697e4(x4, x2, x3)
    x6 = I
    x7 = {item["index"]: item for item in x3}
    for item in x5:
        x8 = x7[item["source_index"]]["union"]
        x6 = fill(x6, x0, x8)
    for item in x5:
        x6 = fill(x6, item["inside_color"], item["inside_patch"])
        x6 = fill(x6, item["outside_color"], item["outside_patch"])
    return x6


def _padded_rect_a25697e4(
    bbox: tuple[Integer, Integer, Integer, Integer],
    height_value: Integer,
    width_value: Integer,
    padding: Integer,
) -> Indices:
    return frozenset(
        (i, j)
        for i in range(max(ZERO, bbox[ZERO] - padding), min(height_value - ONE, bbox[TWO] + padding) + ONE)
        for j in range(max(ZERO, bbox[ONE] - padding), min(width_value - ONE, bbox[THREE] + padding) + ONE)
    )


def _place_cluster_a25697e4(
    patches: tuple[Indices, ...],
    height_value: Integer,
    width_value: Integer,
    blocked: Indices,
) -> tuple[tuple[Indices, ...], Indices] | None:
    x0 = frozenset().union(*patches)
    x1 = _bbox_a25697e4(x0)
    x2 = x1[TWO] - x1[ZERO] + ONE
    x3 = x1[THREE] - x1[ONE] + ONE
    x4 = tuple(_shift_patch_a25697e4(patch, (-x1[ZERO], -x1[ONE])) for patch in patches)
    for _ in range(200):
        x5 = randint(ZERO, height_value - x2)
        x6 = randint(ZERO, width_value - x3)
        x7 = tuple(_shift_patch_a25697e4(patch, (x5, x6)) for patch in x4)
        x8 = frozenset().union(*x7)
        x9 = _padded_rect_a25697e4(_bbox_a25697e4(x8), height_value, width_value, TWO)
        if len(x9 & blocked) > ZERO:
            continue
        return x7, blocked | x9
    return None


def _paint_template_a25697e4(
    grid: Grid,
    anchor_color: Integer,
    source_colors: tuple[Integer, Integer],
    anchor_patches: tuple[Indices, ...],
    source_parts: tuple[dict, ...],
) -> Grid:
    x0 = grid
    for patch in anchor_patches:
        x0 = fill(x0, anchor_color, patch)
    for index, part in enumerate(source_parts):
        x0 = fill(x0, source_colors[index], part["patch"])
    return x0


def generate_template_input_a25697e4(
    diff_lb: float,
    diff_ub: float,
) -> Grid:
    del diff_lb, diff_ub
    x0 = choice(tuple(range(TEN)))
    x1 = tuple(value for value in range(TEN) if value != x0)
    x2 = [choice(PAIR_TEMPLATES_A25697E4)]
    x3 = tuple(sample(x1, THREE))
    x4 = choice((18, 25, 30))
    x5 = choice((18, 25, 30))
    x6 = max(x4, 18)
    x7 = max(x5, 18)
    for _ in range(200):
        x8 = canvas(x0, (x6, x7))
        x9 = frozenset()
        x10 = ZERO
        for item in x2:
            x11 = _place_cluster_a25697e4(item["anchor_components"], x6, x7, x9)
            if x11 is None:
                break
            x12, x9 = x11
            x13 = tuple(part["patch"] for part in item["source_components"])
            x14 = _place_cluster_a25697e4(x13, x6, x7, x9)
            if x14 is None:
                break
            x15, x9 = x14
            x16 = x3[x10]
            x17 = (x3[x10 + ONE], x3[x10 + TWO])
            x18 = tuple(
                {"label": part["label"], "patch": x15[index]}
                for index, part in enumerate(item["source_components"])
            )
            x8 = _paint_template_a25697e4(x8, x16, x17, x12, x18)
            x10 += THREE
        else:
            return x8
    raise RuntimeError("failed to place motif templates")
