from __future__ import annotations

from collections import Counter, defaultdict, deque

from synth_rearc.core import *


TRANSFORMS_6E4F6532 = (
    "id",
    "rot90",
    "rot180",
    "rot270",
    "hmirror",
    "vmirror",
    "dmirror",
    "cmirror",
)

TEMPLATE_SPECS_6E4F6532 = (
    {
        "name": "single_lr_wide",
        "shape_class": "single",
        "rows": (
            ".8888R",
            "L89.8.",
            ".88.R8",
            "..8...",
        ),
    },
    {
        "name": "line2_lr_tall",
        "shape_class": "line2",
        "rows": (
            "..8..",
            "..88R",
            "L889.",
            "..89.",
            "L888.",
        ),
    },
    {
        "name": "line2_lt_crown",
        "shape_class": "line2",
        "rows": (
            ".TT9TT",
            "L88988",
            "L88888",
            "....88",
        ),
    },
    {
        "name": "single_lrb_hook",
        "shape_class": "single",
        "rows": (
            "...88R",
            "L8888R",
            "L89...",
            "L8888R",
            "...8..",
            "...B..",
        ),
    },
    {
        "name": "single_tr_block",
        "shape_class": "single",
        "rows": (
            "..T.",
            "..8R",
            "888.",
            ".9..",
            "888R",
            "888R",
        ),
    },
    {
        "name": "diag2_lt_small",
        "shape_class": "diag2",
        "rows": (
            "..T.",
            ".89.",
            "L889",
            "..88",
        ),
    },
    {
        "name": "block4_lb",
        "shape_class": "block4",
        "rows": (
            "..888",
            "..998",
            "..998",
            "L888.",
            ".B.B.",
        ),
    },
    {
        "name": "single_lb_tall",
        "shape_class": "single",
        "rows": (
            "L888",
            "..88",
            ".888",
            ".898",
            ".888",
            "..88",
            "..B.",
        ),
    },
)


def normalize_patch_6e4f6532(
    patch: Patch,
) -> Indices:
    x0 = toindices(patch)
    if len(x0) == ZERO:
        return frozenset()
    x1 = min(i for i, _ in x0)
    x2 = min(j for _, j in x0)
    return frozenset((i - x1, j - x2) for i, j in x0)


def patch_dims_6e4f6532(
    patch: Patch,
) -> IntegerTuple:
    x0 = normalize_patch_6e4f6532(patch)
    return max(i for i, _ in x0) + ONE, max(j for _, j in x0) + ONE


def _transform_index_6e4f6532(
    loc: IntegerTuple,
    dims: IntegerTuple,
    transform_name: str,
) -> IntegerTuple:
    x0, x1 = loc
    x2, x3 = dims
    if transform_name == "id":
        return x0, x1
    if transform_name == "rot90":
        return x1, x2 - ONE - x0
    if transform_name == "rot180":
        return x2 - ONE - x0, x3 - ONE - x1
    if transform_name == "rot270":
        return x3 - ONE - x1, x0
    if transform_name == "hmirror":
        return x2 - ONE - x0, x1
    if transform_name == "vmirror":
        return x0, x3 - ONE - x1
    if transform_name == "dmirror":
        return x1, x0
    if transform_name == "cmirror":
        return x3 - ONE - x1, x2 - ONE - x0
    raise ValueError(transform_name)


def transform_patch_6e4f6532(
    patch: Patch,
    transform_name: str,
) -> Indices:
    x0 = normalize_patch_6e4f6532(patch)
    if len(x0) == ZERO:
        return x0
    x1 = patch_dims_6e4f6532(x0)
    x2 = frozenset(_transform_index_6e4f6532(x3, x1, transform_name) for x3 in x0)
    return normalize_patch_6e4f6532(x2)


def transform_object_6e4f6532(
    obj: Object,
    transform_name: str,
) -> Object:
    x0 = frozenset(loc for _, loc in obj)
    x1 = ulcorner(x0)
    x2 = patch_dims_6e4f6532(x0)
    x3 = frozenset(
        (x4, _transform_index_6e4f6532(subtract(x5, x1), x2, transform_name))
        for x4, x5 in obj
    )
    x6 = frozenset(loc for _, loc in x3)
    x7 = ulcorner(x6)
    return frozenset((x8, subtract(x9, x7)) for x8, x9 in x3)


def shift_patch_6e4f6532(
    patch: Patch,
    offset: IntegerTuple,
) -> Indices:
    x0, x1 = offset
    return frozenset((i + x0, j + x1) for i, j in toindices(patch))


def shift_object_6e4f6532(
    obj: Object,
    offset: IntegerTuple,
) -> Object:
    x0, x1 = offset
    return frozenset((x2, (x3 + x0, x4 + x1)) for x2, (x3, x4) in obj)


