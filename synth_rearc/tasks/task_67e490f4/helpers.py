from __future__ import annotations

from synth_rearc.core import *


FreeShapeKey67e490f4 = tuple[IntegerTuple, ...]


def rectangle_patch_67e490f4(
    top: Integer,
    left: Integer,
    height_value: Integer,
    width_value: Integer,
) -> Indices:
    return frozenset(
        (x0, x1)
        for x0 in range(top, top + height_value)
        for x1 in range(left, left + width_value)
    )


def orthopad_67e490f4(
    patch: Patch,
) -> Indices:
    x0 = set(toindices(patch))
    for x1 in tuple(x0):
        x0 |= dneighbors(x1)
    return frozenset(x0)


def free_shape_variants_67e490f4(
    patch: Patch,
) -> tuple[Indices, ...]:
    x0 = normalize(toindices(patch))
    x1 = (
        x0,
        hmirror(x0),
        vmirror(x0),
        hmirror(vmirror(x0)),
        dmirror(x0),
        cmirror(x0),
        hmirror(dmirror(x0)),
        vmirror(dmirror(x0)),
    )
    x2 = set()
    x3 = []
    for x4 in x1:
        x5 = frozenset(normalize(x4))
        if x5 in x2:
            continue
        x2.add(x5)
        x3.append(x5)
    return tuple(x3)


def free_shape_key_67e490f4(
    patch: Patch,
) -> FreeShapeKey67e490f4:
    x0 = tuple(
        tuple(sorted(toindices(x1)))
        for x1 in free_shape_variants_67e490f4(patch)
    )
    return min(x0)


def connected_components_67e490f4(
    patch: Patch,
) -> tuple[Indices, ...]:
    x0 = set(toindices(patch))
    x1 = []
    while len(x0) > ZERO:
        x2 = {next(iter(x0))}
        x3 = set()
        while len(x2) > ZERO:
            x4 = x2.pop()
            if x4 not in x0:
                continue
            x0.remove(x4)
            x3.add(x4)
            x2 |= x0 & dneighbors(x4)
        x1.append(frozenset(x3))
    return tuple(sorted(x1, key=lambda x5: (uppermost(x5), leftmost(x5), size(x5))))
