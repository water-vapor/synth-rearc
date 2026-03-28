from synth_rearc.core import *


RECT_HEIGHTS_9B4C17C4 = (ONE, TWO, TWO, TWO, THREE, THREE, FOUR)
RECT_WIDTHS_9B4C17C4 = (ONE, TWO, TWO, TWO, THREE, THREE, FOUR)


def _rect_patch_9b4c17c4(
    top: Integer,
    left: Integer,
    h: Integer,
    w: Integer,
) -> Indices:
    x0 = interval(top, add(top, h), ONE)
    x1 = interval(left, add(left, w), ONE)
    x2 = product(x0, x1)
    return x2


def _pack_segment_9b4c17c4(
    bg: Integer,
    length: Integer,
    count: Integer,
) -> Tuple:
    x0 = branch(
        equality(bg, ONE),
        repeat(ONE, subtract(length, count)) + repeat(TWO, count),
        repeat(TWO, count) + repeat(EIGHT, subtract(length, count)),
    )
    return x0


def _render_output_9b4c17c4(
    gi: Grid,
    vertical: Boolean,
    split: Integer,
    first_bg: Integer,
) -> Grid:
    x0 = branch(equality(first_bg, ONE), EIGHT, ONE)
    x1 = []
    if vertical:
        for x2 in gi:
            x3 = colorcount((x2[:split],), TWO)
            x4 = colorcount((x2[split:],), TWO)
            x5 = _pack_segment_9b4c17c4(first_bg, split, x3)
            x6 = _pack_segment_9b4c17c4(x0, subtract(len(x2), split), x4)
            x1.append(x5 + x6)
        return tuple(x1)
    x2 = width(gi)
    for x3, x4 in enumerate(gi):
        x5 = colorcount((x4,), TWO)
        x6 = branch(x3 < split, first_bg, x0)
        x7 = _pack_segment_9b4c17c4(x6, x2, x5)
        x1.append(x7)
    return tuple(x1)


def _choose_region_count_9b4c17c4(
    region_h: Integer,
    region_w: Integer,
) -> Integer:
    x0 = multiply(region_h, region_w)
    if x0 < 28:
        return choice((ONE, TWO, TWO))
    return choice((ONE, TWO, TWO, THREE))


def _region_margin_patch_9b4c17c4(
    top: Integer,
    left: Integer,
    h: Integer,
    w: Integer,
    bounds: Tuple,
) -> FrozenSet:
    x0, x1, x2, x3 = bounds
    x4 = max(x0, subtract(top, ONE))
    x5 = min(add(x0, x2), increment(add(top, h)))
    x6 = max(x1, subtract(left, ONE))
    x7 = min(add(x1, x3), increment(add(left, w)))
    return frozenset((i, j) for i in range(x4, x5) for j in range(x6, x7))


def _place_region_rectangles_9b4c17c4(
    gi: Grid,
    bounds: Tuple,
    count: Integer,
) -> Grid:
    x0, x1, x2, x3 = bounds
    x4 = set()
    x5 = gi
    x6 = min(FOUR, max(ONE, subtract(x2, ONE)))
    x7 = min(FOUR, max(ONE, subtract(x3, ONE)))
    x8 = tuple(x9 for x9 in RECT_HEIGHTS_9B4C17C4 if x9 <= x6)
    x9 = tuple(x10 for x10 in RECT_WIDTHS_9B4C17C4 if x10 <= x7)
    for _ in range(count):
        x10 = F
        for _ in range(80):
            x11 = choice(x8)
            x12 = choice(x9)
            x13 = randint(x0, subtract(add(x0, x2), x11))
            x14 = randint(x1, subtract(add(x1, x3), x12))
            x15 = _rect_patch_9b4c17c4(x13, x14, x11, x12)
            x16 = _region_margin_patch_9b4c17c4(x13, x14, x11, x12, bounds)
            if any(x17 in x4 for x17 in x16):
                continue
            x5 = fill(x5, TWO, x15)
            x4.update(x16)
            x10 = T
            break
        if not x10:
            return None
    return x5


def generate_9b4c17c4(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = choice((T, F))
        x1 = unifint(diff_lb, diff_ub, (NINE, 15))
        x2 = unifint(diff_lb, diff_ub, (NINE, 15))
        x3 = choice((ONE, EIGHT))
        if x0:
            x4 = unifint(diff_lb, diff_ub, (FOUR, subtract(x2, FOUR)))
            x5 = branch(equality(x3, ONE), EIGHT, ONE)
            x6 = canvas(x3, (x1, x4))
            x7 = canvas(x5, (x1, subtract(x2, x4)))
            gi = hconcat(x6, x7)
            x8 = ((ZERO, ZERO, x1, x4), (ZERO, x4, x1, subtract(x2, x4)))
        else:
            x4 = unifint(diff_lb, diff_ub, (FOUR, subtract(x1, FOUR)))
            x5 = branch(equality(x3, ONE), EIGHT, ONE)
            x6 = canvas(x3, (x4, x2))
            x7 = canvas(x5, (subtract(x1, x4), x2))
            gi = vconcat(x6, x7)
            x8 = ((ZERO, ZERO, x4, x2), (x4, ZERO, subtract(x1, x4), x2))
        x9 = _choose_region_count_9b4c17c4(x8[ZERO][TWO], x8[ZERO][THREE])
        x10 = _choose_region_count_9b4c17c4(x8[ONE][TWO], x8[ONE][THREE])
        gi = _place_region_rectangles_9b4c17c4(gi, x8[ZERO], x9)
        if gi is None:
            continue
        gi = _place_region_rectangles_9b4c17c4(gi, x8[ONE], x10)
        if gi is None:
            continue
        x11 = _render_output_9b4c17c4(gi, x0, x4, x3)
        x12 = colorcount(gi, TWO)
        if x12 < FIVE or x12 > 24:
            continue
        if gi == x11:
            continue
        return {"input": gi, "output": x11}
