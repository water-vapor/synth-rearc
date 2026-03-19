from arc2.core import *


def exterior_background_15663ba9(
    I: Grid,
) -> Indices:
    x0 = objects(I, T, F, F)
    x1 = colorfilter(x0, ZERO)
    x2 = sfilter(x1, lambda x3: bordering(x3, I))
    x3 = mapply(toindices, x2)
    return x3


def corner_mark_15663ba9(
    I: Grid,
    x0: IntegerTuple,
    x1: Integer,
    x2: Indices,
) -> Integer | None:
    x3 = equality(index(I, add(x0, UP)), x1)
    x4 = equality(index(I, add(x0, DOWN)), x1)
    x5 = equality(index(I, add(x0, LEFT)), x1)
    x6 = equality(index(I, add(x0, RIGHT)), x1)
    x7 = sum((x3, x4, x5, x6))
    if not equality(x7, TWO):
        return None
    x8 = either(both(x3, x4), both(x5, x6))
    if x8:
        return None
    if both(x3, x6):
        x9 = add(x0, DOWN_LEFT)
    elif both(x3, x5):
        x9 = add(x0, UNITY)
    elif both(x4, x6):
        x9 = add(x0, NEG_UNITY)
    else:
        x9 = add(x0, UP_RIGHT)
    x10 = equality(index(I, x9), ZERO)
    x11 = contained(x9, x2)
    x12 = both(x10, flip(x11))
    x13 = branch(x12, TWO, FOUR)
    return x13

def _notched_rectangle_outline_15663ba9(
    height_value: Integer,
    width_value: Integer,
    side_name: str,
) -> Indices:
    x0 = box(asindices(canvas(ZERO, (height_value, width_value))))
    if equality(side_name, "top"):
        x1 = randint(TWO, width_value - FIVE)
        x2 = randint(x1 + TWO, width_value - THREE)
        x3 = randint(TWO, height_value - THREE)
        x4 = connect((ZERO, x1), (ZERO, x2))
        x5 = connect((ZERO, x1), (x3, x1))
        x6 = connect((x3, x1), (x3, x2))
        x7 = connect((ZERO, x2), (x3, x2))
        x8 = difference(x0, x4)
        x9 = combine(x5, combine(x6, x7))
        x10 = combine(x8, x9)
        return x10
    if equality(side_name, "bottom"):
        x1 = randint(TWO, width_value - FIVE)
        x2 = randint(x1 + TWO, width_value - THREE)
        x3 = randint(TWO, height_value - THREE)
        x4 = decrement(height_value)
        x5 = subtract(x4, x3)
        x6 = connect((x4, x1), (x4, x2))
        x7 = connect((x4, x1), (x5, x1))
        x8 = connect((x5, x1), (x5, x2))
        x9 = connect((x4, x2), (x5, x2))
        x10 = difference(x0, x6)
        x11 = combine(x7, combine(x8, x9))
        x12 = combine(x10, x11)
        return x12
    if equality(side_name, "left"):
        x1 = randint(TWO, height_value - FIVE)
        x2 = randint(x1 + TWO, height_value - THREE)
        x3 = randint(TWO, width_value - THREE)
        x4 = connect((x1, ZERO), (x2, ZERO))
        x5 = connect((x1, ZERO), (x1, x3))
        x6 = connect((x1, x3), (x2, x3))
        x7 = connect((x2, ZERO), (x2, x3))
        x8 = difference(x0, x4)
        x9 = combine(x5, combine(x6, x7))
        x10 = combine(x8, x9)
        return x10
    x1 = randint(TWO, height_value - FIVE)
    x2 = randint(x1 + TWO, height_value - THREE)
    x3 = randint(TWO, width_value - THREE)
    x4 = decrement(width_value)
    x5 = subtract(x4, x3)
    x6 = connect((x1, x4), (x2, x4))
    x7 = connect((x1, x4), (x1, x5))
    x8 = connect((x1, x5), (x2, x5))
    x9 = connect((x2, x4), (x2, x5))
    x10 = difference(x0, x6)
    x11 = combine(x7, combine(x8, x9))
    x12 = combine(x10, x11)
    return x12


def sample_component_outline_15663ba9(
    height_value: Integer,
    width_value: Integer,
    require_notch: Boolean,
) -> tuple[Indices, Boolean]:
    x0 = box(asindices(canvas(ZERO, (height_value, width_value))))
    x1 = greater(height_value, SIX)
    x2 = greater(width_value, SIX)
    x3 = both(x1, x2)
    x4 = both(x3, choice((F, F, T)))
    x1 = branch(require_notch, T, x4)
    if not x1:
        return x0, F
    x2 = choice(("top", "bottom", "left", "right"))
    x3 = _notched_rectangle_outline_15663ba9(height_value, width_value, x2)
    return x3, T
