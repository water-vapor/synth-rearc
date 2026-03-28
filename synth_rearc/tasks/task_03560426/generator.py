from synth_rearc.core import *


def _bounded_parts_03560426(
    total: Integer,
    count: Integer,
    lower: Integer,
    upper: Integer,
) -> Tuple:
    parts = []
    remaining = total
    for idx in range(count - 1):
        slots_left = count - idx - 1
        lo = max(lower, remaining - upper * slots_left)
        hi = min(upper, remaining - lower * slots_left)
        parts.append(randint(lo, hi))
        remaining -= parts[-1]
    parts.append(remaining)
    shuffle(parts)
    return tuple(parts)


def _rect_object_03560426(
    color_value: Integer,
    height_value: Integer,
    width_value: Integer,
) -> Object:
    x0 = frozenset({(ZERO, ZERO), (height_value - ONE, width_value - ONE)})
    x1 = backdrop(x0)
    x2 = recolor(color_value, x1)
    return x2


def _compose_chain_03560426(
    objs: Tuple,
    dims: IntegerTuple,
) -> Grid:
    x0 = canvas(ZERO, dims)
    x1 = (ZERO, ZERO)
    x2 = x0
    for x3 in objs:
        x4 = shift(normalize(x3), x1)
        x2 = paint(x2, x4)
        x1 = lrcorner(x4)
    return x2


def generate_03560426(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    dims = (TEN, TEN)
    colors = remove(ZERO, interval(ZERO, TEN, ONE))
    while True:
        count = choice((THREE, THREE, FOUR))
        total_width = unifint(diff_lb, diff_ub, (SEVEN, EIGHT)) if count == THREE else unifint(diff_lb, diff_ub, (SIX, SEVEN))
        total_height = unifint(diff_lb, diff_ub, (EIGHT, 11)) if count == THREE else unifint(diff_lb, diff_ub, (NINE, 12))
        widths = _bounded_parts_03560426(total_width, count, ONE, FOUR)
        heights = _bounded_parts_03560426(total_height, count, TWO, FIVE)
        if maximum(widths) == ONE:
            continue
        if maximum(heights) == TWO:
            continue
        palette_values = tuple(sample(colors, count))
        objs = []
        left = ZERO
        gi = canvas(ZERO, dims)
        for color_value, height_value, width_value in zip(palette_values, heights, widths):
            obj = _rect_object_03560426(color_value, height_value, width_value)
            placed = shift(obj, (TEN - height_value, left))
            gi = paint(gi, placed)
            objs.append(placed)
            left += width_value + ONE
        go = _compose_chain_03560426(tuple(objs), dims)
        if gi == go:
            continue
        return {"input": gi, "output": go}
