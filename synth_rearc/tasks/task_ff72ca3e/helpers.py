from synth_rearc.core import *


def chebyshev_ff72ca3e(
    a: IntegerTuple,
    b: IntegerTuple,
) -> Integer:
    x0 = abs(subtract(a[ZERO], b[ZERO]))
    x1 = abs(subtract(a[ONE], b[ONE]))
    return max(x0, x1)


def square_patch_ff72ca3e(
    center_loc: IntegerTuple,
    radius: Integer,
) -> Indices:
    x0 = subtract(center_loc[ZERO], radius)
    x1 = subtract(center_loc[ONE], radius)
    x2 = add(center_loc[ZERO], radius)
    x3 = add(center_loc[ONE], radius)
    x4 = frozenset({(x0, x1), (x2, x3)})
    return backdrop(x4)


def nearest_marker_distance_ff72ca3e(
    center_loc: IntegerTuple,
    markers: Indices,
) -> Integer:
    x0 = tuple(markers)
    if len(x0) == ZERO:
        raise ValueError("ff72ca3e requires at least one marker")
    return min(chebyshev_ff72ca3e(center_loc, x1) for x1 in x0)


def clip_patch_ff72ca3e(
    patch: Patch,
    dims: IntegerTuple,
) -> Indices:
    x0 = dims[ZERO]
    x1 = dims[ONE]
    return frozenset(
        (x2, x3)
        for x2, x3 in toindices(patch)
        if 0 <= x2 < x0 and 0 <= x3 < x1
    )
