from arc2.core import *


MOTIF_TO_COLOR_009d5c81 = {
    (
        (ONE, ONE, ONE),
        (ONE, ZERO, ONE),
        (ZERO, ONE, ZERO),
    ): SEVEN,
    (
        (ONE, ZERO, ONE),
        (ZERO, ONE, ZERO),
        (ONE, ONE, ONE),
    ): THREE,
    (
        (ZERO, ONE, ZERO),
        (ONE, ONE, ONE),
        (ZERO, ONE, ZERO),
    ): TWO,
}

MOTIFS_009d5c81 = tuple(MOTIF_TO_COLOR_009d5c81.keys())

DIRECTIONS_009d5c81 = (
    UP,
    DOWN,
    LEFT,
    RIGHT,
    UNITY,
    NEG_UNITY,
    UP_RIGHT,
    DOWN_LEFT,
)


def motif_to_color_009d5c81(motif: Grid) -> Integer:
    if motif not in MOTIF_TO_COLOR_009d5c81:
        raise ValueError(f"unknown 009d5c81 motif: {motif}")
    return MOTIF_TO_COLOR_009d5c81[motif]


def motif_patch_009d5c81(motif: Grid, loc: IntegerTuple) -> Patch:
    x0 = ofcolor(motif, ONE)
    x1 = shift(x0, loc)
    return x1


def _in_bounds_009d5c81(loc: IntegerTuple, dims: IntegerTuple) -> Boolean:
    x0 = loc[0]
    x1 = loc[1]
    x2 = dims[0]
    x3 = dims[1]
    return 0 <= x0 < x2 and 0 <= x1 < x3


def make_signal_patch_009d5c81(
    diff_lb: float,
    diff_ub: float,
) -> Patch:
    box_h = unifint(diff_lb, diff_ub, (THREE, EIGHT))
    box_w = unifint(diff_lb, diff_ub, (SIX, TEN))
    base_row = randint(ZERO, box_h - ONE)
    left = randint(ZERO, box_w - SIX)
    right = randint(left + FIVE, box_w - ONE)
    patch = connect((base_row, left), (base_row, right))
    cursor = choice(totuple(patch))
    nstrokes = unifint(diff_lb, diff_ub, (SEVEN, 14))
    for _ in range(nstrokes):
        if randint(ZERO, THREE) == ZERO:
            cursor = choice(totuple(patch))
        direction = choice(DIRECTIONS_009d5c81)
        span = unifint(diff_lb, diff_ub, (ONE, FOUR))
        current = cursor
        for _ in range(span):
            nxt = add(current, direction)
            if not _in_bounds_009d5c81(nxt, (box_h, box_w)):
                break
            patch = combine(patch, initset(nxt))
            current = nxt
        cursor = current
    return normalize(patch)


def signal_patch_is_valid_009d5c81(patch: Patch) -> Boolean:
    x0 = height(patch)
    x1 = width(patch)
    x2 = size(patch)
    x3 = multiply(x0, x1)
    if x0 < THREE or x0 > EIGHT:
        return False
    if x1 < SIX or x1 > TEN:
        return False
    if x2 < 14 or x2 > 31:
        return False
    if x2 == x3:
        return False
    if x2 * 100 < x3 * 30:
        return False
    if x2 * 100 > x3 * 80:
        return False
    x4 = canvas(ZERO, (x0, x1))
    x5 = fill(x4, EIGHT, patch)
    x6 = objects(x5, T, T, T)
    x7 = colorfilter(x6, EIGHT)
    return size(x7) == ONE
