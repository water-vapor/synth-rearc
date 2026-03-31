from __future__ import annotations

from synth_rearc.core import *

from .helpers import (
    TRANSFORMS_5545F144,
    canonical_patch_5545f144,
    in_bounds_5545f144,
    motif_names_5545f144,
    panel_variants_5545f144,
    patch_dims_5545f144,
    relative_motif_5545f144,
    render_patch_5545f144,
    render_output_5545f144,
    shift_patch_5545f144,
    transform_patch_5545f144,
)


def _direction_vector_5545f144(
    direction: str,
) -> IntegerTuple:
    return {
        "N": UP,
        "S": DOWN,
        "E": RIGHT,
        "W": LEFT,
    }[direction]


def _anchor_bounds_5545f144(
    direction: str,
    motif_name: str,
    dims: IntegerTuple,
) -> tuple[tuple[Integer, Integer], tuple[Integer, Integer]]:
    x0 = relative_motif_5545f144(direction, motif_name)
    x1 = min(i for i, _ in x0)
    x2 = max(i for i, _ in x0)
    x3 = min(j for _, j in x0)
    x4 = max(j for _, j in x0)
    x5, x6 = dims
    return (
        (subtract(ZERO, x1), subtract(subtract(x5, ONE), x2)),
        (subtract(ZERO, x3), subtract(subtract(x6, ONE), x4)),
    )


def _common_anchors_5545f144(
    direction: str,
    anchor: IntegerTuple,
    patch: Indices,
    dims: IntegerTuple,
) -> tuple[IntegerTuple, ...]:
    x0 = []
    x1, x2 = _direction_vector_5545f144(direction)
    x3 = max(i for i, _ in patch)
    x4 = min(i for i, _ in patch)
    x5 = max(j for _, j in patch)
    x6 = min(j for _, j in patch)
    if direction == "S":
        x7 = subtract(dims[0], add(x3, TWO))
    elif direction == "N":
        x7 = subtract(x4, ONE)
    elif direction == "E":
        x7 = subtract(dims[1], add(x5, TWO))
    else:
        x7 = subtract(x6, ONE)
    x8 = choice((ONE, ONE, TWO))
    for x9 in range(x8):
        x10 = add(TWO, x9 * TWO)
        if x10 > x7:
            break
        x11 = add(anchor[0], x1 * x10)
        x12 = add(anchor[1], x2 * x10)
        if ZERO <= x11 < dims[0] and ZERO <= x12 < dims[1]:
            x0.append((x11, x12))
    return tuple(x0)


def _placement_candidates_5545f144(
    patch: Indices,
    anchor: IntegerTuple,
    direction: str,
    dims: IntegerTuple,
    forbidden: Indices,
) -> tuple[Indices, ...]:
    x0 = patch_dims_5545f144(patch)
    x1, x2 = dims
    x2a = set(forbidden)
    for x2b in forbidden:
        x2a |= neighbors(x2b)
    x3 = []
    for x4 in range(add(x1, ONE - x0[0])):
        for x5 in range(add(x2, ONE - x0[1])):
            x6 = shift_patch_5545f144(patch, (x4, x5))
            if x6 & x2a:
                continue
            if direction == "S" and sum(i for i, _ in x6) / len(x6) <= anchor[0]:
                continue
            if direction == "N" and sum(i for i, _ in x6) / len(x6) >= anchor[0]:
                continue
            if direction == "E" and sum(j for _, j in x6) / len(x6) <= anchor[1]:
                continue
            if direction == "W" and sum(j for _, j in x6) / len(x6) >= anchor[1]:
                continue
            x3.append(x6)
    shuffle(x3)
    return tuple(x3)


def _add_singletons_5545f144(
    patch: Indices,
    occupied: Indices,
    dims: IntegerTuple,
    count: Integer,
) -> Indices:
    x0 = set(patch)
    x1 = set(occupied)
    for x2 in occupied:
        x1 |= neighbors(x2)
    x2 = [(i, j) for i in range(dims[0]) for j in range(dims[1])]
    shuffle(x2)
    for x3 in x2:
        if len(x0) >= add(len(patch), count):
            break
        if x3 in x1:
            continue
        x0.add(x3)
        x1.add(x3)
        x1 |= neighbors(x3)
    return frozenset(x0)


def _attached_noise_5545f144(
    patch: Indices,
    occupied: Indices,
    dims: IntegerTuple,
) -> Indices:
    x0 = set(occupied)
    x0 -= set(patch)
    x1 = []
    for x2 in patch:
        for x3 in neighbors(x2):
            if not (ZERO <= x3[0] < dims[0] and ZERO <= x3[1] < dims[1]):
                continue
            if x3 in occupied:
                continue
            x1.append(x3)
    if len(x1) == ZERO:
        return patch
    return patch | {choice(x1)}


