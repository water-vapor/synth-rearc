from synth_rearc.core import *


SEED_COLOR_4A21E3DA = TWO
SHAPE_COLOR_4A21E3DA = SEVEN


def _align_patch_4a21e3da(
    indices: Indices,
    dims: IntegerTuple,
    row_side: str | None,
    col_side: str | None,
) -> Indices:
    if len(indices) == ZERO:
        return indices
    x0, x1 = dims
    x2 = ZERO
    x3 = ZERO
    if row_side == "top":
        x2 = -uppermost(indices)
    elif row_side == "bottom":
        x2 = x0 - ONE - lowermost(indices)
    if col_side == "left":
        x3 = -leftmost(indices)
    elif col_side == "right":
        x3 = x1 - ONE - rightmost(indices)
    return shift(indices, (x2, x3))


def verify_4a21e3da(
    I: Grid,
) -> Grid:
    x0 = shape(I)
    x1, x2 = x0
    x3 = ofcolor(I, SHAPE_COLOR_4A21E3DA)
    x4 = tuple(sorted(ofcolor(I, SEED_COLOR_4A21E3DA)))
    x5 = tuple((i, j) for i, j in x4 if i == ZERO)
    x6 = tuple((i, j) for i, j in x4 if i == x1 - ONE)
    x7 = tuple((i, j) for i, j in x4 if j == ZERO)
    x8 = tuple((i, j) for i, j in x4 if j == x2 - ONE)
    x9 = tuple(i for i, _ in combine(x7, x8))
    x10 = tuple(j for _, j in combine(x5, x6))
    x11 = minimum(x9) if len(x9) > ZERO else None
    x12 = minimum(x10) if len(x10) > ZERO else None
    x13 = canvas(mostcolor(I), x0)
    for x14, x15 in combine(x5, x6):
        x16 = equality(x14, ZERO)
        if x11 is None:
            x17 = x3
        elif x16:
            x17 = frozenset((i, j) for i, j in x3 if i < x11)
        else:
            x17 = frozenset((i, j) for i, j in x3 if i > x11)
        x18 = frozenset((i, j) for i, j in x17 if j < x15)
        x19 = frozenset((i, j) for i, j in x17 if j > x15)
        x20 = frozenset((i, j) for i, j in x3 if j == x15)
        x21 = _align_patch_4a21e3da(x18, x0, "top" if x16 else "bottom", "left")
        x22 = _align_patch_4a21e3da(x19, x0, "top" if x16 else "bottom", "right")
        x13 = fill(x13, SHAPE_COLOR_4A21E3DA, x21)
        x13 = fill(x13, SHAPE_COLOR_4A21E3DA, x22)
        x13 = fill(x13, SHAPE_COLOR_4A21E3DA, x20)
        if len(x20) == ZERO:
            x23 = frozenset({(x14, x15)})
        elif x16:
            x23 = frozenset((i, x15) for i in range(ZERO, lowermost(x20) + ONE))
        else:
            x23 = frozenset((i, x15) for i in range(uppermost(x20), x1))
        x13 = underfill(x13, SEED_COLOR_4A21E3DA, x23)
    for x24, x25 in combine(x7, x8):
        x26 = equality(x25, x2 - ONE)
        if x12 is None:
            x27 = x3
        elif x26:
            x27 = frozenset((i, j) for i, j in x3 if j > x12)
        else:
            x27 = frozenset((i, j) for i, j in x3 if j < x12)
        x28 = frozenset((i, j) for i, j in x27 if i < x24)
        x29 = frozenset((i, j) for i, j in x27 if i > x24)
        x30 = frozenset((i, j) for i, j in x3 if i == x24)
        x31 = _align_patch_4a21e3da(x28, x0, "top", "right" if x26 else "left")
        x32 = _align_patch_4a21e3da(x29, x0, "bottom", "right" if x26 else "left")
        x13 = fill(x13, SHAPE_COLOR_4A21E3DA, x31)
        x13 = fill(x13, SHAPE_COLOR_4A21E3DA, x32)
        x13 = fill(x13, SHAPE_COLOR_4A21E3DA, x30)
        if len(x30) == ZERO:
            x33 = frozenset({(x24, x25)})
        elif x26:
            x33 = frozenset((x24, j) for j in range(leftmost(x30), x2))
        else:
            x33 = frozenset((x24, j) for j in range(ZERO, rightmost(x30) + ONE))
        x13 = underfill(x13, SEED_COLOR_4A21E3DA, x33)
    return x13
