from arc2.core import *


BLOCK_SHAPE_B20F7C8B = (FIVE, FIVE)
GRID_SHAPE_B20F7C8B = (18, 22)
LEGEND_SHAPES_B20F7C8B = (
    frozenset({(0, 0), (1, 1), (1, 2), (2, 0)}),
    frozenset({(0, 0), (0, 1), (0, 2), (1, 1), (2, 0)}),
    frozenset({(0, 0), (0, 1), (0, 2), (1, 1), (2, 0), (2, 2)}),
    frozenset({(0, 0), (0, 1), (1, 0), (1, 1), (2, 2)}),
    frozenset({(0, 1), (0, 2), (1, 0), (1, 2), (2, 1), (2, 2)}),
    frozenset({(0, 0), (1, 0), (1, 1), (1, 2), (2, 0)}),
    frozenset({(0, 2), (1, 0), (1, 1), (2, 0), (2, 2)}),
    frozenset({(0, 0), (0, 1), (1, 0), (1, 2), (2, 1), (2, 2)}),
    frozenset({(0, 0), (0, 1), (1, 1), (2, 1), (2, 2)}),
    frozenset({(0, 1), (1, 0), (1, 1), (1, 2), (2, 1)}),
)


def normalize_indices_b20f7c8b(
    patch: Patch,
) -> Indices:
    return normalize(toindices(patch))


def rotate90_indices_b20f7c8b(
    patch: Patch,
) -> Indices:
    x0 = normalize_indices_b20f7c8b(patch)
    x1 = height(x0)
    x2 = frozenset((j, x1 - ONE - i) for i, j in x0)
    return normalize_indices_b20f7c8b(x2)


def dihedral_variants_b20f7c8b(
    patch: Patch,
) -> tuple[Indices, ...]:
    x0 = normalize_indices_b20f7c8b(patch)
    x1 = []
    x2 = x0
    for _ in range(FOUR):
        x3 = normalize_indices_b20f7c8b(x2)
        x4 = normalize_indices_b20f7c8b(vmirror(x2))
        if x3 not in x1:
            x1.append(x3)
        if x4 not in x1:
            x1.append(x4)
        x2 = rotate90_indices_b20f7c8b(x2)
    return tuple(x1)


def shape_key_b20f7c8b(
    patch: Patch,
) -> tuple[tuple[int, int], ...]:
    x0 = tuple(tuple(sorted(x1)) for x1 in dihedral_variants_b20f7c8b(patch))
    return sorted(x0)[ZERO]


def block_indices_b20f7c8b(
    start: tuple[int, int],
) -> Indices:
    x0, x1 = start
    x2 = interval(x0, x0 + FIVE, ONE)
    x3 = interval(x1, x1 + FIVE, ONE)
    return product(x2, x3)


def render_pattern_block_b20f7c8b(
    patch: Patch,
) -> Grid:
    x0 = canvas(TWO, BLOCK_SHAPE_B20F7C8B)
    x1 = shift(normalize_indices_b20f7c8b(patch), UNITY)
    return fill(x0, ONE, x1)


def paint_solid_at_b20f7c8b(
    grid: Grid,
    start: tuple[int, int],
    value: Integer,
) -> Grid:
    x0 = block_indices_b20f7c8b(start)
    return fill(grid, value, x0)


def paint_pattern_at_b20f7c8b(
    grid: Grid,
    start: tuple[int, int],
    patch: Patch,
) -> Grid:
    x0 = block_indices_b20f7c8b(start)
    x1 = fill(grid, TWO, x0)
    x2 = shift(normalize_indices_b20f7c8b(patch), add(start, UNITY))
    return fill(x1, ONE, x2)
