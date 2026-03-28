from synth_rearc.core import *


PROTOTYPES_D6542281 = (
    {
        "grid": (
            (1, 1, 0),
            (1, 2, 0),
            (0, 0, 1),
        ),
        "anchor": 2,
    },
    {
        "grid": (
            (1, 0, 2),
            (1, 2, 0),
            (1, 1, 1),
        ),
        "anchor": 2,
    },
    {
        "grid": (
            (1, 1, 0, 0),
            (1, 2, 0, 0),
            (0, 0, 2, 1),
            (0, 0, 1, 3),
        ),
        "anchor": 3,
    },
    {
        "grid": (
            (1, 0, 0, 0),
            (0, 2, 0, 1),
            (0, 0, 2, 1),
            (0, 1, 1, 3),
        ),
        "anchor": 2,
    },
    {
        "grid": (
            (1, 0, 0, 0, 0),
            (0, 1, 1, 0, 0),
            (0, 1, 2, 1, 0),
            (0, 0, 1, 1, 0),
            (0, 0, 0, 0, 1),
        ),
        "anchor": 2,
    },
    {
        "grid": (
            (1, 1, 0, 0),
            (1, 2, 0, 0),
            (0, 0, 2, 3),
            (0, 0, 3, 3),
        ),
        "anchor": 2,
    },
    {
        "grid": (
            (1, 1, 1),
            (1, 2, 1),
            (1, 1, 1),
        ),
        "anchor": 2,
    },
    {
        "grid": (
            (0, 0, 0, 1),
            (0, 1, 1, 0),
            (0, 2, 1, 0),
            (1, 0, 0, 0),
        ),
        "anchor": 2,
    },
    {
        "grid": (
            (1, 1, 0, 0),
            (1, 2, 3, 0),
            (0, 3, 2, 4),
            (0, 0, 4, 4),
        ),
        "anchor": 2,
    },
)


SYMMETRIES_D6542281 = (
    identity,
    rot90,
    rot180,
    rot270,
    hmirror,
    vmirror,
    lambda x: rot90(hmirror(x)),
    lambda x: rot90(vmirror(x)),
)


def prototype_group_patches_d6542281(grid: Grid) -> dict:
    x0 = frozenset(
        (i, j)
        for i, row in enumerate(grid)
        for j, value in enumerate(row)
        if value != ZERO
    )
    x1 = invert(ulcorner(x0))
    x2 = tuple(sorted(remove(ZERO, palette(grid))))
    return {x3: shift(ofcolor(grid, x3), x1) for x3 in x2}


def build_object_d6542281(
    groups: dict,
    colors: dict,
    anchor_group: Integer,
    trim_unmatched_singletons: Boolean,
) -> Object:
    x0 = tuple(sorted(groups))
    x1 = tuple(
        recolor(colors[x2], groups[x2])
        for x2 in x0
        if not both(
            trim_unmatched_singletons,
            both(flip(equality(x2, anchor_group)), equality(size(groups[x2]), ONE)),
        )
    )
    return merge(x1)


def expanded_indices_d6542281(patch: Patch) -> Indices:
    x0 = toindices(patch)
    x1 = mapply(neighbors, x0)
    return combine(x0, x1)


def transformed_prototype_d6542281() -> dict:
    x0 = choice(PROTOTYPES_D6542281)
    x1 = choice(SYMMETRIES_D6542281)
    x2 = x1(x0["grid"])
    x3 = prototype_group_patches_d6542281(x2)
    return {
        "anchor": x0["anchor"],
        "groups": x3,
    }
