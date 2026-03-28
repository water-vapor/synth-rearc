from synth_rearc.core import *


def _split_positive_4364c1c4(
    total: Integer,
    count: Integer,
) -> Tuple:
    if count == ONE:
        return (total,)
    x0 = tuple(sorted(sample(interval(ONE, total, ONE), count - ONE)))
    x1 = (ZERO,) + x0 + (total,)
    x2 = tuple(x1[idx + ONE] - x1[idx] for idx in range(count))
    return x2


def _split_nonnegative_4364c1c4(
    total: Integer,
    count: Integer,
) -> Tuple:
    if count == ONE:
        return (total,)
    x0 = tuple(sorted(sample(interval(ONE, total + count, ONE), count - ONE)))
    x1 = (ZERO,) + x0 + (total + count,)
    x2 = tuple(x1[idx + ONE] - x1[idx] - ONE for idx in range(count))
    return x2


def _profile_4364c1c4(
    height_value: Integer,
    width_value: Integer,
) -> Tuple:
    x0 = min(THREE, width_value)
    x1 = min(choice((ONE, TWO, TWO, THREE)), x0)
    x2 = _split_positive_4364c1c4(width_value, x1)
    x3 = [randint(ONE, height_value) for _ in x2]
    if max(x3) < height_value:
        x4 = randint(ZERO, len(x3) - ONE)
        x3[x4] = height_value
    if len(x3) > ONE and min(x3) == height_value and height_value > ONE:
        x4 = randint(ZERO, len(x3) - ONE)
        x3[x4] = randint(ONE, height_value - ONE)
    x5 = []
    for x6, x7 in zip(x2, x3):
        x5.extend((x7,) * x6)
    return tuple(x5)


def _profile_object_4364c1c4(
    color_value: Integer,
    profile: Tuple,
    top_aligned: Boolean,
) -> Object:
    x0 = max(profile)
    x1 = set()
    for x2, x3 in enumerate(profile):
        x4 = range(x3) if top_aligned else range(x0 - x3, x0)
        for x5 in x4:
            x1.add((x5, x2))
    x6 = frozenset(x1)
    x7 = recolor(color_value, x6)
    return x7


def _pair_objects_4364c1c4(
    top_color: Integer,
    bottom_color: Integer,
    max_width: Integer,
    max_height: Integer,
) -> Tuple[Object, Object]:
    x0 = randint(THREE, max_width)
    x1 = randint(ONE, max_height)
    x2 = randint(ONE, max_height)
    x3 = _profile_4364c1c4(x1, x0)
    x4 = _profile_4364c1c4(x2, x0)
    x5 = _profile_object_4364c1c4(top_color, x3, F)
    x6 = _profile_object_4364c1c4(bottom_color, x4, T)
    x7 = shift(x6, (x1, ZERO))
    return x5, x7


def generate_4364c1c4(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    x0 = choice((ONE, ONE, TWO))
    x1 = unifint(diff_lb, diff_ub, (12, 17))
    x2 = unifint(diff_lb, diff_ub, (12, 16))
    x3 = unifint(diff_lb, diff_ub, (ZERO, NINE))
    x4 = remove(x3, interval(ZERO, TEN, ONE))
    while True:
        x5 = []
        for _ in range(x0):
            x6 = tuple(sample(x4, TWO))
            x7, x8 = _pair_objects_4364c1c4(x6[ZERO], x6[ONE], min(SEVEN, x2 - TWO), FIVE)
            x9 = lowermost(x8) + ONE
            x10 = rightmost(x7) + ONE
            x5.append((x7, x8, x9, x10))
        if x0 == ONE:
            x11 = first(x5)
            x12 = x1 - x11[TWO] - TWO
            if x12 < ZERO:
                continue
            x13, x14 = _split_nonnegative_4364c1c4(x12, TWO)
            x15 = (ONE + x13,)
        else:
            x11, x12 = x5
            x13 = x1 - x11[TWO] - x12[TWO] - THREE
            if x13 < ZERO:
                continue
            x14, x15, x16 = _split_nonnegative_4364c1c4(x13, THREE)
            x17 = ONE + x14
            x18 = x17 + x11[TWO] + ONE + x15
            x15 = (x17, x18)
        x19 = canvas(x3, (x1, x2))
        x20 = canvas(x3, (x1, x2))
        for x21, x22 in zip(x5, x15):
            x23 = x21[THREE]
            x24 = randint(ONE, x2 - x23 - ONE)
            x25 = shift(x21[ZERO], (x22, x24))
            x26 = shift(x21[ONE], (x22, x24))
            x19 = paint(x19, x25)
            x19 = paint(x19, x26)
            x20 = paint(x20, shift(x25, LEFT))
            x20 = paint(x20, shift(x26, RIGHT))
        return {"input": x19, "output": x20}