def _compose_multi_input_5545f144(
    panels: tuple[Grid, ...],
    separator_color: Integer,
) -> Grid:
    x0 = []
    for x1, x2 in enumerate(panels):
        if x1:
            x3 = tuple((separator_color,) for _ in range(height(x2)))
            x0.append(x3)
        x0.append(x2)
    return x0[ZERO] if len(x0) == ONE else mpapply(combine, x0[:-ONE], x0[ONE:])[-ONE]


def _hconcat_panels_5545f144(
    panels: tuple[Grid, ...],
    separator_color: Integer,
) -> Grid:
    x0 = panels[ZERO]
    x1 = canvas(separator_color, astuple(height(x0), ONE))
    for x2 in panels[ONE:]:
        x0 = hconcat(x0, x1)
        x0 = hconcat(x0, x2)
    return x0


def _single_case_5545f144(
    bg: Integer,
    fg: Integer,
    direction: str,
    motif_name: str,
) -> dict:
    x0 = randint(EIGHT, add(TEN, THREE))
    x1 = randint(EIGHT, add(TEN, THREE))
    x2 = astuple(x0, x1)
    x3, x4 = _anchor_bounds_5545f144(direction, motif_name, x2)
    x5 = astuple(randint(x3[0], x3[1]), randint(x4[0], x4[1]))
    x6 = canonical_patch_5545f144(direction, motif_name, x5)
    x7 = choice(TRANSFORMS_5545F144)
    x8 = transform_patch_5545f144(x6, x7)
    x9 = frozenset({x5})
    x10 = _placement_candidates_5545f144(x8, x5, direction, x2, x9)
    if len(x10) == ZERO:
        raise ValueError("no single-panel placement")
    x11 = x10[ZERO]
    x12 = _add_singletons_5545f144(x11, x9 | x11, x2, randint(TWO, FIVE))
    x13 = render_patch_5545f144(x2, bg, fg, x12 | {x5})
    x14 = render_patch_5545f144(x2, bg, fg, x6)
    return {"input": x13, "output": x14}


def _multi_case_5545f144(
    bg: Integer,
    fg: Integer,
    separator_color: Integer,
    direction: str,
    motif_name: str,
) -> dict:
    x0 = choice((TWO, THREE, FOUR))
    x1 = randint(EIGHT, add(TEN, THREE))
    x2 = randint(SIX, (30 - (x0 - ONE)) // x0)
    x3 = astuple(x1, x2)
    x4, x5 = _anchor_bounds_5545f144(direction, motif_name, x3)
    x6 = astuple(randint(x4[0], x4[1]), randint(x5[0], x5[1]))
    x7 = canonical_patch_5545f144(direction, motif_name, x6)
    x8 = _common_anchors_5545f144(direction, x6, x7, x3)
    x9 = frozenset({x6} | set(x8))
    x10 = tuple(
        transform_patch_5545f144(x7, choice(TRANSFORMS_5545F144))
        for _ in range(x0)
    )
    x11 = randint(ZERO, subtract(x0, ONE))
    x12 = []
    for x13, x14 in enumerate(x10):
        x15 = _placement_candidates_5545f144(x14, x6, direction, x3, x9)
        if len(x15) == ZERO:
            raise ValueError("no multi-panel placement")
        x16 = x15[ZERO]
        if both(x13 == x11, choice((T, F))):
            x16 = _attached_noise_5545f144(x16, x9 | x16, x3)
        x17 = _add_singletons_5545f144(x16, x9 | x16, x3, randint(ONE, FOUR))
        x18 = render_patch_5545f144(x3, bg, fg, x17 | x9)
        x12.append(x18)
    x13 = _hconcat_panels_5545f144(tuple(x12), separator_color)
    x14 = render_patch_5545f144(x3, bg, fg, x7)
    return {"input": x13, "output": x14}


def generate_5545f144(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    del diff_lb, diff_ub
    while True:
        x0 = sample(range(TEN), THREE)
        x1, x2 = x0[:TWO]
        x3 = x0[TWO]
        x4 = choice(("S", "S", "N", "E", "W"))
        x5 = choice(motif_names_5545f144())
        try:
            if choice((T, T, F)):
                x6 = _multi_case_5545f144(x1, x2, x3, x4, x5)
            else:
                x6 = _single_case_5545f144(x1, x2, x4, x5)
        except ValueError:
            continue
        try:
            x7 = render_output_5545f144(x6["input"])
        except ValueError:
            continue
        if x7 != x6["output"]:
            continue
        return x6
