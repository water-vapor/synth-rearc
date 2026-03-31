from __future__ import annotations

from synth_rearc.core import *


TRANSFORMS_5545F144 = (
    "id",
    "hmirror",
    "vmirror",
    "rot90",
    "rot180",
    "rot270",
    "dmirror",
    "cmirror",
)


_SOUTH_MOTIFS_5545F144 = {
    "vee3": frozenset({(0, 0), (1, -1), (1, 1)}),
    "tee4": frozenset({(0, 0), (1, -1), (1, 0), (1, 1)}),
    "fork4": frozenset({(0, 0), (1, 0), (2, -1), (2, 1)}),
    "hex6": frozenset({(0, 0), (1, -1), (1, 0), (1, 1), (2, -1), (2, 1)}),
}

_EAST_MOTIFS_5545F144 = {
    "vee3": frozenset({(0, 0), (-1, 1), (1, 1)}),
    "tee4": frozenset({(-1, 1), (0, 0), (0, 1), (1, 1)}),
    "fork4": frozenset({(-1, 2), (0, 0), (0, 1), (1, 2)}),
    "hex6": frozenset({(-1, 1), (-1, 2), (0, 0), (0, 1), (1, 1), (1, 2)}),
}


def motif_names_5545f144() -> tuple[str, ...]:
    return tuple(_SOUTH_MOTIFS_5545F144)


def _normalize_patch_5545f144(
    patch: Indices,
) -> Indices:
    if len(patch) == ZERO:
        return patch
    x0 = min(i for i, _ in patch)
    x1 = min(j for _, j in patch)
    return frozenset((i - x0, j - x1) for i, j in patch)


def transform_patch_5545f144(
    patch: Indices,
    transform_name: str,
) -> Indices:
    x0 = _normalize_patch_5545f144(patch)
    x1 = max(i for i, _ in x0) + ONE
    x2 = max(j for _, j in x0) + ONE
    if transform_name == "id":
        return x0
    if transform_name == "hmirror":
        return frozenset((x1 - ONE - i, j) for i, j in x0)
    if transform_name == "vmirror":
        return frozenset((i, x2 - ONE - j) for i, j in x0)
    if transform_name == "rot90":
        return frozenset((j, x1 - ONE - i) for i, j in x0)
    if transform_name == "rot180":
        return frozenset((x1 - ONE - i, x2 - ONE - j) for i, j in x0)
    if transform_name == "rot270":
        return frozenset((x2 - ONE - j, i) for i, j in x0)
    if transform_name == "dmirror":
        return frozenset((j, i) for i, j in x0)
    if transform_name == "cmirror":
        return frozenset((x2 - ONE - j, x1 - ONE - i) for i, j in x0)
    raise ValueError(transform_name)


def shift_patch_5545f144(
    patch: Indices,
    offset: IntegerTuple,
) -> Indices:
    x0, x1 = offset
    return frozenset((i + x0, j + x1) for i, j in patch)


def patch_dims_5545f144(
    patch: Indices,
) -> IntegerTuple:
    x0 = _normalize_patch_5545f144(patch)
    return max(i for i, _ in x0) + ONE, max(j for _, j in x0) + ONE


def in_bounds_5545f144(
    patch: Indices,
    dims: IntegerTuple,
) -> Boolean:
    x0, x1 = dims
    return all(ZERO <= i < x0 and ZERO <= j < x1 for i, j in patch)


def relative_motif_5545f144(
    direction: str,
    motif_name: str,
) -> Indices:
    if direction == "S":
        return _SOUTH_MOTIFS_5545F144[motif_name]
    if direction == "N":
        return frozenset((-i, j) for i, j in _SOUTH_MOTIFS_5545F144[motif_name])
    if direction == "E":
        return _EAST_MOTIFS_5545F144[motif_name]
    if direction == "W":
        return frozenset((i, -j) for i, j in _EAST_MOTIFS_5545F144[motif_name])
    raise ValueError(direction)


