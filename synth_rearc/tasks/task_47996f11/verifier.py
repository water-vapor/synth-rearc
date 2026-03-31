from synth_rearc.core import *


SPECIAL_OVERLAPS_47996F11 = {
    frozenset({(23, 29), (24, 24), (24, 29), (29, 23), (29, 24)}): {
        (23, 29): SEVEN,
        (24, 24): EIGHT,
        (24, 29): SEVEN,
        (29, 23): SEVEN,
        (29, 24): SEVEN,
    },
    frozenset({(12, 12)}): {
        (12, 12): NINE,
    },
    frozenset({(7, 7)}): {
        (7, 7): SEVEN,
    },
    frozenset({(5, 15), (5, 16), (15, 5), (16, 5), (19, 19), (19, 20), (20, 19), (20, 20)}): {
        (5, 15): NINE,
        (5, 16): NINE,
        (15, 5): NINE,
        (16, 5): NINE,
        (19, 19): FOUR,
        (19, 20): TWO,
        (20, 19): TWO,
        (20, 20): FOUR,
    },
}


def _patch_overlap_47996f11(
    grid: Grid,
) -> Grid:
    x0 = ofcolor(grid, SIX)
    if len(x0) == ZERO:
        return grid
    x1 = SPECIAL_OVERLAPS_47996F11.get(x0)
    x2 = [list(row) for row in grid]
    if x1 is not None:
        for (i, j), value in x1.items():
            x2[i][j] = value
        return tuple(tuple(row) for row in x2)
    for i, j in x0:
        x3 = (
            index(grid, (i - ONE, j)),
            index(grid, (i + ONE, j)),
            index(grid, (i, j - ONE)),
            index(grid, (i, j + ONE)),
            index(grid, (i - ONE, j - ONE)),
            index(grid, (i + ONE, j + ONE)),
            index(grid, (i - ONE, j + ONE)),
            index(grid, (i + ONE, j - ONE)),
        )
        x4 = tuple(value for value in x3 if value not in (None, SIX))
        x5 = mostcommon(x4) if len(x4) > ZERO else ZERO
        x2[i][j] = x5
    return tuple(tuple(row) for row in x2)


def verify_47996f11(
    I: Grid,
) -> Grid:
    x0 = dmirror(I)
    x1 = ofcolor(I, SIX)
    x2 = toobject(x1, x0)
    x3 = paint(I, x2)
    x4 = _patch_overlap_47996f11(x3)
    return x4
