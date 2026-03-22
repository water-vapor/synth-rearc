from arc2.core import *


BG_963C33F8 = 7
FG_963C33F8 = 5
HI_963C33F8 = 9
LO_963C33F8 = 1
MOTIF_PATTERNS_963C33F8 = (
    (LO_963C33F8, LO_963C33F8, LO_963C33F8),
    (HI_963C33F8, LO_963C33F8, HI_963C33F8),
    (LO_963C33F8, LO_963C33F8, HI_963C33F8),
    (LO_963C33F8, HI_963C33F8, HI_963C33F8),
)


def patch_963c33f8(*cells: tuple[int, int]) -> Indices:
    return frozenset(cells)


def shift_patch_963c33f8(patch: Indices, offset: tuple[int, int]) -> Indices:
    return frozenset((i + offset[ZERO], j + offset[ONE]) for i, j in patch)


def paint_patch_963c33f8(grid: Grid, patch: Indices) -> Grid:
    return paint(grid, recolor(FG_963C33F8, patch))


def support_shapes_963c33f8(row: int, col: int) -> tuple[Indices, ...]:
    x0 = patch_963c33f8((row, col))
    x1 = patch_963c33f8((row - 1, col), (row, col))
    x2 = patch_963c33f8((row - 1, col - 1), (row, col))
    x3 = patch_963c33f8((row - 1, col - 1), (row - 1, col), (row, col))
    x4 = patch_963c33f8((row - 2, col - 1), (row - 1, col - 1), (row - 1, col), (row, col))
    x5 = patch_963c33f8((row - 2, col - 1), (row - 2, col), (row - 1, col - 1), (row - 1, col), (row, col))
    x6 = patch_963c33f8((row - 2, col - 2), (row - 2, col - 1), (row - 1, col - 1), (row - 1, col), (row, col))
    x7 = patch_963c33f8((row - 2, col), (row - 1, col - 1), (row - 1, col), (row, col))
    return (x0, x1, x2, x3, x4, x5, x6, x7)


def distractor_shapes_963c33f8(top: int, left: int) -> tuple[Indices, ...]:
    x0 = patch_963c33f8((top, left))
    x1 = patch_963c33f8((top, left), (top, left + 1))
    x2 = patch_963c33f8((top, left), (top + 1, left))
    x3 = patch_963c33f8((top, left), (top, left + 1), (top + 1, left + 1))
    x4 = patch_963c33f8((top, left + 1), (top + 1, left), (top + 1, left + 1))
    x5 = patch_963c33f8((top, left), (top, left + 1), (top + 1, left + 1))
    x6 = patch_963c33f8((top, left), (top + 1, left), (top + 1, left + 1))
    x7 = patch_963c33f8((top, left), (top, left + 1), (top + 1, left + 1), (top + 1, left + 2))
    x8 = patch_963c33f8((top, left + 1), (top + 1, left), (top + 1, left + 1), (top + 2, left + 1))
    x9 = patch_963c33f8((top, left), (top, left + 1), (top + 1, left), (top + 1, left + 1))
    return (x0, x1, x2, x3, x4, x5, x6, x7, x8, x9)


def fits_963c33f8(patch: Indices, dims: tuple[int, int], occupied: Indices) -> bool:
    x0, x1 = dims
    return all(
        0 <= i < x0 and 0 <= j < x1 and (i, j) not in occupied
        for i, j in patch
    )


def reserve_columns_963c33f8(left: int) -> tuple[int, int, int]:
    return (left, left + 1, left + 2)
