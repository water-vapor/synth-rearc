from arc2.core import *


def verify_2753e76c(I: Grid) -> Grid:
    x0 = objects(I, T, F, T)
    x1 = fgpartition(I)
    x2 = order(x1, lambda x3: (invert(size(colorfilter(x0, color(x3)))), color(x3)))
    x3 = apply(lambda x4: size(colorfilter(x0, color(x4))), x2)
    x4 = maximum(x3)
    x5 = papply(
        lambda x6, x7: fill(
            canvas(ZERO, (ONE, x4)),
            color(x6),
            connect((ZERO, subtract(x4, x7)), (ZERO, decrement(x4))),
        ),
        x2,
        x3,
    )
    x8 = first(x5)
    for x9 in x5[ONE:]:
        x8 = vconcat(x8, x9)
    return x8
