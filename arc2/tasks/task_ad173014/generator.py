from arc2.core import *

from .helpers import (
    BOX_COLORS_AD173014,
    MOTIF_LIBRARY_3_AD173014,
    MOTIF_LIBRARY_5_AD173014,
    anchor_ad173014,
    elbow_path_ad173014,
    order_boxes_ad173014,
    paint_box_ad173014,
)
from .verifier import verify_ad173014


def _family_trb_ad173014(
    size_value: Integer,
) -> tuple[dict, ...]:
    return (
        {"slot": "top", "top": ZERO, "left": size_value + 1 + choice((ZERO, ONE)), "size": size_value},
        {"slot": "right", "top": size_value + 1 + choice((ZERO, ONE)), "left": 2 * size_value + 3 + choice((ZERO, ONE, TWO)), "size": size_value},
        {"slot": "bottom", "top": 2 * size_value + 2 + choice((ZERO, ONE)), "left": size_value + 2 + choice((ZERO, ONE, TWO)), "size": size_value},
    )


def _family_tlr_ad173014(
    size_value: Integer,
) -> tuple[dict, ...]:
    return (
        {"slot": "top", "top": ZERO, "left": size_value + 1 + choice((ZERO, ONE, TWO)), "size": size_value},
        {"slot": "left", "top": size_value + 2 + choice((ZERO, ONE, TWO)), "left": ZERO, "size": size_value},
        {"slot": "right", "top": size_value + 1 + choice((ZERO, ONE)), "left": 2 * size_value + 2 + choice((ZERO, ONE, TWO)), "size": size_value},
    )


def _family_tlbr_ad173014(
    size_value: Integer,
) -> tuple[dict, ...]:
    return (
        {"slot": "top", "top": ZERO, "left": size_value + 2 + choice((ZERO, ONE)), "size": size_value},
        {"slot": "left", "top": size_value + 2 + choice((ZERO, ONE)), "left": ZERO, "size": size_value},
        {"slot": "bottom", "top": 2 * size_value + 5 + choice((ZERO, ONE)), "left": size_value + 1 + choice((ZERO, ONE)), "size": size_value},
        {"slot": "right", "top": size_value + 2 + choice((ZERO, ONE)), "left": 2 * size_value + 4 + choice((ZERO, ONE)), "size": size_value},
    )


def _family_tlbrtr_ad173014(
    size_value: Integer,
) -> tuple[dict, ...]:
    return (
        {"slot": "top_left", "top": ZERO, "left": size_value - ONE + choice((ZERO, ONE)), "size": size_value},
        {"slot": "left", "top": size_value + 2 + choice((ZERO, ONE, TWO)), "left": ZERO, "size": size_value},
        {"slot": "bottom", "top": 2 * size_value + 5 + choice((ZERO, ONE)), "left": size_value + 3 + choice((ZERO, ONE, TWO)), "size": size_value},
        {"slot": "right", "top": size_value + 2 + choice((ZERO, ONE)), "left": 2 * size_value + 4 + choice((ZERO, ONE)), "size": size_value},
        {"slot": "top_right", "top": ZERO, "left": 2 * size_value + ONE + choice((ZERO, ONE)), "size": size_value},
    )


def _translated_boxes_ad173014(
    box_specs: tuple[dict, ...],
) -> tuple[dict, ...]:
    scaffold = _scaffold_patch_ad173014(box_specs)
    rows = [box_spec["top"] for box_spec in box_specs] + [box_spec["top"] + box_spec["size"] - ONE for box_spec in box_specs]
    cols = [box_spec["left"] for box_spec in box_specs] + [box_spec["left"] + box_spec["size"] - ONE for box_spec in box_specs]
    if len(scaffold) > ZERO:
        rows.extend(i for i, _ in scaffold)
        cols.extend(j for _, j in scaffold)
    min_i = min(rows)
    max_i = max(rows)
    min_j = min(cols)
    max_j = max(cols)
    offset_i = randint(-min_i, 29 - max_i)
    offset_j = randint(-min_j, 29 - max_j)
    translated = []
    for box_spec in box_specs:
        translated.append(
            {
                **box_spec,
                "top": box_spec["top"] + offset_i,
                "left": box_spec["left"] + offset_j,
            }
        )
    return tuple(translated)


def _box_by_slot_ad173014(
    box_specs: tuple[dict, ...],
    slot_name: str,
) -> dict | None:
    for box_spec in box_specs:
        if box_spec["slot"] == slot_name:
            return box_spec
    return None


