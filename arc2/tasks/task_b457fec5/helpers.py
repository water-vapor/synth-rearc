from arc2.core import *


def diagonal_band_patch_b457fec5(
    size: int,
    thickness: int,
    mirrored: bool,
) -> Indices:
    x0 = frozenset(
        (i, j)
        for i in range(size)
        for j in range(size)
        if abs(i - j) < thickness
    )
    x1 = branch(mirrored, vmirror(x0), x0)
    return x1


def recolor_band_patch_b457fec5(
    key: tuple[int, ...],
    patch: Patch,
) -> Object:
    x0 = normalize(patch)
    x1 = toindices(x0)
    x2 = width(x0)
    x3 = sum(1 for i, _ in x1 if i == ZERO)
    x4 = contained(ORIGIN, x1)
    x5 = len(key)
    x6 = frozenset(
        (
            key[min(branch(x4, j, x2 - ONE - j), min(i, x2 - x3)) % x5],
            (i, j),
        )
        for i, j in x1
    )
    x7 = shift(x6, ulcorner(patch))
    return x7


__all__ = [
    "diagonal_band_patch_b457fec5",
    "recolor_band_patch_b457fec5",
]
