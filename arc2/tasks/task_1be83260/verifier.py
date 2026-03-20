from arc2.core import *


def verify_1be83260(I: Grid) -> Grid:
    x0 = asindices(I)
    x1 = ofcolor(I, ZERO)
    x2 = difference(x0, x1)
    x3 = subgrid(x2, I)
    x4 = height(x3)
    x5 = width(x3)
    x6 = tuple(i for i, row in enumerate(x3) if all(value == ZERO for value in row))
    x7 = tuple(j for j in range(x5) if all(row[j] == ZERO for row in x3))
    x8 = (-ONE,) + x6 + (x4,)
    x9 = (-ONE,) + x7 + (x5,)
    x10 = tuple((a + ONE, b) for a, b in zip(x8, x8[ONE:]) if a + ONE < b)
    x11 = tuple((a + ONE, b) for a, b in zip(x9, x9[ONE:]) if a + ONE < b)
    x12 = x10[ZERO][ONE] - x10[ZERO][ZERO]
    x13 = x11[ZERO][ONE] - x11[ZERO][ZERO]
    x14 = tuple(v for row in x3 for v in row if v != ZERO)
    x15 = mostcommon(x14)
    x16 = tuple(crop(x3, (a, b), (x12, x13)) for a, _ in x10 for b, _ in x11)
    x17 = extract(x16, lambda g: all(value in (ZERO, x15) for row in g for value in row))
    x18 = extract(x16, lambda g: any(value not in (ZERO, x15) for row in g for value in row))
    x19 = ofcolor(x17, x15)
    x20 = tuple(a for a, _ in x10)
    x21 = tuple(a for a, _ in x11)
    x22 = tuple(range(ONE, x12, TWO))
    x23 = tuple(range(ONE, x13, TWO))
    x24 = canvas(x15, shape(x3))
    for a, i in enumerate(x20):
        for b, j in enumerate(x21):
            x25 = x18[x22[a]][x23[b]]
            x26 = branch(equality(x25, ZERO), x15, x25)
            x27 = shift(x19, (i, j))
            x24 = fill(x24, x26, x27)
    return x24
