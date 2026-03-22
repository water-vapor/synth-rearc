from arc2.core import *


TL_CORNER_93C31FBE = frozenset({ORIGIN, RIGHT, DOWN})
TR_CORNER_93C31FBE = frozenset({ORIGIN, RIGHT, UNITY})
BL_CORNER_93C31FBE = frozenset({ORIGIN, DOWN, UNITY})
BR_CORNER_93C31FBE = frozenset({RIGHT, DOWN, UNITY})

FRAME_COLORS_93C31FBE = (TWO, THREE, FOUR, EIGHT)
WIDE_93C31FBE = ZERO
TALL_93C31FBE = ONE


def marker_color_93c31fbe(
    grid: Grid,
) -> Integer:
    x0 = tuple(x1 for x1 in palette(grid) if x1 not in (ZERO, ONE))
    return first(x0)


def marker_patch_93c31fbe(
    box: Tuple,
) -> Indices:
    r0, c0, r1, c1 = box
    return frozenset(
        {
            (r0, c0),
            (r0, c0 + ONE),
            (r0 + ONE, c0),
            (r0, c1 - ONE),
            (r0, c1),
            (r0 + ONE, c1),
            (r1 - ONE, c0),
            (r1, c0),
            (r1, c0 + ONE),
            (r1 - ONE, c1),
            (r1, c1 - ONE),
            (r1, c1),
        }
    )


def paint_boxes_93c31fbe(
    grid: Grid,
    boxes: Tuple,
    color: Integer,
) -> Grid:
    x0 = grid
    for x1 in boxes:
        x0 = fill(x0, color, marker_patch_93c31fbe(x1))
    return x0


def box_orientation_93c31fbe(
    box: Tuple,
) -> Integer:
    r0, c0, r1, c1 = box
    return WIDE_93C31FBE if greater(c1 - c0, r1 - r0) else TALL_93C31FBE


def reflect_points_93c31fbe(
    points: Indices,
    box: Tuple,
) -> Indices:
    r0, c0, r1, c1 = box
    if box_orientation_93c31fbe(box) == WIDE_93C31FBE:
        return frozenset((i, c0 + c1 - j) for i, j in points)
    return frozenset((r0 + r1 - i, j) for i, j in points)


def find_boxes_93c31fbe(
    grid: Grid,
) -> Tuple:
    x0 = marker_color_93c31fbe(grid)
    x1 = colorfilter(objects(grid, T, F, T), x0)
    x2 = []
    x3 = []
    x4 = []
    x5 = []
    for x6 in x1:
        x7 = normalize(toindices(x6))
        x8 = (uppermost(x6), leftmost(x6), lowermost(x6), rightmost(x6))
        if x7 == TL_CORNER_93C31FBE:
            x2.append(x8)
        elif x7 == TR_CORNER_93C31FBE:
            x3.append(x8)
        elif x7 == BL_CORNER_93C31FBE:
            x4.append(x8)
        elif x7 == BR_CORNER_93C31FBE:
            x5.append(x8)
    x9 = frozenset((x10[ZERO], x10[THREE]) for x10 in x3)
    x10 = frozenset((x11[TWO], x11[ONE]) for x11 in x4)
    x11 = set()
    for x12 in x2:
        r0, c0, _, _ = x12
        for x13 in x5:
            _, _, r1, c1 = x13
            if r1 <= r0 + ONE or c1 <= c0 + ONE:
                continue
            if (r0, c1) not in x9 or (r1, c0) not in x10:
                continue
            x11.add((r0, c0, r1, c1))
    return tuple(sorted(x11))
