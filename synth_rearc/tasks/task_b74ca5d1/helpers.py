from synth_rearc.core import *


def corner_map_b74ca5d1(
    grid: Grid,
) -> dict[int, tuple[int, int]]:
    bg = mostcolor(grid)
    h, w = shape(grid)
    corners = (
        (ZERO, ZERO),
        (ZERO, w - ONE),
        (h - ONE, ZERO),
        (h - ONE, w - ONE),
    )
    return {index(grid, loc): loc for loc in corners if index(grid, loc) != bg}


def align_to_corner_b74ca5d1(
    patch: Patch,
    corner: tuple[int, int],
    dims: tuple[int, int],
) -> Indices:
    h, w = dims
    x0 = normalize(toindices(patch))
    if corner == (ZERO, ZERO):
        return x0
    if corner == (ZERO, w - ONE):
        return shift(x0, (ZERO, w - width(x0)))
    if corner == (h - ONE, ZERO):
        return shift(x0, (h - height(x0), ZERO))
    return shift(x0, (h - height(x0), w - width(x0)))


def expand_bbox_b74ca5d1(
    patch: Patch,
    margin: int,
    dims: tuple[int, int],
) -> Indices:
    h, w = dims
    min_i = max(ZERO, uppermost(patch) - margin)
    min_j = max(ZERO, leftmost(patch) - margin)
    max_i = min(h - ONE, lowermost(patch) + margin)
    max_j = min(w - ONE, rightmost(patch) + margin)
    return frozenset((i, j) for i in range(min_i, max_i + ONE) for j in range(min_j, max_j + ONE))
