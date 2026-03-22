from arc2.core import *


_BASE_PATTERNS_8BA14F53 = {
    ONE: (
        (
            "###",
            "#.#",
            "###",
        ),
    ),
    TWO: (
        (
            "####",
            "#..#",
            "####",
        ),
    ),
    THREE: (
        (
            "###.",
            "#.##",
            "#..#",
            "####",
        ),
    ),
    FOUR: (
        (
            "####",
            "#..#",
            "#..#",
            "####",
        ),
    ),
    SIX: (
        (
            "#####",
            "#...#",
            "#...#",
            "#####",
        ),
    ),
}

_PATCH_TRANSFORMS_8BA14F53 = (
    identity,
    hmirror,
    vmirror,
    compose(hmirror, vmirror),
    dmirror,
    cmirror,
    compose(hmirror, dmirror),
    compose(vmirror, dmirror),
)


def pattern_to_patch_8ba14f53(
    pattern: tuple[str, ...],
) -> Patch:
    return frozenset(
        (i, j)
        for i, row in enumerate(pattern)
        for j, value in enumerate(row)
        if value == "#"
    )


def normalize_patch_8ba14f53(
    patch: Patch,
) -> Patch:
    return normalize(toindices(patch))


def hole_count_8ba14f53(
    patch: Patch,
) -> Integer:
    if len(patch) == ZERO:
        return ZERO
    x0 = normalize_patch_8ba14f53(patch)
    x1 = canvas(ZERO, shape(x0))
    x2 = fill(x1, EIGHT, x0)
    x3 = objects(x2, T, F, F)
    x4 = colorfilter(x3, ZERO)
    x5 = compose(flip, rbind(bordering, x2))
    x6 = sfilter(x4, x5)
    x7 = merge(x6)
    return size(x7)


def _variants_8ba14f53(
    pattern: tuple[str, ...],
) -> tuple[Patch, ...]:
    x0 = pattern_to_patch_8ba14f53(pattern)
    x1 = []
    for x2 in _PATCH_TRANSFORMS_8BA14F53:
        x3 = normalize_patch_8ba14f53(x2(x0))
        if greater(height(x3), FOUR) or greater(width(x3), FIVE):
            continue
        if x3 not in x1:
            x1.append(x3)
    return tuple(x1)


MOTIF_BANK_8BA14F53 = {
    x0: tuple(
        x2
        for x1 in x3
        for x2 in _variants_8ba14f53(x1)
    )
    for x0, x3 in _BASE_PATTERNS_8BA14F53.items()
}

for x0, x1 in MOTIF_BANK_8BA14F53.items():
    for x2 in x1:
        if hole_count_8ba14f53(x2) != x0:
            raise ValueError(f"invalid 8ba14f53 motif for hole count {x0}")
