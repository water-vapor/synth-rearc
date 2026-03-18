from arc2.core import *


def _normalize_f9a67cb5(
    grid: Grid,
) -> tuple[Grid, callable]:
    x0 = ofcolor(grid, TWO)
    x1 = first(x0)
    x2 = height(grid)
    x3 = width(grid)
    if last(x1) == ZERO:
        return grid, identity
    if last(x1) == decrement(x3):
        return vmirror(grid), vmirror
    if first(x1) == ZERO:
        return rot270(grid), rot90
    if first(x1) == decrement(x2):
        return rot90(grid), rot270
    return grid, identity


def verify_f9a67cb5(I: Grid) -> Grid:
    x0, x1 = _normalize_f9a67cb5(I)
    x2 = height(x0)
    x3 = width(x0)
    x4 = set(ofcolor(x0, TWO))
    x5 = [first(x4)]
    x6 = set()
    while len(x5) > ZERO:
        x7 = x5.pop()
        if x7 in x6:
            continue
        x6.add(x7)
        x8, x9 = x7
        x10 = None
        for x11 in range(x9 + ONE, x3):
            if x0[x8][x11] == EIGHT:
                x10 = x11
                break
        if x10 is None:
            x4 |= set(connect(x7, (x8, decrement(x3))))
            continue
        x4 |= set(connect(x7, (x8, decrement(x10))))
        x12 = tuple(i for i in range(x2) if x0[i][x10] != EIGHT)
        x13 = tuple(i for i in x12 if i < x8)
        x14 = tuple(i for i in x12 if i > x8)
        x15 = last(x13) if len(x13) > ZERO else ZERO
        x16 = first(x14) if len(x14) > ZERO else decrement(x2)
        x17 = connect((x15, decrement(x10)), (x16, decrement(x10)))
        x4 |= set(x17)
        if len(x13) > ZERO:
            x18 = (x15, x10)
            x4.add(x18)
            x5.append(x18)
        if len(x14) > ZERO:
            x19 = (x16, x10)
            x4.add(x19)
            x5.append(x19)
    x20 = fill(x0, TWO, frozenset(x4))
    return x1(x20)
