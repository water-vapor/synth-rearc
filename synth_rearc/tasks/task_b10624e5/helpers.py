from synth_rearc.core import *


BACKGROUND_10624E5 = FOUR
DIVIDER_10624E5 = ONE
ANCHOR_10624E5 = TWO
GRID_SIZE_10624E5 = 27
CROSS_INDEX_10624E5 = 13
MOTIF_COLORS_10624E5 = (ONE, THREE, EIGHT, NINE)
MOTIF_TEMPLATES_10624E5 = {
    "up_full": {"offset": (-2, 0), "dims": (2, 2)},
    "up_half_right": {"offset": (-2, 1), "dims": (2, 1)},
    "left_half": {"offset": (0, -1), "dims": (2, 1)},
    "left_double": {"offset": (0, -4), "dims": (2, 4)},
    "right_full": {"offset": (0, 2), "dims": (2, 2)},
    "down_full": {"offset": (2, 0), "dims": (2, 2)},
    "diag_up_left_full": {"offset": (-2, -2), "dims": (2, 2)},
    "diag_up_left_half": {"offset": (-1, -1), "dims": (1, 1)},
}


def rectangle_object_10624e5(
    value: Integer,
    upper_left: IntegerTuple,
    dims: IntegerTuple,
) -> Object:
    x0, x1 = upper_left
    x2, x3 = dims
    return frozenset((value, (i, j)) for i in range(x0, add(x0, x2)) for j in range(x1, add(x1, x3)))


def foreground_objects_10624e5(
    grid: Grid,
    bg: Integer,
) -> Objects:
    x0 = objects(grid, T, F, F)
    x1 = matcher(color, bg)
    x2 = compose(flip, x1)
    x3 = sfilter(x0, x2)
    return x3


def find_divider_10624e5(
    grid: Grid,
) -> tuple[Integer, Integer, Integer]:
    x0 = frontiers(grid)
    x1 = sfilter(x0, hline)
    x2 = sfilter(x0, vline)
    for x3 in x1:
        x4 = color(x3)
        x5 = sfilter(x2, matcher(color, x4))
        if size(x5) == ZERO:
            continue
        x6 = first(x5)
        return uppermost(x3), leftmost(x6), x4
    raise ValueError("expected a matching cross divider")


def scale_object_10624e5(
    obj: Object,
    numerator: Integer,
    denominator: Integer,
) -> Object:
    x0 = set()
    for x1, (x2, x3) in obj:
        x4 = divide(multiply(x2, numerator), denominator)
        x5 = divide(add(multiply(add(x2, ONE), numerator), decrement(denominator)), denominator)
        x6 = divide(multiply(x3, numerator), denominator)
        x7 = divide(add(multiply(add(x3, ONE), numerator), decrement(denominator)), denominator)
        for x8 in range(x4, x5):
            for x9 in range(x6, x7):
                x0.add((x1, (x8, x9)))
    return frozenset(x0)


def render_output_10624e5(
    I: Grid,
) -> Grid:
    x0 = mostcolor(I)
    x1, x2, _ = find_divider_10624e5(I)
    x3 = crop(I, ORIGIN, (x1, x2))
    x4 = foreground_objects_10624e5(x3, x0)
    x5 = merge(x4)
    x6 = subgrid(x5, x3)
    x7 = foreground_objects_10624e5(x6, x0)
    x8 = first(colorfilter(x7, ANCHOR_10624E5))
    x9 = height(x8)
    x10 = (
        ((ZERO, increment(x2)), (x1, subtract(width(I), increment(x2))), F, T),
        ((increment(x1), ZERO), (subtract(height(I), increment(x1)), x2), T, F),
        (
            (increment(x1), increment(x2)),
            (subtract(height(I), increment(x1)), subtract(width(I), increment(x2))),
            T,
            T,
        ),
    )
    x11 = I
    for x12, x13, x14, x15 in x10:
        x16 = crop(I, x12, x13)
        x17 = foreground_objects_10624e5(x16, x0)
        x18 = colorfilter(x17, ANCHOR_10624E5)
        if size(x18) == ZERO:
            continue
        x19 = x6
        if x14:
            x19 = hmirror(x19)
        if x15:
            x19 = vmirror(x19)
        x20 = foreground_objects_10624e5(x19, x0)
        x21 = merge(x20)
        x22 = first(colorfilter(x20, ANCHOR_10624E5))
        x23 = height(first(x18))
        x24 = scale_object_10624e5(x21, x23, x9)
        x25 = scale_object_10624e5(x22, x23, x9)
        x26 = subtract(add(x12, ulcorner(first(x18))), ulcorner(x25))
        x27 = shift(x24, x26)
        x11 = paint(x11, x27)
    return x11
