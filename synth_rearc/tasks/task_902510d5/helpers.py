from synth_rearc.core import *


CORNER_NAMES_902510D5 = ("tl", "tr", "bl", "br")


def corner_cell_902510d5(
    corner: str,
    dims: IntegerTuple,
) -> IntegerTuple:
    h, w = dims
    if corner == "tl":
        return (ZERO, ZERO)
    if corner == "tr":
        return (ZERO, w - ONE)
    if corner == "bl":
        return (h - ONE, ZERO)
    return (h - ONE, w - ONE)


def corner_cells_902510d5(
    dims: IntegerTuple,
) -> frozenset[IntegerTuple]:
    return frozenset(corner_cell_902510d5(corner, dims) for corner in CORNER_NAMES_902510D5)


def corner_name_from_cell_902510d5(
    cell: IntegerTuple,
    dims: IntegerTuple,
) -> str:
    for corner in CORNER_NAMES_902510D5:
        if cell == corner_cell_902510d5(corner, dims):
            return corner
    raise ValueError(f"{cell} is not a grid corner for {dims}")


def triangle_patch_902510d5(
    corner: str,
    side: Integer,
    dims: IntegerTuple,
) -> frozenset[IntegerTuple]:
    h, w = dims
    cells = set()
    if corner == "tl":
        for i in range(side):
            for j in range(side - i):
                cells.add((i, j))
    elif corner == "tr":
        for i in range(side):
            for j in range(w - side + i, w):
                cells.add((i, j))
    elif corner == "bl":
        for i in range(side):
            row = h - side + i
            for j in range(i + ONE):
                cells.add((row, j))
    else:
        for i in range(side):
            row = h - side + i
            length = i + ONE
            for j in range(w - length, w):
                cells.add((row, j))
    return frozenset(cells)


def neighborhood_902510d5(
    cells: frozenset[IntegerTuple] | set[IntegerTuple],
) -> frozenset[IntegerTuple]:
    out = set()
    for i, j in cells:
        for di in (-ONE, ZERO, ONE):
            for dj in (-ONE, ZERO, ONE):
                out.add((i + di, j + dj))
    return frozenset(out)
