from arc2.core import *


def verify_1b59e163(I: Grid) -> Grid:
    x0 = mostcolor(I)
    x1 = objects(I, F, T, T)
    x2 = sizefilter(x1, ONE)
    x3 = difference(x1, x2)
    x4 = sfilter(x3, compose(flip, matcher(numcolors, ONE)))
    x5 = canvas(x0, shape(I))

    def x6(x7: Object) -> Object:
        x8 = leastcolor(x7)
        x9 = extract(x7, matcher(first, x8))
        x10 = last(x9)
        x11 = subtract(x10, ulcorner(x7))
        x12 = normalize(x7)
        x13 = sfilter(x2, matcher(color, x8))

        def x14(x15: Object) -> Object:
            x16 = first(toindices(x15))
            x17 = subtract(x16, x11)
            return shift(x12, x17)

        x18 = apply(x14, x13)
        x19 = merge(x18)
        return x19

    x20 = mapply(x6, x4)
    x21 = paint(x5, x20)
    return x21
