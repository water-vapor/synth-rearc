from arc2.core import *


def _border_side_13713586(
    I: Grid,
) -> Integer:
    x0 = ofcolor(I, FIVE)
    x1 = height(I)
    x2 = width(I)
    x3 = decrement(x1)
    x4 = decrement(x2)
    if len(x0) == x2 and uppermost(x0) == ZERO and lowermost(x0) == ZERO:
        return ZERO
    if len(x0) == x2 and uppermost(x0) == x3 and lowermost(x0) == x3:
        return ONE
    if len(x0) == x1 and leftmost(x0) == ZERO and rightmost(x0) == ZERO:
        return TWO
    return THREE


def _distance_13713586(
    I: Grid,
    obj: Object,
    side: Integer,
) -> Integer:
    x0 = decrement(height(I))
    x1 = decrement(width(I))
    if side == ZERO:
        return uppermost(obj)
    if side == ONE:
        return subtract(x0, lowermost(obj))
    if side == TWO:
        return leftmost(obj)
    return subtract(x1, rightmost(obj))


def _span_13713586(
    I: Grid,
    obj: Object,
    side: Integer,
) -> Indices:
    x0 = uppermost(obj)
    x1 = lowermost(obj)
    x2 = leftmost(obj)
    x3 = rightmost(obj)
    x4 = decrement(decrement(height(I)))
    x5 = decrement(decrement(width(I)))
    if side == ZERO:
        x6 = frozenset({(ONE, x2), (x1, x3)})
    elif side == ONE:
        x6 = frozenset({(x0, x2), (x4, x3)})
    elif side == TWO:
        x6 = frozenset({(x0, ONE), (x1, x3)})
    else:
        x6 = frozenset({(x0, x2), (x1, x5)})
    return backdrop(x6)


def verify_13713586(
    I: Grid,
) -> Grid:
    x0 = objects(I, T, F, T)
    x1 = extract(x0, matcher(color, FIVE))
    x2 = remove(x1, x0)
    x3 = _border_side_13713586(I)
    x4 = order(
        x2,
        lambda x5: (
            invert(_distance_13713586(I, x5, x3)),
            uppermost(x5),
            leftmost(x5),
        ),
    )
    x5 = I
    for x6 in x4:
        x7 = _span_13713586(I, x6, x3)
        x5 = fill(x5, color(x6), x7)
    return x5
