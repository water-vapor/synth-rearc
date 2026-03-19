from arc2.core import *


def _turn_clockwise_e5790162(direction: IntegerTuple) -> IntegerTuple:
    return {
        RIGHT: DOWN,
        DOWN: LEFT,
        LEFT: UP,
        UP: RIGHT,
    }[direction]


def _turn_counterclockwise_e5790162(direction: IntegerTuple) -> IntegerTuple:
    return {
        RIGHT: UP,
        UP: LEFT,
        LEFT: DOWN,
        DOWN: RIGHT,
    }[direction]


def verify_e5790162(I: Grid) -> Grid:
    x0 = ofcolor(I, THREE)
    x1 = first(x0)
    x2 = I
    x3 = x1
    x4 = RIGHT
    x5 = height(I)
    x6 = width(I)
    while True:
        x7 = add(x3, x4)
        x8 = x3
        while (
            ZERO <= x7[0] < x5
            and ZERO <= x7[1] < x6
            and index(I, x7) == ZERO
        ):
            x8 = x7
            x7 = add(x7, x4)
        x2 = fill(x2, THREE, connect(x3, x8))
        if not (ZERO <= x7[0] < x5 and ZERO <= x7[1] < x6):
            return x2
        x9 = index(I, x7)
        if x9 == SIX:
            x4 = _turn_clockwise_e5790162(x4)
        elif x9 == EIGHT:
            x4 = _turn_counterclockwise_e5790162(x4)
        else:
            return x2
        x3 = x8