def object_cells_6e4f6532(
    obj: Object,
) -> Indices:
    return frozenset(loc for _, loc in obj)


def object_bbox_6e4f6532(
    obj: Object,
) -> tuple[Integer, Integer, Integer, Integer]:
    x0 = object_cells_6e4f6532(obj)
    return (
        min(i for i, _ in x0),
        min(j for _, j in x0),
        max(i for i, _ in x0),
        max(j for _, j in x0),
    )


def padded_patch_6e4f6532(
    patch: Patch,
    margin: Integer = ONE,
) -> Indices:
    x0 = set()
    for x1, x2 in toindices(patch):
        for x3 in range(x1 - margin, x1 + margin + ONE):
            for x4 in range(x2 - margin, x2 + margin + ONE):
                x0.add((x3, x4))
    return frozenset(x0)


def _connected_components_6e4f6532(
    patch: Patch,
    *,
    diagonal: Boolean,
) -> tuple[Indices, ...]:
    x0 = set(toindices(patch))
    x1 = []
    x2 = neighbors if diagonal else dneighbors
    while len(x0) > ZERO:
        x3 = {next(iter(x0))}
        x4 = set()
        while len(x3) > ZERO:
            x5 = x3.pop()
            if x5 not in x0:
                continue
            x0.remove(x5)
            x4.add(x5)
            x3 |= x0 & x2(x5)
        x1.append(frozenset(x4))
    return tuple(sorted(x1, key=lambda x6: (ulcorner(x6), size(x6))))


def _rect_expand_6e4f6532(
    patch: Patch,
    margin: Integer,
    dims: IntegerTuple,
) -> tuple[Integer, Integer, Integer, Integer]:
    x0 = toindices(patch)
    return (
        max(ZERO, min(i for i, _ in x0) - margin),
        max(ZERO, min(j for _, j in x0) - margin),
        min(dims[0] - ONE, max(i for i, _ in x0) + margin),
        min(dims[1] - ONE, max(j for _, j in x0) + margin),
    )


def _rectangles_intersect_6e4f6532(
    a: tuple[Integer, Integer, Integer, Integer],
    b: tuple[Integer, Integer, Integer, Integer],
) -> Boolean:
    return not (a[2] < b[0] or b[2] < a[0] or a[3] < b[1] or b[3] < a[1])


def cluster_motifs_6e4f6532(
    grid: Grid,
) -> tuple[tuple[Object, ...], Indices, Indices, Integer]:
    x0 = mostcolor(grid)
    x1 = shape(grid)
    x2 = _connected_components_6e4f6532(ofcolor(grid, EIGHT), diagonal=F)
    x3 = tuple(_rect_expand_6e4f6532(x4, ONE, x1) for x4 in x2)
    x4 = list(range(len(x2)))

    def x5(x6: Integer) -> Integer:
        while x4[x6] != x6:
            x4[x6] = x4[x4[x6]]
            x6 = x4[x6]
        return x6

    def x6(x7: Integer, x8: Integer) -> None:
        x9 = x5(x7)
        x10 = x5(x8)
        if x9 != x10:
            x4[x10] = x9

    for x7 in range(len(x2)):
        for x8 in range(x7 + ONE, len(x2)):
            if _rectangles_intersect_6e4f6532(x3[x7], x3[x8]):
                x6(x7, x8)
    x7 = defaultdict(list)
    for x8, x9 in enumerate(x2):
        x7[x5(x8)].append(x9)
    x8 = []
    x9 = set()
    x10 = set()
    for x11 in x7.values():
        x12 = merge(x11)
        x13, x14, x15, x16 = _rect_expand_6e4f6532(x12, ONE, x1)
        x17 = frozenset(
            (grid[x18][x19], (x18, x19))
            for x18 in range(x13, x15 + ONE)
            for x19 in range(x14, x16 + ONE)
            if grid[x18][x19] != x0
        )
        x8.append(x17)
        x10 |= object_cells_6e4f6532(x17)
        x9 |= frozenset(loc for x20, loc in x17 if x20 == NINE)
    x18 = tuple(sorted(x8, key=lambda x21: ulcorner(object_cells_6e4f6532(x21))))
    return x18, frozenset(x9), frozenset(x10), x0


def marker_patches_6e4f6532(
    grid: Grid,
    source_nines: Patch,
) -> tuple[Indices, ...]:
    x0 = difference(ofcolor(grid, NINE), source_nines)
    return _connected_components_6e4f6532(x0, diagonal=T)


