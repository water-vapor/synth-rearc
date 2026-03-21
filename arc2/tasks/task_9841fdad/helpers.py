from arc2.core import *


def make_rect_object_9841fdad(
    value: Integer,
    top: Integer,
    left: Integer,
    obj_height: Integer,
    obj_width: Integer,
) -> Object:
    return frozenset(
        (value, (i, j))
        for i in range(top, top + obj_height)
        for j in range(left, left + obj_width)
    )


def project_panel_object_9841fdad(
    left_width: Integer,
    right_width: Integer,
    obj: Object,
) -> Object:
    x0 = color(obj)
    x1 = leftmost(obj)
    x2 = width(obj)
    x3 = subtract(left_width, TWO)
    x4 = subtract(right_width, TWO)
    if x2 == x3:
        x5 = frozenset(i for i, _ in toindices(obj))
        return frozenset((x0, (i, j)) for i in x5 for j in range(ONE, subtract(right_width, ONE)))
    x5 = subtract(x3, x2)
    x6 = subtract(x4, x2)
    x7 = branch(
        equality(x5, ZERO),
        ONE,
        add(ONE, round((subtract(x1, ONE) * x6) / x5)),
    )
    return shift(obj, (ZERO, subtract(x7, x1)))
