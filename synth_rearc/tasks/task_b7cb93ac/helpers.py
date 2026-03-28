from __future__ import annotations

from synth_rearc.core import *


OUTPUT_DIMS_B7CB93AC = (THREE, FOUR)


def extract_components_b7cb93ac(
    grid: Grid,
    without_bg: Boolean = T,
) -> tuple[Object, ...]:
    x0 = objects(grid, T, F, without_bg)
    return tuple(sorted(x0, key=lambda x1: (uppermost(x1), leftmost(x1), size(x1), color(x1))))


def normalized_shape_b7cb93ac(
    patch: Patch,
) -> Indices:
    return frozenset(toindices(normalize(patch)))


def _rot90_shape_b7cb93ac(
    patch: Indices,
) -> Indices:
    x0 = normalized_shape_b7cb93ac(patch)
    x1 = height(x0)
    x2 = frozenset((x3[1], subtract(subtract(x1, ONE), x3[0])) for x3 in x0)
    return normalized_shape_b7cb93ac(x2)


def shape_rotations_b7cb93ac(
    patch: Patch,
) -> tuple[Indices, ...]:
    x0 = normalized_shape_b7cb93ac(patch)
    x1 = []
    x2 = set()
    for _ in range(FOUR):
        if x0 not in x2:
            x1.append(x0)
            x2.add(x0)
        x0 = _rot90_shape_b7cb93ac(x0)
    return tuple(x1)