def _side_in_object_6e4f6532(
    patch: Patch,
    obj: Object,
) -> str | None:
    x0 = object_cells_6e4f6532(obj)
    x1 = min(i for i, _ in x0)
    x2 = max(i for i, _ in x0)
    x3 = min(j for _, j in x0)
    x4 = max(j for _, j in x0)
    x5 = toindices(patch)
    if all(x6[1] == x3 for x6 in x5):
        return "L"
    if all(x6[1] == x4 for x6 in x5):
        return "R"
    if all(x6[0] == x1 for x6 in x5):
        return "T"
    if all(x6[0] == x2 for x6 in x5):
        return "B"
    return None


def _expected_side_6e4f6532(
    obj: Object,
    landmark: Patch,
) -> str:
    x0 = object_cells_6e4f6532(obj)
    x1 = min(i for i, _ in x0)
    x2 = max(i for i, _ in x0)
    x3 = min(j for _, j in x0)
    x4 = max(j for _, j in x0)
    x5 = toindices(landmark)
    x6 = min(i for i, _ in x5)
    x7 = max(i for i, _ in x5)
    x8 = min(j for _, j in x5)
    x9 = max(j for _, j in x5)
    x10 = (x1 + x2) / TWO
    x11 = (x3 + x4) / TWO
    x12 = (x6 + x7) / TWO
    x13 = (x8 + x9) / TWO
    x14 = x7 - x6 + ONE
    x15 = x9 - x8 + ONE
    if x14 > x15:
        return "R" if x13 > x11 else "L"
    return "B" if x12 > x10 else "T"


def render_output_6e4f6532(
    grid: Grid,
) -> Grid:
    x0, x1, x2, x3 = cluster_motifs_6e4f6532(grid)
    x4 = marker_patches_6e4f6532(grid, x1)
    x5 = defaultdict(set)
    for x6, row in enumerate(grid):
        for x7, x8 in enumerate(row):
            if x7 and x8:
                pass
            if (x6, x7) in x2 or x8 in (x3, EIGHT, NINE):
                continue
            x5[x8].add((x6, x7))
    x6 = []
    x7 = set()
    for x8 in x0:
        x9 = []
        for x10, x11 in enumerate(x4):
            if x10 in x7:
                continue
            for x12, x13 in enumerate(TRANSFORMS_6E4F6532):
                x14 = transform_object_6e4f6532(x8, x13)
                x15 = frozenset(loc for x16, loc in x14 if x16 == NINE)
                if normalize_patch_6e4f6532(x15) != normalize_patch_6e4f6532(x11):
                    continue
                x16 = subtract(ulcorner(x11), ulcorner(x15))
                x17 = shift_object_6e4f6532(x14, x16)
                x18 = ZERO
                x19 = ZERO
                x20 = frozenset(x21 for x21, _ in x17 if x21 not in (EIGHT, NINE))
                for x21 in x20:
                    x22 = frozenset(loc for x23, loc in x17 if x23 == x21)
                    x24 = _side_in_object_6e4f6532(x22, x17)
                    if x24 is None or x21 not in x5:
                        continue
                    x19 += ONE
                    if x24 == _expected_side_6e4f6532(x17, x5[x21]):
                        x18 += ONE
                x9.append((x18, x19, negate(x12), negate(x10), x17, x10))
        if len(x9) == ZERO:
            raise ValueError("unable to match motif to marker")
        x10 = max(x9)
        x7.add(x10[-ONE])
        x6.append(x10[-TWO])
    x8 = canvas(x3, shape(grid))
    x9 = set(x2)
    for x10 in x4:
        x9 |= set(x10)
    x11 = set()
    for x12, row in enumerate(grid):
        for x13, x14 in enumerate(row):
            if (x12, x13) in x9:
                continue
            x11.add((x14, (x12, x13)))
    x12 = paint(x8, frozenset(x11))
    for x13 in x6:
        x12 = paint(x12, x13)
    return x12


def negate(
    value: Integer,
) -> Integer:
    return ZERO - value


def template_roles_6e4f6532(
    template_spec: dict,
) -> tuple[str, ...]:
    x0 = tuple(
        sorted(
            {
                x1
                for x2 in template_spec["rows"]
                for x1 in x2
                if x1 in {"L", "R", "T", "B"}
            }
        )
    )
    return x0


def template_shape_class_6e4f6532(
    template_spec: dict,
) -> str:
    return template_spec["shape_class"]


def render_template_object_6e4f6532(
    template_spec: dict,
    role_colors: dict[str, Integer],
) -> Object:
    x0 = []
    for x1, x2 in enumerate(template_spec["rows"]):
        for x3, x4 in enumerate(x2):
            if x4 == ".":
                continue
            if x4 == "8":
                x5 = EIGHT
            elif x4 == "9":
                x5 = NINE
            else:
                x5 = role_colors[x4]
            x0.append((x5, (x1, x3)))
    return frozenset(x0)
