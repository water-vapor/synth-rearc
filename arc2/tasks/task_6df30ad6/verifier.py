from arc2.core import *


def verify_6df30ad6(I: Grid) -> Grid:
    x0 = objects(I, T, F, T)
    x1 = extract(x0, matcher(color, FIVE))
    x2 = remove(ZERO, palette(I))
    x3 = remove(FIVE, x2)
    x4 = tuple(x3)
    x5 = lambda x6: valmin(colorfilter(x0, x6), lambda x7: manhattan(x1, x7))
    x6 = lambda x7: (x5(x7), colorcount(I, x7), x7)
    x7 = argmin(x4, x6)
    x8 = canvas(ZERO, shape(I))
    x9 = fill(x8, x7, x1)
    return x9
