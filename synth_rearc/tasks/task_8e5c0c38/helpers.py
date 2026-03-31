from synth_rearc.core import *


def axis_subset_8e5c0c38(
    patch: Patch,
    axis_twice: Integer,
) -> Indices:
    x0 = toindices(patch)
    return frozenset((i, j) for i, j in x0 if (i, axis_twice - j) in x0)


def best_vertical_subset_8e5c0c38(
    patch: Patch,
) -> tuple[Indices, Integer]:
    x0 = toindices(patch)
    x1 = sorted({j for _, j in x0})
    x2 = frozenset()
    x3 = None
    for x4 in x1:
        for x5 in x1:
            x6 = x4 + x5
            x7 = axis_subset_8e5c0c38(x0, x6)
            if len(x7) > len(x2) or (len(x7) == len(x2) and (x3 is None or x6 < x3)):
                x2 = x7
                x3 = x6
    return x2, x3
