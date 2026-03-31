from synth_rearc.core import *


SIDE_TO_VECTOR_5961CC34 = {
    "u": (-1, 0),
    "d": (1, 0),
    "l": (0, -1),
    "r": (0, 1),
}

VECTOR_TO_SIDE_5961CC34 = {value: key for key, value in SIDE_TO_VECTOR_5961CC34.items()}
OPPOSITE_SIDE_5961CC34 = {
    "u": "d",
    "d": "u",
    "l": "r",
    "r": "l",
}

SHAPE_PROFILES_5961CC34 = (
    (TWO, FOUR, FOUR, TWO),
    (TWO, THREE, THREE, TWO),
    (TWO, FOUR, SIX, FOUR, TWO),
    (TWO, FOUR, FIVE, FIVE, FOUR, TWO),
)


def _profile_patch_5961cc34(
    profile: tuple[int, ...],
) -> Indices:
    width0 = max(profile)
    cells = set()
    for i, row_width in enumerate(profile):
        start = (width0 - row_width + ONE) // TWO
        for j in range(start, start + row_width):
            cells.add((i, j))
    return frozenset(cells)


def rot90_patch_5961cc34(
    patch: Patch,
) -> Indices:
    x0 = normalize(toindices(patch))
    x1 = height(x0)
    return frozenset((j, x1 - ONE - i) for i, j in x0)


def orient_patch_5961cc34(
    patch: Patch,
    turns: Integer,
) -> Indices:
    x0 = normalize(toindices(patch))
    for _ in range(turns % FOUR):
        x0 = rot90_patch_5961cc34(x0)
    return normalize(x0)


SHAPE_LIBRARY_5961CC34 = tuple(_profile_patch_5961cc34(profile) for profile in SHAPE_PROFILES_5961CC34)


def side_patch_5961cc34(
    patch: Patch,
    side: str,
) -> Indices:
    x0 = toindices(patch)
    if side == "u":
        x1 = uppermost(x0)
        return frozenset((i, j) for i, j in x0 if i == x1)
    if side == "d":
        x1 = lowermost(x0)
        return frozenset((i, j) for i, j in x0 if i == x1)
    if side == "l":
        x1 = leftmost(x0)
        return frozenset((i, j) for i, j in x0 if j == x1)
    x1 = rightmost(x0)
    return frozenset((i, j) for i, j in x0 if j == x1)


def marker_patch_5961cc34(
    patch: Patch,
    side: str,
) -> Indices:
    x0 = side_patch_5961cc34(patch, side)
    x1 = SIDE_TO_VECTOR_5961CC34[side]
    return shift(x0, x1)


def ordered_line_5961cc34(
    patch: Patch,
    direction: tuple[int, int],
) -> tuple[tuple[int, int], ...]:
    x0 = tuple(toindices(patch))
    if direction[0] != ZERO:
        return tuple(sorted(x0, key=lambda ij: (ij[1], ij[0])))
    return tuple(sorted(x0, key=lambda ij: (ij[0], ij[1])))


def subset_options_5961cc34(
    patch: Patch,
    width0: Integer,
    direction: tuple[int, int],
) -> tuple[Indices, ...]:
    x0 = ordered_line_5961cc34(patch, direction)
    if len(x0) < width0:
        return ()
    if len(x0) == width0:
        return (frozenset(x0),)
    return tuple(frozenset({cell}) for cell in x0)


def place_shape_on_ray_5961cc34(
    current_patch: Patch,
    direction: tuple[int, int],
    shape_patch: Patch,
    entry_side: str,
    entry_subset: Patch,
    distance: Integer,
) -> tuple[Indices, Indices]:
    x0 = ordered_line_5961cc34(current_patch, direction)
    x1 = ordered_line_5961cc34(entry_subset, direction)
    x2 = tuple((i + distance * direction[0], j + distance * direction[1]) for i, j in x0)
    x3 = (x2[0][0] - x1[0][0], x2[0][1] - x1[0][1])
    x4 = shift(shape_patch, x3)
    x5 = shift(entry_subset, x3)
    return x4, x5


def paired_segment_5961cc34(
    start_patch: Patch,
    stop_patch: Patch,
    direction: tuple[int, int],
) -> Indices:
    x0 = ordered_line_5961cc34(start_patch, direction)
    x1 = ordered_line_5961cc34(stop_patch, direction)
    x2 = frozenset()
    for a, b in zip(x0, x1):
        x2 = x2 | connect(a, b)
    return x2


def ray_to_border_5961cc34(
    start_patch: Patch,
    direction: tuple[int, int],
    dims: tuple[int, int],
) -> Indices:
    h, w = dims
    cells = set()
    for i, j in toindices(start_patch):
        ci, cj = i, j
        while 0 <= ci < h and 0 <= cj < w:
            cells.add((ci, cj))
            ci += direction[0]
            cj += direction[1]
    return frozenset(cells)


def in_bounds_5961cc34(
    patch: Patch,
    dims: tuple[int, int],
) -> Boolean:
    h, w = dims
    return all(0 <= i < h and 0 <= j < w for i, j in toindices(patch))


def expand4_5961cc34(
    patch: Patch,
) -> Indices:
    x0 = set(toindices(patch))
    for cell in tuple(x0):
        x0.update(dneighbors(cell))
    return frozenset(x0)
