import math

from synth_rearc.core import *


BOX_COLORS_AD173014 = (THREE, FOUR, SIX, SEVEN, EIGHT)

_BASE_MOTIFS_3_AD173014 = (
    frozenset({(0, 1), (1, 0), (1, 1), (1, 2), (2, 1)}),
    frozenset({(0, 1), (1, 0), (1, 2), (2, 1)}),
    frozenset({(0, 1), (1, 1), (1, 2), (2, 0)}),
    frozenset({(0, 1), (0, 2), (1, 0), (1, 1), (2, 0)}),
    frozenset({(0, 0), (0, 1), (1, 0), (1, 1), (2, 2)}),
    frozenset({(0, 1), (1, 1), (1, 2)}),
)

_BASE_MOTIFS_5_AD173014 = (
    frozenset({(0, 2), (1, 1), (1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 3)}),
    frozenset({(1, 2), (1, 3), (2, 0), (2, 1), (2, 2), (2, 4), (3, 2), (3, 3)}),
    frozenset({(1, 0), (1, 2), (2, 0), (2, 1), (2, 2), (2, 3), (3, 0), (3, 2)}),
    frozenset({(1, 1), (1, 3), (2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (3, 3), (4, 2)}),
    frozenset({(1, 1), (1, 2), (1, 3), (2, 0), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 3)}),
    frozenset({(0, 1), (1, 1), (1, 2), (2, 2), (2, 3), (3, 3), (3, 4), (4, 3)}),
    frozenset({(0, 2), (1, 0), (1, 1), (1, 2), (1, 3), (2, 2), (3, 2), (3, 3), (3, 4)}),
    frozenset({(0, 2), (1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (2, 2), (3, 2), (4, 1), (4, 2)}),
)


def _rot90_patch_ad173014(
    patch: Indices,
    size_value: Integer,
) -> Indices:
    return frozenset((j, size_value - ONE - i) for i, j in patch)


def _vmirror_patch_ad173014(
    patch: Indices,
    size_value: Integer,
) -> Indices:
    return frozenset((i, size_value - ONE - j) for i, j in patch)


def _motif_library_ad173014(
    base_patches: tuple[Indices, ...],
    size_value: Integer,
) -> tuple[Indices, ...]:
    seen = set()
    ordered = []
    for patch in base_patches:
        current = patch
        for _ in range(FOUR):
            for variant in (current, _vmirror_patch_ad173014(current, size_value)):
                key = tuple(sorted(variant))
                if key in seen:
                    continue
                seen.add(key)
                ordered.append(variant)
            current = _rot90_patch_ad173014(current, size_value)
    return tuple(ordered)


MOTIF_LIBRARY_3_AD173014 = _motif_library_ad173014(_BASE_MOTIFS_3_AD173014, THREE)
MOTIF_LIBRARY_5_AD173014 = _motif_library_ad173014(_BASE_MOTIFS_5_AD173014, FIVE)


def frame_patch_ad173014(
    top: Integer,
    left: Integer,
    size_value: Integer,
) -> Indices:
    bottom = top + size_value - ONE
    right = left + size_value - ONE
    top_edge = connect((top, left), (top, right))
    left_edge = connect((top, left), (bottom, left))
    bottom_edge = connect((bottom, left), (bottom, right))
    right_edge = connect((top, right), (bottom, right))
    return combine(combine(top_edge, left_edge), combine(bottom_edge, right_edge))


def shift_patch_ad173014(
    patch: Indices,
    offset: IntegerTuple,
) -> Indices:
    return frozenset(add(cell, offset) for cell in patch)


def anchor_ad173014(
    box_spec: dict,
    side: str,
) -> IntegerTuple:
    top = box_spec["top"]
    left = box_spec["left"]
    size_value = box_spec["size"]
    mid = size_value // TWO
    if side == "left":
        return (top + mid, left)
    if side == "right":
        return (top + mid, left + size_value - ONE)
    if side == "top":
        return (top, left + mid)
    return (top + size_value - ONE, left + mid)


def elbow_path_ad173014(
    start: IntegerTuple,
    end: IntegerTuple,
    corner: IntegerTuple,
) -> Indices:
    return combine(connect(start, corner), connect(corner, end))


def paint_box_ad173014(
    grid: Grid,
    box_spec: dict,
) -> Grid:
    frame = frame_patch_ad173014(box_spec["top"], box_spec["left"], box_spec["size"])
    motif = shift_patch_ad173014(box_spec["motif"], (box_spec["top"] + ONE, box_spec["left"] + ONE))
    painted = fill(grid, TWO, frame)
    return fill(painted, box_spec["color"], motif)


def order_boxes_ad173014(
    box_specs: tuple[dict, ...],
) -> tuple[dict, ...]:
    centers = tuple(
        (
            box_spec["top"] + box_spec["size"] // TWO,
            box_spec["left"] + box_spec["size"] // TWO,
            box_spec,
        )
        for box_spec in box_specs
    )
    center_i = sum(i for i, _, _ in centers) / len(centers)
    center_j = sum(j for _, j, _ in centers) / len(centers)
    ordered = sorted(
        centers,
        key=lambda item: math.atan2(center_j - item[1], item[0] - center_i),
        reverse=True,
    )
    return tuple(item[2] for item in ordered)
