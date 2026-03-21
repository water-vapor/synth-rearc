from arc2.core import *


RIGHT_MARKER_9BEBAE7A = frozenset({
    (ZERO, ZERO),
    (ZERO, ONE),
    (ZERO, TWO),
    (ONE, ONE),
    (TWO, ONE),
})
LEFT_MARKER_9BEBAE7A = frozenset({
    (ZERO, ONE),
    (ONE, ONE),
    (TWO, ZERO),
    (TWO, ONE),
    (TWO, TWO),
})
UP_MARKER_9BEBAE7A = frozenset({
    (ZERO, ONE),
    (ONE, ZERO),
    (ONE, ONE),
    (ONE, TWO),
    (ONE, THREE),
    (TWO, ONE),
})
DOWN_MARKER_9BEBAE7A = frozenset({
    (ZERO, TWO),
    (ONE, ZERO),
    (ONE, ONE),
    (ONE, TWO),
    (ONE, THREE),
    (TWO, TWO),
})


def verify_9bebae7a(I: Grid) -> Grid:
    x0 = fgpartition(I)
    x1 = first(colorfilter(x0, FOUR))
    x2 = first(colorfilter(x0, SIX))
    x3 = normalize(toindices(x2))
    x4 = cover(I, x2)
    if x3 == RIGHT_MARKER_9BEBAE7A:
        x5 = vmirror(x1)
        x6 = shift(x5, (ZERO, width(x1)))
    elif x3 == LEFT_MARKER_9BEBAE7A:
        x5 = vmirror(x1)
        x6 = shift(x5, (ZERO, -width(x1)))
    elif x3 == UP_MARKER_9BEBAE7A:
        x5 = hmirror(x1)
        x6 = shift(x5, (-height(x1), ZERO))
    else:
        x5 = hmirror(x1)
        x6 = shift(x5, (height(x1), ZERO))
    x7 = paint(x4, x6)
    return x7
