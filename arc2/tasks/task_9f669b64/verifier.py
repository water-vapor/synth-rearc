from arc2.core import *


def verify_9f669b64(I: Grid) -> Grid:
    x0 = tuple(objects(I, T, F, T))
    x1 = min(x0, key=lambda obj: (max(shape(obj)), size(obj), color(obj)))
    x2 = tuple(obj for obj in x0 if obj != x1)
    x3 = min(
        x2,
        key=lambda obj: (
            ZERO if size(obj) == height(obj) * width(obj) else ONE,
            -color(obj),
        ),
    )
    x4 = first(tuple(obj for obj in x2 if obj != x3))
    x5 = ulcorner(x3)
    x6 = lrcorner(x3)
    x7 = shape(x3)
    x8 = color(x3)
    if x7[ONE] >= x7[ZERO]:
        x9 = x7[ONE] // TWO
        x10 = frozenset(
            (i, j - ONE)
            for i in range(x5[ZERO], x6[ZERO] + ONE)
            for j in range(x5[ONE], x5[ONE] + x9)
        )
        x11 = frozenset(
            (i, j + ONE)
            for i in range(x5[ZERO], x6[ZERO] + ONE)
            for j in range(x5[ONE] + x9, x6[ONE] + ONE)
        )
        x12 = recolor(x8, combine(x10, x11))
    else:
        x9 = x7[ZERO] // TWO
        x10 = frozenset(
            (i - ONE, j)
            for i in range(x5[ZERO], x5[ZERO] + x9)
            for j in range(x5[ONE], x6[ONE] + ONE)
        )
        x11 = frozenset(
            (i + ONE, j)
            for i in range(x5[ZERO] + x9, x6[ZERO] + ONE)
            for j in range(x5[ONE], x6[ONE] + ONE)
        )
        x12 = recolor(x8, combine(x10, x11))
    x13 = lrcorner(x1)
    x14 = shape(x1)
    x15 = shape(I)
    x16 = x15[ZERO] - x14[ZERO]
    x17 = x15[ONE] - x14[ONE]
    x18 = max(ZERO, min(x5[ZERO] + x6[ZERO] - x13[ZERO], x16))
    x19 = max(ZERO, min(x5[ONE] + x6[ONE] - x13[ONE], x17))
    x20 = shift(normalize(x1), (x18, x19))
    x21 = mostcolor(I)
    x22 = canvas(x21, x15)
    x23 = paint(x22, x4)
    x24 = paint(x23, x12)
    x25 = paint(x24, x20)
    return x25
