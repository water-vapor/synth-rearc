from collections import deque

from synth_rearc.core import *


Cell62ab2642 = tuple[int, int]


def border_cells_62ab2642(
    dims: IntegerTuple,
) -> tuple[Cell62ab2642, ...]:
    h, w = dims
    x0 = [(ZERO, j) for j in range(ONE, subtract(w, ONE))]
    x1 = [(subtract(h, ONE), j) for j in range(ONE, subtract(w, ONE))]
    x2 = [(i, ZERO) for i in range(ONE, subtract(h, ONE))]
    x3 = [(i, subtract(w, ONE)) for i in range(ONE, subtract(h, ONE))]
    return tuple(x0 + x1 + x2 + x3)


def segment_62ab2642(
    a: Cell62ab2642,
    b: Cell62ab2642,
) -> frozenset[Cell62ab2642] | None:
    x0, x1 = a
    x2, x3 = b
    if x0 == x2:
        x4, x5 = sorted((x1, x3))
        return frozenset((x0, j) for j in range(x4, x5 + ONE))
    if x1 == x3:
        x4, x5 = sorted((x0, x2))
        return frozenset((i, x1) for i in range(x4, x5 + ONE))
    return None


def l_path_62ab2642(
    a: Cell62ab2642,
    b: Cell62ab2642,
    order: Integer,
) -> frozenset[Cell62ab2642] | None:
    x0 = (a[ZERO], b[ONE]) if order == ZERO else (b[ZERO], a[ONE])
    x1 = segment_62ab2642(a, x0)
    x2 = segment_62ab2642(x0, b)
    if x1 is None or x2 is None:
        return None
    return x1 | x2


def _neighbors_62ab2642(
    cell: Cell62ab2642,
) -> tuple[Cell62ab2642, ...]:
    x0, x1 = cell
    return ((x0 + ONE, x1), (x0 - ONE, x1), (x0, x1 + ONE), (x0, x1 - ONE))


def _on_border_62ab2642(
    cell: Cell62ab2642,
    dims: IntegerTuple,
) -> bool:
    x0, x1 = cell
    x2, x3 = dims
    return x0 in (ZERO, subtract(x2, ONE)) or x1 in (ZERO, subtract(x3, ONE))


def _degrees_62ab2642(
    cells: frozenset[Cell62ab2642],
) -> dict[Cell62ab2642, int]:
    return {x0: sum(x1 in cells for x1 in _neighbors_62ab2642(x0)) for x0 in cells}


def valid_tree_62ab2642(
    cells: frozenset[Cell62ab2642],
    dims: IntegerTuple,
) -> bool:
    if len(cells) == ZERO:
        return False
    x0 = _degrees_62ab2642(cells)
    if maximum(frozenset(x0.values())) > THREE:
        return False
    if any(x1 == ONE and not _on_border_62ab2642(x2, dims) for x2, x1 in x0.items()):
        return False
    if any(x1 == THREE and _on_border_62ab2642(x2, dims) for x2, x1 in x0.items()):
        return False
    x1 = next(iter(cells))
    x2 = {x1}
    x3 = deque((x1,))
    while len(x3) > ZERO:
        x4 = x3.popleft()
        for x5 in _neighbors_62ab2642(x4):
            if x5 not in cells or x5 in x2:
                continue
            x2.add(x5)
            x3.append(x5)
    if len(x2) != len(cells):
        return False
    x6 = sum(sum(x7 in cells for x7 in _neighbors_62ab2642(x8)) for x8 in cells) // TWO
    return x6 == subtract(len(cells), ONE)


def interior_degree_two_cells_62ab2642(
    cells: frozenset[Cell62ab2642],
    dims: IntegerTuple,
) -> tuple[Cell62ab2642, ...]:
    x0 = _degrees_62ab2642(cells)
    return tuple(x1 for x1, x2 in x0.items() if x2 == TWO and not _on_border_62ab2642(x1, dims))


def leaf_count_62ab2642(
    cells: frozenset[Cell62ab2642],
) -> Integer:
    x0 = _degrees_62ab2642(cells)
    return sum(x1 == ONE for x1 in x0.values())


def zero_regions_62ab2642(
    grid: Grid,
) -> tuple[Indices, ...]:
    x0 = objects(grid, T, F, F)
    x1 = colorfilter(x0, ZERO)
    return tuple(sorted((toindices(x2) for x2 in x1), key=lambda x3: (len(x3), ulcorner(x3))))
