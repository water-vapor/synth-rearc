from arc2.core import *


def _push_rows_2faf500b(G: Grid) -> Grid:
    x0 = width(G)
    x1 = halve(x0)
    x2 = []
    for x3 in G:
        x4 = x3.index(SIX)
        x5 = subtract(subtract(x0, x4), ONE)
        x6 = combine(repeat(NINE, x4), repeat(ZERO, subtract(x1, x4)))
        x7 = combine(repeat(ZERO, subtract(x1, x5)), repeat(NINE, x5))
        x8 = combine(x6, repeat(ZERO, TWO))
        x9 = combine(x8, x7)
        x2.append(x9)
    return tuple(x2)


def _transform_local_2faf500b(G: Grid) -> Grid:
    x0 = portrait(G)
    x1 = branch(x0, dmirror(G), G)
    x2 = _push_rows_2faf500b(x1)
    x3 = branch(x0, dmirror(x2), x2)
    return x3


def _transform_object_2faf500b(I: Grid, O: Object) -> Object:
    x0 = subgrid(O, I)
    x1 = portrait(x0)
    x2 = _transform_local_2faf500b(x0)
    x3 = ofcolor(x2, NINE)
    x4 = recolor(NINE, x3)
    x5 = branch(x1, decrement(uppermost(O)), uppermost(O))
    x6 = branch(x1, leftmost(O), decrement(leftmost(O)))
    x7 = astuple(x5, x6)
    x8 = shift(x4, x7)
    return x8


def verify_2faf500b(I: Grid) -> Grid:
    x0 = objects(I, F, F, T)
    x1 = canvas(ZERO, shape(I))
    x2 = tuple(_transform_object_2faf500b(I, x3) for x3 in x0)
    x3 = merge(x2)
    x4 = paint(x1, x3)
    return x4
