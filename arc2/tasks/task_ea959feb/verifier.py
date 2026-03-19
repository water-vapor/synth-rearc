from arc2.core import *


def _normalize_color_ea959feb(
    value: Integer,
    row_index: Integer,
    period: Integer,
) -> Integer:
    return ((value - row_index - ONE) % period) + ONE


def _horizontal_period_ea959feb(
    sequence: tuple[Integer, ...],
) -> Integer:
    x0 = len(sequence)
    for x1 in range(ONE, x0 + ONE):
        if all(sequence[x2] == sequence[x2 % x1] for x2 in range(x0)):
            return x1
    return x0


def verify_ea959feb(I: Grid) -> Grid:
    x0 = height(I)
    x1 = width(I)
    x2 = max(max(row) for row in I)
    x3 = tuple(
        tuple(_normalize_color_ea959feb(I[x4][x5], x4, x2) for x4 in range(x0))
        for x5 in range(x1)
    )
    x4 = tuple(mostcommon(x5) for x5 in x3)
    x5 = _horizontal_period_ea959feb(x4)
    x6 = x4[:x5]
    x7 = tuple(
        tuple((((x6[x8 % x5] + x9 - ONE) % x2) + ONE) for x8 in range(x1))
        for x9 in range(x0)
    )
    return x7
