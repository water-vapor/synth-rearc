from synth_rearc.core import *


def has_diagonal_run_ecb67b6d(
    patch: Patch,
) -> bool:
    x0 = toindices(patch)
    for i, j in x0:
        if (i - ONE, j - ONE) in x0 and (i + ONE, j + ONE) in x0:
            return True
        if (i - ONE, j + ONE) in x0 and (i + ONE, j - ONE) in x0:
            return True
    return False


def halo_ecb67b6d(
    patch: Patch,
) -> Indices:
    x0 = set(toindices(patch))
    x1 = tuple(x0)
    for loc in x1:
        x0.update(neighbors(loc))
    return frozenset(x0)
