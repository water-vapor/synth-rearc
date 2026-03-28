from collections import Counter

from synth_rearc.core import *


def verify_f3e14006(I: Grid) -> Grid:
    x0 = height(I)
    x1 = width(I)
    x2 = tuple(sum(v != ZERO for v in row) for row in I)
    x3 = x2.index(max(x2))
    x4 = tuple(tuple(I[i][j] for i in range(x0)) for j in range(x1))
    x5 = tuple(sum(v != ZERO for v in col) for col in x4)
    x6 = x5.index(max(x5))
    x7 = tuple(v for v in I[x3] if v != ZERO)
    x8 = tuple(I[i][x6] for i in range(x0) if I[i][x6] != ZERO)
    x9 = Counter(x7)
    x10 = Counter(x8)
    x11 = x9.most_common(ONE)[ZERO][ZERO]
    x12 = x10.most_common(ONE)[ZERO][ZERO]
    x13 = Counter(v for v in x7 if v != x11).most_common(ONE)[ZERO][ZERO]
    x14 = Counter(v for v in x8 if v != x12).most_common(ONE)[ZERO][ZERO]
    x15 = tuple(j for j, v in enumerate(I[x3]) if v == x13)
    x16 = min(x15)
    x17 = max(x15)
    x18 = tuple(i for i in range(x0) if I[i][x6] == x14)
    x19 = max(x18) < x3
    x20 = branch(x19, min(x18), x3)
    x21 = branch(x19, x3, max(x18))
    x22 = branch(x19, max(x18), min(x18))
    x23 = index(I, (x3, x6))
    x24 = canvas(ZERO, shape(I))
    x25 = tuple(j for j in range(x16, x17 + ONE) if even(j - x16))
    x26 = tuple(j for j in range(x16, x17 + ONE) if not even(j - x16))
    x27 = tuple(i for i in range(x20, x21 + ONE) if even(i - x20))
    x28 = tuple(i for i in range(x20, x21 + ONE) if not even(i - x20))
    if x19:
        x29 = tuple(i for i in x27 if i > x22)
        x30 = tuple(i for i in x27 if i < x22)
    else:
        x29 = tuple(i for i in x27 if i < x22)
        x30 = tuple(i for i in x27 if i > x22)
    x31 = initset(x22) if contained(x22, x27) else frozenset()
    x32 = fill(x24, x11, product(x28, x25))
    x33 = fill(x32, x23, product(x28, x26))
    x34 = fill(x33, x13, product(x29, x25))
    x35 = fill(x34, x12, product(x29, x26))
    x36 = fill(x35, x14, product(x30, x25))
    x37 = fill(x36, x12, product(x30, x26))
    x38 = fill(x37, x14, product(x31, x25))
    x39 = fill(x38, x23, product(x31, x26))
    return x39
