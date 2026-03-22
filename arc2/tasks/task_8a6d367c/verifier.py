from arc2.core import *


def verify_8a6d367c(
    I: Grid,
) -> Grid:
    x0 = objects(I, T, T, T)
    x1 = lambda x: both(greater(height(x), TWO), greater(width(x), TWO))
    x2 = lambda x: equality(toindices(x), box(x))
    x3 = fork(both, x1, x2)
    x4 = sfilter(x0, x3)
    x5 = argmax(x4, size)
    x6 = subgrid(x5, I)
    x7 = color(x5)
    x8 = remove(EIGHT, palette(x6))
    x9 = other(x8, x7)
    x10 = trim(x6)
    x11 = ofcolor(x10, x9)
    x12 = uppermost(x5)
    x13 = lambda x: greater(x12, uppermost(x))
    x14 = order(sfilter(x0, x13), ulcorner)
    x15 = height(x10)
    x16 = width(x10)
    x17 = lambda x: equality(multiply(height(x), divide(x15, height(x))), x15)
    x18 = lambda x: equality(multiply(width(x), divide(x16, width(x))), x16)
    x19 = lambda x: equality(divide(x15, height(x)), divide(x16, width(x)))
    x20 = fork(both, fork(both, x17, x18), x19)
    x21 = lambda x: equality(
        x11,
        intersection(
            x11,
            toindices(
                upscale(
                    recolor(x9, normalize(x)),
                    divide(x15, height(x)),
                )
            ),
        ),
    )
    x22 = fork(both, x20, x21)
    x23 = extract(x14, x22)
    x24 = divide(x15, height(x23))
    x25 = recolor(x9, normalize(x23))
    x26 = upscale(x25, x24)
    x27 = shift(x26, UNITY)
    x28 = canvas(EIGHT, shape(x5))
    x29 = paint(x28, x27)
    x30 = normalize(x5)
    x31 = paint(x29, x30)
    return x31