def canonical_patch_5545f144(
    direction: str,
    motif_name: str,
    anchor: IntegerTuple,
) -> Indices:
    x0, x1 = anchor
    return frozenset((add(x0, i), add(x1, j)) for i, j in relative_motif_5545f144(direction, motif_name))


def split_panels_5545f144(
    grid: Grid,
) -> tuple[Integer, tuple[Grid, ...]]:
    x0 = mostcolor(grid)
    x1 = width(grid)
    x2 = tuple(
        x3
        for x3 in range(x1)
        if both(
            all(index(grid, (x4, x3)) == index(grid, (ZERO, x3)) for x4 in range(height(grid))),
            index(grid, (ZERO, x3)) != x0,
        )
    )
    if len(x2) == ZERO:
        return x0, (grid,)
    x3 = (-ONE,) + x2 + (x1,)
    x4 = []
    for x5, x6 in zip(x3, x3[1:]):
        x4.append(tuple(row[x5 + ONE : x6] for row in grid))
    return x0, tuple(x4)


def panel_components_5545f144(
    panel: Grid,
) -> tuple[Indices, ...]:
    x0 = tuple(toindices(x1) for x1 in objects(panel, T, T, T))
    return tuple(sorted(x0, key=lambda x2: (len(x2), ulcorner(x2)), reverse=T))


def main_component_5545f144(
    panel: Grid,
) -> Indices:
    x0 = tuple(x1 for x1 in panel_components_5545f144(panel) if len(x1) > ONE)
    if len(x0) == ZERO:
        raise ValueError("expected a nontrivial component")
    x1 = max(len(x2) for x2 in x0)
    x2 = tuple(x3 for x3 in x0 if len(x3) == x1)
    return min(x2, key=ulcorner)


def singleton_cells_5545f144(
    panel: Grid,
) -> frozenset[IntegerTuple]:
    x0 = tuple(x1 for x1 in panel_components_5545f144(panel) if len(x1) == ONE)
    return frozenset(next(iter(x1)) for x1 in x0)


def nearest_singleton_5545f144(
    anchor_candidates: frozenset[IntegerTuple],
    patch: Indices,
) -> IntegerTuple:
    return min(
        anchor_candidates,
        key=lambda x0: (
            min(abs(x0[0] - x1[0]) + abs(x0[1] - x1[1]) for x1 in patch),
            x0,
        ),
    )


def choose_direction_5545f144(
    anchor: IntegerTuple,
    other_anchors: tuple[IntegerTuple, ...],
    main_components: tuple[Indices, ...],
) -> str:
    if len(other_anchors) > ZERO:
        x0 = (
            sum(x1[0] - anchor[0] for x1 in other_anchors) / len(other_anchors),
            sum(x1[1] - anchor[1] for x1 in other_anchors) / len(other_anchors),
        )
    else:
        x0 = (
            sum(sum(i for i, _ in x1) / len(x1) - anchor[0] for x1 in main_components) / len(main_components),
            sum(sum(j for _, j in x1) / len(x1) - anchor[1] for x1 in main_components) / len(main_components),
        )
    x1, x2 = x0
    if abs(x1) >= abs(x2):
        return "S" if x1 > ZERO else "N"
    return "E" if x2 > ZERO else "W"


def border_cells_5545f144(
    patch: Indices,
    direction: str,
) -> frozenset[IntegerTuple]:
    x0 = _normalize_patch_5545f144(patch)
    if direction == "S":
        x1 = min(i for i, _ in x0)
        return frozenset(x2 for x2 in x0 if x2[0] == x1)
    if direction == "N":
        x1 = max(i for i, _ in x0)
        return frozenset(x2 for x2 in x0 if x2[0] == x1)
    if direction == "E":
        x1 = min(j for _, j in x0)
        return frozenset(x2 for x2 in x0 if x2[1] == x1)
    x1 = max(j for _, j in x0)
    return frozenset(x2 for x2 in x0 if x2[1] == x1)