def _scaffold_patch_ad173014(
    box_specs: tuple[dict, ...],
) -> Indices:
    top_box = _box_by_slot_ad173014(box_specs, "top")
    top_left_box = _box_by_slot_ad173014(box_specs, "top_left")
    top_right_box = _box_by_slot_ad173014(box_specs, "top_right")
    left_box = _box_by_slot_ad173014(box_specs, "left")
    bottom_box = _box_by_slot_ad173014(box_specs, "bottom")
    right_box = _box_by_slot_ad173014(box_specs, "right")
    patch = frozenset()
    if top_left_box is not None and left_box is not None:
        a = anchor_ad173014(top_left_box, "left")
        b = anchor_ad173014(left_box, "top")
        patch = combine(patch, elbow_path_ad173014(a, b, (a[0], b[1])))
    if top_box is not None and left_box is not None:
        a = anchor_ad173014(top_box, "left")
        b = anchor_ad173014(left_box, "top")
        patch = combine(patch, elbow_path_ad173014(a, b, (a[0], b[1])))
    if left_box is not None and bottom_box is not None:
        a = anchor_ad173014(left_box, "bottom")
        b = anchor_ad173014(bottom_box, "left")
        patch = combine(patch, elbow_path_ad173014(a, b, (b[0], a[1])))
    if bottom_box is not None and right_box is not None:
        a = anchor_ad173014(bottom_box, "right")
        b = anchor_ad173014(right_box, "bottom")
        patch = combine(patch, elbow_path_ad173014(a, b, (a[0], b[1])))
    if right_box is not None and top_box is not None:
        a = anchor_ad173014(right_box, "top")
        b = anchor_ad173014(top_box, "right")
        patch = combine(patch, elbow_path_ad173014(a, b, (b[0], a[1])))
    if right_box is not None and top_right_box is not None:
        a = anchor_ad173014(right_box, "top")
        b = anchor_ad173014(top_right_box, "bottom")
        patch = combine(patch, elbow_path_ad173014(a, b, (b[0], a[1])))
    if top_left_box is not None and top_right_box is not None:
        a = anchor_ad173014(top_left_box, "right")
        b = anchor_ad173014(top_right_box, "left")
        patch = combine(patch, connect(a, b))
    if top_box is not None and bottom_box is not None and left_box is None:
        a = anchor_ad173014(top_box, "left")
        b = anchor_ad173014(bottom_box, "left")
        outer_col = min(a[1], b[1]) - ONE
        patch = combine(patch, connect(a, (a[0], outer_col)))
        patch = combine(patch, connect((a[0], outer_col), (b[0], outer_col)))
        patch = combine(patch, connect((b[0], outer_col), b))
    if left_box is not None and right_box is not None and bottom_box is None:
        a = anchor_ad173014(left_box, "bottom")
        b = anchor_ad173014(right_box, "bottom")
        outer_row = max(a[0], b[0]) + ONE
        patch = combine(patch, connect(a, (outer_row, a[1])))
        patch = combine(patch, connect((outer_row, a[1]), (outer_row, b[1])))
        patch = combine(patch, connect((outer_row, b[1]), b))
    return patch


def _motif_library_for_size_ad173014(
    size_value: Integer,
) -> tuple[Indices, ...]:
    if size_value == FIVE:
        return MOTIF_LIBRARY_3_AD173014
    return MOTIF_LIBRARY_5_AD173014


def _paint_example_ad173014(
    box_specs: tuple[dict, ...],
    dims: IntegerTuple,
) -> dict:
    ordered = order_boxes_ad173014(box_specs)
    input_grid = canvas(ZERO, dims)
    input_grid = fill(input_grid, ONE, _scaffold_patch_ad173014(box_specs))
    for box_spec in box_specs:
        input_grid = paint_box_ad173014(input_grid, box_spec)
    output_grid = fill(canvas(ZERO, dims), ONE, _scaffold_patch_ad173014(box_specs))
    rotated_colors = (ordered[-ONE]["color"],) + tuple(box_spec["color"] for box_spec in ordered[:-ONE])
    replacement = {id(box_spec): rotated_colors[idx] for idx, box_spec in enumerate(ordered)}
    for box_spec in box_specs:
        output_grid = paint_box_ad173014(output_grid, {**box_spec, "color": replacement[id(box_spec)]})
    return {"input": input_grid, "output": output_grid}


def generate_ad173014(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    del diff_lb, diff_ub
    families = (
        _family_trb_ad173014,
        _family_tlr_ad173014,
        _family_tlbr_ad173014,
        _family_tlbrtr_ad173014,
    )
    while True:
        size_value = choice((FIVE, SEVEN))
        base_boxes = choice(families)(size_value)
        box_specs = _translated_boxes_ad173014(base_boxes)
        colors = tuple(sample(BOX_COLORS_AD173014, len(box_specs)))
        motifs = tuple(sample(_motif_library_for_size_ad173014(size_value), len(box_specs)))
        complete_boxes = tuple(
            {
                **box_spec,
                "color": colors[idx],
                "motif": motifs[idx],
            }
            for idx, box_spec in enumerate(box_specs)
        )
        scaffold = _scaffold_patch_ad173014(complete_boxes)
        max_i = max(
            [box_spec["top"] + box_spec["size"] - ONE for box_spec in complete_boxes]
            + [i for i, _ in scaffold]
        )
        max_j = max(
            [box_spec["left"] + box_spec["size"] - ONE for box_spec in complete_boxes]
            + [j for _, j in scaffold]
        )
        dims = (max_i + ONE, max_j + ONE)
        example = _paint_example_ad173014(complete_boxes, dims)
        if example["input"] == example["output"]:
            continue
        if verify_ad173014(example["input"]) != example["output"]:
            continue
        return example