def direction_ok_5545f144(
    patch: Indices,
    anchor_cell: IntegerTuple,
    direction: str,
) -> Boolean:
    x0 = sum(i for i, _ in patch) / len(patch) - anchor_cell[0]
    x1 = sum(j for _, j in patch) / len(patch) - anchor_cell[1]
    if direction == "S":
        return x0 > ZERO
    if direction == "N":
        return x0 < ZERO
    if direction == "E":
        return x1 > ZERO
    return x1 < ZERO


def panel_variants_5545f144(
    patch: Indices,
    anchor: IntegerTuple,
    direction: str,
    dims: IntegerTuple,
) -> tuple[Indices, ...]:
    x0 = []
    for x1 in TRANSFORMS_5545F144:
        x2 = transform_patch_5545f144(patch, x1)
        for x3 in border_cells_5545f144(x2, direction):
            if not direction_ok_5545f144(x2, x3, direction):
                continue
            x4 = shift_patch_5545f144(x2, (anchor[0] - x3[0], anchor[1] - x3[1]))
            if in_bounds_5545f144(x4, dims):
                x0.append(x4)
    return tuple(dict.fromkeys(x0))


def symmetry_penalty_5545f144(
    patch: Indices,
    anchor: IntegerTuple,
    direction: str,
) -> Integer:
    if direction in ("S", "N"):
        x0 = frozenset((i, subtract(double(anchor[1]), j)) for i, j in patch)
    else:
        x0 = frozenset((subtract(double(anchor[0]), i), j) for i, j in patch)
    return len(patch ^ x0)


def select_patch_5545f144(
    dims: IntegerTuple,
    main_components: tuple[Indices, ...],
    anchor_sets: tuple[frozenset[IntegerTuple], ...],
) -> Indices:
    if len(main_components) == ONE:
        x0 = nearest_singleton_5545f144(anchor_sets[ZERO], main_components[ZERO])
        x1 = choose_direction_5545f144(x0, (), main_components)
        x2 = panel_variants_5545f144(main_components[ZERO], x0, x1, dims)
        x3 = min(
            x2,
            key=lambda x4: (
                symmetry_penalty_5545f144(x4, x0, x1),
                tuple(sorted(x4)),
            ),
        )
        return x3
    x0 = frozenset.intersection(*anchor_sets)
    x1 = frozenset(x2 for x2 in x0 if all(x2 not in x3 for x3 in main_components))
    if len(x1) == ZERO:
        x1 = x0
    x2 = []
    for x3 in sorted(x1):
        x4 = tuple(sorted(x1 - {x3}))
        x5 = choose_direction_5545f144(x3, x4, main_components)
        x6 = tuple(panel_variants_5545f144(x7, x3, x5, dims) for x7 in main_components)
        x7 = frozenset().union(*x6)
        for x8 in x7:
            x9 = sum(min(len(x8 ^ x10) for x10 in x11) for x11 in x6)
            x10 = symmetry_penalty_5545f144(x8, x3, x5)
            x2.append((x9, x10, tuple(sorted(x8)), x8))
    return min(x2)[-1]


def render_patch_5545f144(
    dims: IntegerTuple,
    bg: Integer,
    fg: Integer,
    patch: Indices,
) -> Grid:
    x0 = canvas(bg, dims)
    return fill(x0, fg, patch)


def render_output_5545f144(
    grid: Grid,
) -> Grid:
    x0, x1 = split_panels_5545f144(grid)
    x2 = tuple(main_component_5545f144(x3) for x3 in x1)
    x3 = tuple(singleton_cells_5545f144(x4) for x4 in x1)
    x4 = shape(x1[ZERO])
    x5 = select_patch_5545f144(x4, x2, x3)
    x6 = other(palette(x1[ZERO]), x0)
    return render_patch_5545f144(x4, x0, x6, x5)
